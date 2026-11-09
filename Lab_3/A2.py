import string

password = input()
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'

reliable = True
if len(password) != 8:
    print("Длина пароля не равна 8")
    reliable = False
if password == password.lower():
    print("В пароле отсутствуют заглавные буквы")
    reliable = False
if password == password.upper():
    print("В пароле отсутствуют строчные буквы")
    reliable = False
if not any(symbol.isdigit() for symbol in password):
    print("В пароле отсутствуют цифры")
    reliable = False
if not any(symbol in '*-#' for symbol in password):
    print("В пароле отсутствуют специальные символы")
    reliable = False
if not all(symbol in allowed for symbol in password):
    print("В пароле используются непредусмотренные символы")
    reliable = False
if reliable:
    print("Надежный пароль")