# dumps() : Encryption
# loads() : Decryption

'''
1. JSON
2. pickle
'''

import json

file = open("enc_deCry.txt", "a+")
data = {
    "fullName": "hehe",
    "id": 2345678,
    "password": "hahaha"
}

# print(f"Original data: {data}")
# print(f"Type of original data: {type (data)}")

enc_data = json.dumps(data)
file.write(enc_data)

file.seek(0)

encReadData = file.read()
print(encReadData, type(encReadData))

ori_data = json.loads(encReadData)
print(ori_data, type(ori_data))

# print(f"Encrypted data: {enc_data}")
# print(f"Type of Encrypted data: {type (enc_data)}")

# dec_data = json.loads(enc_data)
# print(f"Decrypted data: {dec_data}")
# print(f"Type of Decrypted data: {type (dec_data)}")

file.close()


# Replace json with pickle for pickle