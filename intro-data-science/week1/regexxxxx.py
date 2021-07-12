import re

a = "This is a good day"

print(re.search("goo", a))
print(re.search("good", a))
print(re.search("gsxs", a))

a = "Bora works diligently. Bora gets good grades. Our student Bora is successful"

print(re.search("Bora", a))
print(re.search("^Bora", a))
print(re.split("Bora", a))
print(re.findall("Bora", a))
print(len(re.findall("Bora", a)))

a = "ACAAAABCBCBAA"

print(re.findall("B", a))
print(re.findall("[AB]", a)) # A or B
print(re.findall("[A][BC]", a))
print(re.findall("[A][B-C]", a))
print(re.findall("AB|AC", a))
print(re.findall("^A", a))
print(re.findall("[^A]", a))
print(re.findall("^[^A]", a))
print(re.findall("A{2,10}", a))
print(re.findall("A{2,2}", a))
print(re.findall("A{2}", a))
print(re.findall("AA", a))
print(re.findall("A{2, 2}", a)) # NO SPACE !!!!!!
print(re.findall("A{2,10}", a))
print(re.findall("A{1,10}B{1,10}C{1,10}", a))
print(re.findall("[A]*", a))
print(re.findall("A*", a))
print(re.findall("[A]+", a))
print(re.findall("A+", a))

with open("ferpa.txt", "r") as file:
	wiki = file.read()
	#print(wiki)

print(re.findall("[a-zA-Z]{1,100}\[edit\]", wiki))
print(re.findall("[\w]{1,100}\[edit\]", wiki))
print(re.findall("[\w]*\[edit\]", wiki))
print(re.findall("[\w ]*\[edit\]", wiki))

for title in re.findall("[\w ]*\[edit\]", wiki):
	print(re.split("[\[]", title)[0])


#groups

print(re.findall("([\w ]*)(\[edit\])", wiki))

print("------------------------------------------")

for item in re.finditer("([\w ]*)(\[edit\])", wiki):
	print(item.groups())
	print(item.group())
	print(item.group(0))
	print(item.group(1))
	print(item.group(2))

print("------------------------------------------")

for item in re.finditer("(?P<title>[\w ]*)(?P<edit_link>\[edit\])", wiki):
	print(item.groupdict())
	print(item.groupdict()["title"])

