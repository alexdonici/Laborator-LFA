if nrL > 1:
exprf = input("Input: ")
for i in expr:
simb = set()
for j in i:
if j != '(' and j!= ')' and j!= '*' and j!= '+':


expr.append(input(f"L{i+1}: "))

simb.add(j)nrL = int(input("Introduceti numarul de limbaje: "))
print("Introduceti: ")
expr = []
exprf = ''
for i in range (nrL):

