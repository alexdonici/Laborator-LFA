#                   1.
###########################################
#citirea fisierului de intrare "random.txt"
###########################################

def read(file):
    global starea_init
    DFA = {}
    with open(file, "r") as fin:
        tranz = {}
        stari_acc = set()
        linii = fin.readlines()
        for l in linii:
            parti = l.strip().split()
            if l != linii[-1]:
                if len(l) == 6:
                    stare, stare_urmatoare = parti
                    tranz[(stare, "")] = stare_urmatoare
                else:
                    stare, simbol, stare_urmatoare = parti
                    tranz[(stare, simbol)] = stare_urmatoare
            elif l == linii[-1]:
                for parte in parti:
                    stari_acc.add(parte)
            else:
                print(f"Linii ignorate: {l.strip()}")

        alfabet = set()
        states = set()
        for (stare, simbol) in tranz:
            alfabet.add(simbol)
            states.add(stare)
            states.add(tranz[(stare, simbol)])
        starea_init = "q" + min([x[1] for x in states])
        DFA['alphabet'] = alfabet
        DFA['states'] = states

        DFA['start_state'] = starea_init
        DFA['accept_states'] = stari_acc
        DFA['transitions'] = tranz
    return DFA


global x
x = 0



#              2.
##################################
##### GENERARE CUVINTE DFA #######
##################################



def generate_words(DFA, lungime):
    def backtrack(stare, cuv, clung):
        global x
        if clung > lungime:
            return
        if clung <= lungime and stare in DFA['accept_states']:
            print(cuv)
            x += 1
        for edge_label, stare_urm in DFA['transitions'].items():
            if stare == edge_label[0]:
                new_word = cuv + edge_label[1]
                backtrack(stare_urm, new_word, clung + 1)
            elif stare == edge_label[0] and edge_label[1] == '':
                backtrack(stare_urm, cuv, clung)

    start = DFA['start_state']
    backtrack(start, '', 0)




#               3.
###########################################
########APELAREA FUNCTIILOR-FINAL##########
###########################################



if __name__ == "__main__":
    DFA = read('random.txt')
    generate_words(DFA, 4)
