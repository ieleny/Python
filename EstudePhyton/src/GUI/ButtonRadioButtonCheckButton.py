
from tkinter import*

class RadioFont(Frame):
    
    def __init__(self):
        
        #Radio
        Frame.__init__(self)
        self.pack(expand = YES,fill = BOTH)
        self.master.title("Demostracao do RadioButton, checbutton e botao")
        
        self.frame1 = Frame(self)
        self.frame1.pack()
        
        self.text = Entry(self.frame1,width=40,font="Arial 10")
        self.text.insert(INSERT,"Trocando de Cor Para")
        self.text.pack(padx=5,pady=5)
        
        self.frame2 = Frame(self)
        self.frame2.pack()
        
        self.chosenColor = StringVar()
        self.chosenColor.set(0)
        self.radioRed = Radiobutton(self.frame2, text = "Vermelho", variable = self.chosenColor, value="red",command=self.changeColor)
        self.radioRed.pack(side=LEFT,padx=5,pady=5)
        self.radioGreen = Radiobutton(self.frame2, text = "Verde", variable = self.chosenColor, value="green",command=self.changeColor)
        self.radioGreen.pack(side=LEFT,padx=5,pady=5)
        self.radioBlue = Radiobutton(self.frame2, text = "Azul", variable = self.chosenColor, value="blue",command=self.changeColor)
        self.radioBlue.pack(side=LEFT,padx=5,pady=5)
        
        #Checkbox
        self.frame3 = Frame(self)
        self.frame3.pack()
        
        self.boldOn = BooleanVar()
        self.checkBold = Checkbutton(self.frame3,text = "Bold" , variable = self.boldOn, command = self.changeFont)
        self.checkBold.pack(side=LEFT,padx=5,pady=5)
         
        self.boldOnItalic = BooleanVar()
        self.checkItalic = Checkbutton(self.frame3,text = "Bold" , variable = self.boldOnItalic, command = self.changeFont)
        self.checkItalic.pack(side=LEFT,padx=5,pady=5)
        
        #Button Com Imagem
        self.frame4 = Frame(self)
        self.frame4.pack()
        
        self.myImageClear = PhotoImage(file="") #<-- Caminho da imagem
        self.ClearButton  = Button(self.frame4,image = self.myImageClear,command = self.clearFields)
        self.ClearButton.pack(side=LEFT,padx=5,pady=5)
    
    def changeColor(self):
        if self.chosenColor.get() == "red":
           self.text.configure(fg="red")
        elif self.chosenColor.get() == "green":
           self.text.configure(fg="green") 
        elif self.chosenColor.get() == "blue":
           self.text.configure(fg="blue") 
    
    def changeFont(self):
        
        desiredFont = "Arial 10"
        
        if self.boldOn.get():
            desiredFont += " bold"
            
        if self.boldOnItalic.get():
            desiredFont += " italic"
        
        self.text.config(font=desiredFont)
            
    def clearFields(self):
        self.text.delete(0,END)
           
def main():
    RadioFont().mainloop()
    
if __name__ == "__main__":
    main()
    

    