# This is the second day of a 90 day challenge
# Today am working on a credentials validator that checks if credentials are true or not

user_email = "Admin@test.com"
user_password = "1234"

print("Welcome to Credentials login \n\n")

email = input("Enter Email: ")
password = input("Enter Password: ")

if email==user_email and password == user_password:
    login_message ="Logged in Successfully ✅"
elif email!=user_email and password != user_password:
     login_message = "Both your email and password are wrong ❌"
elif email !=user_email:
    login_message = "Your email is wrong ❗️"
else:
    login_message = "Your password is wrong ❗️"
print(f"\n{login_message}")



