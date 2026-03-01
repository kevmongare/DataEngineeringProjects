#this is a recap for Conditionals — write program to validate user credentials

stored_email = "admin@test.com"
stored_password = "admin"

email = input(("Share User Email: "))
password = input(("Share your User Password: "))

print(("Welcome To Test Login Site!! \n\n"))

if email==stored_email and password == stored_password:
    print("Logged in Successfully")
elif email !=stored_email and password !=stored_password:
    print("Failed to Login Both your email and password are wrong")
elif email==stored_email and password != stored_password:
    print("Password is wrong")
else:
    print("Your Email is wrong")