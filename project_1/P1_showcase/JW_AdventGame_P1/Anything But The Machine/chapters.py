import random

import game_classes as gc

keychain = {2:["FFD209","PKL164","ADG050"], 3:["FGH483","BMZ912","LLW125"], 4:["RPQ569","GLB862","AXW119"]}

#Each chapter is a scripted sequence where an instantiated Scene() object is created,
#populated with GameObjects(), and then used for all different types of loops that 
#create changes within the scene itself until finally calling the next chapter.


def get_key(chapter):
    codes = keychain[chapter].copy()
    random.shuffle(codes)
    if chapter != 4:
        print("\n\nPassword to Chapter "+str(chapter)+": "+codes[0])
    else:
        print("\n\nPassword to end: "+codes[0])

def end():

    hub = gc.EndGame()
    a = hub.play()
    get_key(4)


def chapter_3():


    hub = gc.SecondReturn()
    a = hub.play()

    if a == True:
        
        pack_3 = gc.TextPack(3)
        
        print(pack_3.expo)
        
        scene = gc.Scene("You are in a dark void.")
        
        woman = gc.Npc("woman", "A small old woman.", "Hm?", pack_3.convo["woman"], scene, False)
        phone = gc.Item("phone","A rotary phone. Its making a curious hissing noise.", "world", scene, True)
        corpse = gc.Item("corpse", 
            "A dead person. The blood is still flowing out of him, so he must not have died very long ago.", "world", 
                                                                                                         scene, False)
        blood = gc.Item("blood pool", 
            "The pool of blood is uncomfortably hypnotic. You quickly look away as to not fall into a trance.",
                                                                                         "world", scene, False)
        eyes = gc.Body("my eyes","Nothing out of the ordinary.", scene)
        ears = gc.Body("my ears","Nothing out of the ordinary.", scene)
        fingers = gc.Body("my fingers","Nothing out of the ordinary.", scene)
        body = gc.Body("my body","Nothing out of the ordinary.", scene)

        eyes_blood = gc.Link(eyes, blood, 
                "You fall under hypnosis. Before your eyes you see: '202-555-0106'. You wake up soon after.", scene)
        ears_phone = gc.Link(ears, phone, "At first you hear only hissing, but then..."+pack_3.misc[0], scene)
        fingers_phone = gc.Link(fingers, phone, "You decide to try a number.", scene)

        while scene.game == True:
            scene.render()
            meta_one = scene.trig_loop([ears_phone, fingers_phone])
            if meta_one == fingers_phone.message:
                meta_two = scene.password_loop("enter a phone number in the form: 'xxx-xxx-xxxx' or enter 'back' to return.",
                    "number: ","That number didn't seem to work","","202-555-0106")
                if meta_two == "":
                    machine = gc.Npc("machine", "", "I won't pick up again. Make it fast.", 
                                                       pack_3.convo["machine"], scene, False)
                    machine.talk()
                    machine.delete(scene)
                    break
            if meta_one == ears_phone.message:
                woman.delete(scene)
                woman = gc.Npc("woman", "A small old woman.", "Hm?", pack_3.convo["woman2"], scene, False)

        fingers_phone.__init__(fingers, phone, "The phone is broken now.", scene)
        ears_phone.__init__(ears, phone, "Once you put the phone to your ear, the hissing stopped.", scene)
        green = gc.Item("green crystal", "A green crystal the size of your head.", "inventory", scene, True)
        green_man = gc.Link(green, corpse, "The man has come back to life!", scene)

        scene.render()
        scene.trig_loop([green_man])

        man = gc.Npc("man", "The once dead man is looking well.","I'm alive!, here take this crystal.", 
                                                                      pack_3.convo["man"], scene, False)
        blood.delete(scene)
        
        scene.render()
        scene.talk_loop("Ok, bye!")

        red = gc.Item("red crystal", "A red crystal the size of your head.", "inventory", scene, True)
        red_woman = gc.Link(red, woman, "\nShe burst into flames and died.", scene)
        green_woman = gc.Link(green, woman, "\nShe turned into an eagle and flew away. Strange town...", scene)

        scene.render()
        scene.trig_loop([red_woman, green_woman])

        if scene.game == True:
            print(pack_3.outro)
            end()
        else:
            get_key(3)
    else:
        get_key(3)


def chapter_2():

    hub = gc.FirstReturn()
    a = hub.play()
    if a == True:

        pack_2 = gc.TextPack(2)
        print(pack_2.expo)

        code_1 = "> "+"(<<>( "+"::^> "
        code_2 = "^<>^^ "+"<<> "+"|>|^ "
        code_3 = "<(<)> "+"))< "+"^^>< "
        cipher = "0 = > \n1 = <<> \n2 = ^^>< \n3 = (<<>( \n4 = |>|^ \n5 = ))< \n6 = ^<>^^ \n7 = <(<)>"                                                                                       +"\n8 = ::^>"
        scene = gc.Scene("You are in a worn down library. There are only a few books here.")
        
        book_1 = gc.Item("autobiography", pack_2.misc[0]+"\n"+code_1, "world", scene, False)
        book_2 = gc.Item("magazine article", pack_2.misc[1]+"\n"+code_2, "world", scene, False)
        book_3 = gc.Item("novel", pack_2.misc[2]+"\n"+code_3, "world", scene, False)
        blank = gc.Item("unmarked book", "The book is blank", "world", scene, False)
        rock = gc.Item("boulder", "A message reads:\n"+pack_2.misc[3]+"\nBelow this is some sort of cipher:\n"+cipher,
                                                                                                 "world", scene, False)
        chalk = gc.Item("chalk", "A stick of chalk in front of the boulder.", "inventory", scene, True)
        body = gc.Body("my body","Nothing out of the ordinary.", scene)

        chalk_rock = gc.Link(chalk, rock, "You engage the boulder with the chalk.", scene)
        
        scene.render()

        while scene.game == True:
            meta_one = scene.trig_loop([chalk_rock])

            meta_two = scene.password_loop("(enter 'back' to return)","What do you write? ",
                                                 "Your enscription erased itself.","","038614752")
            if meta_two == "":
                print("\nYour enscription glows red and burns into the boulder.")
                print("\n\nThe walls enclosing the library are blown apart. "
                              +"A glowing yellow cube falls from the sky into your hands.")
                break
        chalk_rock.__init__(chalk, rock, "Somehow, the chalk no longer leaves marks.", scene)
        cube = gc.Item("cube", "A solid cube the size of your hand with strange writing on it.", "inventory", scene, True)
        cube_blank = gc.Link(cube, blank, "\nBefore your eyes you see the message: 'DESTROY THE MACHINE'."
             +" The bookshelves start to rise into the sky. A pool of water is revealed to have been beneath one of them.", 
                                                                                                                      scene)
        scene.desc = "The walls to the library are gone, and outside is a barren wasteland."
        scene.render()
        scene.trig_loop([cube_blank])
        
        pool = gc.Item("pool", "A pool of water like the one you used to get here.", "world", scene, False)
        portal = gc.Link(body, pool, "You sink into darkness", scene)
        book_1.delete(scene)
        book_2.delete(scene)
        book_3.delete(scene)
        blank.delete(scene)
        
        scene.render()
        scene.trig_loop([portal])

        if scene.game == True:
            print(pack_2.outro)
            chapter_3()
        else:
            get_key(2)
    else:
        get_key(2)



def chapter_1():

    hub = gc.Beginning()
    a = hub.play()

    if a == True:

        pack_1 = gc.TextPack(1)
        print(pack_1.expo)
        
        scene = gc.Scene("You are surrounded by white padded walls.")
        
        AI = gc.Npc("AI terminal","A wall mounted terminal accessing an artifiial intelligence",
                                               "Hello, how can I help?",pack_1.convo["AI"], scene, False)
        safe = gc.Item("safe","A locked electronic safe. It looks like it is unlocked by entering the correct passcode.", 
                                                                                                    "world", scene, False)
        port = gc.Item("wall socket", "A wide and deep holl in the wall. 'Power Input Bay' is written bellow.", 
                                                                                           "world", scene,False)
        face = gc.Body("my face", "You can't see your own face.", scene)
        hands = gc.Body("my hands", "Nothing out of the ordinary here.", scene)
        body = gc.Body("my body", "Your whole body.", scene)
        mirror = gc.Item("mirror", "A handheld mirror.", "inventory", scene, True)
        
        trigger_a = "You look at yourself in the mirror and see that a number is written on your face."                                                                            +" The number is '0056309'"
        mirror_face = gc.Link(mirror, face,trigger_a, scene)
        engage_safe = gc.Link(hands, safe, "You engage the keypad.", scene)

        scene.render()
        
        while scene.game == True:
            scene.trig_loop([engage_safe])
            meta = scene.password_loop("Enter passcode below, or enter 'back' to return","passcode:  "
                                                              ,"PASSCODE DENIED","PASSCODE ACCEPTED","0056309")
            if meta == "PASSCODE ACCEPTED":
                print("The safe swings open, revealing a toolbox and a a large cylinder.")
                break
                
        tube = gc.Item("cylinder", "It feels warm.", "world", scene, True)
        tools = gc.Item("toolbox","A set of very science-y looking tools.", "world", scene, True)
        tube_port = gc.Link(tube,port,"You put the tube into the socket, but it is not secured.", scene)
        tools_port = gc.Link(tools,port,"You don't know what you are doing.", scene)
        
        scene.render()
        scene.trig_loop([tube_port])
        
        tube.delete(scene)
        tools_port.__init__(tools, port, 
                    "AI: 'Power supply secured.' The door opens to reveal a pool of water in the next room.", scene)
        
        scene.render()
        scene.trig_loop([tools_port])
        
        pool = gc.Item("pool","A pool of water like the one you used to get here.", "world", scene, False)
        portal = gc.Link(body, pool, "You sink into darkness", scene)
        tools.delete(scene)
        
        scene.render()
        scene.trig_loop([portal])

        if scene.game == True:
            print(pack_1.outro)
            chapter_2()