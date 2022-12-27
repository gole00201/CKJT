from cffi import FFI

ffibuilder = FFI()

ffibuilder.cdef(""" 
   struct Point{
        int x;
        int y;
    };
    extern int x;
    extern struct Point A;
    extern struct Point B[3];
""")


ffibuilder.set_source("_example", r"""
    struct Point{
        int x;
        int y;
    };
    struct Point B[3] = {{1,2},{3,4},{5,6}};
    int x = 10;
    struct Point A = {1,2};
""", libraries =[])


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)