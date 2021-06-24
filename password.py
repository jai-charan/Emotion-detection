import random
import string

def passgen(lenght):
   power=string.ascii_letters + string.digits + string.punctuation
   password="".join(random.sample(power,lenght))
   print(password)



lenght=int(input("Enter the Lenght"))
passgen(lenght)
