x = 3
y = '<pic_call>'
z = 'alexis'
q = '.jpg</pic_call>'
s = ''

for i in range(x):
    pic = y + z + str(i) + q
    s = s + pic
    print(pic)
print(s)    

tup = [('a', 1), ('b', 2), ('c', 3)]

len_tuple =  len(tup)

print(len_tuple)
for i in range(0, len_tuple):
    print("hello" + str(i))
