from ._wrap import _func, _register_funcs
from ctypes import (POINTER, c_int, c_uint, c_uint8, c_uint16, c_uint32, c_int32, c_char_p, c_void_p, Structure, c_bool, CFUNCTYPE, py_object)

from .bps import bps_event_t

#----------------------------
# from ids.h
#

# Version of the IDS library
IDS_VERSION = 1001000
# Version of the IDS library as a string
IDS_VERSION_STRING = "1.1.0"

# IDS result codes returned to the application
IDS_FAILURE = -1
IDS_SUCCESS = 0
IDS_DEFAULT_ERROR = 49999
IDS_NAME_TOO_LONG = 50002
IDS_ACCOUNT_LOCALLY_LOCKED_OUT = 50003
IDS_USER_COULD_NOT_BE_AUTHENTICATED = 50004
IDS_TOO_MANY_NAMES_PASSED = 50005
IDS_INVALID_REQUEST = 50006
IDS_DOES_NOT_EXIST = 50007
IDS_UNKNOWN_TOKEN_TYPE = 50008
IDS_UNKNOWN_APPLIES_TO = 50009
IDS_NOT_ENOUGH_RESOURCES = 50010
IDS_CANNOT_GET_TOKEN_WHILE_OFFLINE = 50011
IDS_ERROR_WHILE_CONTACTING_SERVICE = 50012
IDS_NULL_OR_UNKNOWN_PARAMETERS = 50015
IDS_NOT_ALLOWED = 50017
IDS_VALUE_TOO_LARGE = 50107
IDS_ALREADY_EXISTS = 50159
IDS_NOT_READY = 50207
IDS_QUOTA_EXCEEDED = 50018
# Deprecated Return Codes
IDS_PROPERTY_DOES_NOT_EXIST = 50007
IDS_PROPERTY_NOT_AUTHORIZED = 50017
IDS_CLEAR_TOKEN_FAIL = 50016
IDS_NAME_MUST_BE_SET = 50107

# An opaque handle that the IDS library uses to maintain information
# related to a specific identity provider
class ids_provider_t(Structure):
    _fields_ = []

# Additional information for token parameters
class ids_token_param_t(Structure):
    _fields_ = [("name", c_char_p), ("value", c_char_p)]

# The property value associated with an identity
class ids_property_t(Structure):
    _fields_ = [("name", c_char_p), ("value", c_char_p)]

# A generic data container for use with identity providers'
# data storage
class ids_data_t(Structure):
    _fields_ = [("name", c_char_p), ("value", c_void_p), ("length", c_int)]

# The success callback function for @c ids_get_token()
get_token_cb_func = CFUNCTYPE(None, c_uint, c_char_p, c_int, POINTER(ids_token_param_t), py_object)

# The success callback function for @c ids_clear_token()
clear_token_cb_func = CFUNCTYPE(None, c_uint, c_bool, py_object)

# The success callback function for @c ids_get_properties()
get_properties_cb_func = CFUNCTYPE(None, c_uint, c_int, POINTER(ids_property_t), py_object)

# The success callback function for @c ids_get_data()
get_data_cb_func = CFUNCTYPE(None, c_uint, POINTER(ids_data_t), py_object)

# The success callback function for @c ids_list_data()
list_cb_func = CFUNCTYPE(None, c_uint, c_int, POINTER(c_char_p), py_object)

# The success callback function for @c ids_challenge()
challenge_cb_func = CFUNCTYPE(None, c_uint, c_int, py_object)

# The success callback function for requests that do not have data to
# return to the calling application
success_cb_func = CFUNCTYPE(None, c_uint, py_object)

# The function that is executed to notify that a change was detected
# for the given entry
notify_cb_func = CFUNCTYPE(None, c_int, c_char_p, c_int, py_object)

# The failure callback function
failure_cb_func = CFUNCTYPE(None, c_uint, c_int, c_char_p, py_object)

# Retrieve the version of the IDS APIs
ids_get_version = _func(c_int)
ids_initialize = _func(c_int)
ids_shutdown = _func(None)
ids_register_provider = _func(c_int, c_char_p, POINTER(POINTER(ids_provider_t)), POINTER(c_int))
ids_process_msg = _func(c_int, c_int)

#*****************************************************************************
# User Identity Functions
#*****************************************************************************

IDS_LOG_NONE = "Silent"
IDS_LOG_NORMAL = "Normal"
IDS_LOG_VERBOSE = "Verbose"

IDS_OPT_GUI_ALLOWED = 0
IDS_OPT_GROUP_ID = 1
IDS_OPT_VERBOSITY = 2

ids_set_option = _func(c_int, c_int, c_char_p)
ids_get_token = _func(c_int, POINTER(ids_provider_t), c_char_p, c_char_p, get_token_cb_func, failure_cb_func, py_object, POINTER(c_int))
ids_clear_token = _func(c_int, POINTER(ids_provider_t), c_char_p, c_char_p, clear_token_cb_func, failure_cb_func, py_object, POINTER(c_int))

IDS_MAX_PROPERTY_COUNT = 10
IDS_MAX_PROPERTY_NAME_LEN = 32
IDS_MAX_DATA_NAME_LEN = 128

ids_get_properties = _func(c_int, POINTER(ids_provider_t), c_int, c_int, POINTER(c_char_p), get_properties_cb_func, failure_cb_func, py_object, POINTER(c_uint))
ids_get_data = _func(c_int, POINTER(ids_provider_t), c_int, c_int, c_char_p, get_data_cb_func, failure_cb_func, py_object, POINTER(c_uint))
ids_set_data = _func(c_int, POINTER(ids_provider_t), c_int, c_int, POINTER(ids_data_t), success_cb_func, failure_cb_func, py_object, POINTER(c_uint))
ids_create_data = _func(c_int, POINTER(ids_provider_t), c_int, c_int, POINTER(ids_data_t), success_cb_func, failure_cb_func, py_object, POINTER(c_uint))
ids_delete_data = _func(c_int, POINTER(ids_provider_t), c_int, c_int, c_char_p, success_cb_func, failure_cb_func, py_object, POINTER(c_uint))
ids_list_data = _func(c_int, POINTER(ids_provider_t), c_int, c_int, list_cb_func, failure_cb_func, py_object, POINTER(c_uint))
ids_challenge = _func(c_int, POINTER(ids_provider_t), c_int, c_int, challenge_cb_func, failure_cb_func, py_object, POINTER(c_uint))
ids_register_notifier = _func(c_int, POINTER(ids_provider_t), c_int, c_int, c_char_p, notify_cb_func, py_object)

#*****************************************************************************
# ids_blackberry_id.h
#*****************************************************************************
BLACKBERRY_ID_PROVIDER = b"ids:rim:bbid"

BBID_PROPERTY_CORE = 0

IDS_BBID_PROP_USERNAME   = b"urn:bbid:username"
IDS_BBID_PROP_SCREENNAME = b"urn:bbid:screenname"
IDS_BBID_PROP_FIRSTNAME  = b"urn:bbid:firstname"
IDS_BBID_PROP_LASTNAME   = b"urn:bbid:lastname"
IDS_BBID_PROP_UID        = b"urn:bbid:uid"

IDS_BBID_LEVEL_AUTH_OFFLINE = 0
IDS_BBID_LEVEL_AUTH_ONLINE = 1

BBID_AUTHENTICATE = 0

BBID_CHALLENGE_DEFAULT = 0

IDS_BBID_NOTIFIER_START = 0x00000000
IDS_BBID_NOTIFIER_STOP  = 0x00000001

IDS_BBID_NOTIFY_STARTED = 0x00000000
IDS_BBID_NOTIFY_STOPPED = 0x00000001
IDS_BBID_NOTIFY_CHANGED = 0x00000002

#*****************************************************************************
# ids_blackberry_profile.h
#*****************************************************************************

BLACKBERRY_PROFILE_PROVIDER = b"ids:rim:profile"

IDS_PROFILE_TYPE_APP = 1
IDS_PROFILE_TYPE_VENDOR = 2

IDS_PROFILE_CREATE_DATA_DEFAULT  = 0x00000000
IDS_PROFILE_CREATE_DATA_ENCRYPT_D2D = 0x00000001
IDS_PROFILE_CREATE_DATA_CACHE    = 0x00000010

IDS_PROFILE_GET_DATA_DEFAULT  = 0x00000000
IDS_PROFILE_GET_DATA_CACHE    = 0x00000001

IDS_PROFILE_SET_DATA_DEFAULT  = 0x00000000
IDS_PROFILE_SET_DATA_CACHE    = 0x00000001

IDS_PROFILE_DELETE_DATA_DEFAULT     = 0x00000000
IDS_PROFILE_DELETE_DATA_CACHE_ONLY  = 0x00000001
IDS_PROFILE_DELETE_DATA_ALL         = 0x00000002

IDS_PROFILE_LIST_DATA_DEFAULT = 0x00000000

IDS_PROFILE_NOTIFIER_START = 0x00000000
IDS_PROFILE_NOTIFIER_STOP  = 0x00000001

IDS_PROFILE_NOTIFY_STARTED = 0x00000000
IDS_PROFILE_NOTIFY_STOPPED = 0x00000001
IDS_PROFILE_NOTIFY_CHANGED = 0x00000002

_register_funcs('libbbplatform.so', globals(), use_errno = True)