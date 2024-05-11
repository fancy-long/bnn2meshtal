
import os
import argparse

title = "      X coordinate: from  0.0000E+00 to  1.0000E+01 cm,    10 bins ( 1.0000E+00 cm wide)\n      Y coordinate: from  0.0000E+00 to  1.0000E+01 cm,    10 bins ( 1.0000E+00 cm wide)";
x=title.split( );
# print (x);
print(x[3], '\n')

f=open("./README.md", "r")
line1 = f.readline()
counts = 1
list = []
while counts <= 5:
    # print(line1, end="")
    counts += 1
    line1 = f.readline()
    tokens = line1.split()
    list.extend(tokens)
print(list)
print('\n')
f.close


# creat a file in the parent folder
def file_creat(name, msg):
    desktop_path = "."
    full_path = os.path.join(desktop_path, name)
    f=open(full_path, 'a')
    f.write(msg)
    f.close()

#title = "mcnp   version 6     ld=**/**/**  probid =  **/**/** 11:07:07\n C simple fluka input\n Number of histories used for normalizing tallies =        100000.00\n\n Mesh Tally Number         4\n neutron  mesh tally.\n\n Tally bin boundaries:"
#bound = "    X direction:\t"
#file_creat('meshtal', title)

i, j, k = 1, 1, 1  #�õ�������߽�
x_min=1
y_min=2
z_min=3
x_bin=0.1
y_bin=0.2
z_bin=0.3
x_bins, y_bins, z_bins=10, 10, 10
x_bound = ['%.2f' %(x_min + x_bin/2)]
y_bound = ['%.2f' %y_min]
z_bound = [str('%.2f' %z_min)]
while i <= x_bins:
    x = x_min + x_bin*i
    x_bound.append('%.2f' %(x + x_bin/2))
    i += 1
while j <= y_bins:
    y = y_min + y_bin*j
    y_bound.append('%.2f' %y)
    j += 1
while k <= z_bins:
    z = z_min + z_bin*k
    z_bound.append('%.2f' %z)
    k += 1
#x_bound_str=map(str, x_bound)
#x_bound_str = [str(a) for a in x_bound]
# x_bound = "\t".join(x_bound)
print(x_bound, y_bound, z_bound)
print('\n', type(x_bound[2]))
print(x_bound[3])

a = 3*3*3/10
print ('\n', type(a))

