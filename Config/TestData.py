class TestData:

    """DASHBOARD PAGE"""
    LINK_NAMES = ['Dashboard', 'Communication', 'Fallbacks', 'Visitor\'s Log', 'Your Story',
                  'Intent', 'Conversational Flow', 'Webhook PRO', 'Bot Settings', 'Integrations PRO', 'Help',
                  'Edit Profile', 'Sign Out']

    EXPECTED_LOGIN_ERROR_MESSAGE = 'Incorrect username or password!\n×'

    """EDIT PROFILE_CHANGE PASSWORD"""
    EXPECTED_CHANGE_PASSWORD_SUCCESS_MESSAGE = 'Password changed successfully.\n×'
    EXPECTED_CHANGE_PASSWORD_ERROR_MESSAGE = 'New password and confirm password do not match.\n×'

    LOGINPAGE_TITLE = "Yugasa Bot | Dashboard"
    HOMEPAGE_TITLE = "Yugasa Bot | Dashboard"

    PLACEHOLDER_ATT_VALUES = ['Username', 'Email', 'Password', 'Enter 10 digit Mobile Number', 'https://website.com']
    FORGOTPASSWORD_HEADER_TEXT = 'Reset Yugasa Bot Password'

    Edit_Company_Name = 'Test007'
    EDIT_PROFILE_ALERT_TEXT = 'Profile updated successfully'

    RgstPageEle = ['Test1234', 'Test@gmail.com', 'Test@12345', '9888982489', 'www.google.com']

    Expected_Chart_Filters_Options = ['Line Chart', 'Bar Chart']

    IGNORE_BTN_POPUP_TITLE = 'Are you sure?'
    IGNORE_BTN_POPUP_HEADER_TEXT = 'Once deleted, you will not be able to recover this!'

    """Communication Page"""
    EDIT_EMAILID = 'test@gmail.com'
    EDIT_PHONE = '033433222'
    STATUS_DROPDOWN_VALUES = ['Bot Communicated', 'Human Contacted', 'In Progress', 'Proposal Submitted', 'Business Closed', 'Business Lost']
    COMMUNICATION_CHAT = ['this', 'that', 'hi', 'why', 'when', 'test', 'chat', 'bot', 'botchat', '10', '11', 'twelve', '13', '14', '15']


    """FALLBACKS PAGE"""
    FALLBACKS_CREATE_INTENT_HEADER = 'Create Intent'

    """CREATE INTENT PAGE"""
    CREATE_INTENT_PAGE_HEAD_TITLE = 'Intent'
    TRAIN_SUCCESS_TEXT = 'Training done successfully!'
    ADD_INTENT_POPUP_HEAD_TEXT = 'Add Intent'
    INTENT_NAME_TEXT = 'val27'
    EDIT_INTENT_HEADER_TEXT = 'Edit Intent'
    UPLOAD_INTENT_SUCCESS_MESSAGE = 'Successfully uploaded'

    """CONVERSATIONAL PAGE FLOW"""
    CONVERSATIONAL_PAGE_HEAD_TEXT = 'Conversational Flow'

    """Help Page"""
    HELP_PAGE_HEAD_TEXT = 'Get the best out of your Yugasa Bot!'
    CONTACT_US_ALERT_TEXT = 'Thanks for your query, our team will get back to you soon!'

    """Integrations Page"""
    INTEGRATION_PAGE_HEAD_TEXT = 'Properties'

    """Bot Settings Page"""
    DESIGN_TAB_SUCCESS_ALERT_TEXT = 'Style changes saved successfully!'
    INTEGRATION_OPTIONS = ['Web Integration', 'Messenger Integration', 'Hubspot Integration', 'Wordpress Integration', 'Alexa Integration', 'Facebook Integration']

    """RGB COLOR CODES"""
    RED_COLOR = 'rgb(255, 0, 0)'
    BLUE_COLOR = 'rgb(4, 0, 255)'
    PINK_COLOR = 'rgb(255, 0, 247)'
    GREEN_COLOR = 'rgb(89, 255, 0)'
    ORANGE_COLOR = 'rgb(255, 136, 0)'

    """SLOTS PAGE"""
    ADD_SLOTS_CANCEL_BTN_MSG1 = 'Are you sure?'
    ADD_SLOTS_CANCEL_BTN_MSG2 = 'Want to discard changes'
    ADD_SLOTS_CANCELBTN_CLOSE_BTN_MSG = 'Your slots are safe!'
    ADD_SLOTS_SUCCEESS_MSG = 'Slot created successfully'
    UPLOAD_JSON_SUCCESS_MESSAGE = 'Json uploaded successfully'
    TRAIN_BOT_SUCCESS_MESSAGE = 'Training done successfuly'
    TOGGLE_ACTIVE_MSG = 'Slots gets active'
    TOGGLE_INACTIVE_MSG = 'Slots gets inactive'

