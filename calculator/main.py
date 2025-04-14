import standard_calculator.stdcal as std
print(std.add(5,6))
print(std.sub(9,8))
print(std.multiply(22,33))
print(std.division(25,5))

import scientific_calculator.scical as sci
print(sci.sqrt(4))
print(sci.power(3,4))
print(sci.log(10))
print(sci.sine(30))
print(sci.cosine(60))
print(sci.tangent(45))

import programmers_calculator.prgcal as prg
print(prg.convert_number("0xFF", "hex", "dec")) 
print(prg.bitwise_operations("0b1010", "0b1100", "and"))   
print(prg.bitwise_operations("10", "2", "lshift")) 
print(prg.bitwise_operations("0xFF", op="not")) 