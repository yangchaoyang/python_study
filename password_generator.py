import randomchar

def generate_password(length):
    if length < 4:
        raise ValueError('密码至少4位')

    random_char = randomchar.RandomChar()

    password = random_char.uppercase()
    password += random_char.lowercase()
    password += random_char.digit()
    password += random_char.special()

    count = 5
    while count <= length:
        password += random_char.anyone()
        count += 1

    return password


password_length = input('请输入密码长度（8 ~ 20）：')
password_length = int(password_length)

if password_length < 8 or password_length > 20:
    raise ValueError('密码长度不符')

password = generate_password(password_length)
print(password)