import funk
import pickle

#Laddar in sparat saldo om möjligt, annars except
try:
    with open("data.dat", "rb") as data:
        saldo = pickle.load(data)
except:
    saldo = 0

#Inloggningsskärm
funk.login()

#Menysystem
while True:
    funk.logo()
    print("\n\tSaldo: " + str(saldo))
    print("\n\t1. Insättning")
    print("\t2. Uttag")
    print("\t3. Skänk hälften till välgörenhet") #Funk behövs
    print("\t4. Byt PIN-kod")
    print("\t5. Avsluta\n")
    choice = 0
    
    while True: #Menyvalsinput med undantagshantering
        try:
            choice = int(input("\tMenyval: "))
            if choice < 1 or choice > 5:
                input("\tVal ej giltigt.\n\tTryck retur för att fortsätta.")
                break
            else:
                break
        except:
            input("\tEndast siffror.\n\tTryck retur för att fortsätta.")
            break

    #Menyvalen
    #Insättning
    if(choice == 1):
        saldo = saldo + funk.deposit(saldo)
    #Uttag
    elif(choice == 2):
        withdrawal = funk.withdrawal(saldo)
        if(withdrawal > saldo):
            withdrawal = 0
            print("\tTäckning saknas")
            input()
            funk.console_clear()
        else:
            saldo = saldo - withdrawal
    #Välgörenhet
    elif choice == 3:
        saldo = funk.charity(saldo)
    elif choice == 4:
        funk.changepin()
    #Avsluta
    elif(choice == 5):
        funk.logo()
        print("\tHejdå!")
        input()
        break

#Spara saldo
with open("data.dat", "wb") as data:
    pickle.dump(saldo, data)



