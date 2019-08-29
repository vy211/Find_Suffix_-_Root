#Vipin Yadav
#this is new line comment
from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('600x250')
root.title("Find Root and Suffix")
label_1 = Label(root, text="Word:",width=20,font=("bold", 15))
label_1.place(x=10,y=50)
label_2 = Label(root, text="Root:",width=20,font=("bold", 15))
label_2.place(x=10,y=100)
label_3 = Label(root, text="Suffix:",width=20,font=("bold", 15))
label_3.place(x=10,y=150)

entry_1 = Entry(root,bd=3,width=20,font=('bold',15))
entry_1.place(x=190,y=50)
entry_1.focus_set()
entry_2 = Entry(root,bd=3,width=20,font=('bold',15))
entry_2.place(x=190,y=100)
entry_3 = Entry(root,bd=3,width=20,font=('bold',15))
entry_3.place(x=190,y=150)

def find_root_suffix():
        w=entry_1.get()
        suffix = ['s', 'es', 'ies', 'ves', 'a', 'e', 'ices', 'ces', 'i', 'm']
        for i in suffix:

                if w.endswith(i):
                        if i == 's':
                                if w.endswith('es'):
                                        if w.endswith("ies"):
                                                l = w.split('ies')
                                                l[0] = l[0] + 'y'
                                                print("root: ", l[0])
                                                entry_2.insert(0,l[0])
                                                entry_3.insert(0, "ies")
                                                print("suffix: ies")

                                                break
                                        elif w.endswith("ves"):
                                                l = w.split('ves')
                                                l[0] = l[0] + 'f'
                                                print("root: ", l[0])
                                                entry_2.insert(0, l[0])
                                                entry_3.insert(0, "ves")
                                                print("suffix: ves")
                                                break

                                        elif w.endswith("ces"):
                                                if w.endswith("ices"):
                                                        l = w.split('ices')
                                                        l[0] = l[0] + 'ex'
                                                        print("root: ", l[0])
                                                        print("suffix: ices")
                                                        entry_2.insert(0, l[0])
                                                        entry_3.insert(0, "ices")
                                                        break
                                                else:
                                                        l = w.split('ces')
                                                        l[0] = l[0] + 'x'
                                                        print("root: ", l[0])
                                                        print("suffix: ces")
                                                        entry_2.insert(0, l[0])
                                                        entry_3.insert(0, "ces")
                                                        break
                                        else:
                                                l = w.split('es')
                                                print("root: ", l[0])
                                                print("suffix: es")
                                                entry_2.insert(0, l[0])
                                                entry_3.insert(0, "es")
                                                break
                                else:
                                        l = w.split('s')
                                        print("root: ", l[0])
                                        print("suffix: s")
                                        entry_2.insert(0, l[0])
                                        entry_3.insert(0, "s")
                                        break
                        elif w.endswith('a'):

                                w = w[:-1]
                                w = w + 'um'
                                print("root: ", w)
                                print("suffix: a")
                                entry_2.insert(0, l[0])
                                entry_3.insert(0, "a")
                                break
                        elif w.endswith('e'):
                                w = w[:-1]
                                print("root: ", w)
                                print("suffix: e")
                                entry_2.insert(0, l[0])
                                entry_3.insert(0, "e")
                                break
                        elif w.endswith('i'):
                                w = w[:-1]
                                w = w + 'us'
                                print("root: ", w)
                                print("suffix: i")
                                entry_2.insert(0, l[0])
                                entry_3.insert(0, "i")
                                break
                        elif w.endswith('im'):
                                l = w.split('im')
                                print("root: ", l[0])
                                print("suffix: im")
                                entry_2.insert(0, l[0])
                                entry_3.insert(0, "im")
                                break
                        else:
                                messagebox.showinfo("Sorry", "Answer Not Define")


def clear():
        entry_1.select_clear()
        entry_2.select_clear()
        entry_3.select_clear()

Button(root, text='Find',width=20,bg='brown',fg='white',command=find_root_suffix).place(x=50,y=200)
Button(root, text='Clear',width=20,bg='brown',fg='white',command=clear).place(x=300,y=200)

root.mainloop()
                                                
                                        
                                
                                        
                        
                                      

