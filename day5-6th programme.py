def delchar(s,c):
  k = s.replace(c,"")
  return k
f = input("Enter string: ")
x = input("Enter element to be removed: ")
print(delchar(f,x))
