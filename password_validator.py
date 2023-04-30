'''
PASSWORD VALIDATOR

The function verifies if the password is between 8 and 16 characters, letters and numbers
Made by Alessandro Silvestri © 2022 <alessandro.silvestri.work@gmail.com>
'''

MIN_PASSWORD_LENGHT = 8
MAX_PASSWORD_LENGHT = 16
user_pw = ''

def check_pw2(pw:str):
    return MIN_PASSWORD_LENGHT <= len(pw) <= MAX_PASSWORD_LENGHT and not \
    pw.isnumeric() and not \
    pw.isalpha()

while not check_pw2(user_pw):
    user_pw = input('''insert a valid password: letters, numbers and between 8 - 16 characters: -> ''')
    if check_pw2(user_pw.lower()):
        print('Done! Password ok')
