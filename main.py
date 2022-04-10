from tkinter import *
from tkinter import messagebox
import math
from datetime import *
root = Tk()
root.title("pp make cum")
dnes = datetime.now()
#####################################################################class ceník
class currency:

    def __init__(self,cur,state,amount,price_per_amount):
        self.cur = cur
        self.stete = state
        self.amount = amount
        self.price = price_per_amount
        self.pp = price_per_amount / amount
        self.line= cur + "    " + state + "    " + str(amount) + "    " + str(price_per_amount)


cur_1 = currency("USD", "USA", 1  , 22.5)
cur_2 = currency("EUR", "EU ", 1  , 24.4)
cur_3 = currency("PLN", "PL ", 1  , 5.2)
cur_4 = currency("JPY", "JP ", 100, 18.1)

print (cur_1.line)

####################################################################### nadpis
napis=Label(root,text="Exchange",fg="red", font=("Arial",25))  
napis.grid(row=0, column=0, columnspan=2,sticky=E)

############################################################################ check box sell/buy
Buy = IntVar() #BooleanVar()
Buy.set(1)

Sell = IntVar() #BooleanVar()
Sell.set(0)

def c_buy():
    Sell.set(0)
    Buy.set(1)

def c_sell():
    Buy.set(0)
    Sell.set(1)
    

buy = Checkbutton(root, text="Buy", variable=Buy, command=c_buy) 
buy.grid(row=1,column=1) 

sell = Checkbutton(root, text="Sell", variable=Sell, command=c_sell) 
sell.grid(row=2,column=1)


####################################################################Option menu 
promenna = StringVar()
promenna.set(cur_1.cur) # standardní hodnota
def test(hodnota):
    print ("hodnota je:", hodnota)
    print ("hodnota je:", promenna.get())
sez=[cur_1.cur, cur_2.cur, cur_3.cur,cur_4.cur]
w = OptionMenu(root, promenna,*sez,command=test)
w.grid(row=1, column=0)

########################################################### entry
napis=Label(root,text="Entry amount:",fg="red", font=("Arial",10))  
napis.grid(row=3, column=0,sticky=E)

entry_cur=StringVar()
vstup=Entry(root,textvariable=entry_cur)
vstup.grid(row=4, column=0, columnspan=2)

napis=Label(root,text="",fg="red", font=("Arial",5))  
napis.grid(row=5, column=0,sticky=E)

##################################################################### 2 buttons
def ZavriOkno():
    global top
    top.destroy()
    tlacitko2["state"]="normal"
    

def rates():
    global top
    top = Toplevel()
    top.geometry("500x200")
    top.title("Rates")
    tlacitko2["state"]="disabled"
    top.protocol("WM_DELETE_WINDOW",ZavriOkno)
    
    text = Text(top)
    text.insert(INSERT, "state currency amount  price")
    text.insert(INSERT, "\n")
    text.insert(INSERT, cur_1.line)
    text.insert(INSERT, "\n")
    text.insert(INSERT, cur_2.line)
    text.insert(INSERT, "\n")
    text.insert(INSERT, cur_3.line)
    text.insert(INSERT, "\n")
    text.insert(INSERT, cur_4.line)
    
    text.pack()

def exchange_button():
    try:
        entry = float(entry_cur.get())
        if entry <= 0:
            s = 1/0    
    except:
        messagebox.showwarning("cum", "Not valid input")

    print (entry)

    if Sell.get() == 1:
        print ("sell")

        if promenna.get() == cur_1.cur:
            give = round(float(entry_cur.get()),2)
            get =  round(float(float(entry_cur.get()) * cur_1.pp * 1.05),2)
            fee = round(float(get - give * cur_1.pp ),2)
            cur = cur_1.cur
        if promenna.get() == cur_2.cur:
            give = round(float(entry_cur.get()),2)
            get =  round(float(float(entry_cur.get()) * cur_2.pp * 1.05),2)
            fee = round(float(get - give * cur_2.pp ),2)
            cur = cur_2.cur
        if promenna.get() == cur_3.cur:
            give = round(float(entry_cur.get()),2)
            get =  round(float(float(entry_cur.get()) * cur_3.pp * 1.05),2)
            fee = round(float(get - give * cur_3.pp ),2)
            cur = cur_3.cur
        if promenna.get() == cur_4.cur:
            give = round(float(entry_cur.get()),2)
            get =  round(float(float(entry_cur.get()) * cur_4.pp * 1.05),2)
            fee = round(float(get - give * cur_4.pp ),2)
            cur = cur_4.cur
            
        top = Toplevel()
        top.geometry("300x100")
        top.title("Transaction")

        napis=Label(top,text="Get:" + str(get) + " Kč"  ,fg="green", font=("Arial",10))  
        napis.grid(row=2, column=0,sticky=W)

        napis=Label(top,text="Fee:" + str(fee)  + " Kč" ,font=("Arial",10))  
        napis.grid(row=1, column=0,sticky=W)

        napis=Label(top,text="Give:" + str(give)+   str(cur) ,fg="red", font=("Arial",10))  
        napis.grid(row=0, column=0,sticky=W)

    if Buy.get() == 1:
        print ("buy")

        if promenna.get() == cur_1.cur:
            give = round(float(entry_cur.get()),2)
            get =  round(float(float(entry_cur.get()) * cur_1.pp * 0.95),2)
            fee = round(float(get - give * cur_1.pp ),2)
            cur = cur_1.cur
        if promenna.get() == cur_2.cur:
            give = round(float(entry_cur.get()),2)
            get =  round(float(float(entry_cur.get()) * cur_2.pp * 0.95),2)
            fee = round(float(get - give * cur_2.pp ),2)
            cur = cur_2.cur
        if promenna.get() == cur_3.cur:
            give = round(float(entry_cur.get()),2)
            get =  round(float(float(entry_cur.get()) * cur_3.pp * 0.95),2)
            fee = round(float(get - give * cur_3.pp ),2)
            cur = cur_3.cur
        if promenna.get() == cur_4.cur:
            give = round(float(entry_cur.get()),2)
            get =  round(float(float(entry_cur.get()) * cur_4.pp * 0.95),2)
            fee = round(float(get - give * cur_4.pp ),2)
            cur = cur_4.cur
            
        top = Toplevel()
        top.geometry("300x100")
        top.title("Transaction")

        napis=Label(top,text="Get:" + str(give)+   str(cur) ,fg="green", font=("Arial",10))  
        napis.grid(row=2, column=0,sticky=W)

        napis=Label(top,text="Fee:" + str(fee)  + " Kč" ,font=("Arial",10))  
        napis.grid(row=1, column=0,sticky=W)

        napis=Label(top,text="Give:" + str(get) + " Kč"  ,fg="red", font=("Arial",10))  
        napis.grid(row=0, column=0,sticky=W)

tlacitko=Button(root,text="exchange",command=exchange_button)
tlacitko.grid(row=6, column=0,sticky=EW)

tlacitko2=Button(root,text="rates",command=rates)
tlacitko2.grid(row=6, column=1,sticky=EW)

###################################################################### čas

hodiny=Label(root,fg="red",font=("Arial",15))
hodiny.grid(row=7, column=0,sticky=E)

def AktualizujCas():
    ted=datetime.now()
    vystup=f"{ted.hour:02}:{ted.minute:02}:{ted.second:02}"
    hodiny["text"]=vystup
    root.after(1000,AktualizujCas)

AktualizujCas() 




mainloop()