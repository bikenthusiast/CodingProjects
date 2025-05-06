import hashlib

content = "Random String"
hash_object = hashlib.sha256(content.encode('utf-8'))
hex_dig = hash_object.hexdigest()
print(f"Content: '{content}'")


print(f"Hashed String: {hex_dig}")