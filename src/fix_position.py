from pprint import PrettyPrinter

from model.fix.enum.msg_type import MsgType
from model.fix.enum.ord_status import OrdStatus
from model.fix.enum.ord_type import OrdType
from model.fix.message import Message

_positions = []


def create_position(account, symbol, quantity, price):
    acc_position_idx, acc_position_value = try_get_position_by_account(account=account)
    sym_position_idx, sym_position_value = try_get_position_by_symbol(acc_position_value['positions'], symbol)
    new_position = {'symbol': symbol, 'open_quantity': int(sym_position_value['open_quantity']) + int(quantity or '0'),
                    'average_price': price, 'trades': sym_position_value['trades']}
    if sym_position_idx == -1:
        acc_position_value['positions'].append(new_position)
    else:
        acc_position_value['positions'][sym_position_idx] = new_position

    if acc_position_idx == -1:
        _positions.append(acc_position_value)
    else:
        _positions[acc_position_idx] = acc_position_value


def update_position(account, symbol, quantity: int = '0', price: float = None, trade_id: str = None):
    acc_position_idx, acc_position_value = try_get_position_by_account(account=account)
    sym_position_idx, sym_position_value = try_get_position_by_symbol(acc_position_value['positions'], symbol)
    new_position = {'symbol': symbol,
                    'open_quantity': int(sym_position_value['open_quantity']) + (int(quantity or '0') * -1),
                    'average_price': price if len(sym_position_value['trades']) == 0 else round(
                        (float(sym_position_value['average_price']) + float(price)) / (
                                len(sym_position_value['trades']) + 1), 2), 'trades': sym_position_value['trades']}
    new_position['trades'].append({'trade_id': trade_id, 'executed': quantity, 'price': price})
    if sym_position_idx == -1:
        acc_position_value['positions'].append(new_position)
    else:
        acc_position_value['positions'][sym_position_idx] = new_position

    if acc_position_idx == -1:
        _positions.append(acc_position_value)
    else:
        _positions[acc_position_idx] = acc_position_value


def try_get_position_by_account(account) -> tuple:
    try:
        return next((idx, item) for (idx, item) in enumerate(_positions) if item['account'] == account)
    except StopIteration:
        return -1, {'account': account, 'positions': []}


def try_get_position_by_symbol(positions, symbol):
    try:
        return next((idx, item) for (idx, item) in enumerate(positions) if item['symbol'] == symbol)
    except StopIteration:
        return -1, {'symbol': symbol, 'open_quantity': 0, 'average_price': 0.0, 'trades': []}


def process_new_order_single(message_text: Message):
    account = message_text.get_value(tag=1)
    side = message_text.get_value(tag=54)
    quantity = message_text.get_value(tag=38)
    symbol = message_text.get_value(tag=55)
    ord_type = OrdType(message_text.get_value(tag=40))
    price = message_text.get_value(
        tag=44) if ord_type == OrdType.Limit else 'Market' if ord_type == OrdType.Market else '?'
    print('The account {a} send an order of {s} of {q} quantities of {sy} at {p}'.format(a=account,
                                                                                         s='Buy' if side else 'Sell',
                                                                                         q=quantity, sy=symbol,
                                                                                         p=price))


def process_execution_report(message_text: Message):
    account = message_text.get_value(tag=1)
    side = message_text.get_value(tag=54)
    last_quantity = message_text.get_value(tag=32)
    quantity = message_text.get_value(tag=38)
    symbol = message_text.get_value(tag=55)
    ord_type = message_text.get_value(tag=40)
    price = 0
    if ord_type:
        price = message_text.get_value(
            tag=44) if OrdType(ord_type) == OrdType.Limit else 'Market' if ord_type == OrdType.Market else '?'
    last_price = message_text.get_value(tag=31)
    trade_id = message_text.get_value(tag=19)
    if message_text.ord_status == OrdStatus.New:
        create_position(account=account, symbol=symbol, quantity=int(quantity) * (1 if side == '1' else -1),
                        price=price)
    elif message_text.ord_status in (OrdStatus.Partially_filled, OrdStatus.Filled):
        update_position(account=account, symbol=symbol, quantity=int(last_quantity) * (1 if side == '1' else -1),
                        price=float(last_price), trade_id=trade_id)
    else:
        print('This message was not suported yet. MsgType={mt} and OrdStatus={os}'.format(mt=message_text.msg_type,
                                                                                          os=message_text.ord_status))


if __name__ == '__main__':
    filename = 'c:\\temp\\fix.messages.log'
    msgs = []
    with open(filename, 'r+') as messages:
        for message in messages:
            msg = Message(message)
            msgs.append(msg)
            if msg.msg_type == MsgType.New_Order_Single:
                process_new_order_single(message_text=msg)
            elif msg.msg_type == MsgType.Execution_Report:
                process_execution_report(message_text=msg)
            else:
                pass
    pp = PrettyPrinter(indent=4, sort_dicts=True, compact=True)
    for position in _positions:
        for account_position in position['positions']:
            if account_position['trades']:
                for trade in account_position['trades']:
                    print(
                        'account={a}\tsymbol={s}\topen_orders={o}\torder_price={p}\texecuted={e}\ttrade_price={r}\t'
                        'trade_id={t}'.format(
                            a=position['account'], s=account_position['symbol'], o=account_position['open_quantity'],
                            p=account_position['average_price'], e=trade['executed'], r=trade['price'],
                            t=trade['trade_id']))
            else:
                print('account={a}\tsymbol={s}\topen_orders={o}\torder_price={p}'.format(a=position['account'],
                                                                                         s=account_position['symbol'],
                                                                                         o=account_position[
                                                                                             'open_quantity'],
                                                                                         p=account_position[
                                                                                             'average_price']))
    # pp.pprint(_positions)
