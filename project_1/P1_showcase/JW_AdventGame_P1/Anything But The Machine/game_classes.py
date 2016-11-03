class GameObject():
    
    #The base class for objects in the game. Every object has a name, a description, and a boolean variable
    #that determines whether or not the object can be picked up by the player. Every object also has a delete 
    #method that will remove it from the Scene() object that instantiated for the level. 
    
    def __init__(self,name,desc,loot=False):
        self.name = name
        self.description = desc
        self.loot = loot
        
    def delete(self,scene):

        try:
            scene.w_obj.remove(self)
        except:
            pass
        try:
            scene.i_obj.remove(self)
        except:
            pass
        try:
            scene.p_obj.remove(self)
        except:
            pass


class Item(GameObject):
    
    #This class of object is the second most general object. These objects
    #have a use method that will check if there exists in the Scene() a 
    #Link() object this object and some other object in the level.
    
    
    def __init__(self,name,desc,where,scene,loot):
        GameObject.__init__(self,name,desc,loot)
        scene.populate(self,where)
              
    def use(self,thing,scene):
        if (self.name, thing.name) in scene.links.keys():
            return scene.links[(self.name, thing.name)]
        else:
            return "Nothing happened."

class Body(Item):
    
    #This class of objects is identical to the Item class, but is seperate because they are organized differently.
    #This class takes the place of "direct" interaction in normal puzzle games, so that you can specify how you 
    #will interact directly.
    
    def __init__(self,name,desc,scene):
        GameObject.__init__(self,name,desc,False)
        scene.populate(self,"player")
        
class Npc(GameObject):
    
    #These objects are for characters that you can talk to.  They have a talk() method that produces a 
    #scripted sequence emulating a conversation.
    
    collection = []
    def __init__(self,name,desc,intro,convo,scene,loot):
        GameObject.__init__(self,name,desc,loot)
        self.intro = intro
        self.convo = convo
        self.switch = True
        self.responses = []
        scene.populate(self,"world")
        
    def talk(self):
        if self.switch == True:
            print(self.name + " said: " + self.intro)
        prompt = ""
        for i in range(0,len(self.convo)):
            prompt += " | " + "("+str(i) + ")" + self.convo[i][0]+ " | "
        print(prompt)
        try:
            ans = int(input("Select a response: "))
            print("\n"+self.name + " said: "+ self.convo[ans][1],"\n")
            self.responses.append(self.convo[ans][1])
            if ans != 0:
                self.switch = False
                self.talk()
            else:
                self.switch = True

        except:
            print("invalid response \n")
            self.switch = False
            self.talk()
        return self.responses
    
        
class Link():
    
    #This is the class of objects defining when two objects can interact with each other.  If two objects can interact,
    #a string gets returned in the Scene() control() method that indicates that the interaction took place.
    
    def __init__(self,actor,actee,message,scene):
        try:
            del scene.links[self.name]
        except:
            pass
        self.actor = actor
        self.actee = actee
        self.message = message
        self.name = (self.actor.name, self.actee.name)
        scene.populate(self,"link")
        
    def delete(self,scene):
        del scene.link[self.name]
        
class Space():
    
    #This class is a simple organization tool. The objects in the game will be 
    #compartmentalized, which is easily done by putting every object into a different
    #dictionary. This is done automatically here by making that dictionary an instance 
    #attribute.
    
    def __init__(self,objs,desc=""):
        self.library = {i.name: i for i in objs}
        self.description = desc
        
    def read(self):
        return " | ".join(self.library.keys())

        
    
class Scene():
      
    #This object organizes all of the mechanics in the game. On initialization, lists 
    #are created that can store objects in the level. The objects are then stored automatically 
    #when they themselves are initialized. After the objects are created, the render() method 
    #is called which organizes these objects into Space() objects. This makes it easier for the 
    #control() method to reference objects in the level, and simplifies the process of 
    #compartmentalizing those objects so the player interacts with them in an intuitive way.
    
    def __init__(self,desc):
        self.game = True
        self.desc = desc
        self.w_obj = []
        self.i_obj = []
        self.p_obj = []
        self.e_obj = []
        self.links = {}

    def render(self):
        self.world = Space(self.w_obj,self.desc)
        self.inventory = Space(self.i_obj)
        self.player = Space(self.p_obj)
        self.everything = Space(self.e_obj)
        
    #This method is called when a GameObject is initialized so that it is stored 
    #within the Scene() object associated with that level.
    def populate(self,obj,kind):
        
        if kind == "world":
            self.w_obj.append(obj)
        if kind == "inventory":
            self.i_obj.append(obj)
        if kind == "player":
            self.p_obj.append(obj)
        if kind == "link":
            self.links.update({obj.name: obj.message})
        if kind != "link":
            self.e_obj.append(obj)
        
    #Progress in the game is experienced as a series of While loops. 
    #These loops are generalized with three different Scene() methods.
    #trig_loop is a generalized loop that loops until the command() 
    #method returns the message attribute from a provided Link().
    def trig_loop(self,triggers):

        if self.game == True:
            while self.game == True:
                turn = self.command()
                if turn in [i.message for i in triggers]:
                    break
            return turn


    #this loop method is a generalized loop that loops until a character
    #says something to you.
    def talk_loop(self,response):
        
        if self.game == True:
            while self.game == True:
                turn = self.command()
                try:
                    if response in turn:
                        break
                except:
                    pass
            return response

    #Unlike the other loops, this loop is more specialized and does not involve 
    #the command() method. In the game, you might interact with an object 
    #that requires a password in order to progress.
    def password_loop(self,display,prompt,err_msg,acc_msg,ans):
        solve = False
        while self.game == True:
            print("\n"*2 + display + "\n"*2)

            inwords = input("\n"+prompt)
            if inwords == ans:
                print("\n"+acc_msg)
                solve = True
                break
            elif inwords == "back":
                break
            else:
                print("\n"+err_msg)
        if solve == True:
            return acc_msg
    
    #This method asks you to input a command, and then returns some value that may 
    #or may not trigger something in the game. 
    def command(self):
        com = input("Enter a command: ")
        if com == "look":
            print("\n"+self.world.description,"You can see: ")
            print(self.world.read())
            return None
        elif com == "use":
            print("\n" + self.inventory.read() + " | *direct*")
            item = input("Which item would you like to use? (to interact directly, input 'direct') ")
            if item == "direct":
                print("\n"+self.player.read())
                part = input("What would you like to use to interact directly? ")
                print("\n"+self.everything.read())
                obj = input("What would you like to interact with? ")
                try:
                    print(self.player.library[part].use(self.everything.library[obj],self))
                    return self.player.library[part].use(self.everything.library[obj],self)
                except:
                    print("\nThat doesn't work")
                    return None
            else:
                print("\n"+self.everything.read())
                obj = input("What would you like to interact with? ")
                try:
                    print(self.inventory.library[item].use(self.everything.library[obj],self))
                    return self.inventory.library[item].use(self.everything.library[obj],self)
                except:
                    print("\nThat doesn't work")
                    return None         
        elif com == "take":
            print("\n"+self.world.read())
            obj = input("What would you like to pick up? ")
            if obj in self.world.library.keys():
                if self.world.library[obj].loot == True:
                    del self.world.library[obj]
                    for i in self.w_obj:
                        if i.name == obj:
                            self.w_obj.remove(i)
                            self.i_obj.append(i)
                    self.inventory.library.update({self.everything.library[obj].name:self.everything.library[obj]})
                    print("\n"+obj,"has been added to your inventory")
                    return "took_"+obj
                else:
                    print("\nThat cannot be picked up")
                    return None
            elif obj in self.everything.library.keys():
                print("\nThat cannot be picked up")
                return None
            else:
                print("\nThat doesn't work")
                return None
        elif com == "drop":
            print("\n"+self.inventory.read())
            obj = input("\nWhat would you like to drop? ")
            if obj in self.inventory.library.keys():
                del self.inventory.library[obj]
                self.world.library.update({self.everything.library[obj].name:self.everything.library[obj]})
                print("\n"+obj,"has been dropped")
                return "dropped_"+obj
            else:
                print("\nThat doesn't work")
                return None
        elif com == "talk":
            print("\n"+self.world.read())
            person = input("Who would you like to talk to? ")
            try:
                print("\n \n")
                return self.everything.library[person].talk()
            except:
                print("\nThere is no such person")
                return None
        elif com == "inventory":
            print("\nYou are currently holding: ")
            print(self.inventory.read())
            return None
        elif com == "inspect":
            print("\n" + self.world.read()+" | "+self.inventory.read()+" | "+self.player.read())
            obj = input("What would you like to inspect? ")
            try:
                print("\n"+self.everything.library[obj].description)
                return None
            except:
                print("\nThere is no such thing")
                return None
        elif com == "quit":
            self.game = False
        else:
            print("\nInvalid Entry")
            return "skip"  

        
#To make scripting levels more streamlined, it is convienient to store all of 
#the expositional text and conversation text in a single text file that is 
#organized in a particular way. This class then disects that text file and 
#organizes all of the different types of text for a given level into 
#instance attributes.
class TextPack():
    
    def __init__(self,chap):
        
        self.expo = TextPack.pack(str(chap)+"expo"+str(chap))
        self.outro = TextPack.pack(str(chap)+"outro"+str(chap))
        self.convo = TextPack.pack(str(chap)+"convo"+str(chap))
        self.misc = TextPack.pack(str(chap)+"misc"+str(chap))
        
    @staticmethod
    def pack(bookends):
        
        with open("game_text","r") as intext:
            all_lines = intext.readlines().copy()
        div = []
        index = 0
        for i in all_lines:
            if bookends in i:
                div.append(index)
            index += 1
        select = all_lines[div[0]+1: div[1]]
        if bookends[1:5] == "expo" or bookends[1:6] == "outro":
            return " ".join(select)
        elif bookends[1:6] == "convo":
            names = select[::2]
            words = select[1::2]
            end = {}
            index = 0
            for i in words:
                conv = []
                for x in i.split("|"):
                    exchange = tuple([i.replace("\n","") for i in x.split("<>")])
                    conv.append(exchange)
                end.update({names[index].replace("\n",""):conv})
                index += 1
            return end
        else:
            return " ".join(select).split("<>")
        
#Ideally, it is preferable to generalize the gameplay as much as possible into classes. 
#For this game, that can only go so far and the levels themselves are too different from 
#each other to make generalizing the level structure feasable.  However, there is one area 
#in the game that you will regularly return to, sort of like a main hub.  This one area 
#can be generalized, and that is the idea behind the Hub() class and all of its children. 
class Hub():
    
    def __init__(self):
        self.desc = "You are in a damp cave."
        self.intro = "You are back in the cave with the machine. You have brought something with you."
        self.outwords = "You sink into darkness."
        self.machine_desc = "A large machine of steel and brass."
        self.pool_desc = "The pool of water you used to go places."
        self.text = TextPack(0)
        self.scene = Scene(self.desc)
        
        self.fix_words = "You really shouldn't mess around with anything until you know what you're doing."
        self.cube_words = self.text.misc[0]

    def make_objects(self,time):
        
        self.machine = Item("machine", self.machine_desc,"world", self.scene, False)
        self.pool = Item("pool",self.pool_desc,"world", self.scene, False)
        self.body = Body("my body","Nothing out of the ordinary.",self.scene)
        self.portal = Link(self.body, self.pool, self.outwords, self.scene)
        
        if time >= 1:
            self.tools = Item("toolbox", "A box of science-y looking tools.", "inventory", self.scene, True)
            self.fix = Link(self.tools, self.machine, self.fix_words, self.scene)
        if time >= 2:
            self.cube = Item("cube","A solid cube the size of your fist with strange writing on it.","inventory",self.scene,True)
            self.analyze = Link(self.cube, self.machine, self.cube_words, self.scene)
        if time == 3:
            self.green = Item("green crystal", "A green crystal the size of your head", "inventory", self.scene, True)
            self.red = Item("red crystal", "A red crystal the size of your head", "inventory", self.scene, True)
            self.green_mach = Link(self.green, self.machine, self.text.misc[2], self.scene)
            self.red_mach = Link(self.red, self.machine, self.text.misc[3], self.scene)

        
    def play(self):
        
        print(self.intro)
        self.scene.render()
        self.scene.trig_loop([self.portal])
        
        if self.scene.game == True:
            return True
        else:
            return False
        
class Beginning(Hub):

    def __init__(self):
        Hub.__init__(self)
        self.intro = self.text.expo
        self.outwords = "You get into the pool of water, but you are unable to float. You sink into darkness."
        self.pool_desc = "A pool of water. The water is very clear, but you somehow cannot see the bottom."
        self.make_objects(0)


class FirstReturn(Hub):
    
    def __init__(self):
        Hub.__init__(self)
        self.make_objects(1)
                
                             
class SecondReturn(FirstReturn):
    
    def __init__(self):
        FirstReturn.__init__(self)
        self.make_objects(2)

#The end of the game also takes place in this main hub, but the scenerio plays out differently than the
#others so the play() method is an entirely different script. 
class EndGame(SecondReturn):
    
    def __init__(self):
        SecondReturn.__init__(self)
        self.machine_desc = "You notice something you never noticed before, a large round hole near the top."
        self.pool_desc = "The pool is all dried up. The remaining pit isn't that deep, how is it that you couldn't even "                                                                                                +"see the bottom before?"
        self.outwords = "There is nothing interesting at the bottom of the pit."
        self.fix_words = self.text.misc[1]
        self.intro = "You are back in the cave with the machine. Something is very different this time..."
        self.make_objects(3)
    
    def play(self):
        
        print(self.intro)
        self.scene.render()
        
        choice = self.scene.trig_loop([self.green_mach, self.red_mach])
        self.fix.__init__(self.tools, self.machine, "You secured the crystal in place, and now the cube is glowing.",self.scene)
        self.machine.description = "The crystal is not yet secure."
        
        if choice == self.green_mach.message:
            self.analyze.__init__(self.cube, self.machine, self.text.misc[5], self.scene)
            self.green.delete(self.scene)
        if choice == self.red_mach.message:
            self.analyze.__init__(self.cube, self.machine, self.text.misc[4], self.scene)
            self.red.delete(self.scene)
        
        self.machine.description = "The crystal is secure."
        
        self.scene.render()
        self.scene.trig_loop([self.analyze])
        
        if self.scene.game == True:
            print(self.text.outro)