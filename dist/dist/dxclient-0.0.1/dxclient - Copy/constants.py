import datetime

# The URL of the API
DXL_API_URL = "https://api.dxopen.com/DxlApi/Xml"
QA1_DOMAIN  = 'https://qa1.msf.markit.com/'
PROD_DOMAIN = 'https://msf.markit.com/'
DXLAPI_PATH = 'Dxlapi'
DXOPEN_PATH = 'DxOpen'

# The names of pages within the API
PAGE_API               = 'XmlApi'
PAGE_CHART             = 'Charts/LineChart'
PAGE_DATA_UPDATE_DATES = 'DataUpdateDates'
PAGE_JSON              = 'Json'
PAGE_LOGIN             = 'XmlLogin'
PAGE_LOGOUT            = 'XmlLogout'
PAGE_SYS_INFO          = 'SysInfo'

QA_DXOPEN_URL   = QA1_DOMAIN  + DXOPEN_PATH
PROD_DXOPEN_URL = PROD_DOMAIN + DXOPEN_PATH
QA_DXLAPI_URL   = QA1_DOMAIN  + DXLAPI_PATH
PROD_DXLAPI_URL = PROD_DOMAIN + DXLAPI_PATH

MIN_DATE = datetime.date(datetime.MINYEAR, 1, 1)   # Caution: C# Max year is 10000, Python supports 9999
MAX_DATE = datetime.date(datetime.MAXYEAR, 1, 1)
DEFAULT_DATE_FORMAT = '%Y%m%d'

DEBUG_QUERY_PRINT = True

# The names of parameters passed to API queries
class Parameters(object):
    PARAM_BATCH               = 'BATCH'
    PARAM_CATEGORY            = 'CATEGORY'
    PARAM_CHARTSTYLE          = 'CHARTSTYLE'
    PARAM_CHARTTEMPLATE       = 'CHARTTEMPLATE'
    PARAM_CHARTTYPE           = 'CHARTTYPE'
    PARAM_CLEAR_CACHE         = 'CLEARCACHE'
    PARAM_CLIENT_ID           = 'CLIENTID'
    PARAM_CURRENCY            = 'CURRENCY'
    PARAM_DAYS                = 'DAYS'
    PARAM_ERRATA_CHANGE_TYPES = 'ERRATACHANGETYPES'
    PARAM_FIELDS              = 'FIELD'
    PARAM_FILTER              = 'FILTER'
    PARAM_FROM_DATE           = 'FROMDATE'
    PARAM_HEIGHT              = 'HEIGHT'
    PARAM_IDENTIFIER          = 'IDENTIFIER'
    PARAM_IDTYPE              = 'IDTYPE'
    PARAM_IDVALUE             = 'IDVALUE'
    PARAM_MODIFIER            = 'MODIFIER'
    PARAM_OFFSET_FROM_DATE    = 'OFFSETFROMDATE'
    PARAM_OFFSET_TO_DATE      = 'OFFSETTODATE'
    PARAM_PASSWORD            = 'PASSWORD'
    PARAM_SOURCE              = 'SOURCE'
    PARAM_TO_DATE             = 'TODATE'
    PARAM_USERNAME            = 'USERNAME'
    PARAM_VERSION             = 'VERSION'
    PARAM_WIDTH               = 'WIDTH'

    #DATE_FORMAT          = 'yyyyMMdd'
    IDENTIFIER_SEPARATOR = '&'
    SOURCE_SEPARATOR     = '.'
    VALUE_SEPARATOR      = ';'
    VALUE_ASSIGN         = '='

class Credentials(object):
    API2_USER = 'API_Test002'
    API2_PASSWORD = 'sp0rtNik'

    INTERNAL_USER = 'API_Test004'
    INTERNAL_PASSWORD = 'sp0rtNik'

    USER = INTERNAL_USER #None
    PASSWORD = INTERNAL_PASSWORD #None