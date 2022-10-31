from cffi import FFI

C = FFI()
#Подружаем весь хэдр 
with open("struct.h") as file:
    C.cdef(file.read())
#Устанавливаем источники и подключаем библиотеку
C.set_source("_s", '#include "struct.h"', libraries = ['./struct'], library_dirs = ['./'])
#Компилируем "обвязку" под уже созданную билиотеку
if __name__ == "__main__":
    C.compile(verbose=True)