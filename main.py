import time
import concurrent.futures
import dao
from bean import Bean
from dao import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
win=Tk()
win.state("zoomed")
win.configure(bg='pink')
win.title("ATM")
l1=Label(win,text="Student Bank Of India",font=('Arial',30,"bold"),bd=3,bg="pink",fg="black")
l1.pack(side="top", anchor="center")
ab=Bean()
thread=concurrent.futures.ThreadPoolExecutor(max_workers=2)
def welcome():
    frm = Frame(win)
    frm.configure(bg="pink")
    frm.place(relx=0, rely=.1, relwidth=1, relheight=.9)
    l1=Label(frm,text=f"Welcom to our ATM {ab.getname()} ",font=('Arial',25,), bd=3, bg="pink",fg="black")
    l1.pack(side="top", anchor="center")
    def withdrow():
        frm = Frame(win)
        frm.configure(bg="pink")
        frm.place(relx=0, rely=.1, relwidth=1, relheight=.9)
        l1 = Label(frm, text="Case Withdrow", font=('Arial', 25,), bd=3, bg="pink", fg="grey")
        l1.pack(side="top", anchor="center")
        def Withdrow1():
            a=e1.get()
            if(len(a)==0 or a.isnumeric()==0):
                messagebox.showwarning("Warning","Enter valid Ammount")
            else:
                ab.setTransType("Withdrow")
                ab.setDebitAmmount(float(a))
                z=dao.Withdrow().withdrow(ab)
                if(z==1):
                    messagebox.showinfo("withdrow","Sucessfull")
                    frm.destroy()
                    login()
                else:
                    messagebox.showinfo("Transaction","Failed Withdrow")
                    frm.destroy()
                    login()
        def back():
            welcome()
        l2=Label(frm, text="Withdraw Amount:", font=('Arial', 20,'bold'), bd=3, bg="pink", fg="orange")
        l2.place(relx=.25,rely=.20)
        e1=Entry(frm,font=('Arial',20),bd=3,bg='white',fg='black')
        e1.place(relx=.45, rely=.20)
        e1.focus()
        b1 = Button(frm, text="     Enter    ", font=('Arial', 20,), bd=3, bg="grey", fg="blue", command=Withdrow1)
        b1.place(relx=.5 ,rely=.30)
        b2 = Button(frm, text="    Back     ", font=('Arial', 20,), bd=3, bg="grey", fg="blue",command=back)
        b2.place(relx=.35, rely=.30)
    def deposit():
        frm = Frame(win)
        frm.configure(bg="pink")
        frm.place(relx=0, rely=.1, relwidth=1, relheight=.9)
        l1 = Label(frm, text="Case Deposit", font=('Arial', 25,), bd=3, bg="pink", fg="grey")
        l1.pack(side="top", anchor="center")
        def deposit1():
            a=e1.get()
            if(len(a)==0 or a.isnumeric()==0):
                messagebox.showwarning("Warning","Enter valid Amount")
            else:
                ab.setTransType("Deposit")
                ab.setCreditAmmount(float(a))
                z1=dao.Deposit()
                z=z1.deposit(ab)
                if(z==1):
                    messagebox.showinfo("Deposit","Sucessfull")
                    frm.destroy()
                    login()
                else:
                    messagebox.showinfo("Deposit","Failed Deposit")
                    frm.destroy()
                    login()
        def back():
            welcome()
        l2=Label(frm, text="Deposit Amount:", font=('Arial', 20,'bold'), bd=3, bg="pink", fg="orange")
        l2.place(relx=.25,rely=.20)
        e1=Entry(frm,font=('Arial',20),bd=3,bg='white',fg='black')
        e1.place(relx=.45, rely=.20)
        e1.focus()
        b1 = Button(frm, text="     Enter    ", font=('Arial', 20,), bd=3, bg="grey", fg="blue", command=deposit1)
        b1.place(relx=.5 ,rely=.30)
        b2 = Button(frm, text="    Back     ", font=('Arial', 20,), bd=3, bg="grey", fg="blue",command=back)
        b2.place(relx=.35, rely=.30)
    def Transfer():
        frm = Frame(win)
        frm.configure(bg="pink")
        frm.place(relx=0, rely=.1, relwidth=1, relheight=.9)
        l1 = Label(frm, text="Transfer", font=('Arial', 25,), bd=3, bg="pink", fg="grey")
        l1.pack(side="top", anchor="center")
        def Transfer1():
            a=e1.get()
            b=e2.get()
            if(len(a)==0 or a.isnumeric()==0 ):
                messagebox.showwarning("Warning","Enter valid Amount Or Account_No")
            else:
                ab.setTransType("Transfer")
                ab.setTransferAmmount(float(a))
                ab.setAccountNo1(b)
                z=dao.Transfer()
                y=z.transfer(ab)
                if(y==1):
                    messagebox.showinfo("Transfer","Sucessfull")
                    frm.destroy()
                    login()
                else:
                    messagebox.showinfo("Transfer","Failed ")
                    frm.destroy()
                    login()
        def back():
            welcome()
        l2=Label(frm, text="Transfer Amount:", font=('Arial', 20,'bold'), bd=3, bg="pink", fg="orange")
        l2.place(relx=.25,rely=.20)
        e1=Entry(frm,font=('Arial',20),bd=3,bg='white',fg='black')
        e1.place(relx=.45, rely=.20)
        l3 = Label(frm, text="     Account No:", font=('Arial', 20, 'bold'), bd=3, bg="pink", fg="orange")
        l3.place(relx=.27, rely=.30)
        e2 = Entry(frm, font=('Arial', 20), bd=3, bg='white', fg='black')
        e2.place(relx=.45, rely=.30)
        e1.focus()
        b1 = Button(frm, text="     Enter    ", font=('Arial', 20,), bd=3, bg="grey", fg="blue", command=Transfer1)
        b1.place(relx=.5 ,rely=.40)
        b2 = Button(frm, text="    Back     ", font=('Arial', 20,), bd=3, bg="grey", fg="blue",command=back)
        b2.place(relx=.35, rely=.40)

    def Transaction():
        frm = Frame(win)
        frm.configure(bg="pink")
        frm.place(relx=0, rely=.1, relwidth=1, relheight=.9)
        l1 = Label(frm, text="Transaction History", font=('Arial', 25,), bd=3, bg="pink", fg="grey")
        l1.pack(side="top", anchor="center")
        def back():
            welcome()
        def Trans():
            a=e1.get()
            a1=a.split(sep="/")
            a2=a1[2]+"-"+a1[0]+"-"+a1[1]
            frm = Frame(win)
            frm.configure(bg="pink")
            frm.place(relx=0, rely=.1, relwidth=1, relheight=.9)
            l1 = Label(frm, text="Transaction History", font=('Arial', 25,), bd=3, bg="pink", fg="grey")
            l1.pack(side="top", anchor="center")
            tv = ttk.Treeview(frm, columns=("0", "1", "2", "3", "4", "5"), show="headings", height=10)
            tv.pack()
            tv.heading("0", text="TransID ", anchor="w")
            tv.heading("1", text="TransType ", anchor="w")
            tv.heading("2", text="TransDate ", anchor="w")
            tv.heading("3", text="CreditAmount", anchor="w")
            tv.heading("4", text="DebitAmount", anchor="w")
            tv.heading("5", text="TotalAmount", anchor="w")
            z = TransactionHistory()
            y = z.Transaction(ab, a2)
            for i in y:
                tv.insert("", "end", values=i)
            b11 = Button(frm, text=" Ok ", font=('Arial', 12, "bold"), bd=1, bg="black", fg="white", command=welcome)
            b11.pack()
        l2 = Label(frm, text="Date(yyyy:mm:dd):", font=('Arial', 15, 'bold'), bg="pink", fg="black")
        l2.place(relx=.30, rely=.22)
        e1 = DateEntry(frm,selectmode='day',background="grey")
        e1.place(relx=.45, rely=.23)
        b1 = Button(frm, text="     Enter  ", font=('Arial', 12,"bold"), bd=1, bg="grey", fg="white", command=Trans)
        b1.place(relx=.5, rely=.30)
        b2 = Button(frm, text="    Back   ", font=('Arial', 12,"bold"), bd=1, bg="grey", fg="white", command=back)
        b2.place(relx=.42, rely=.30)
    def quite():
        login()
    def check_bal():
        frm = Frame(win)
        frm.configure(bg="pink")
        frm.place(relx=0, rely=.1, relwidth=1, relheight=.9)
        l1 = Label(frm, text="Available Balance", font=('Arial', 30,), bd=3, bg="pink", fg="black")
        l1.pack(side="top", anchor="center")
        l1 = Label(frm, text=f"{ab.getTotalAmmount()}", font=('Arial', 30,), bd=3, bg="white", fg="black")
        l1.pack()
        b1 = Button(frm, text="  Ok  ", font=('Arial', 20, "bold"), bd=1, bg="grey", fg="blue", command=welcome)
        b1.place(x=600,y=130)
    b1=Button(frm,text="Cash Withdraw", font=('Arial',20,), bd=3, bg="grey",fg="blue",command=withdrow)
    b1.place(relx=.3,rely=.20)
    b2 = Button(frm, text="Cash Deposit", font=('Arial', 20,), bd=3, bg="grey", fg="blue",command=deposit)
    b2.place(relx=.5, rely=.20)
    b3 = Button(frm, text="Money Transfer", font=('Arial', 20,), bd=3, bg="grey", fg="blue" ,command=Transfer)
    b3.place(relx=.3, rely=.35)
    b4 = Button(frm, text="Trans_History", font=('Arial', 20,), bd=3, bg="grey", fg="blue", command=Transaction)
    b4.place(relx=.5, rely=.35)
    b5 = Button(frm, text="   Quit_trans  ", font=('Arial', 20,), bd=3, bg="grey", fg="blue",command=quite)
    b5.place(relx=.5,rely=.5)
    b4 = Button(frm, text="Check Balance ", font=('Arial', 20,), bd=3, bg="grey", fg="blue",command=check_bal)
    b4.place(relx=.3, rely=.5)
def login():
    frm = Frame(win)
    frm.configure(bg="grey")
    frm.place(relx=0, rely=.1, relwidth=1, relheight=.9)
    def logout():
        time.sleep(30)
        login()
    def loginpage():
        try:
            a = e1.get()
            b = e2.get()
            if(len(a)==0 or len(e2.get())==0 or b.isnumeric()==0):
                messagebox.showwarning("Warning","Enter Valid ID and PIN")
            else:
                c=int(b)
                cur = DbConnection.connection().cursor()
                ser=cur.execute("select * from account where ID=%s and Pin=%s", (a, c))
                a1=cur.fetchone()
                if(ser > 0):
                    if(a1[0]==a and a1[1]==c):
                        ab.setAccountNo(a1[2])
                        ab.setname(a1[3])
                        ab.setTotalAmmount(a1[4])
                        frm.destroy()
                        thread.submit(welcome)
                        thread.submit(logout)
                    else:
                        messagebox.showerror("Error" ,"Invalid ID and PIN")
                else:
                    messagebox.showerror("Error", "Invalid ID and PIN")
        except EXCEPTION :
            messagebox.showerror("Error", "Exception")
    l1=Label(frm,text="ID:",font=('Arial',30,'bold'),fg='orange',bg="grey")
    l1.place(relx=.28,rely=.2)
    e1=Entry(frm,font=('Arial',30),bg='white')
    e1.place(relx=.33,rely=.2)
    e1.focus()
    l2=Label(frm,text="PIN:",font=('Arial',30,'bold'),fg='orange',bg="grey")
    l2.place(relx=.26,rely=.32)
    e2=Entry(frm,font=('Arial',30),bg='white',show='*')
    e2.place(relx=.33,rely=.32)
    b1=Button(frm,text="ENTER",font=('Arial',20,),bd=3,bg="powder blue",command=loginpage)
    b1.place(relx=.33,rely=.44)
login()
win.mainloop()
