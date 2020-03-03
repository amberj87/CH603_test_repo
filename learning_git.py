def subtract(a,b):
  c=a-b
  return(c)

def addition(a,b):
  if(a>b):
    c=a+b
  else:
    c=a-b
  return(c)

print("Hello World")
a=1.0
b=3.0
print(a+b)
print("adding using function")
print(addition(a,b))
print("subtracting using function")
print(subtract(a,b))

c=a*b
print("This version has added more changes")
print(c*c)
