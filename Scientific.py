from tkinter import*
import math
import parser
import tkinter.messagebox

root=Tk()
root.title("Scientific Calculator")
root.configure(background="powder blue")
root.resizable(width=False,height=False)
root.geometry("480x568+0+0")

calc=Frame(root)
calc.grid()

class Calc():
    def __init__(self):
        self.total=0
        self.current=""
        self.input_value=True
        self.check_sum=False
        self.op=""
        self.result=False
    
    def numberEnter(self,num):
        self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current=secondnum
            self.input_value=False
        else:
            if secondnum=='.':
                if secondnum in firstnum:
                    return
            self.current=firstnum+secondnum
        self.display(self.current)

    def display(self,value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0,value)
    def valid_function(self):
        if self.op=="add":
            self.total +=self.current
        if self.op=="sub":
            self.total -=self.current
        if self.op=="multi":
            self.total *=self.current
        if self.div=="div":
            self.total /=self.current
        if self.mode=="mod":
            self.total %=self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)


    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum == True:
            self.valid_function()

        else:
            self.total=float(txtDisplay.get())
    def operation(self,op):
        self.current=float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False

    def clear_Entry(self):
        self.result=False
        self.current="0"
        self.display(0)
        self.input_value=True

    def all_clear_Entry(self):
        self.clear_Entry()
        self.total=0

    def exp(self):
        self.result=False
        self.current=math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result=False
        self.current=math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def tan(self):
        self.result=False
        self.current=math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result=False
        self.current=math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)
       
    def cos(self):
        self.result=False
        self.current=math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)
       
    def sinh(self):
        self.result=False
        self.current=math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
       
    def cosh(self):
        self.result=False
        self.current=math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
       
    def tanh(self):
        self.result=False
        self.current=math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result=False
        self.current=math.log(float(txtDisplay.get()))
        self.display(self.current)   
       
    def ln(self):
        self.result=False
        self.current=math.ln(float(txtDisplay.get()))
        self.display(self.current)   
       



added_value=Calc()


txtDisplay=Entry(calc,font=('arial',20,'bold'), bg="powder blue", bd=30,width=29,justify=RIGHT)
txtDisplay.grid(row=0,column=0,columnspan=4,ipady=4)
txtDisplay.insert(0,"0")

numberpad="789456123"
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc,width=6,height=2,font=('arial',20,'bold'),bd=4,text=numberpad[i]))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i]["command"]=lambda x=numberpad[i]:added_value.numberEnter[x]
        i+=1

# -----------------------------------------------------------------------------------------------------------------Standard Calculator-------------------------------------------------------------------------
btnClear=Button(calc,text=chr(67),width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=added_value.clear_Entry).grid(row=1,column=0,ipady=1)

btnAllClear=Button(calc,text=chr(67)+chr(69),width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=added_value.all_clear_Entry).grid(row=1,column=1,ipady=1)
btnSq=Button(calc,text="√",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue").grid(row=1,column=2,ipady=1)

btnAdd=Button(calc,text="+",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=lambda: added_value.numberEnter("add")).grid(row=1,column=3,ipady=1)

btnSub=Button(calc,text="-",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=lambda:added_value.numberEnter("sub")).grid(row=2,column=3,ipady=1)
btnMul=Button(calc,text="*",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=lambda:added_value.numberEnter("multi")).grid(row=3,column=3,ipady=1)
btnDiv=Button(calc,text=chr(177),width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=lambda:added_value.numberEnter("div")).grid(row=4,column=3,ipady=1)
btnEql=Button(calc,text="=",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=lambda:added_value.sum_of_total).grid(row=5,column=3,ipady=1)

btnMod=Button(calc,text="%",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=lambda:added_value.numberEnter("mod")).grid(row=6,column=0,ipady=1)
btnZero=Button(calc,text="0",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=lambda:added_value.numberEnter(0)).grid(row=6,column=1,ipady=1)
btnDeci=Button(calc,text=".",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=lambda:added_value.numberEnter(".")).grid(row=6,column=2,ipady=1)
btnEXP=Button(calc,text="EXP",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=added_value.exp).grid(row=6,column=3,ipady=1)


# ----------------------------------------------------------------Scientific Calculator-----------------------------------------------------------------------------
btnClear=Button(calc,text=chr(67),width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=added_value.clear_Entry).grid(row=1,column=0,ipady=1)

btnAllClear=Button(calc,text=chr(67)+chr(69),width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=added_value.all_clear_Entry).grid(row=1,column=1,ipady=1)
btnSq=Button(calc,text="√",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue").grid(row=1,column=2,ipady=1)

btnAdd=Button(calc,text="+",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=lambda: added_value.numberEnter("add")).grid(row=1,column=3,ipady=1)

btnSub=Button(calc,text="-",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=lambda:added_value.numberEnter("sub")).grid(row=2,column=3,ipady=1)
btnMul=Button(calc,text="*",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=lambda:added_value.numberEnter("multi")).grid(row=3,column=3,ipady=1)
btnDiv=Button(calc,text=chr(177),width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=lambda:added_value.numberEnter("div")).grid(row=4,column=3,ipady=1)
btnEql=Button(calc,text="=",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=lambda:added_value.sum_of_total).grid(row=5,column=3,ipady=1)

btnMod=Button(calc,text="%",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=lambda:added_value.numberEnter("mod")).grid(row=6,column=0,ipady=1)
btnZero=Button(calc,text="0",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=lambda:added_value.numberEnter(0)).grid(row=6,column=1,ipady=1)
btnDeci=Button(calc,text=".",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=lambda:added_value.numberEnter(".")).grid(row=6,column=2,ipady=1)
btnEXP=Button(calc,text="EXP",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=added_value.exp).grid(row=6,column=3,ipady=1)

btnSin=Button(calc,text="sin",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=added_value.sin).grid(row=1,column=4,ipady=1)
btnCos=Button(calc,text="cos",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=added_value.cos).grid(row=1,column=5,ipady=1)
btnTan=Button(calc,text="tan",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=added_value.cos).grid(row=1,column=6,ipady=1)

btnSinIn=Button(calc,text="arc(sin)",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=added_value.sinh).grid(row=2,column=4,ipady=1)
btnCosIn=Button(calc,text="arc(cos)",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=added_value.cosh).grid(row=2,column=5,ipady=1)
btnTanIn=Button(calc,text="arc(tan)",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=added_value.tanh).grid(row=2,column=6,ipady=1)

btnLog=Button(calc,text="log",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=added_value.log).grid(row=3,column=4,ipady=1)
btLn=Button(calc,text="ln",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=added_value.ln).grid(row=3,column=5,ipady=1)
btnInX=Button(calc,text="1/x",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="powder blue",command=added_value.exp).grid(row=3,column=6,ipady=1)






# -------------------------------------Menu----------------------------------------------------------------------------

def iExit():
    iExit=tkinter.messagebox("Scientific Calculator","Confirm if you want to exit")
    if iExit>0:
        root.destroy
        return
def Scientific():
    root.resizable(width=False,height=False)
    root.geometry("480x568+0+0")

def standard():
    root.resizable(width=False,height=False)
    root.geometry("480x568+0+0")


menubar=Menu(calc)

filemenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="standard")
filemenu.add_command(label="scientific")
filemenu.add_separator()
filemenu.add_command(label="Exit")

editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_cascade(label="cut")
editmenu.add_cascade(label="copy")
editmenu.add_separator()
editmenu.add_command(label="Paste")

helpmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="View Help")


