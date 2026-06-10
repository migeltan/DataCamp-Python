
# Normal Import
print("Normal Import")
import IPT.Midterms.A6_LABS_SW.calc as calc

from IPT.Midterms.A6_LABS_SW.calc import mul
print("Multiplication:", mul(10, 5))

print("Addition:      ", calc.add(10, 5))
print("Subtraction:   ", calc.subtract(10, 5))

print("Division:      ", calc.divide(10, 5))
print("Modulo:        ", calc.modulo(10, 5))
 
# Selective Import
print("\nSelective Import")
from IPT.Midterms.A6_LABS_SW.calc import add, multiply, modulo
print("Addition:      ", add(8, 2))
print("Multiplication:", multiply(8, 2))
print("Modulo:        ", modulo(8, 2))
 
# Import with Alias
print("\nImport with Alias")
import IPT.Midterms.A6_LABS_SW.calc as c
print("Addition:", c.add(6, 3))
print("Division:", c.divide(6, 3))
print("Modulo:  ", c.modulo(6, 3))
 
# Import All
print("\nImport All")
from IPT.Midterms.A6_LABS_SW.calc import *
print("Subtraction:   ", subtract(9, 4))
print("Multiplication:", multiply(9, 4))
print("Modulo:        ", modulo(9, 4))