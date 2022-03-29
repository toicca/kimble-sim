import numpy as np

def noppa():
    return np.random.randint(1, 7)

pelaajat = [0, 1, 2, 3]
vuorot = 0
lauta = np.zeros((len(pelaajat), 50))
alussa = [4, 4, 4, 4]
maalissa = [0, 0, 0, 0]

# aloitus
# syönti -> uusi -> liike

while (vuorot < 50):
    for pelaaja in pelaajat:

        nappulat = np.count_nonzero(lauta[pelaaja, :])
        paikat = np.where(lauta[pelaaja,:] == 1)[0]
        print(paikat)
        if not any(paikat):
            paikat = [0, 0, 0, 0]
        heitto = noppa()
        muut_pelaajat = list(pelaajat)
        muut_pelaajat.remove(pelaaja)

        if heitto == 6:
            for nappula in paikat:
                # tarkista syönti
                for vastustaja in muut_pelaajat:
                    # onko vastustajan nappula tulevassa paikassa
                    if nappula + heitto < 49 and lauta[vastustaja, nappula + heitto] == 1:
                        lauta[vastustaja, nappula + heitto] = 0
                        alussa[vastustaja] += 1
                        lauta[pelaaja, nappula + heitto] = 1   
                        break

                # tarkista aloitus
                if alussa[pelaaja] != 0:
                    print(alussa[pelaaja])
                    alussa[pelaaja] -= 1

                    heitto = noppa()
                    lauta[pelaaja, pelaaja*8] = 0
                    lauta[pelaaja, pelaaja*8 + heitto] = 1
                    break

                else:
                    # print(np.max(paikat) + heitto)

                    if np.max(paikat) + heitto >= 50:
                        maalissa[pelaaja] += 1
                        lauta[pelaaja, np.max(paikat)] = 0
                        
                    else:
                        lauta[pelaaja, np.max(paikat)] = 0
                        lauta[pelaaja, np.max(paikat) + heitto] = 1
                                 
            # voiko syödä
            # for paikat in range(pelaajat):
            #     for nappula in range(nappulat):
            #         paikka = paikat[nappula]
            #         if any()
                    
                    
            # voiko saada uuden
            # liiku
        # else:
        #     lauta[pelaaja, np.max(paikat)] = 0
        #     lauta[pelaaja, np.max(paikat) + heitto] = 1
    vuorot += 1

print()
print(lauta)
print()
print(maalissa)
    
    

