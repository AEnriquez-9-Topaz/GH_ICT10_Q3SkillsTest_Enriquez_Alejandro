from pyscript import display, document #If statements for Sign up Page

def verify(e):
    document.getElementById('output1').innerHTML = ''  # Clear previous output

    username = document.getElementById('Name').value 
    password = document.getElementById('Pass').value
    
    #Nested If statements to accomodate all conditions
    if len(username) >= 7 and len(password)>= 10:
        if not password.isalpha(): #If there are no letters in password
            if password.isdigit():
                display(f'Please add letters to your password', target='output1')
            else: #Condition for successful signup
                display(f'Your signup is valid! Congrats, {username}, and enjoy the intramurals!', target='output1')
        elif password.isalpha():
            display(f'Your password has no digits, please add numbers.', target='output1')
    elif not len(password)>= 10 and len(username)>= 7: #If only username length is valid
        display(f'Your password is too short, please make a new one.', target='output1')
    elif not len(username)>= 7 and len(password)>= 10: #If only password length is valid
        display(f'Your username is too short, please make a new one.', target='output1')
    else:
        display(f'Please lengthen both your password and username.', target='output1') 




        

     
    



    
