def gship(weight):
  if weight <= 2:
    return weight*1.50+20
  elif weight>2 and weight <= 6:
    return weight*3+20
  elif weight>6 and weight <= 10:
    return (weight*4)+20
  elif weight > 10:
    return weight*4.75+20

print(gship(8.4));

prem_gship = 125

def dship(weight):
  if weight <= 2:
    return weight*4.50
  elif weight>2 and weight <= 6:
    return weight*9.00
  elif weight>6 and weight <= 10:
    return (weight*12.00)
  elif weight > 10:
    return weight*14.25
  
print(dship(1.5))

def cheapship(weight):
  if gship(weight)<dship(weight) and gship(weight)<prem_gship:
    print("Ground shipping method is the cheaptest and it will cost {} USD".format(gship(weight)))
  elif dship(weight)<gship(weight) and dship(weight)<prem_gship:
    print("Drone shipping method is the cheaptest and it will cost {} USD".format(dship(weight)))
  elif prem_gship<gship(weight) and prem_gship<dship(weight):
    print("Premium shipping method is the cheaptest and it will cost {} USD".format(prem_gship))

cheapship(41.8);