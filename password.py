import re

def check_password_complexity(passwords):
    complex=5
    
    if len(passwords)<8:
        complex-=1
        print("\nYour password length must be more than 8")
    if not re.search("[a-z]",passwords):
         complex-=1
         print("\nYour password must contain atleast one lower case character")
    if not re.search('[A-Z]',passwords):
           complex-=1
           print('\nYour password must contain atleast one upper case character')
    if not re.search('[0-9]',passwords):
            complex-=1
            print('\nYour password must contain atleast one numerical character')
    if not re.search('[!@#$%^&*(),.?\":{}|<>]',passwords): 
            complex-=1
            print('\nYour password must contain atleast one special character (!@#$%^&*(),.?\":{}|<>)')
    return complex
      

password=input("\nEnter your password to check its complexity\n")
result=check_password_complexity(password)
print("\nYour password strength(on scale of 0-5) is : ", result)
if result<=2:
    print("\nYour password is weak\n")
elif result<=4:
    print("\nYour password is moderate\n")
else:
    print("\nYour password is strong\n")


    
