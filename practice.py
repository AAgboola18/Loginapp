import random
Firstname = input(str("First Name"))
Surname = input(str("Surname"))
First_letter = Firstname[0]
Username = First_letter.upper() + Surname.lower()
whole_user = Username + random.randint(100)
print(whole_user)