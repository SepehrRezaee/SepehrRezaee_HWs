#At first, we give a password from user.
password = input("please enter your password: ")

#Secondly, we check the password for understanding that is strong or not.
upper = any([char.isupper() for char in password])
lower = any([char.islower() for char in password])
digit = any([char.isdigit() for char in password])
special_chr = any([password.find("!")+1 , password.find("@")+1 ,
    password.find("#")+1 , password.find("$")+1 , password.find("%")+1,
    password.find("^")+1 , password.find("&")+1, password.find("*")+1,
    password.find("(")+1 , password.find(")")+1 , password.find("-")+1 ,
    password.find("+")+1])

#Finally, we print the result of checking.
print("STRONG password:)") if all([upper,lower,digit,special_chr,len(password) >= 6]) else print("not a STRONG password:)")