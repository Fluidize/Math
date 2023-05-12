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

if __name__ == "__main__":
    pass