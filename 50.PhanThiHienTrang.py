def ceasar(plaintext, k):
    S = ""
    for i in plaintext:
        if i.isalpha():
            base = ord("A") if i.isupper() else ord("a")
            S = S + (chr((ord(i) - base + k) % 26 + base))
        else:
            S = S + i
    return S

K = 50   
plaintext = "PhanThiHienTrang"
ciphertext = ceasar(plaintext, K)
print(ciphertext)
