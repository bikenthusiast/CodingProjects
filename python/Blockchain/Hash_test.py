import hashlib

# Der gegebene Hash
target_hash = "d3ffa2bcb37fb6c6a467512c2fa5b67e1a3106896e1592a858841bef06a40b81"

# Liste möglicher Varianten
possible_variants = [
    "Random String",
    "Random String ",
    "Random String\n",
    "Random String\r\n",
    "Random String\t",
    " Random String",
    "random string",
    "random string\n",
    "random string ",
    "Random  String",
    "RandomString",
    "Random  String ",
]

# Finde die Variante, die den Hash ergibt
for variant in possible_variants:
    hashed = hashlib.sha256(variant.encode('utf-8')).hexdigest()
    if hashed == target_hash:
        print(f"Treffer: '{variant}' -> {hashed}")
