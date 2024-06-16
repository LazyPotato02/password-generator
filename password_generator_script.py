import random
import array

# maximum length of password needed
# this can be changed to suit your password length

# declare arrays of the character that we need in out password
# Represented as chars to enable easy string concatenation
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

# combines all the character arrays above to form one array
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS


def get_random_choices():
    # uses random to chose symbols from the lists
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    # generates random password
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    # returns the password
    return temp_pass


def generate_password():
    MAX_LEN = int(input('Enter password length: '))
    # checks if password length is higher then 3
    while MAX_LEN <= 3:
        print("Length needs to be higher than 3")
        MAX_LEN = int(input('Enter password length: '))

    # calls the get_random_choices function, so we can generate password
    temp_pass = get_random_choices()

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

    # shuffles the password
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x

    print(password)


generate_password()

# randomly select at least one character from each character set above
