unverif = ['user1', 'user2', 'user3', 'user4', 'user5']
verif=[]
i=0
print(f"Unverificated: {unverif}")
print(f"Verificated: {verif}\n\n")
while unverif:
    transfer=unverif.pop()
    verif.append(transfer)
    i+=1
verif.sort()
print(f"Unverificated: {unverif}")
print(f"Verificated: {verif}")
    
