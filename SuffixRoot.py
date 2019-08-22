#Vipin Yadav
#this is new line comment
run=True
while run:
        print("=================================================")
        w=str(input("Input: "))
        suffix=['s','es','ies','ves','a','e','ices','ces','i','m']
        for i in suffix:
        
                if w.endswith(i):
                        if i=='s':
                                if w.endswith('es'):
                                        if w.endswith("ies"):
                                                l=w.split('ies')
                                                l[0]=l[0]+'y'
                                                print("root: ",l[0])
                                                print("suffix: ies")
                                                break
                                        elif w.endswith("ves"):
                                                l=w.split('ves')
                                                l[0]=l[0]+'f'
                                                print("root: ",l[0])
                                                print("suffix: ves")
                                                break
                                
                                        elif w.endswith("ces"):
                                                if w.endswith("ices"):
                                                        l=w.split('ices')
                                                        l[0]=l[0]+'ex'
                                                        print("root: ",l[0])
                                                        print("suffix: ices")
                                                        break
                                                else:
                                                        l=w.split('ces')
                                                        l[0]=l[0]+'x'
                                                        print("root: ",l[0])
                                                        print("suffix: ces")
                                                        break
                                        else:
                                                l=w.split('es')
                                                print("root: ",l[0])
                                                print("suffix: es")
                                                break
                                else:
                                        l=w.split('s')
                                        print("root: ",l[0])
                                        print("suffix: s")
                                        break
                        elif w.endswith('a'):
                        
                                w=w[:-1]
                                w=w+'um'
                                print("root: ",w)
                                print("suffix: a")
                                break
                        elif w.endswith('e'):
                                w=w[:-1]
                                print("root: ",w)
                                print("suffix: e")
                                break
                        elif w.endswith('i'):
                                w=w[:-1]
                                w=w+'us'
                                print("root: ",w)
                                print("suffix: i")
                                break
                        elif w.endswith('im'):
                                l=w.split('im')
                                print("root: ",l[0])
                                print("suffix: im")
                                break
                        else:
                                print("Sorry!! Not define!")
                
        
        #print("Test More Press y:")
        char=str(input("Test More Press Y:"))
        if char=='Y' or char=='y':
                run=True
        else:
                run=False
                        
                                                
                                        
                                
                                        
                        
                                      

