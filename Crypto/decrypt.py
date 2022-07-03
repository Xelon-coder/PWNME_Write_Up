# uncompyle6 version 3.5.0
# Python bytecode 3.8 (3413)
# Decompiled from: Python 2.7.5 (default, Nov 16 2020, 22:23:17) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)]
# Embedded file name: C:\Users\Express\Documents\Toronto\challrev.py
# Size of source mod 2**32: 555 bytes
from Cryptodome.Util.number import long_to_bytes, bytes_to_long
from pwn import xor

def decrypt(first,xor):
    reverse_first = first[::-1]
    print(reverse_first)
    print(int(reverse_first)^xor)
    print(long_to_bytes(int(reverse_first)^xor))
    decrypt("219516015989366871732728605936755197601",13)
    decrypt("2130689570892075754234400430874403925069147738764347075321",37)