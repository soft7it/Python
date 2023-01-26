class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"


p1 = Person("John", 36)
p2 = Person("Ahon", 13)
p3 = Person("Maia", 21)

print(p1)
print(p2)
print(p3)
