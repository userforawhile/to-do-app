password = input("Enter a new password:")

results = {}

if len(password) >= 8:
    results["length"] = True

else:
    results["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

results["digits"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

results["uppercase"] = uppercase
print(results)

if all(results.values()):
    print('Strong Password')
else:
    print('Weak Password')