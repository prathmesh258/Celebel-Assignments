#Find Angle MBC

import math
ab = int(input())
bc = int(input())
hypotenuse=math.sqrt(ab**2+bc**2)
MBC=math.acos(bc/hypotenuse )
degree=chr(176)#for using degree symbol
print(str(round(math.degrees(MBC)))+degree)
