from tkinter import*

#Instanciar widgget
root = Tk()
#Criar Label
myApp = Label(root,text="Hello Wordl")
#Ajusta para a label
myApp.pack()
#Funcao para que ela so feche quando clicar em fechar
root.mainloop()

#Criar Classe
class App:
    #Construtor
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        
        self.buthey = Button(frame,text="Quit",fg="red",command=self.quit)
        self.buthey.pack(side=LEFT)
        
        self.butHELLO = Button(frame,text="Hello",command=self.hello)
        self.butHELLO.pack(side=LEFT)
        
    def quit(self):
        root.destroy()
    
    def hello(self):
        root = Tk()
        myApp = Label(root,text="Hello Wordl Bugado")
        myApp.pack()
        root.mainloop()
      
root = Tk()
app = App(root)
root.mainloop()