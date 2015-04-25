# for sys/siginfo.h

from ctypes import (Structure, Union, POINTER, c_int, c_void_p,
    CFUNCTYPE, c_uint, c_short)

class sigval(Union):
    _fields_ = [
        ('sival_int', c_int),
        ('sival_ptr', c_void_p),
        ]

func_sigev_notify_function = CFUNCTYPE(None, sigval)

class union_sigev_un1(Union):
    _fields_ = [
        ('sigev_signo', c_int),
        ('sigev_coid', c_int),
        ('sigev_id', c_int),
        ('sigev_notify_function', func_sigev_notify_function),
        ('sigev_addr', POINTER(c_uint)),
        ]

class struct_st(Structure):
    _fields_ = [
        ('sigev_code', c_short),
        ('sigev_priority', c_short),
        ]

class pthread_attr_t(Structure):
    _fields_ = []

class union_sigev_un2(Union):
    _anonymous_ = ('_st',)
    _fields_ = [
        ('_st', struct_st),
        ('sigev_notify_attributes', POINTER(pthread_attr_t)),
        ('sigev_memop', c_int),
        ]

class sigevent(Structure):
    _anonymous_ = ('_sigev_un1', '_sigev_un2')
    _fields_ = [
        ('sigev_notify', c_int),
        ('_sigev_un1', union_sigev_un1),
        ('sigev_value', sigval),
        ('_sigev_un2', union_sigev_un2),
        ]


# def dump_sigevent(ev):
#     print('sigev_notify', ev.sigev_notify)
#     print('sigev_signo', ev._sigev_un1.sigev_signo)
#     print('sigev_value.sival_int', ev.sigev_value.sival_int)
#     print('sigev_code', ev.sigev_code)
#     print('sigev_priority', ev.sigev_priority)