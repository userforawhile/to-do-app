contents = ["io000000000000000000",
            "tuooooooooooooooooooooo",
            "loro''''''''''''''''''''''''"]
filenames = ["uno.txt", "due.txt", "tre.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)

contents = [
    "The true meaning of obscurity lies underneath the most delicate structures of viscosity. The idea of changing that balance is obscure by itself."]
filenames = ["quattro.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)

    file = open(f"../files/quattro.txt", 'r')
    content = file.read()

    nr_chars = len(content)
    print(nr_chars)

filenames = ['1.doc', '1.report', '1.presentations']

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]


