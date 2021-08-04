x = 4
print hex(id(x))

### bytes[] to short[]
temp = len(byte_arr)//2
short_arr = struct.unpack('>'+'h'*temp, byte_arr)
# option H: unsigned short
# option h: short
# option <: little endian
# option >: big  endian
