import math
import time
print("*/*/*/*/*/*/*/*/matvid*/*/*/*/*/*/*/*")
time.sleep(5)
a=float(input("weight in grams of the projectile : "))
b=float(input("speed in m/s of the projectile: "))
c=float(input("caliber of the bullet: "))
d=int(math.sqrt(((a*b)/c)*202.5))
print("the bullet will come about ",d,"meters")
time.sleep(5)
