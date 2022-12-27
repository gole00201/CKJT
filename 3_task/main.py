import cffi
import _example.lib
#обращение к переменной 
dot = _example.lib.x
print("Переменная x:", dot)
print("Массив структур B: ")
for i in range(int(_example.ffi.sizeof(_example.lib.B) / _example.ffi.sizeof(_example.lib.B[0]))):
    print("[" , _example.lib.B[i].x , _example.lib.B[i].y, "]")
