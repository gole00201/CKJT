import cffi 
import _s.lib
#Работаем с данными инициализированными в библиотеке
print("Перменная x: ", _s.lib.x)
dot = _s.lib.B[0]
array_s = _s.lib.B
size = _s.ffi.sizeof(array_s) / _s.ffi.sizeof(dot)
print("Масив структур: ")
for i in range(int(size)):
    print("[ " , _s.lib.B[i].x , _s.lib.B[i].y, " ]")