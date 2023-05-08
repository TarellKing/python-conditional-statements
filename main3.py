# Adventure Game Tarell King
print("You are lost underground in a maze of tunnels")
import random
dangerTunnel = random.randint(1,4)
firstTunnel = (1)
secondTunnel = (2)
thirdTunnel = (3)
fourthTunnel = (4)
#print("dragon in tunnel", dangerTunnel)
tunnelChoice = int(input("Choose tunnel 1 through 4:"))

tunnelChoice = 0
while tunnelChoice < 1 or tunnelChoice > 5:
     tunnelChoice = int(input("Choose tunnel 1 through 4:"))



print("You chose tunnel", tunnelChoice)

if tunnelChoice == dangerTunnel:
    print("You entered a tunnel with a dragon. Watch out!")

if tunnelChoice == firstTunnel:
    print("You entered an empty tunnel. You are safe..for now")

if tunnelChoice == secondTunnel:
    print("You entered an empty tunnel. You are safe..for now")

if tunnelChoice == thirdTunnel:
    print("You entered an empty tunnel. You are safe..for now")

if tunnelChoice == fourthTunnel:
    print("You entered an empty tunnel. You are safe..for now")

