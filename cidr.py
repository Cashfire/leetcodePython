

def find_subnet(ips):
    n = len(ips)
    bits_list = [[0 for i in range(n)] for j in range(32)]
    for col in range(n):
        tmp = [bin(int(x)+256)[3:] for x in ips[col].split('.')]
        row = 0
        for bits in tmp:
            for b in bits:
                bits_list[row][col] = int(b)
                row += 1
    print(bits_list)

    for row in range(32):
        row_sum = sum(bits_list[row])
        if row_sum == 0 or row_sum == n:
            continue
        else:
            return row
    return row

if __name__ == "__main__":
    ips1 = [ "10.0.4.128", "10.0.4.129", "10.0.4.130", "10.0.4.131" ]
    ips2 = ['10.0.1.33', '10.0.1.34']#, '10.0.1.125']
    ips3 = ['10.0.2.126', '10.0.2.125']
    print(find_subnet(ips3))
    # print([bin(int(x)+256)[3:] for x in "10.0.4.128".split('.')])
