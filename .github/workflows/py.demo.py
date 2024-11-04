def decide(floor1, passenger, floor2):
  if floor1 - passenger < floor2 - person:
    return floor1 
  elif floor2 - passenger < floor1 - person:
    return floor2 


def main():
  floor1 = int(input("Floor 1: "))
  floor2 = int(input("Floor 2: "))
  person = int(input("What floor is the passanger located on? "))
  decide(floor1, passenger, floor2)
