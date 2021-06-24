import random
import string

def passgen(lenght):
  power= string.ascii_letters + string.digits + string.punctuation
  password="".join(random.choice(power) for i in range(lenght))
  print(password)

  
print("PASSWORD GENERATOR !!!!!!")
lenght=int(input("Enter the Lenght"))
passgen(lenght)
