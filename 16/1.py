d={
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
        }

#ip = 'input_test.txt'

#with open(ip, 'r') as f:
#    pass

#h = 'D2FE28'
#h = '38006F45291200'
#h = 'EE00D40C823060'
#h='8A004A801A8002F478'
#h='620080001611562C8802118E34'
#h='C0015000016115A2E0802F182340'
#h='A0016C880162017C3686B18A3D4780'
h='0052E4A00905271049796FB8872A0D25B9FB746893847236200B4F0BCE5194401C9B9E3F9C63992C8931A65A1CCC0D222100511A00BCBA647D98BE29A397005E55064A9DFEEC86600BD002AF2343A91A1CCE773C26600D126B69D15A6793BFCE2775D9E4A9002AB86339B5F9AB411A15CCAF10055B3EFFC00BCCE730112FA6620076268CE5CDA1FCEB69005A3800D24F4DB66E53F074F811802729733E0040E5C5E5C5C8015F9613937B83F23B278724068018014A00588014005519801EC04B220116CC0402000EAEC03519801A402B30801A802138801400170A0046A800C10001AB37FD8EB805D1C266963E95A4D1A5FF9719FEF7FDB4FB2DB29008CD2BAFA3D005CD31EB4EF2EBE4F4235DF78C66009E80293AE9310D3FCBFBCA440144580273BAEE17E55B66508803C2E0087E630F72BCD5E71B32CCFBBE2800017A2C2803D272BCBCD12BD599BC874B939004B5400964AE84A6C1E7538004CD300623AC6C882600E4328F710CC01C82D1B228980292ECD600B48E0526E506F700760CCC468012E68402324F9668028200C41E8A30E00010D8B11E62F98029801AB88039116344340004323EC48873233E72A36402504CB75006EA00084C7B895198001098D91AE2190065933AA6EB41AD0042626A93135681A400804CB54C0318032200E47B8F71C0001098810D61D8002111B228468000E5269324AD1ECF7C519B86309F35A46200A1660A280150968A4CB45365A03F3DDBAE980233407E00A80021719A1B4181006E1547D87C6008E0043337EC434C32BDE487A4AE08800D34BC3DEA974F35C20100BE723F1197F59E662FDB45824AA1D2DDCDFA2D29EBB69005072E5F2EDF3C0B244F30E0600AE00203229D229B342CC007EC95F5D6E200202615D000FB92CE7A7A402354EE0DAC0141007E20C5E87A200F4318EB0C'
b = "".join([d[_] for _ in h])
print(b)

vsum = 0

def read_package(b):
    ver = int(b[0:3], 2)
    b = b[3:]
    tid = int(b[0:3], 2)
    b = b[3:]
    #print(ver, tid)
    if tid==4:
        b = read_num_package(ver, tid, b)
    else:
        b = read_op_package(ver, tid, b)
    return b

def read_op_package(ver, tid, b):
    global vsum
    vsum += ver
    print('op', b)
    lid = b[0]
    b = b[1:]
    if lid == '0': # next 15 bits are totel length of sub packages in bits
        n_bits = int(b[:15], 2)
        b = b[15:]
        package_bits=b[:n_bits]
        print(ver, tid, n_bits, 'p bits', b)
        while package_bits is not None and len(package_bits) > 0:
            package_bits = read_package(package_bits)
        b =  b[n_bits:]
    elif lid == '1': # next 11 bits are number of sub packages imm contained
        n_packets = int(b[:11], 2)
        b = b[11:]
        print(ver, tid, n_packets, 'ps', b)
        for i in range(n_packets):
            b = read_package(b)
    return b

def read_num_package(ver, tid, b):
    global vsum
    vsum += ver
    print('num', b)
    plen = 0
    bits = ''
    while True:
        start = b[0]
        rest = b[1:5]
        b = b[5:]
        bits += rest
        plen += 5
        if start == '0':
            break
    #empty_bits = plen%4
    #b = b[empty_bits:]
    num = int(bits, 2)
    print(ver, tid, num, b)
    return b

read_package(b)
print(vsum)

exit()

while len(b) > 0:
    ver = int(b[0:3], 2)
    vsum+= ver
    b = b[3:]
    tid = int(b[0:3], 2)
    b = b[3:]
    if tid == 4:
        plen = 0
        bits = ''
        while True:
            start = b[0]
            rest = b[1:5]
            b = b[5:]
            bits += rest
            plen += 5
            if start == '0':
                break
        empty_bits = plen%4
        b = b[empty_bits:]
        num = int(bits, 2)
        print(ver, tid, num, b)
    else:
        lid = b[0]
        b = b[1:]
        n_bits = None
        n_packets = None
        if lid == '0': # next 15 bits are totel length of sub packages in bits
            n_bits = int(b[:15], 2)
            b = b[15:]
        if lid == '1': # next 11 bits are number of sub packages imm contained
            n_packets = int(b[:11], 2)
            b = b[11:]
        print(ver, tid, n_bits, n_packets, b)

print(vsum) 
