#18. WAP to demonstrate string immutability in Python

msg = "hellostudents"
print("Given String: ", msg)
msg ='H'+msg[1:5] +'S'+msg[6:]
print("New msg: ",msg)
print(msg[0:5])