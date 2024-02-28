import random

lowercases = "abcdefghijklmnopqrstuvwxyz"
uppercases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "-+=!@#%&*^()|/"

all_chars = lowercases + uppercases + numbers + symbols

passnum = int(input("Number of passwords to be generated: "))
passlen = int(input("Length of passwords to be generated: "))

passwords = []

for count in range(passnum):
    password = random.choice(lowercases) + random.choice(uppercases) + random.choice(numbers) + random.choice(symbols)
    password += ''.join(random.choice(all_chars) for i in range(passlen - 4))
    password_list = list(password)
    random.shuffle(password_list)
    passwords.append(''.join(password_list))

print("Passwords")
count = 1
for password in passwords:
    print(str(count) + ": " + password)
    count += 1

decision = input("Do you want to store the passwords (y/n) : ")

if decision == 'y':

    filename = input("Enter the filename to save passwords: ")
    with open(filename, 'w') as file:
        count = 1
        for password in passwords:
            file.write(f"{count}. {password}\n")
            count += 1

    print("passwords have been stored in file named",filename)

elif decision == 'n':
     print("Passwords were not stored.")

else:
    print("Invalid input")
