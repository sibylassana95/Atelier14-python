from tkinter import *
 
def action():
    name = entryName.get()
    v.set("Hello " + name)
    
root = Tk()
root.geometry("350x200")
root.title("Message")

# création du label qui affiche le résultat
v = StringVar()
lblResult = Label(root , textvariable = v)
lblResult.place(x = 100 , y = 50)

# création du champ de saisie Entry
entryName = Entry(root)
entryName.place(x = 100 , y = 80 , width = 150)
# création du bouton valider
btn_validate = Button(root , text = "Validate!" , command = action)
btn_validate.place(x = 100 , y = 110 , width = 150)

root.mainloop()
