# admin , password
admin:str = "zigzaktik"
password:str = "Time187Fly@"

times = 0
while times < 3:
    user_admin = input("what is your admin: ").strip()
    user_password = input("what is your password: ").strip()

    if user_admin == admin and user_password == password:
        print("Successfully access")
        break
    else:
        print("Please try again!")
        times += 1

if times == 3:
    print("you can not access today, please wait tomorrow")

    