import pickle


try:
    with open("logs.dat", "rb") as logs:
        pin = pickle.load(logs)
except:
    pin = 1234

def console_clear():
    import os
    os.system('cls' if os.name == 'nt' else "clear")

def logo():
    console_clear()
    print("\t----------------")
    print("\t--Bankomatikus--")
    print("\t----------------")

def login():
    
    checksum = 0
    while True:
        logo()
        print("\tVar vänlig ange PIN-kod")
        #Felhantering bokstäver
        while True:
            try:
                userpin = int(input("\tPIN: "))
                break
            #Om bokstäver används sätts felaktig userpin och låter if-satsen ta över
            except:
                checksum + checksum + 1
                userpin = 0
                break
        #Villkor för om PIN är godkänd
        if(pin == userpin):
            logo()
            input("\tRätt PIN-kod, välkommen!\n\tTryck retur för att fortsätta!")
            break
        elif(checksum == 3):
            logo()
            input("\tDu har skrivit fel kod tre gånger. Nu ringer jag SÄPO.\n\tTryck retur för att avsluta samt bli anhållen.")
            exit()
        else:
            checksum = checksum + 1
            logo()
            input("\tFel pin! Försök igen")

def charity(charity):
    charity = charity / 2
    console_clear()
    return charity

def deposit(deposit):
    while True:
        try:
            deposit = int(input("\tAnge belopp: "))
            break
        except:
            input("\tFelaktig summa.\n\tTryck retur för att fortsätta.")
            break

    if(deposit < 1):
        input("\tFelaktig summa.\n\tTransaktion ej godkänd.")
        deposit = 0
    return deposit

def withdrawal(withdrawal):
    while True:
        try:
            withdrawal = int(input("\tAnge belopp:"))
            if(withdrawal < 1):
                input("\tFelaktig summa.\n\tTransaktion ej godkänd.")
                withdrawal = 0
            break
        except:
            input("\tFelaktigt belopp.\n\tTryck retur för att fortsätta")
            break

    return withdrawal
    
def changepin():
    logo()
    global pin #Krävs för att kunna ändra variabler utanför metoden(globala variabler)
    userpin = input("\tNuvarande PIN: ")

    #Felhantering gammal pin
    if(userpin.isdigit()):
        userpin = int(userpin)
        if(pin == userpin):   
            newpin = input("\tNy PIN: ")
            #Felhantering ny pin
            if(len(newpin) != 4):
                input("\tPIN-kod måste ha 4 tecken.\n\tTryck retur för att fortsätta.")
                return
                #felhantering med len() funkar ej för integer, därav typkonversionen efteråt
            #Korrekt input
            else:
                input("\tDin nya PIN-kod är " + newpin + "\n\tKvitto på nytt PIN sparat till hårddisk.\n\tTryck retur för att fortsätta.")
                newpin = int(newpin)
                pin = newpin
                #pickle - sparar ny pin i systemet
                with open("logs.dat", "wb") as logs:
                    pickle.dump(pin, logs)
                fil = open("pin.txt", "w")
                fil.write("Din nya PIN-kod är: " + str(pin))
                fil.close()
        else:
            input("\tFel PIN!\n\tTryck retur för att fortsätta.")
    else:
        input("\tPin måste vara siffror.\n\tTryck retur för att fortsätta.")
    #pickle kan ligga även här och funktionen är densamma
    
    