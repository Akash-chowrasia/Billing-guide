
from tkinter import *
import random
import tkinter.messagebox
import csv
import os
import datetime as dt


#FUNCTION TO ADD TRANSACTION

def addtransaction():
    user_id = str(entry_1.get()).split()
    tran_ammounts = str(entry_2.get()).split(" ")
    '''t=''
    for i in tran_ammounts:
        t+=i+' '
    iExit=tkinter.messagebox.askyesno("TRANSACTION MANAGEMENT SYSTEM","Amounts To be Added: "+t)
    if iExit>0:
        pass
    else:
        return '''
    with open('user-transaction.csv') as f3:
        thereader = csv.reader(f3)
        temp = []
        for row in thereader:
            for i in range(len(row)):
                temp.append(f'{row[i]}')
            if temp[0] in user_id:
                temp[1] = int(temp[1])+sum([int(j) for j in tran_ammounts])
                for j in range(len(tran_ammounts)):
                    temp.append(tran_ammounts[j])
            with open('temporary.csv','a',newline='') as f4:
                writing = csv.writer(f4)
                writing.writerow(temp)
            temp = []
    os.remove('user-transaction.csv')
    os.rename('temporary.csv','user-transaction.csv')
    ireset()
    tkinter.messagebox.showinfo("TRANSACTION MANAGEMENT SYSTEM","Transaction Added Successfully")


        

#FUNCTION TO EXIT
    
def iexit():
    iExit=tkinter.messagebox.askyesno("TRANSACTION MANAGEMENT SOFTWARE","DO YOU WANT TO EXIT ?")
    if iExit>0:
        root.destroy()
        return

def ireset():    
    entry_1.delete(0,'end')
    entry_2.delete(0,'end')
    entry_3.delete(0,'end')
    entry_4.delete(0,'end')
    entry_5.delete(0,'end')
    entry_6.delete(0,'end')



#FUNCTION FOR TRANSACTION REMOVE

def removetransaction():
    id_list = str(entry_3.get()).split(" ")
    '''iExit=tkinter.messagebox.askyesno("TRANSACTION MANAGEMENT SYSTEM","Do you want to Remove transactions?")
    if iExit>0:
        pass
    else:
        return'''
    with open('user-transaction.csv') as f5:
        thereader = csv.reader(f5)
        temp = []
        for row in thereader:
            if f'{row[0]}' in id_list:
                temp.append(f'{row[0]}')
                temp.append(0)
            else:
                for i in range(len(row)):
                        temp.append(f'{row[i]}')
            with open('temp.csv','a',newline='') as f6:
                thewriter = csv.writer(f6)
                thewriter.writerow(temp)
            temp = []
    os.remove('user-transaction.csv')
    os.rename('temp.csv','user-transaction.csv')    
    ireset()
    tkinter.messagebox.showinfo("TRANSACTION MANAGEMENT SYSTEM","Transaction removed successfully")


def removeperticular():
    tran_list = str(entry_6.get()).split()
    userid = str(entry_5.get())
    with open('user-transaction.csv') as f:
        thereader = csv.reader(f)
        temp = []
        total = 0
        for row in thereader:
            temp.append(f'{row[0]}')
            if f'{row[0]}' == userid:
                temp.append(' ')
                for i in range(2,len(row)):
                    if f'{row[i]}' in tran_list:
                        print(tran_list)
                        tran_list.remove(f'{row[i]}')
                    else:
                        total += int(f'{row[i]}')
                        temp.append(f'{row[i]}')
                    temp[1] = total
            else:
                temp.append(f'{row[1]}')
                for i in range(2,len(row)):
                    temp.append(f'{row[i]}')
            with open('temp.csv','a',newline='') as f1:
                thewriter = csv.writer(f1)
                thewriter.writerow(temp)
            temp = []
            total = 0
    os.remove('user-transaction.csv')
    os.rename('temp.csv','user-transaction.csv')
    ireset()
    tkinter.messagebox.showinfo("TRANSACTION MANAGEMENT SYSTEM","Transaction removed successfully")


def removeall():
    '''iExit=tkinter.messagebox.askyesno("TRANSACTION MANAGEMENT SYSTEM","Do You Want To Remove All Transactions?")
    if iExit>0:
        pass
    else:
        return'''
    '''with open('user-transaction.csv') as f5:
        thereader = csv.reader(f5)
        temp = []
        l = 0
        for row in thereader:
            temp.append(f'{row[0]}')
            if l == 0:
                temp.append('Total')
                l = 1
            else:
                temp.append(0)
            with open('temp.csv','a',newline='') as f6:
                thewriter = csv.writer(f6)
                thewriter.writerow(temp)
            temp = []'''
    os.remove('user-transaction.csv')
    #os.rename('temp.csv','user-transaction.csv')
    with open('user-transaction.csv','a',newline='') as f:
        thewriter = csv.writer(f)
        temp = ['ID','TOTAL']
        thewriter.writerow(temp)
        for i in range(1,101):
            temp = [i,0]
            thewriter.writerow(temp)
    ireset()
    tkinter.messagebox.showinfo("TRANSACTION MANAGEMENT SYSTEM","Transaction Removed Successfully")


#FUNCTION FOR GENERATING REPORTS

def generatereport():
    dr = os.listdir()
    if 'reports' in dr:
        if os.path.isdir('reports') == True:
            pass
        else:
            os.mkdir('reports')
    else:
        os.mkdir('reports')
    id_list = str(entry_4.get()).split()
    '''iExit=tkinter.messagebox.askyesno("TRANSACTION MANAGEMENT SYSTEM","Press YES To Generate Reports.")
    if iExit>0:
        pass
    else:
        return'''
    total = 0        
    d = str(dt.datetime.date(dt.datetime.now()))
    p = 'reports\\'+ 'report-'+'('
    for i in id_list:
        p+=i+','
    p+=')'+'-'
    p+=d        
    p+='.txt'    
    temp = ['  USER-IDS           TOTAL                 TRANSACTION  ']
    with open(p,'w',newline='') as f1:
        thewriter = csv.writer(f1)
        thewriter.writerow(temp)
    temp = [' '*2+'-'*2+' '*16+'-'*5+' '*18+'-'*10]        
    with open(p,'a',newline='') as f1:
        thewriter = csv.writer(f1)
        thewriter.writerow(temp)      
    with open('user-transaction.csv') as f:
        thereader = csv.reader(f)    
        for row in thereader:
            if f'{row[0]}' in id_list:                
                total += int(f'{row[1]}')                       
                t =' '*3+ f'{row[0]}'
                t =t+' '*(21-len(t))+f'{row[1]}'+' '*20
                for i in range(2,len(row)):
                    t += f'{row[i]}'+' '
                tm = [t]
                with open(p,'a',newline='') as f1:
                    thewriter = csv.writer(f1)
                    thewriter.writerow(tm)
        temp = [' '*2+'-'*5+' '*13+'-'*5]
        with open(p,'a',newline='') as f1:
            thewriter = csv.writer(f1)
            thewriter.writerow(temp)                                    
        temp = ['  TOTAL'+' '*14+str(total)]
        with open(p,'a',newline='') as f1:
            thewriter = csv.writer(f1)
            thewriter.writerow(temp)
        temp = [' '*2+'-'*5+' '*13+'-'*5]
        with open(p,'a',newline='') as f1:
            thewriter = csv.writer(f1)
            thewriter.writerow(temp) 
            
    ireset()
    tkinter.messagebox.showinfo("TRANSACTION MANAGEMENT SYSTEM","Report Is Stored Into Reports Folder!")


def generatecompletereport():
    dr = os.listdir()
    if 'reports' in dr:
        if os.path.isdir('reports') == True:
            pass
        else:
            os.mkdir('reports')
    else:
        os.mkdir('reports')
    '''iExit=tkinter.messagebox.askyesno("TRANSACTION MANAGEMENT SYSTEM","Press YES To Generate Reports.")
    if iExit>0:
        pass
    else:
        return'''
    total = 0        
    d = str(dt.datetime.date(dt.datetime.now()))
    p = 'reports\\'+ 'report-'+'all'+'-'    
    p+=d        
    p+='.txt'
    temp = ['  USER-IDS             TOTAL                 TRANSACTION  ']
    with open(p,'w',newline='') as f1:
        thewriter = csv.writer(f1)
        thewriter.writerow(temp)
    temp = [' '*2+'-'*2+' '*16+'-'*5+' '*18+'-'*10]        
    with open(p,'a',newline='') as f1:
        thewriter = csv.writer(f1)
        thewriter.writerow(temp)
    l=0 
    with open('user-transaction.csv') as f:
        thereader = csv.reader(f)    
        for row in thereader:
            if l == 0:
                l = 1
            else:    
                total += int(f'{row[1]}')                       
                t =' '*3+ f'{row[0]}'
                t =t+' '*(21-len(t))+f'{row[1]}'+' '*20
                for i in range(2,len(row)):
                    t += f'{row[i]}'+' '
                tm = [t]
                with open(p,'a',newline='') as f1:
                    thewriter = csv.writer(f1)
                    thewriter.writerow(tm)
        temp = [' '*2+'-'*5+' '*13+'-'*5]
        with open(p,'a',newline='') as f1:
            thewriter = csv.writer(f1)
            thewriter.writerow(temp)                                    
        temp = ['  TOTAL'+' '*14+str(total)]
        with open(p,'a',newline='') as f1:
            thewriter = csv.writer(f1)
            thewriter.writerow(temp)
        temp = [' '*2+'-'*5+' '*13+'-'*5]
        with open(p,'a',newline='') as f1:
            thewriter = csv.writer(f1)
            thewriter.writerow(temp) 
            
    ireset()
    tkinter.messagebox.showinfo("TRANSACTION MANAGEMENT SYSTEM","Report is stored into reports folder!")


root = Tk()
root.geometry("1300x700+0+0")
root.maxsize(width = 1600,height = 730)
root.minsize(width = 1150,height = 730)
root.title("TRANSACTION MANAGEMENT SOFTWARE")


#======= COLOR ============================
bg_color = "#074463"
fg_color = "white"
lbl_color = "white"

#TILTLE OF THE APP
title = Label(root,text = "TRANSACTION MANAGEMENT SOFTWARE",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)


#========== ADD TRANSACTION FRAME ==========#

F1 = LabelFrame(root,text = "ADD TRANSACTION",font = ("time new roman",12,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
F1.place(x = 0,y = 80,relwidth = 1,height = 120)

#=============== USER ID ===========#
Label(F1,text="USER-ID",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
entry_1 = Entry(F1,bd = 8,relief = GROOVE)
entry_1.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

#================= TRANSACTION AMOUNT ==============#
Label(F1,text = "TRANSACTION AMOUNTS",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
entry_2 = Entry(F1,bd = 8,relief = GROOVE)
entry_2.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)
        
#==================== Add Transaction Button ===============#
Button(F1,text = "  ADD TRANSACTION  ",bd = 7,relief = GROOVE,font = ("lucida",12,"bold"),bg = bg_color,fg = fg_color,command = addtransaction).grid(row = 0,column = 8,ipady = 5,padx = 60,ipadx = 19,pady = 5)





#========== REMOVE TRANSACTION ==========#

F2 = LabelFrame(root,text = "  REMOVE USER TRANSACTION  ",font = ("time new roman",12,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
F2.place(x = 0,y = 210,relwidth = 1,height = 120)

#=============== USERID ===========#
Label(F2,text="USER-ID",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
entry_3 = Entry(F2,bd = 8,relief = GROOVE)
entry_3.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)
        
#==================== REMOVE BUTTON ===============#
Button(F2,text = "REMOVE USER TRANSACTION",bd = 7,relief = GROOVE,font = ("lucida",12,"bold"),bg = bg_color,fg = fg_color,command = removetransaction).grid(row = 0,column = 4,ipady = 5,padx = 60,ipadx = 19,pady = 5)



#========== REMOVE PARTICULAR TRANSACTION ==========#

F7 = LabelFrame(root,text = "  REMOVE PARTICULAR TRANSACTION OF USER  ",font = ("time new roman",12,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
F7.place(x = 0,y = 340,relwidth = 1,height = 120)

#=============== USERID ===========#
Label(F7,text="USER-ID",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
entry_5 = Entry(F7,bd = 8,relief = GROOVE)
entry_5.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

#=============== TRANSACTIONS ===========#
Label(F7,text = "TRANSACTION",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
entry_6 = Entry(F7,bd = 8,relief = GROOVE)
entry_6.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)
        
#==================== REMOVE BUTTON ===============#
Button(F7,text = "REMOVE PARTICULAR TRANSACTIONS",bd = 7,relief = GROOVE,font = ("lucida",12,"bold"),bg = bg_color,fg = fg_color,command = removeperticular).grid(row = 0,column = 4,ipady = 5,padx = 60,ipadx = 19,pady = 5)




#========== USER REPORT ==========#

F3 = LabelFrame(root,text = "  GENERATE USER REPORT  ",font = ("time new roman",12,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
F3.place(x = 0,y = 470,relwidth = 1,height = 120)

#=============== USERID ===========#
Label(F3,text="USER-ID",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
entry_4 = Entry(F3,bd = 8,relief = GROOVE)
entry_4.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)
        
#==================== REMOVE BUTTON ===============#
Button(F3,text = "GENERATE USER REPORT",bd = 7,relief = GROOVE,font = ("lucida",12,"bold"),bg = bg_color,fg = fg_color,command = generatereport).grid(row = 0,column = 4,ipady = 5,padx = 60,ipadx = 19,pady = 5)        





#===========FOOTER ACTIONS=============#
F4 = LabelFrame(root,text = "  ACTIONS MENU  ",bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",12,"bold"))
F4.place(x = 0,y = 600,relwidth = 1,height = 110)

Button(F4,text = "REMOVE ALL TRANSACTIONS",bd = 7,relief = GROOVE,font = ("lucida",12,"bold"),bg = bg_color,fg = fg_color,command = removeall).grid(row = 0,column = 6,ipady = 5,padx = 60,ipadx = 19,pady = 5)

#========================
Button(F4,text = "GENERATE FINAL REPORT",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = generatecompletereport).grid(row = 0,column = 10,ipady = 5,padx = 60,ipadx = 19,pady = 5)

#====================
Button(F4,text = "RESET",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = ireset).grid(row = 0,column = 12,ipady = 5,padx = 60,ipadx = 19,pady = 5)

#======================
Button(F4,text = "EXIT",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = iexit).grid(row = 0,column = 14,ipady = 5,padx = 60,ipadx = 19,pady = 5)

LabelFrame(root,text = '  TRANSACTION MANAGEMENT SOFTWARE | DEVELOPED BY - TECHOX LLP  ',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("lucida",8,"bold")).place(x = 0,y = 713,relwidth = 1,height = 20)


root.mainloop()

