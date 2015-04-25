'''Wrappers for libbps routines'''

import os

import ctypes
from ctypes import (c_int, c_float, c_char_p, POINTER, Structure)

from bb._wrap import _func, _register_funcs
from bb.bps import _dll, bps_event_t

#-------------------------------------
BATTERY_INFO        = 0x01

BATTERY_CHARGER_ERROR      = 0
BATTERY_CHARGER_BAD        = 1
BATTERY_CHARGER_NONE       = 2
BATTERY_CHARGER_PLUGGED    = 3
BATTERY_CHARGER_CHARGING   = 4
battery_charger_info_t = c_int

BATTERY_CHARGING_NOT_CHARGING     = 0
BATTERY_CHARGING_TRICKLE_CHARGING = 1
BATTERY_CHARGING_CONSTANT_CURRENT = 2
BATTERY_CHARGING_CONSTANT_VOLTAGE = 3
BATTERY_CHARGING_DONE_CHARGING    = 4
battery_charging_state_t = c_int

BATTERY_TIME_NA = 65535
BATTERY_INVALID_VALUE = 80000000
battery_special_values_t = c_int

class battery_info_t(Structure):
    _fields_ = []

battery_request_events = _func(c_int, c_int)
battery_stop_events = _func(c_int, c_int)
battery_get_domain = _func(c_int)
battery_event_get_info = _func(POINTER(battery_info_t), POINTER(bps_event_t))
battery_get_info = _func(c_int, POINTER(POINTER(battery_info_t)))
battery_free_info = _func(None, POINTER(POINTER(battery_info_t)))

battery_info_is_battery_ready = _func(c_int, POINTER(battery_info_t))
battery_info_is_battery_present = _func(c_int, POINTER(battery_info_t))
battery_info_get_battery_id = _func(c_int, POINTER(battery_info_t))
battery_info_is_battery_ok = _func(c_int, POINTER(battery_info_t))
battery_info_get_state_of_charge = _func(c_int, POINTER(battery_info_t))
battery_info_get_state_of_health = _func(c_int, POINTER(battery_info_t))
battery_info_get_charger_info = _func(c_int, POINTER(battery_info_t))
battery_info_get_device_name = _func(c_char_p, POINTER(battery_info_t))
battery_info_get_time_to_empty = _func(c_int, POINTER(battery_info_t))
battery_info_get_time_to_full = _func(c_int, POINTER(battery_info_t))
battery_info_get_version = _func(c_int, POINTER(battery_info_t))

# added in 10.2
osver = tuple(int(n) for n in os.getenv('OS_VERSION', '10.0').split('.'))
if osver >= (10, 2):
    battery_info_get_battery_name = _func(c_char_p, POINTER(battery_info_t))
    battery_info_get_battery_voltage = _func(c_int, POINTER(battery_info_t))
    battery_info_get_battery_available_energy = _func(c_int, POINTER(battery_info_t))
    battery_info_get_battery_average_current = _func(c_int, POINTER(battery_info_t))
    battery_info_get_battery_average_power = _func(c_int, POINTER(battery_info_t))
    battery_info_get_battery_alert = _func(c_int, POINTER(battery_info_t))
    battery_info_get_battery_cycle_count = _func(c_int, POINTER(battery_info_t))
    battery_info_get_battery_temperature = _func(c_float, POINTER(battery_info_t))
    battery_info_get_battery_design_capacity = _func(c_int, POINTER(battery_info_t))
    battery_info_get_battery_full_available_capacity = _func(c_int, POINTER(battery_info_t))
    battery_info_get_battery_full_charge_capacity = _func(c_int, POINTER(battery_info_t))
    battery_info_get_battery_max_load_current = _func(c_int, POINTER(battery_info_t))
    battery_info_get_battery_max_load_time_to_empty = _func(c_int, POINTER(battery_info_t))
    battery_info_get_battery_nominal_available_capacity = _func(c_int, POINTER(battery_info_t))
    battery_info_get_battery_time_to_empty_at_constant_power = _func(c_int, POINTER(battery_info_t))

    battery_info_is_charger_ready = _func(c_int, POINTER(battery_info_t))
    battery_info_get_charger_max_input_current = _func(c_int, POINTER(battery_info_t))
    battery_info_get_charger_max_charge_current = _func(c_int, POINTER(battery_info_t))
    battery_info_get_charger_name = _func(c_char_p, POINTER(battery_info_t))

    battery_info_is_system_ready = _func(c_int, POINTER(battery_info_t))
    battery_info_get_system_voltage = _func(c_int, POINTER(battery_info_t))
    battery_info_get_system_input_current_monitor = _func(c_int, POINTER(battery_info_t))
    battery_info_get_system_charging_state = _func(c_int, POINTER(battery_info_t))
    battery_info_get_system_max_voltage = _func(c_int, POINTER(battery_info_t))
    battery_info_get_system_min_voltage = _func(c_int, POINTER(battery_info_t))
    battery_info_get_system_charge_current = _func(c_int, POINTER(battery_info_t))

#----------------------------
# apply argtypes/restype to all functions
#
_register_funcs(_dll, globals())


# EOF