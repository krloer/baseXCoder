BASE32_ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
'2', '3', '4', '5', '6', '7', '='] 

BASE32_LOWER_ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/', '=']

def base32_encoder(text):
    b = ""
    for c in text:
        a = bin(ord(c)).replace("0b", "")
        while (len(a) < 8):
            a = "0" + a
        b += a

    result = ""
    i = 0
    values = 0
    while (i < len(b)):
        a = b[i:i+5] 
        while (len(a) < 5):
            a += "0"
        a = int(a, 2)
        result += BASE32_LOWER_ALPHABET[a]
        i += 6
        values += 1
    
    pad = 8 - (values % 8)
    
    for i in range(pad):
        result += "="
    return result

def base32_decoder(encoded):
    b = ""
    for c in encoded:
        a = bin(BASE32_LOWER_ALPHABET.index(c)).replace("0b", "")
        while (len(a) < 5):
            a = "0" + a
        b += a
    result = ""
    i = 0
    while (i < len(b)):
        a = b[i:i+8]
        a = int(a, 2)
        result += chr(a)
        i += 8
    return result