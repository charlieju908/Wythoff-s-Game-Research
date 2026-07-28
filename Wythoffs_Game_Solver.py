NumCalc = 2
NearFactor = 0
DeadNum = 0
Connector = 0
Diff = 0
FirstMove = True
Invalid = True
PrevNum1 = 0
PrevNum2 = 0
Num1 = 0
Num2 = 0
Diagonal = True
index = 0
def PastConnector(Connector,Past):
    Series = []
    GrowthFactor = 1
    for i in range(1, (Connector + 1)):
        Series.append(i)
    for x in Series:
        if x == "X":
            continue
        elif x != "X":
            if not (x + GrowthFactor > Connector):
                Series.insert((x-1 + GrowthFactor),"X")
                Series.remove((x + GrowthFactor))
                GrowthFactor += 1
    for i in range(len(Series)):
        if "X" in Series:
            Series.remove("X")


    return Series[(-1 - Past)]

def FindPair(Num1, Num2):
    used = set()
    index = 1
    connector = 1
    while True:
        while connector in used:
            connector += 1
        dead = connector + index
        if Num1 == connector and Num2 == dead:
            return (Num1, dead, True, index, True)
        if Num1 == connector and Num2 > dead:
            return (Num1, dead, True, index,False)
        if Num1 == connector and Num2 < dead:
            return (Num1, Num2, True, index, False) 
        if Num1 == dead:
            return (Num1, connector, True, index,False)
        if connector > Num1:
            return (Num1, Num2, False, index,False)
        used.add(connector)
        used.add(dead)
        connector += 1
        index += 1



while True:
    if Invalid == False:
        PrevNum1 = Num1
        PrevNum2 = Num2
    Num1, Num2 = map(int, input("Enter the two numbers: ").replace(" ", "").split(","))
    if FirstMove == False:
        if (Num1 > PrevNum1) or (Num2 > PrevNum2) and PrevNum1 != 0 and PrevNum2 != 0:
            print("Cannot increase numbers. Try again.")
            Invalid = True
            continue
        if (PrevNum1 - Num1) != 0 and (PrevNum2 - Num2) != 0:
            if  (PrevNum1 - Num1) != (PrevNum2 - Num2):
                print("Cannot take two different amounts. Try again.")
                Invalid = True
                continue
    if Num1 > Num2:
        Temp = Num2
        Num2 = Num1
        Num1 = Temp
    Num1, Num2, Diagonal, index, zugzwang = FindPair(Num1, Num2)
    if Num1 > Num2:
        Temp = Num2
        Num2 = Num1
        Num1 = Temp

    for i in range((int(Num1/13) + 1)):
        Invalid = False
        FirstMove = False
        if Num1 == Num2:
            print(f"Computer subtracts {Num1} from both. Computer wins!!!")
            Num1 = 0
            Num2 = 0
            break
        if Num1 == 0:
            print(f"Computer takes {Num2} from {Num2}. Computer Wins!!!")
            break
        if Num2 == 0:
            print(f"Computer takes {Num1} from {Num1}. Computer Wins!!!")
            break
        if Num1 == 1 or Num2 == 1 or Num1 == 2 or Num2 == 2:
            if Num1 == 1:
                Num2 = 2
                print(f"The new numbers are {Num1}, {int(Num2)}.")
                break
            if Num1 == 2:
                Num2 = 1
                print(f"The new numbers are {Num1}, {int(Num2)}.")
                break
            if Num2 == 1:
                Num1 = 2
                print(f"The new numbers are {Num1}, {int(Num2)}.")
                break
            if Num2 == 2:
                Num1 = 1
                print(f"The new numbers are {Num1}, {int(Num2)}.")
                break
        if Diagonal == False:
            if zugzwang == True:
                    print("Computer says you go first!")
                    break
            else:
                print(f"The new numbers are {Num1} and {Num2}")
                break



            ### CONNECTOR CODE ###


        elif Diagonal == True:
            if zugzwang == True:
                print("Computer says you go first!")
                break

            else:
                Diff = Num1 - PastConnector(Num1, ((Num1+index)-Num2))
                Num1 -= Diff
                Num2 -= Diff
                print(f"The new numbers are {Num1}, {int(Num2)}.")
                break
            
