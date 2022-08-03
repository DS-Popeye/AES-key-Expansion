from input_value import *
from Key_making import k1,k2,k3,k4

#For XOR Operation of row 1 Ricon table
output_a1 = k1 ^ a1 ^ 0x01
output_b1 = k2 ^ b1 ^ 0x00
output_c1 = k3 ^ c1 ^ 0x00
output_d1 = k4 ^ d1 ^ 0x00

#For XOR Operation of row 2
output_a2 = output_a1 ^ a2
output_b2 = output_b1 ^ b2
output_c2 = output_c1 ^ c2
output_d2 = output_d1 ^ d2

#For XOR Operation of row 3
output_a3 = output_a2 ^ a3
output_b3 = output_b2 ^ b3
output_c3 = output_c2 ^ c3
output_d3 = output_d2 ^ d3

#For XOR Operation of row 4
output_a4 = output_a3 ^ a4
output_b4 = output_b3 ^ b4
output_c4 = output_c3 ^ c4
output_d4 = output_d3 ^ d4

print("\n")

print(f"{(hex(output_a1))[2:].upper()} | {(hex(output_a2))[2:].upper()} | {(hex(output_a3))[2:].upper()} | {(hex(output_a4))[2:].upper()}")
print("------------------")
print(f"{(hex(output_b1))[2:].upper()} | {(hex(output_b2))[2:].upper()} | {(hex(output_b3))[2:].upper()} | {(hex(output_b4))[2:].upper()}")
print("------------------")
print(f"{(hex(output_c1))[2:].upper()} | {(hex(output_c2))[2:].upper()} | {(hex(output_c3))[2:].upper()} | {(hex(output_c4))[2:].upper()}")
print("------------------")
print(f"{(hex(output_d1))[2:].upper()} | {(hex(output_d2))[2:].upper()} | {(hex(output_d3))[2:].upper()} | {(hex(output_d4))[2:].upper()}")
