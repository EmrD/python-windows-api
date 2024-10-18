import ctypes
import time

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

hdc = user32.GetDC(0)

left = width // 2 - 25
top = height // 2 - 25
right = left + 50
bottom = top + 50

red_brush = gdi32.CreateSolidBrush(0x0000FF) 
gdi32.SelectObject(hdc, red_brush)
gdi32.Rectangle(hdc, left, top, right, bottom)

user32.ReleaseDC(0, hdc)