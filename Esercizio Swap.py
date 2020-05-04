t = 5
N = 65000000
TF = 0.056
TV = 0.0725
iTF = N * TF
print(iTF)
iTV = N * TV
print(iTV)
P = iTV - iTF
print(P)
S = P * ((1/TV) - (1/(TV * (1 + TV) ** t)))
print(S)