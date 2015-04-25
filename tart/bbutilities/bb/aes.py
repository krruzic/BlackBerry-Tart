'''Wrappers for libhuapi routines'''

import ctypes
from ctypes import (c_bool, c_int, c_char_p, c_void_p, c_uint, c_size_t,
    POINTER, Structure, byref)

from ._wrap import _func, _register_funcs


#----------------------------
# from sbdef.h
#
sb_GlobalCtx = c_void_p
sb_Provider = c_void_p
sb_Session = c_void_p
sb_Params = c_void_p
sb_Key = c_void_p
sb_PublicKey = c_void_p
sb_PrivateKey = c_void_p
sb_Context = c_void_p
sb_YieldCtx = c_void_p
sb_RNGCtx = c_void_p
sb_RngCtx = c_void_p
sb_ECCalcOrderInt = c_void_p
sb_ECCalcECPoint = c_void_p


#----------------------------
# from hugse56.h
#
# Note: incomplete, some items are missing

hu_InitSbg56 = _func(c_int, sb_GlobalCtx)
hu_RegisterSbg56 = _func(c_int, sb_GlobalCtx)

#----------------------------
# from huseed.h
#
# Note: incomplete, some items are missing

hu_RegisterSystemSeed = _func(c_int, sb_GlobalCtx)

#----------------------------
# from huctx.h
#
# Note: incomplete, some items are missing

# hu_GlobalCtxCreate = _func(c_int,
#     POINTER(hu_MallocFunc),
#     POINTER(hu_FreeFunc),
#     POINTER(hu_MemCpyFunc),
#     POINTER(hu_MemCmpFunc),
#     POINTER(hu_MemSetFunc),
#     POINTER(hu_TimeFunc),
#     c_void_p,
#     POINTER(sb_GlobalCtx))

hu_GlobalCtxCreateDefault = _func(c_int, POINTER(sb_GlobalCtx))

# hu_GlobalCtxGet = _func(c_int,
#     sb_GlobalCtx,
#     POINTER(POINTER(hu_MallocFunc)),
#     POINTER(POINTER(hu_FreeFunc)),
#     POINTER(POINTER(hu_MemCpyFunc)),
#     POINTER(POINTER(hu_MemCmpFunc)),
#     POINTER(POINTER(hu_MemSetFunc)),
#     POINTER(POINTER(hu_TimeFunc)),
#     POINTER(c_void_p))

hu_GlobalCtxCreateFromOriginal = _func(c_int, sb_GlobalCtx, POINTER(sb_GlobalCtx))
hu_GlobalCtxCopyCrypto = _func(c_int, sb_GlobalCtx, sb_GlobalCtx)
hu_GlobalCtxDestroy = _func(c_int, POINTER(sb_GlobalCtx))


#----------------------------
# from huaes.h
#

# CTR mode macros
SB_AES_CTR_BASE     = 7
SB_AES_CTR = lambda ctrBits: SB_AES_CTR_BASE | (ctrBits << 8)

# Modes of operation
SB_AES_ECB      = 1
SB_AES_CBC      = 2
SB_AES_CFB128   = 3
SB_AES_OFB128   = 4
SB_AES_KEYWRAP  = 5
SB_AES_CFB8     = 6
SB_AES_CTR8     = SB_AES_CTR(8)
SB_AES_CTR16    = SB_AES_CTR(16)
SB_AES_CTR32    = SB_AES_CTR(32)
SB_AES_CTR64    = SB_AES_CTR(64)
SB_AES_CTR128   = SB_AES_CTR(128)

# XTS mode (NIST SP 800-38A) macros
# unitBytes is the number of bytes in a Data Unit
SB_AES_XTS_BASE         = 8
SB_AES_XTS = lambda unitBytes: SB_AES_XTS_BASE | (unitBytes << 8)

# Block length
SB_AES_128_BLOCK_BITS       = 128
SB_AES_128_BLOCK_BYTES      = (SB_AES_128_BLOCK_BITS >> 3)

SB_AES_KEYWRAP_BLOCK_BITS   = 64
SB_AES_KEYWRAP_BLOCK_BYTES  = (SB_AES_KEYWRAP_BLOCK_BITS >> 3)

# Key length
SB_AES_128_KEY_BITS         = 128
SB_AES_128_KEY_BYTES        = (SB_AES_128_KEY_BITS >> 3)
SB_AES_192_KEY_BITS         = 192
SB_AES_192_KEY_BYTES        = (SB_AES_192_KEY_BITS >> 3)
SB_AES_256_KEY_BITS         = 256
SB_AES_256_KEY_BYTES        = (SB_AES_256_KEY_BITS >> 3)

SB_AES_128_XTS_KEY_BITS     = 256
SB_AES_128_XTS_KEY_BYTES    = (SB_AES_128_XTS_KEY_BITS >> 3)
SB_AES_256_XTS_KEY_BITS     = 512
SB_AES_256_XTS_KEY_BYTES    = (SB_AES_256_XTS_KEY_BITS >> 3)


hu_AESParamsCreate = _func(c_int, c_int, c_size_t, sb_RNGCtx, sb_YieldCtx, POINTER(sb_Params), sb_GlobalCtx)
hu_AESParamsGet = _func(c_int, sb_Params, POINTER(c_int), POINTER(c_size_t), sb_GlobalCtx)
hu_AESParamsDestroy = _func(c_int, POINTER(sb_Params), sb_GlobalCtx)
hu_AESKeySet = _func(c_int, sb_Params, c_size_t, c_char_p, POINTER(sb_Key), sb_GlobalCtx)
hu_AESEncryptKeySet = _func(c_int, sb_Params, c_size_t, c_char_p, POINTER(sb_Key), sb_GlobalCtx)
hu_AESDecryptKeySet = _func(c_int, sb_Params, c_size_t, c_char_p, POINTER(sb_Key), sb_GlobalCtx)
hu_AESKeyGen = _func(c_int, sb_Params, c_size_t, POINTER(sb_Key), sb_GlobalCtx)
hu_AESEncryptKeyGen = _func(c_int, sb_Params, c_size_t, POINTER(sb_Key), sb_GlobalCtx)
hu_AESKeyGet = _func(c_int, sb_Params, sb_Key, POINTER(c_size_t), c_char_p, sb_GlobalCtx)
hu_AESKeyDestroy = _func(c_int, sb_Params, POINTER(sb_Key), sb_GlobalCtx)
hu_AESBegin = _func(c_int, sb_Params, sb_Key, c_size_t, c_char_p, POINTER(sb_Context), sb_GlobalCtx)
hu_AESBeginV2 = _func(c_int,  sb_Params, sb_Key, c_int, c_size_t, c_char_p, POINTER(sb_Context), sb_GlobalCtx)
hu_AESEncrypt = _func(c_int, sb_Context, c_size_t, c_char_p, c_char_p, sb_GlobalCtx)
hu_AESDecrypt = _func(c_int, sb_Context, c_size_t, c_char_p, c_char_p, sb_GlobalCtx)
hu_AESCtxReset = _func(c_int, c_size_t, c_char_p, sb_Context, sb_GlobalCtx)
hu_AESEnd = _func(c_int,  POINTER(sb_Context), sb_GlobalCtx)
hu_AESEncryptMsg = _func(c_int, sb_Params, sb_Key, c_size_t, c_char_p, c_size_t, c_char_p, c_char_p, sb_GlobalCtx)
hu_AESDecryptMsg = _func(c_int, sb_Params, sb_Key, c_size_t, c_char_p, c_size_t, c_char_p, c_char_p, sb_GlobalCtx)
hu_AESKeyWrap = _func(c_int, sb_Params, sb_Key, c_size_t, c_char_p, POINTER(c_size_t), c_char_p, sb_GlobalCtx)
hu_AESKeyUnwrap = _func(c_int, sb_Params, sb_Key, c_size_t, c_char_p, POINTER(c_size_t), c_char_p, sb_GlobalCtx)
hu_AESCCMStarAuthEncrypt = _func(c_int, sb_Params, sb_Key, c_size_t, c_char_p, c_size_t, c_char_p, c_size_t, c_char_p, c_size_t, c_char_p, sb_GlobalCtx)
hu_AESCCMStarAuthDecrypt = _func(c_int, sb_Params, sb_Key, c_size_t, c_char_p, c_size_t, c_char_p, c_size_t, c_char_p, c_size_t, c_char_p, sb_GlobalCtx)
hu_AESCCMAuthEncrypt = _func(c_int, sb_Params, sb_Key, c_size_t, c_char_p, c_size_t, c_char_p, c_size_t, c_char_p, c_size_t, c_char_p, sb_GlobalCtx)
hu_AESCCMAuthDecrypt = _func(c_int, sb_Params, sb_Key, c_size_t, c_char_p, c_size_t, c_char_p, c_size_t, c_char_p, c_size_t, c_char_p, sb_GlobalCtx)
hu_AESXTSIVSet = _func(c_int, c_size_t, c_uint, c_size_t, c_char_p, sb_GlobalCtx)

#----------------------------
# apply argtypes/restype to all functions
#
_dll = _register_funcs('libhuapi.so', globals())