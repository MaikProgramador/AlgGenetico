import time # importa a biblioteca time
import os

#funcçao++++++++++++++++++++++++++++
def limpar():
    return os.system('clear')

def tempo():
    return time.sleep(1)

def tempo2():
    return time.sleep(2)

def tempo3():
    return time.sleep(1.5)
#++++++++++++++++++++++++++++++++++++


#Interação e registro login++++++++++
MAIK = "Maik: (◣ _ ◢) "
LIPE = "Lipe: 💢 "
PASSI = "Passi: 😊 "
EMILY = "Emily: 👧 "
MARIANA = "Mari: ☣ "
#+++++++++++++++++++++++++++++++++++++

#prints iniciar
INICIAR = "🎉" *10
PRONTO = "START"
TELEFONE = "Telefone TOCANDO 💢 📱💢"

#+++++++++++++++++++++++++++++++++++++
#INICIANDO +++++++++++++++++++++++++++

print(f"{INICIAR}"*4)
print(f"{INICIAR}"*4)
start = input("Clique em [I] para 'Festa' ou [D] para 'Dormir': ")
limpar()
iniciar = start == "i" or start == "I"

if iniciar:
    print("======== INICIANDO ========")
    tempo()
    limpar()

    print("============ 1 ============")
    tempo()
    limpar()

    print("============ 2 ============")
    tempo()
    limpar()
    
    print("============ 3 ============")
    tempo()
    limpar()
    print("INICIANDO...AGUARDE")
    tempo2()
    limpar()

    print(f"{MAIK} VAMOS PARA FESTAAA!!")
    tempo()
    print(".........")
    tempo()
    limpar()

    time.sleep(1)
    print(f"{TELEFONE}")

else:
    print(f"{LIPE}VAI PERDER MESMO A FESTA??")
    tempo3()
    print(".......")
    tempo3()
    limpar()

    certeza = input("Tem certeza?: [S] ou [N]")
    if certeza == "N" or certeza == "n":
        print(f"{LIPE}Ainda bem, preciso de vc aqui!")

