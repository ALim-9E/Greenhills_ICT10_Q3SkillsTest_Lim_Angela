from pyscript import display, document

def signing_up(e):
    document.getElementById('output').innerHTML = ' '

    user = document.getElementById('username').value
    password = document.getElementById('password').value

    user_length = len(user)
    pass_length = len(password)

    if user_length < 7:
        display(f'Your username must be atleast seven characters', target='output')
    
    if pass_length < 10:
        display(f'Your password must be atleast 10 characters', target='output')
    elif not any(char.isalpha() for char in password):
        display('Password must have at least 1 letter', target='output')
    elif not any(char.isdigit() for char in password):
        display('Password must have at least 1 number', target='output')
    else:
        display(f'You are now signed in!', target='output')