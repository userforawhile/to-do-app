# program that convert feet in meter
from esercizi.funzioni.converters import convert
from esercizi.funzioni.parsers import parse

feet_inches = input('Enter a new inches:')

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print('Kid is too small')
else:
    print('Kid can use the slide')
