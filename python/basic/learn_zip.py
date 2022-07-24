# 複雑なzip

S = ['A', 'B', 'C', 'D', 'E']
L = {
    "0": {
        "address": "Tokyo",
        "sex": "man",
    },
    "1": {
        "address": "Osaka",
        "sex": "woman",
    },
}

dic_0 = {s: l for s, l in zip(S, L.items())}
print(dic_0)
# {'A': ('0', {'address': 'Tokyo', 'sex': 'man'}), 'B': ('1', {'address': 'Osaka', 'sex': 'woman'})}

dic_1 = {s: l[1]["address"] for s, l in zip(S, L.items())}
print(dic_1)
# {'A': 'Tokyo', 'B': 'Osaka'}
