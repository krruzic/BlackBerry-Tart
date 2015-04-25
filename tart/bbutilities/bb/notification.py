'''Wrappers for libbps notification routines'''

import ctypes
from ctypes import (c_int, c_char_p, c_void_p,
    POINTER, Structure)

from bb._wrap import _func, _register_funcs
from bb.bps import _dll, bps_event_t


#-------------------------------------
class notification_message_t(Structure):
    _fields_ = []

# The possible application perimeter types
NOTIFICATION_PERIMETER_TYPE_UNSPECIFIED = 0
NOTIFICATION_PERIMETER_TYPE_PERSONAL    = 1
NOTIFICATION_PERIMETER_TYPE_ENTERPRISE  = 2
notification_perimeter_type_t = c_int

# The possible notification response events
NOTIFICATION_OK = 0x00
NOTIFICATION_ERROR = 0x01
NOTIFICATION_CHOICE = 0x02
notification_response_t = c_int

# The maximum number of prompt choices that can be displayed by a dialog.
NOTIFICATION_MAX_PROMPT_CHOICES = 4

notification_request_events = _func(c_int, c_int)
notification_stop_events = _func(c_int, c_int)
notification_get_domain = _func(c_int)
notification_message_create = _func(c_int, POINTER(POINTER(notification_message_t)))
notification_message_destroy = _func(None, POINTER(POINTER(notification_message_t)))

notification_message_set_request_id = _func(c_int, POINTER(notification_message_t), c_char_p)
notification_message_set_item_id = _func(c_int, POINTER(notification_message_t), c_char_p)
notification_message_set_title = _func(c_int, POINTER(notification_message_t), c_char_p)
notification_message_set_subtitle = _func(c_int, POINTER(notification_message_t), c_char_p)
# deprecated notification_message_set_badge = _func(c_int, POINTER(notification_message_t))
notification_message_set_sound_url = _func(c_int, POINTER(notification_message_t), c_char_p)
notification_message_set_invocation_target = _func(c_int, POINTER(notification_message_t), c_char_p)
notification_message_set_invocation_payload = _func(c_int, POINTER(notification_message_t), c_void_p, c_int)
notification_message_set_invocation_encoded_payload = _func(c_int, POINTER(notification_message_t), c_char_p)
notification_message_set_invocation_type = _func(c_int, POINTER(notification_message_t), c_char_p)
notification_message_set_invocation_payload_uri = _func(c_int, POINTER(notification_message_t), c_char_p)
notification_message_set_invocation_action = _func(c_int, POINTER(notification_message_t), c_char_p)
notification_message_add_prompt_choice = _func(c_int, POINTER(notification_message_t), c_char_p, c_char_p)

notification_alert = _func(c_int, POINTER(notification_message_t))
notification_notify = _func(c_int, POINTER(notification_message_t))
notification_cancel = _func(c_int, POINTER(notification_message_t))
notification_delete = _func(c_int, POINTER(notification_message_t))

notification_event_get_response = _func(c_int, POINTER(bps_event_t))
notification_event_get_item_id = _func(c_char_p, POINTER(bps_event_t))
notification_event_get_request_id = _func(c_char_p, POINTER(bps_event_t))
notification_event_get_context = _func(c_char_p, POINTER(bps_event_t))
notification_event_get_choice = _func(c_int, POINTER(bps_event_t))

# internal functions not available except with use_notify_system permission
# int notification_message_set_invocation_launch_in_background(
#         POINTER(notification_message_t))
# int notification_message_set_perimeter(POINTER(notification_message_t),
#         notification_perimeter_type_t perimeter)
# int notification_message_set_app_id(POINTER(notification_message_t),
#         c_char_p app_id)
# int notification_message_set_type(POINTER(notification_message_t),
#         c_char_p type)
# int notification_message_set_repeating(
#         POINTER(notification_message_t))
# int notification_message_set_event_time(
#         POINTER(notification_message_t),
#         time_t event_time)


#----------------------------
# apply argtypes/restype to all functions
#
_register_funcs(_dll, globals())


# EOF