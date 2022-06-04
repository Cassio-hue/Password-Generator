import random
import time
import os

def randomLetters():
    letters = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    random_num = random.randint(0,22)
    random_choice = random.randint(0, 1)
    return letters[random_choice][random_num]

def randomNumber():
    return str(random.randint(0,9))

def randomSpecialChars():
    special_char = '@<}$|&)=*(\{#]%[+>/?!'
    return special_char[random.randint(0, len(special_char)-1)]

def menu():
    print(f' {"#"*79}#')
    print(f' #{" "*77} #')
    print(f' # {" "*28} PASSWORD GENERATOR {" "*28} #')
    print(f' #{" "*77} #')
    print(f' {"#"*79}#')
    print('\n Choose password type')
    print(' |  L  => Only letters')
    print(' |  N  => Only numbers')
    print(' |  C  => Only special characters')
    print(' | LN  => Letters and numbers')
    print(' | LC  => Letters and special characters')
    print(' | NC  => Numbers and special characters')
    print(' | LNC => Letters, numbers and special characters')
    print()

os.system('cls' if os.name == 'nt' else 'clear')

menu()
while True:
    while True:
        while True:
            typeOf = input(' Type: ')
            if typeOf in ['L', 'l', 'N', 'n', 'C', 'c', 'LN', 'Ln', 'ln', 'LC', 'Lc', 'lc', 'NC', 'Nc', 'nc', 'LNC', 'Lnc', 'lnc']:
                break
            else:
                print( 'Password type is incorrect, enter it again below.\n')

        print('\n How long is your password?')
        while True:
            try:
                length = int(input(' Number of characters: '))
                break
            except:
                print(" I didn't understand, try again...\n")

        password = ''

        if typeOf == 'L' or typeOf == 'l':
            for _ in range(length):
                password += randomLetters()

        elif typeOf == 'N' or typeOf == 'n':
            for _ in range(length):
                password += randomNumber()

        elif typeOf == 'C' or typeOf == 'c':
            for _ in range(length):
                password += randomSpecialChars()

        elif typeOf == 'LN' or typeOf == 'ln':
            for _ in range(length):
                options = [randomNumber(), randomLetters()]
                random_num = random.randint(0, 1)
                password += options[random_num]

        elif typeOf == 'LC' or typeOf == 'lc':
            for _ in range(length):
                options = [randomLetters(), randomSpecialChars()]
                random_num = random.randint(0, 1)
                password += options[random_num]

        elif typeOf == 'NC' or typeOf == 'nc':
            for _ in range(length):
                options = [randomNumber(), randomSpecialChars()]
                random_num = random.randint(0, 1)
                password += options[random_num]

        elif typeOf == 'LNC' or typeOf == 'lnc':
            for _ in range(length):
                options = [randomLetters(), randomNumber(), randomSpecialChars()]
                random_num = random.randint(0, 2)
                password += options[random_num]

        print()
        tam = len(f' #  Your password is: {password}  #')-1
        print(f' {"#"*tam}')
        print(f' #{" "*(tam-2)}#')
        print(f' #  Your password is: {password}  #')
        print(f' #{" "*(tam-2)}#')
        print(f' {"#"*tam}')
        print()
        print(" If you didn't like this password, you can generate another one if you want.")
        tryAgain = input(' Generate other password [Yes / No]: ')

        if tryAgain == 'Yes' or tryAgain == 'yes' or tryAgain == 'Y' or tryAgain == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            menu()
            continue
        else:
            break

    print()
    name = input(' Name your password: ')
    print()

    time.sleep(1)

    with open('./passwords.txt', 'a', encoding='utf-8') as arq:
        linha = f'{name}: {password}\n'
        arq.write(linha)

    time.sleep(.5)

    print(' Your password was saved!')
    print()
    print(' Generate another password?')
    continuar = input(' [Yes / No]: ')
    print()
    if continuar == 'Yes' or continuar == 'yes' or continuar == 'Y' or continuar == 'y':
        continue
    else:
        break