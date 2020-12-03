class obj:
    def __init__(self,prefix="",prefixm="",root="",rootm="",suffix="",suffixm="",example="",definition=""):
        self.prefix = prefix
        self.prefixm = prefixm
        self.root = root
        self.rootm = rootm
        self.suffix = suffix
        self.suffixm = suffixm
        self.example = example
        self.definition = definition

objs_array = []

file = open("suffix.txt","r")
state = 1
suffix=""
suffixm=""
example=""
definition=""
for line in file:
    if state == 1:
        suffix = line
        state+=1
        continue
    if state == 2:
        suffixm = line
        state += 1
        continue
    if state == 3:
        example = line
        state += 1
        continue
    if state == 4:
        definition = line
        objs_array.append(obj("","","","",suffix,suffixm,example,definition))
        state = 1

file.close()
file = open("prefix.txt","r")
state = 1
prefix=""
prefixm=""
example=""
definition=""
for line in file:
    if state == 1:
        prefix = line
        state+=1
        continue
    if state == 2:
        prefixm = line
        state += 1
        continue
    if state == 3:
        example = line
        state += 1
        continue
    if state == 4:
        definition = line
        objs_array.append(obj(prefix,prefixm,"","","","",example,definition))
        state = 1


file = open("root.txt","r")
state = 1
root=""
rootm=""
example=""
definition=""
for line in file:
    if state == 1:
        root = line
        state+=1
        continue
    if state == 2:
        rootm = line
        state += 1
        continue
    if state == 3:
        example = line
        state += 1
        continue
    if state == 4:
        definition = line
        objs_array.append(obj("","",root,rootm,"","",example,definition))
        state = 1



def safeprint(title , value):
    if value != "":
        print(title+": " + value , end=" ")

for k in range(20):
    inp  = input("Order: ")
    for o in objs_array:
        if inp.lower() ==  o.prefix.lower():
            print("PRE:"+o.prefix)
            safeprint("     Meaning",o.prefixm)
            safeprint("     Example", o.example)
            safeprint("     Definition", o.definition)
            break
        elif inp.lower() ==  o.suffix.lower():
            print("SUF:", o.suffix)
            safeprint("     Meaning",o.suffixm)
            safeprint("     Example", o.example)
            safeprint("     Definition", o.definition)
            break
        elif inp.lower() ==  o.root.lower():
            print("ROT:"+o.root)
            safeprint("     Meaning",o.rootm)
            safeprint("     Example", o.example)
            safeprint("     Definition", o.definition)
            break
        if inp.lower() == o.example.lower():
            print("EX:" + o.example)
            safeprint("     Suffix", o.suffix)
            safeprint("     Meaning", o.suffixm)
            safeprint("     Prefix", o.prefix)
            safeprint("     Meaning", o.prefixm)
            safeprint("     Definition", o.definition)
            break
        elif inp.lower() in o.prefix.lower():
            print("PRE:" + o.prefix)
            safeprint("     Meaning", o.prefixm)
            safeprint("     Example", o.example)
            safeprint("     Definition", o.definition)
            continue
        elif inp.lower() in o.suffix.lower():
            print("SUF:", o.suffix)
            safeprint("     Meaning", o.suffixm)
            safeprint("     Example", o.example)
            safeprint("     Definition", o.definition)
            continue
        elif inp.lower() in  o.root.lower():
            print("ROT:"+o.root)
            safeprint("     Meaning",o.rootm)
            safeprint("     Example", o.example)
            safeprint("     Definition", o.definition)
            continue
        elif inp.lower() in  o.example.lower():
            print("EX:"+o.example)
            safeprint("     Suffix" , o.suffix)
            safeprint("     Meaning",o.suffixm)
            safeprint("     Prefix" , o.prefix)
            safeprint("     Meaning" , o.prefixm)
            safeprint("     Root", o.root)
            safeprint("     Meaning", o.rootm)
            safeprint("     Definition" , o.definition)
   
