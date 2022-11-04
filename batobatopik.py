import random

#BATO BATO PIK GAME

print("\n\n----- BATO BATO PIK GAME -----\n")
print("0. Bato\n1. Gunting\n2. Papel\n")

while True:
    pamato = int(input("Pumili ng pamato: "))

    bato = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

    gunting = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

    papel =("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

    laro = [bato, gunting, papel]

    print("\nAng pinili mo ay: ")
    print(laro[pamato])

    bot = random.randint(0,2)
    print("\nAng pinili ng kompyuter ay: ")
    print(laro[bot])


    if pamato >= 3 or pamato < 0:
        print("Maling input!")
    elif pamato == 0 and bot == 2:
        print("Ikaw ay panalo!")
    elif bot == 0 and pamato == 2:
        print("Ikaw ay talo.")
    elif bot > pamato:
        print("Ikaw ay talo.")
    elif pamato > bot:
        print("Ikaw ay panalo.")
    elif bot == pamato:
        print("Patas lamang.")