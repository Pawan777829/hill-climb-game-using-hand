# import ctypes
# import time
# import keyboard
# from ctypes import wintypes
# user32 = ctypes.WinDLL('user32', use_last_error=True)

# sendinput = ctypes.windll.user32

# right_pressed = 0x4D

# left_pressed = 0x4B

# pul = ctypes.POINTER(ctypes.c_ulong)
# class KeyBdInput(ctypes.Structure):
#     _fields_ =[("wVk",ctypes.c_ushort),
#                ("wScan", ctypes.c_ushort),
#                ("dWFlags", ctypes.c_ulong),
#                ("time",ctypes.c_ulong),
#                ("dwExtraInfo",pul)]
    
# class HardwareInput(ctypes.Structure):
#     _fields_ = [("uMsg",ctypes.c_ulong),
#                 ("uParaml",ctypes.c_ulong),
#                 ("wParamh", ctypes.c_ushort)]
    
# class MouseInput(ctypes.Structure):
#     _fields_ = [("dx",ctypes.c_ulong),
#                 ("dy",ctypes.c_ulong),
#                 ("mousedata",ctypes.c_ulong),
#                 ("dwFlags",ctypes.c_ulong),
#                 ("time",ctypes.c_ulong),
#                 ("dwExtraInfo",pul)]
    
# class input_i(ctypes.Union):
#     _fields_ = [("ki",KeyBdInput),
#                 ("mi",MouseInput),
#                 ("hi",HardwareInput)]
    
# class input(ctypes.Structure):
#     _fields_ = [("type",ctypes.c_ulong),
#                 ("ii",input_i)]

# def presskey(hexKeyCode):
#     extra = ctypes.c_ulong(0)
#     ii_ = input_i()
#     ii_.ki = KeyBdInput(0, hexKeyCode,0x0008,0,ctypes.pointer(extra))
#     x= input(ctypes.c_ulong(1),ii_)
#     ctypes.windll.user32.sendinput(1,ctypes.pointer(x),ctypes.sizeof(x))

# def releasekey(hexKeyCode): 
#     extra = ctypes.c_ulong(0)
#     ii_ =input_i()
#     ii_.ki = KeyBdInput(0, hexKeyCode,0x0008 | 0x0002,0,ctypes.pointer(extra))
#     x= input(ctypes.c_ulong(1),ii_)
#     ctypes.windll.user32.sendinput(1, ctypes.pointer(x), ctypes.sizeof(x))
    
# if __name__=='__main__':
#     while (True):
#         presskey(0x11)
#         time.sleep(1)
#         releasekey(0x11)
#         time.sleep(1)

import ctypes
import time

user32 = ctypes.WinDLL('user32', use_last_error=True)

right_pressed = 0x4D
left_pressed = 0x4B

pul = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
    _fields_ = [
        ("wVk", ctypes.c_ushort),
        ("wScan", ctypes.c_ushort),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", pul)
    ]

class HardwareInput(ctypes.Structure):
    _fields_ = [
        ("uMsg", ctypes.c_ulong),
        ("uParaml", ctypes.c_ulong),
        ("wParamh", ctypes.c_ushort)
    ]

class MouseInput(ctypes.Structure):
    _fields_ = [
        ("dx", ctypes.c_ulong),
        ("dy", ctypes.c_ulong),
        ("mousedata", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", pul)
    ]

class input_i(ctypes.Union):
    _fields_ = [
        ("ki", KeyBdInput),
        ("mi", MouseInput),
        ("hi", HardwareInput)
    ]

class input(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_ulong),
        ("ii", input_i)
    ]

def presskey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = input_i()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = input(ctypes.c_ulong(1), ii_)
    user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def releasekey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = input_i()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = input(ctypes.c_ulong(1), ii_)
    user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

if __name__ == '__main__':
    while True:
        presskey(0x11)  # Press 'W' key
        time.sleep(1)
        releasekey(0x11)  # Release 'W' key
        time.sleep(1)
