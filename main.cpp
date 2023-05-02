nrL = int(input("Introduceti numarul de limbaje: "))
print("Introduceti, pe rand, expresia fiecarui limbaj: ")
expr = []
exprf = ''
for i in range (nrL):
expr.append(input(f"L{i+1}: "))
if nrL > 1:
exprf = input("Indroduceti expresia operatiilor dintre limbaje: ")
for i in expr:
simb = set()
for j in i:
if j != '(' and j!= ')' and j!= '*' and j!= '+':
simb.add(j)