import chapters as chap
import game_classes as gc

pack_5 = gc.TextPack(5)

while True:
    
    print("\n \n        Anything But The Machine \n--(0)New Game \n--(1)Enter Password \n--(2)Info \n--(3)Quit")
    
    s = input(" ")
    if s == "0":
        chap.chapter_1()
    if s == "1":
        code = input("Enter Password  ")
        for i in chap.keychain.keys():
            if code in chap.keychain[i]:
                code = i
                break
            else:
                print("Incorrect Password")
                break
        if code == 2:
            chap.chapter_2()
        if code == 3:
            chap.chapter_3()
        if code == 4:
            chap.end()
    if s == "2":
        print("\n\n"+pack_5.expo)
    if s == "3":
        break