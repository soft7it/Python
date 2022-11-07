
age = 1990

now_year = 2022
x = now_year - age
#check_age = int(input("When are you born ? :"))
#x = check_age - age
  
if x >= 1 and x <= 3:
  print(f"You have {x} years", "", "baby") 
elif x >= 4 and x <= 9:
  print(f"You have {x} years", "", "kid") 
elif x >= 10 and x <=15:
  print(f"You have {x} years", "", "teen") 
elif x >= 16 and x <= 18:
  print(f"You have {x} years", "", "young") 
elif x >= 19 and x <= 50:
  print(f"You have {x} years", "", "adult" ) 
else:
  print(f"You have {x} years", "", "old") 

