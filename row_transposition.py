import math

# User Input and Preprocessing
key = input("Enter numeric key (e.g., 31542): ").strip()
plain_text = input("Enter plain text (Letters only): ").lower().replace(" ", "")

key_digits = [int(k) for k in key]
len_key = len(key_digits)
len_plain = len(plain_text)

row = int(math.ceil(len_plain / len_key))
matrix = [['X'] * len_key for _ in range(row)]

# Fill matrix row-wise with plaintext
t = 0
for r in range(row):
    for c in range(len_key):
        if t < len_plain:
            matrix[r][c] = plain_text[t]
            t += 1

# Encryption
cipher_text = ''
# Get column order based on numeric key (1-based positions)
col_order = [key_digits.index(i + 1) for i in range(len_key)]

for c in col_order:
    for r in range(row):
        cipher_text += matrix[r][c]

print("\nEncryption")
print("Plain text is :", plain_text)
print("Cipher text is:", cipher_text)

# Decryption
# Fill columns of matrix based on key order
matrix_new = [['X'] * len_key for _ in range(row)]

t = 0
for c in col_order:
    for r in range(row):
        if t < len(cipher_text):
            matrix_new[r][c] = cipher_text[t]
            t += 1

# Read matrix row-wise to get plain text
decrypted_text = ''
for r in range(row):
    for c in range(len_key):
        if matrix_new[r][c] != 'X':
            decrypted_text += matrix_new[r][c]

print("\nDecryption")
print("Cipher text is:", cipher_text)
print("Plain text is :", decrypted_text)
