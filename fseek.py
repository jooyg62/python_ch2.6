f = open('123.txt', 'wb')
f.write(b'0123456789')
f.close()

f = open('123.txt', 'rb')
print(f.tell())

f.seek(5, 1)
data = f.read(2)
print(data)

f.seek(-5, 1)
data = f.read(3)
print(data)

f.seek(0, 2)    # 맨 끝으로 이동

f.seek(-5, 1)
data = f.read(3)
print(data)



