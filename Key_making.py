from input_value import a4,b4,c4,d4
import pandas as pd
import ast
df = pd.read_csv("s_box.csv")

shift_row1 = hex(b4)
shift_row2 = hex(c4)
shift_row3 = hex(d4)
shift_row4 = hex(a4)

#Some tecnique for K1
Hexa_column11 = (shift_row1[2:3]).upper()
hexa_p3 = f"0x{Hexa_column11}"
Hexa_column12 = shift_row1[3:].upper()
hexa_p4 = f"0x{Hexa_column12}"

#Tecnique for Hexadecimal to Decimal
column1 = ast.literal_eval(hexa_p3)
row1 = ast.literal_eval(hexa_p4)

#s-box value
key1 = df.iloc[column1,row1]
print((f"AES s-box A = {key1}").upper())

#--------------------------------------------------------------------------

#Some tecnique for K2
hexa_col21 = (shift_row2[2:3]).upper()
hex_col211 = f"0x{hexa_col21}"
hexa_row22 = shift_row2[3:].upper()
hex_row222 = f"0x{hexa_row22}"

#Tecnique for Hexadecimal to Decimal
column2 = ast.literal_eval(hex_col211)
row2 = ast.literal_eval(hex_row222)

#s-box value
key2 = df.iloc[column2,row2]
print((f"AES s-box B = {key2}").upper())

#-----------------------------------------------------------------

#Some tecnique for K3
hexa_col31 = (shift_row3[2:3]).upper()
hex_col311 = f"0x{hexa_col31}"
hexa_row32 = shift_row3[3:].upper()
hex_row322 = f"0x{hexa_row32}"

#Tecnique for Hexadecimal to Decimal
column3 = ast.literal_eval(hex_col311)
row3 = ast.literal_eval(hex_row322)
#s-box value
key3 = df.iloc[column3,row3]
print((f"AES s-box c = {key3}").upper())

#----------------------------------------------------------

#Some tecnique for K3
hexa_col41 = (shift_row4[2:3]).upper()
hex_col411 = f"0x{hexa_col41}"
hexa_row42 = shift_row4[3:].upper()
hex_row422 = f"0x{hexa_row42}"

#Tecnique for Hexadecimal to Decimal
column4 = ast.literal_eval(hex_col411)
row4 = ast.literal_eval(hex_row422)
#s-box value
key4 = (df.iloc[column4,row4])
print((f"AES s-box D = {key4}").upper())

#------------------------------------

#Texnique for string to hex k1
hex_string1 = key1
an_integer1 = int(hex_string1, 16)
k1 = an_integer1
#k1 = hex(an_integer1)



#Texnique for string to hex k1
hex_string2 = key2
an_integer2 = int(hex_string2, 16)
k2 = an_integer2
#k2 = hex(an_integer2)

#Texnique for string to hex k1
hex_string3 = key3
an_integer3 = int(hex_string3, 16)
k3 = an_integer3
#k3 = hex(an_integer3)


#Texnique for string to hex k1
hex_string4 = key4
an_integer4 = int(hex_string4, 16)
k4 = an_integer4
#k4 = hex(an_integer4)