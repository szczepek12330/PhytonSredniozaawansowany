from collections import ChainMap

user_account = {"id": "PL43678fhdj", "type": "konto"}
user_profile = {"name": "Jan Kowalski", "type": "profil"}
user = ChainMap(user_account, user_profile)
print(user["id"])
print(user["name"])
user["name"] = "Pokemon"
print(user["name"])
print(user["type"]) #obiekt chainmap zwraca pierwszego z lewej

# print([3, 4, 5, 6, 7] + ["t", "o"])

value = [1, 2, 3]
value += [4, 5, 6]
# print(value)

z1 = {1, 2, 3}
z2 = {1, 4}
# print(z1 & z2)
# print(z1 | z2)
# print(z1 - z2)
# print(z1 ^ z2)

slow1 = {"1": 1}
slow2 = {"2": 2}
slow3 = {}
# print(slow1)
slow1 |= slow2
slow3 |= slow1
# print(slow1)
# print(slow3)
# print(slow1 | slow2)
# print({"1": 1} | {"1": 2, "2": 3})

