def patato_fun():
	print("patato is fun")

melih = "melih"

for i in melih:
	print(i)

tup = (1, 'z', None, 1.0, patato_fun, ('x', 2), [1, 2], [1, "papa"], {"anne" : 1, "baba" : 2})

for i in tup:
	print(type(i))

x = [1, 'a', 2, "b", 3.3]

print(x)

x = x * 2;
x += ["bet", 3]

print(x)

print(1 in x)

x = "This is a string"

print(x[1:5:2])

name = "salih bora ozturk"

mail = name.split(' ')[-1] + name[0] + str(19) + "@itu.edu.tr"

print(mail)

x = {'patato' : 1, 'bora' : 2}

x["bobo"] = None

for name in x:
	print(x[name])

for val in x.values():
	print(val)

for name, val in x.items():
	print(name + " : " + str(val))


x = ["pa", "ta", "to"]

pa, ta, to = x

print(pa)
print(ta)

