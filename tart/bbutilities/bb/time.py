'''Wrappers for time routines'''

from ctypes import (Structure, byref, POINTER, c_int, c_void_p, c_ulong,
    c_uint, c_long, get_errno, cast)

from ._wrap import _func, _register_funcs
from .siginfo import sigevent


CLOCK_REALTIME  = 0
CLOCK_SOFTTIME  = 1
CLOCK_MONOTONIC = 2
CLOCK_HARMONIC  = 5

TIMER_ABSTIME   = 0x80000000
TIMER_TOLERANCE = 0x40000000
TIMER_PRECISE   = 0x20000000


class timespec(Structure):
    _fields_ = [
        ('tv_sec', c_ulong),
        ('tv_nsec', c_long),
        ]

class itimerspec(Structure):
    _fields_ = [
        ('it_value', timespec),
        ('it_interval', timespec),
        ]


timer_create = _func(c_int, c_int, POINTER(sigevent), POINTER(c_int))
timer_settime = _func(c_int, c_int, c_int, POINTER(itimerspec), POINTER(itimerspec))
timer_delete = _func(c_int, c_int)
timer_timeout = _func(c_int, c_int, c_int, POINTER(sigevent), POINTER(itimerspec), POINTER(itimerspec))


#----------------------------
# apply argtypes/restype to all functions
#
_dll = _register_funcs('libc.so', globals(), use_errno=True)


# EOF