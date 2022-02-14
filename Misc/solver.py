from pwn import *
import zlib
from base64 import *

conn = remote('34.159.7.96',30441 )
i = 0
while True:
	i+=1
	print(conn.recvline())
	a = conn.recvline()
	print(a)
	hashy = a.decode("utf-8").replace("\r\n","") 
	print(hashy)
	print(hashy)
	decoded = urlsafe_b64decode(hashy)
	proof = zlib.decompress(decoded)
	print(proof)
	conn.sendline(proof)
	print(conn.recvline())
	print(i)
conn.close()
