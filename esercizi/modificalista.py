
# list comprehension example
filenames = ['1.doc', '1.report', '1.presentations']

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

print(filenames)



print(names)

names = ["john smith", "jay santi", "eva kuki"]
names = [name.title() for name in names]
print(names)