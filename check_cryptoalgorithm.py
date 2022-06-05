import paramiko
import sys

# ssh로 crypto경로 검색 및 파일 다운(다운받은 파일 경로는 localpath에 저장 후 반환)


def file_upload():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('49.236.137.77', '7730', 'root', 'ubuntu')

    cmd = 'find -name "crypto*"'

    (stdin, stdout, stderr) = ssh.exec_command(cmd)
    output = stdout.readlines()
    # print(output)

    # remotepath 슬라이싱
    remotepath = str(output)
    remotepath = remotepath[3:len(remotepath)-4]
    # print(remotepath)

    # get - 파일 다운 '/root/KHN-893NA/proc/crypto.txt'
    remotepath = "/root" + remotepath
    localpath = './/crypto2.txt'
    sftp = ssh.open_sftp()
    sftp.get(remotepath, localpath)
    #print('sftp success\n')
    ssh.close()

    return localpath

# path = localpath(crypto.txt파일 저장 경로) / crypto 파일 열어서 'name:'목록 추출하고 crypto 리스트에 저장 후 반환


def file_extract_namecrypto(path):
    localpath = path
    fcrypto = open(localpath, 'r')
    lines = fcrypto.readlines()
    cryptotmp = []
    crypto = []

    # 'name:'목록 획득
    for line in lines:
        item = line.replace(" ", "")
        cryptotmp.append(item)

    cryptotmp = [s for s in cryptotmp if "name:" in s]

    for i in cryptotmp:
        item = i.replace("name:", "")
        crypto.append(item.replace("\n", ""))

    fcrypto.close()
    # print(crypto)
    return crypto

# cryptoalgoritm check함수 / crypto 리스트를 통해서 안전하지 않은 or 안전한 알고리즘인지 검사


def cryptoalgorithm_check(crypto):
    check = 1  # 안전한 알고리즘 사용 중 표시 = 1 / x = 0
    hash_sum = 0
    publickey_sum = 0
    symmetrickey_sum = 0
    ecrypto_sum = 0

    # ecrypto -> 실제 crypto list
    #ecrypto = ["ecb(arc4)", "stdrng", "lzo", "crc32c", "zlib", "deflate", "arc4", "aes", "twofish", "des3_ede", "des", "sha1", "md5", "md4"]

    # xcrypto -> 사용하면 안되는 암호 알고리즘
    xcrypto = ["DES", "des", "Des", "double length Triple DES", "MD-5", "md-5", "Md-5", "md5", "Sha-1",
               "sha1", "sha-1", "SHA-1", "xor", "Xor", "XOR", "Checksum", "checksum", "BASE64", "Base64"]

    # hash -> 사용 가능한 hash 알고리즘
    #hash = ["SHA-256","SHA-384","SHA-512","SHA-512/224","SHA-512/256","SHA3-224","SHA3-256","SHA3-384","SHA3-512","LSH-224","LSH-256","LSH-384","LSH-512","LSH-512-224","LSH-512-256"]
    hash = ["Sha-224", "Sha_224", "Sha224", "Sha 224", "sha-224", "sha_224", "sha224", "sha 224", "SHA-224", "SHA_224", "SHA224", "SHA 224",
            "Sha-384", "Sha_384", "Sha384", "Sha 384", "sha-384", "sha_384", "sha384", "sha 384", "SHA-384", "SHA_384", "SHA384", "SHA 384",
            "Sha-512", "Sha_512", "Sha512", "Sha 512", "sha-512", "sha_512", "sha512", "sha 512", "SHA-512", "SHA_512", "SHA512", "SHA 512",
            "Sha-512/224", "Sha_512/224", "Sha512/224", "Sha 512/224", "sha-512/224", "sha_512/224", "sha512/224", "sha 512/224", "SHA-512/224", "SHA_512/224", "SHA512/224", "SHA 512/224",
            "Sha-512/256", "Sha_512/256", "Sha512/256", "Sha 512/256", "sha-512/256", "sha_512/256", "sha512/256", "sha 512/256", "SHA-512/256", "SHA_512/256", "SHA512/256", "SHA 512/256",
            "Sha3-224", "Sha3_224", "Sha3224", "Sha3 224", "sha3-224", "sha3_224", "sha3224", "sha3 224", "SHA3-224", "SHA3_224", "SHA3224", "SHA3 224",
            "Sha3-256", "Sha3_256", "Sha3256", "Sha3 256", "sha3-256", "sha3_256", "sha3256", "sha3 256", "SHA3-256", "SHA3_256", "SHA3256", "SHA3 256",
            "Sha3-384", "Sha3_384", "Sha3384", "Sha3 384", "sha3-384", "sha3_384", "sha3384", "sha3 384", "SHA3-384", "SHA3_384", "SHA3384", "SHA3 384",
            "Sha3-512", "Sha3_512", "Sha3512", "Sha3 512", "sha3-512", "sha3_512", "sha3512", "sha3 512", "SHA3-512", "SHA3_512", "SHA3512", "SHA3 512",
            "Lsh-224", "Lsh_224", "Lsh224", "Lsh 224", "lsh-224", "lsh_224", "lsh224", "lsh 224", "LSH-224", "LSH_224", "LSH224", "LSH 224",
            "Lsh-256", "Lsh_256", "Lsh256", "Lsh 256", "lsh-256", "lsh_256", "lsh256", "lsh 256", "LSH-256", "LSH_256", "LSH256", "LSH 256",
            "Lsh-384", "Lsh_384", "Lsh384", "Lsh 384", "lsh-384", "lsh_384", "lsh384", "lsh 384", "LSH-384", "LSH_384", "LSH384", "LSH 384",
            "Lsh-512", "Lsh_512", "Lsh512", "Lsh 512", "lsh-512", "lsh_512", "lsh512", "lsh 512", "LSH-512", "LSH_512", "LSH512", "LSH 512",
            "Lsh-512/224", "Lsh_512/224", "Lsh512/224", "Lsh 512/224", "lsh-512/224", "lsh_512/224", "lsh512/224", "lsh 512/224", "LSH-512/224", "LSH_512/224", "LSH512/224", "LSH 512/224",
            "Lsh-512/256", "Lsh_512/256", "Lsh512/256", "Lsh 512/256", "lsh-512/256", "lsh_512/256", "lsh512/256", "lsh 512/256", "LSH-512/256", "LSH_512/256", "LSH512/256", "LSH 512/256"]
    # pubickey -> 사용가능한 공개키 알고리즘
    #publickey =["DH","ECDH","RSAES","RSA-PSS","KCDSA","ECDSA","EC-KCDSA"]
    publickey = ["DH", "Dh", "dh", "ECDH", "Ecdh", "ecdh", "RSAES", "Rsaes", "rsaes", "RSA-PSS", "RSA_PSS", "RSA PSS", "RSA-Pss", "RSA-pss", "RSA_Pss", "RSA_pss", "RSA Pss", "RSA pss", "Rsa-PSS", "Rsa_PSS", "Rsa PSS", "Rsa-Pss", "Rsa-pss", "Rsa_Pss", "Rsa_pss", "Rsa Pss", "Rsa pss", "rsa-PSS", "rsa_PSS", "rsa PSS", "rsa-Pss", "rsa-pss", "rsa_Pss", "rsa_pss", "rsa Pss", "rsa pss",
                 "KCDSA", "Kcdsa", "kcdsa", "ECDSA", "Ecdsa", "ecdsa", "EC-KCDSA", "EC_KCDSA", "EC KCDSA", "EC-Kcdsa", "EC-kcdsa", "EC_Kcdsa", "EC_kcdsa", "EC Kcdsa", "EC kcdsa", "Ec-KCDSA", "Ec_KCDSA", "Ec KCDSA", "Ec-Kcdsa", "Ec-kcdsa", "Ec_Kcdsa", "Ec_kcdsa", "Ec Kcdsa", "Ec kcdsa", "ec-KCDSA", "ec_KCDSA", "ec KCDSA", "ec-KCDSA", "ec-kcdsa", "ec_Kcdsa", "ec_kcdsa", "ec Kcdsa", "ec kcdsa"]
    # symmetrickey -> 사용한 대칭키 알고리즘
    #symmetrickey = ["SEED","HIGHT","ARIA-128","ARIA-192","ARIA-256","LEA-128","LEA-192","LEA-256"]
    symmetrickey = ["SEED", "Seed", "seed", "HIGHT", "Hight", "hight", "ARIA-128", "ARIA_128", "ARIA 128", "ARIA128", "Aria-128", "Aria_128", "Aria 128", "Aria128", "aria-128", "aria_128", "aria 128", "aria128", "ARIA-192", "ARIA_192", "ARIA 192", "ARIA192", "Aria-192", "Aria_192", "Aria 192", "Aria192", "aria-192", "aria_192", "aria 192", "aria192", "ARIA-256", "ARIA_256", "ARIA 256", "ARIA256", "Aria-256", "Aria_256", "Aria 256", "Aria256",
                    "aria-256", "aria_256", "aria 256", "aria256", "LEA-128", "LEA_128", "LEA 128", "LEA128", "Lea-128", "Lea_128", "Lea 128", "Lea128", "lea-128", "lea_128", "lea 128", "lea128", "LEA-192", "LEA_192", "LEA 192", "LEA192", "Lea-192", "Lea_192", "Lea 192", "Lea192", "lea-192", "lea_192", "lea 192", "lea192", "LEA-256", "LEA_256", "LEA 256", "LEA256", "Lea-256", "Lea_256", "Lea 256", "Lea256", "lea-256", "lea_256", "lea 256", "lea256"]

    crypto_len = len(crypto)
    # print(crypto_len)

    # xcrypto = 사용 금지 / xcrypto 형식 암호알고리즘이 존재하면 0, 존재하지 않으면 1
    for i in crypto:
        if i in xcrypto:
            check = 0
            return 0

    # hash, publickey, symmetrickey(by.kisa) 리스트에 존재하는 알고리즘을 모두 사용했다면 암호알고리즘 양호상태 return 1
    if check == 1:
        for i in crypto:
            if i in hash:
                hash_sum += 1
            if i in publickey:
                publickey_sum += 1
            if i in symmetrickey:
                symmetrickey_sum += 1

    check_sum = hash_sum + publickey_sum + symmetrickey_sum
    if check_sum == crypto_len:
        return 1
    else:
        return 0


# main

def return_res():
    path = file_upload()
    #print("local path: ",path)
    crypto = []
    crypto = file_extract_namecrypto(path)
    #print("crypto: ",crypto)
    result = cryptoalgorithm_check(crypto)
    #print("result(0->unsafe, 1->safe): ",result)
    return result
