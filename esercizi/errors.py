try:
    width = float(input('enter rectangle width:'))
    length = float(input('enter a rectangle length:'))
    if width == length:
        exit("that look like a square")
    area = width * length
    print(area)
except ValueError:
    print('please enter a valid number')