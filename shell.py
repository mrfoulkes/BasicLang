import basic

while True:
    text = input('basic > ')
    if text == 'end': break
    if text.strip() == "": continue
    if text.strip()[0] == '#': continue  # hit endless loop without this line.
    result, error = basic.run('<stdin>', text)

    if error: print(error.as_string())
    elif result: 
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))

