def b2d(n):
  power = 0
  decnum = 0
  while n > 0:
    decnum += 2**power * n%10
    n//10
    power+=1
  return decnum

print(b2d(101011))