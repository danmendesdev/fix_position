from enum import Enum


class MsgType(Enum):
    Heartbeat = '0'
    Test_Request = '1'
    Resend_Request = '2'
    Reject = '3'
    Sequence_Reset = '4'
    Logout = '5'
    IOI = '6'
    Advertisement = '7'
    Execution_Report = '8'
    Order_Cancel_Reject = '9'
    Quote_Status_Request = 'a'
    Logon = 'A'
    Derivative_Security_List = 'AA'
    New_Order_Multileg = 'AB'
    Multileg_Order_Cancel_or_Replace = 'AC'
    Trade_Capture_Report_Request = 'AD'
    Trade_Capture_Report = 'AE'
    Order_Mass_Status_Request = 'AF'
    Quote_Request_Reject = 'AG'
    RFQ_Request = 'AH'
    Quote_Status_Report = 'AI'
    Quote_Response = 'AJ'
    Confirmation = 'AK'
    Position_Maintenance_Request = 'AL'
    Request_For_Positions = 'AN'
    Position_Maintenance_Report = 'AM'
    Request_for_Positions_Ack = 'AO'
    Position_Report = 'AP'
    Trade_Capture_Report_Request_Ack = 'AQ'
    Trade_Capture_Report_Ack = 'AR'
    Allocation_Report = 'AS'
    Allocation_Report_Ack = 'AT'
    Confirmation_Ack = 'AU'
    Settlement_Instruction_Request = 'AV'
    Assignment_Report = 'AW'
    Collateral_Request = 'AX'
    Collateral_Assignment = 'AY'
    Collateral_Response = 'AZ'
    Mass_Quote_Acknowledgement = 'b'
    News = 'B'
    Collateral_Report = 'BA'
    Collateral_Inquiry = 'BB'
    Network_Counterparty_System_Status_Request = 'BC'
    Network_Counterparty_System_Status_Response = 'BD'
    User_Request = 'BE'
    User_Response = 'BF'
    Collateral_Inquiry_Ack = 'BG'
    Confirmation_Request = 'BH'
    Security_Definition_Request = 'c'
    Email = 'C'
    Security_Definition = 'd'
    New_Order_Single = 'D'
    Security_Status_Request = 'e'
    New_Order_List = 'E'
    Security_Status = 'f'
    Order_Cancel_Request = 'F'
    Trading_Session_Status_Request = 'g'
    Order_Cancel_or_Replace_Request = 'G'
    Trading_Session_Status = 'h'
    Order_Status_Request = 'H'
    Mass_Quote = 'i'
    Business_Message_Reject = 'j'
    Allocation_Instruction = 'J'
    Bid_Request = 'k'
    List_Cancel_Request = 'K'
    Bid_Response = 'l'
    List_Execute = 'L'
    List_Strike_Price = 'm'
    List_Status_Request = 'M'
    XML_Message = 'n'
    List_Status = 'N'
    Registration_Instructions = 'o'
    Registration_Instructions_Response = 'p'
    Allocation_Instruction_Ack = 'P'
    Order_Mass_Cancel_Request = 'q'
    Don_t_Know_Trade = 'Q'
    Order_Mass_Cancel_Report = 'r'
    Quote_Request = 'R'
    New_Order_Cross = 's'
    Quote = 'S'
    Cross_Order_Cancel_or_Replace_Request = 't'
    Settlement_Instructions = 'T'
    Cross_Order_Cancel_Request = 'u'
    Security_Type_Request = 'v'
    Market_Data_Request = 'V'
    Security_Types = 'w'
    Market_Data_Snapshot_or_Full_Refresh = 'W'
    Security_List_Request = 'x'
    Market_Data_Incremental_Refresh = 'X'
    Security_List = 'y'
    Market_Data_Request_Reject = 'Y'
    Derivative_Security_List_Request = 'z'
    Quote_Cancel = 'Z'
