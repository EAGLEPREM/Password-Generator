import random
passlen = int(input("Enter the Lenght of Password : "))
s="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
p= "".join(random.sample(s,passlen ))
print(p)