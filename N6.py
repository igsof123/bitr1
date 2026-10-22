SPECIALS ="!@#$%^&*"

def check_password(password):
    problems = []

    if len(password) < 8:
        problems.append("длина меньше 8 символов")
    if not any(c.isupper() for c in password):
        problems.append("нет заглавных букв")
    if not any(c.islower() for c in password):
        problems.append("нет строчных букв")
    if not any(c.isdigit() for c in password):
        problems.append("нет цифр")
    if not any(c in SPECIALS for c in password):
        problems.append("нет спецсимволов")

    if problems:
        return "не соответствует требованиям (" + ", ".join(problems) + ")"

    n = len(password)
    if n <= 10:
        return "слабый"
    if n <= 15:
        return "средний"
    return "сильный"



print(check_password("Password123!"))   # средний
print(check_password("password"))       # не соответствует требованиям (нет заглавных букв, нет цифр, нет спецсимволов)
print(check_password("Abcdef1!"))       # слабый
print(check_password("Abcxfsakgsgsdhsd!"))  # сильный