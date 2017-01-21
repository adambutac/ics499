import sys, math 

usage='Usage: python Sytale.py [encrypt | decrypt] <modulus>  <message>'
debug = True

def encrypt_1(mod, msg):

    width = math.ceil(len(msg)/mod)
    msg += (' ' * (mod*width - len(msg)))
    mlist= list(msg)

    strip = [[] * width for i in range(mod)]
    for i in range(mod):
        strip[i] = mlist[0:width]
        mlist = mlist[width:]
        if(debug):
            print(''.join(strip[i]))

    strop = [[] * mod for i in range(width)]
    for i in range(width):
        for j in range(mod):
            strop[i].append(strip[j].pop(0))
        if(debug):
            print(''.join(strop[i]))

    result = ''
    for s in strop:
        result += ''.join(s)

    return result

def encrypt(mod, msg):

    width = math.ceil(len(msg)/mod)
    msg += (' ' * (mod*width - len(msg)))
    mlist= list(msg)
    olist = [' '] * len(mlist)
     
    for i in range(mod):
        olist[i::mod] = mlist[:width] 
        mlist = mlist[width:]

    return ''.join(olist)

def decrypt(mod, msg):
    
    result = ''
    for i in range(mod):
        result += msg[::mod]
        msg = msg[1:]

    return result
        
def main():
    if(len(sys.argv) != 4):
        sys.exit(usage)

    fnc = sys.argv[1]
    mod = sys.argv[2]
    msg = sys.argv[3]

    try:
        if('.' in mod):
            raise ValueError('Non integer modulus exception.')
        if('-' in mod):
            raise ValueError('Negative modulus exception.')

        mod = int(mod)
        if(mod < 2):
            raise ValueError('Minimum modulus exception.')

    except ValueError:
        print('The modulus must be a number greater than or equal to 2. (no decimals, no negative numbers)')
        sys.exit(usage) 
    
    if(len(msg) < 3):
        print('This algorithm requires a message with more than a few characters. Your message will remain unchanged.')
    if(len(msg) <= mod):
        print('The modulus should be less than the length of the message but it is not. The message will be unaffected by this algorithm.')

    result = ''

    if(fnc == 'encrypt' or fnc == 'encode'):
        result = encrypt(mod, msg) 
        if(debug):
            print('[debug] Original:' + decrypt(mod, result))

    elif(fnc == 'decrypt' or fnc == 'decode'):
        result = decrypt(mod, msg)
        if(debug):
            print('[debug] Original:' + encrypt(mod,result))

    if(debug):
        print('[debug] Result  :' + result)
    else:
        print(result)
main()
