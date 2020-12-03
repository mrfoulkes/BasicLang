import basic

while True:
    text = input('basic > ')
    if text == 'end': break
    result, error = basic.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)


# while True:
#     text = '5 + 3'
#     if text == 'end': break
#     result, error = basic.run('<stdin>', text)

#     if error: print(error.as_string())
#     else: print(result)
#     break
