# with open("binary", 'bw') as bin_file:
#     for i in range(17):
#         bin_file.write(bytes([i]))
#
# with open("binary",'br') as bin_read:
#     for b in bin_read:
#         print(b)

a = 65534   # FF FE
b = 65535   # FF FF
c = 65536   # 00 01 00 00
x = 2998302 # 00 2D C0 1E

with open("binary2", 'bw') as bin_write:
    bin_write.write(a.to_bytes(2, 'big'))
    bin_write.write(b.to_bytes(2, 'big'))
    bin_write.write(c.to_bytes(4, 'big'))
    bin_write.write(x.to_bytes(4, 'big'))
    bin_write.write(x.to_bytes(4, 'little'))
    
with open("binary2", 'br') as bin_read:
    e = int.from_bytes(bin_read.read(2), 'big')
    print(e)
    f = int.from_bytes(bin_read.read(2), 'big')
    print(f)
    g = int.from_bytes(bin_read.read(4), 'big')
    print(g)
    h = int.from_bytes(bin_read.read(4), 'big')
    print(h)
    i = int.from_bytes(bin_read.read(4), 'big')
    print(i)
