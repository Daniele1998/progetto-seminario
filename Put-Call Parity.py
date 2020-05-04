K = 52
S = 50
rf = 0.05
t = 1
P = 12
UP = 0.25
DOWN = 0.5
C = P + S - (K/(1 + rf) * t)
print(C)
PayoffUP = K - (S * (1 + UP)) - P
PayoffDOWN = K - (S * (1 - DOWN)) - P
print(PayoffUP)
print(PayoffDOWN)
if PayoffUP > 0:
    print("Si esercita")
else:
    print("Non si esercita")
if PayoffDOWN > 0:
    print("Si esercita")
else:
    print("Non si esercita")