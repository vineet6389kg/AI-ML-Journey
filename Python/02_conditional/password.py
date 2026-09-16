password = "lalu@123"

if len(password) < 6:
    strenth = "Weak"
elif len(password) <= 10 :
    strenth = "Medium"
else:
    strenth = "Strong"

print("Password Strenth is", strenth)