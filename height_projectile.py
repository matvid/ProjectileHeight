import math
import time
print("                    **//**//**//**//**//**//**//**//**//**//**//**")
print("                    **//**//**//**//**//**//**//**//**//**//**//**")
print("                    **//**//**//**//**//**//**//**//**//**//**//**")
print("                    **//**//**//**//**//**//**//**//**//**//**//**")
a=float(input("peso in grammi del proiettile: "))
b=float(input("velocita' in m/s del proiettile: "))
c=float(input("calibro del proiettile: "))
d=int(math.sqrt(((a*b)/c)*202.5))
print("il proiettile arrivera' a circa ",d,"metri")
time.sleep(5)
