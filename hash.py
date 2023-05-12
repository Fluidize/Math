import hashlib

def checksum(binary, alg="sha1"):
    if isinstance(binary, str) or isinstance(binary, int):
        binary = str.encode(str(binary))

    if alg == "sha1":
        return hashlib.sha1(binary).hexdigest()
    if alg == "sha256":
        return hashlib.sha256(binary).hexdigest()
    if alg == "sha512":
        return hashlib.sha512(binary).hexdigest()

def convert_base(inp, inp_base, outp_base):
    #to make iterable
    inp = str(inp)
    print(inp,inp_base,outp_base)
    if inp_base < outp_base:
        outp = 0
        for digit_count, digit in enumerate(inp):
            outp += (inp_base**digit_count)*int(digit)
    
    return outp


if __name__ == "__main__":
    print(convert_base(111111, 10, 3))