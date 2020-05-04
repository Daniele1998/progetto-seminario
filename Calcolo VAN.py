Rd = 0.10
C = 10000
T = 0.24
D = 3000000
E = 10000000
V = D + E
Re = 0.40
W = Rd * (1 - T) * (D / V) + Re * (E / V)
print(W)
CFa1 = 6000
CFa2 = 4000
CFa3 = 3500
CFa4 = 3000
CFa5 = 2500
Vana = (CFa1 / (1 + W)) + (CFa2 / (1 + W) ** 2) + (CFa3 / (1 + W) ** 3) + (CFa4 / (1 + W) ** 4) + (
            CFa5 / (1 + W) ** 5) - C
print(Vana)
CFb1 = 3000
CFb2 = 3500
CFb3 = 4000
CFb4 = 4500
CFb5 = 5000
Vanb = (CFb1 / (1 + W)) + (CFb2 / (1 + W) ** 2) + (CFb3 / (1 + W) ** 3) + (CFb4 / (1 + W) ** 4) + (
            CFb5 / (1 + W) ** 5) - C
print(Vanb)
if Vana > Vanb:
    print("Better A")
else:
    print("Better B")

