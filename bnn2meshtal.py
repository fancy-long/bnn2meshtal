import os, sys
import argparse

# creat a file in the parent folder
def file_creat(name, msg):
    desktop_path = "."
    full_path = os.path.join(desktop_path, name)
    with open(full_path, 'a') as f:
        f.writelines(msg)


def main():
    """
    Creat a meshtal file with the message of .bnn.

    Parameters:
    -----------
    filename: str
              The .bnn file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", required=True, help=".bnn file")
    args = vars(parser.parse_args())
    if args['filename'] is not None:  # Maybe redundant and can be deleted
        filename = args['filename']
        print("result will be read from {filename}")
    else:
        print("fatal error, please specify the input file")
    result = []
    error = []
    with open(filename, 'r') as fin:
        line = fin.readline()
        counts = 1
        while True:
            line = fin.readline()
            counts += 1
            if counts >= 7:
                break
            if 'X coordinate:' in line:
                itokens = line.split( ) # x��߽硢���ȡ��������������С
                x_min = float(itokens[3])
                x_max = float(itokens[5])
                x_bins = int(itokens[7])
                x_bin = float(itokens[10])
            elif 'Y coordinate:' in line: # y��߽硢���ȡ��������������С
                jtokens = line.split( )
                y_min = float(jtokens[3])
                y_max = float(jtokens[5])
                y_bins = int(jtokens[7])
                y_bin = float(jtokens[10])
            elif 'Z coordinate:' in line: # z��߽硢���ȡ��������������С
                ktokens = line.split( )
                z_min = float(ktokens[3])
                z_max = float(ktokens[5])
                z_bins = int(ktokens[7])
                z_bin = float(ktokens[10])

    with open(filename, 'r') as file:  # ��ͨ����������result, error�����б���
        line = file.readline()
        counts = 1
        while True:
            line = file.readline()
            counts += 1
            if counts <= 9:
                pass
            elif counts <= (z_bins*y_bins*x_bins/10+9):
                tokens = line.strip().split()
                result.append(tokens)
            elif counts <= (z_bins*y_bins*x_bins/10+12):
                pass
            elif counts <= (2*z_bins*y_bins*x_bins/10+12):
                tokens = line.strip().split()
                error.append(tokens)
            else:
                break
    result = [num for elem in result for num in elem]
    error = [num for elem in error for num in elem]

    i, j, k = 1, 1, 1  #�õ�������߽�����������
    x_bound = ['%.2f' %x_min]
    y_bound = ['%.2f' %y_min]
    z_bound = ['%.2f' %z_min]
    x_pos = ['%.3f' %(x_min + x_bin/2)]
    y_pos = ['%.3f' %(y_min + y_bin/2)]
    z_pos = ['%.3f' %(z_min + z_bin/2)]
    while i <= x_bins:
        x = x_min + x_bin*i
        x_bound.append('%.2f' %x)
        x_pos.append('%.3f' %(x + x_bin/2))
        i += 1
    while j <= y_bins:
        y = y_min + y_bin*j
        y_bound.append('%.2f' %y)
        y_pos.append('%.3f' %(y + y_bin/2))
        j += 1
    while k <= z_bins:
        z = z_min + z_bin*k
        z_bound.append('%.2f' %z)
        z_pos.append('%.3f' %(z + z_bin/2))
        k += 1
    x_bound = "\t".join(x_bound)
    y_bound = "\t".join(y_bound)
    z_bound = "\t".join(z_bound)

    title = ["mcnp   version 6     ld=**/**/**  probid =  **/**/** 11:07:07\n C simple fluka input\n Number of histories used for normalizing tallies =        100000.00\n\n Mesh Tally Number         4\n neutron  mesh tally.\n\n Tally bin boundaries:\n"]
    bound = [
        '    X direction:\t', x_bound, 
        '\n    Y direction:\t', y_bound, 
        '\n    Z direction:\t', z_bound,
        '\n    Energy bin boundaries: 0.00E+00 1.00E+36',
        '\n', '      X       Y      Z     Result     Rel Error\n']
    file_creat("meshtal", title) #д��̧ͷ������߽�
    file_creat("meshtal", bound)
    
    n = 0  
    with open('meshtal' ,'a') as of:  #д��������result��error
        k = 0
        while k < z_bins:
            j = 0
            while j < y_bins:
                i =0
                while i < x_bins:
                    line = ['\t', x_pos[i], '\t', y_pos[j], '\t', z_pos[k], '   ', result[n], ' ', error[n], '\n']
                    of.writelines(line)
                    i += 1
                    n += 1
                j += 1
            k += 1

if __name__ == '__main__':
    main()