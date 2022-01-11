from hashlib import sha256

ign = input("Enter your username: ")
print("Your csjh weight is", int(sha256(ign.encode('utf-8')).hexdigest(), 16) % 32000, "points! Wow! :)")
