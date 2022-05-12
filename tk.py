from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox as mbox




class MainMenu():
    
    def __init__(self, master):
        self.master  = master
        self.master.geometry('960x880')
        self.master.title('Ordering System')
        self.master.configure(bg = 'orange')
        self.left_frame()
        self.add_buttons()
        self.right_frame()
        

#-------------------------------------------------Functions------------------------------------------------------------------

    #Exit prompt
    def iExit(self):
        self.exitPrompt = mbox.askyesno("Exit Prompt","Are you sure you want to exit?")
        if self.exitPrompt:
            self.master.destroy()
        else:
            return 

      
#----------------------------------Frames--------------------------------------
    def left_frame(self):
        self.Left_Frame = Frame(self.master, width = 200, height = 140,  bg = 'orange')
        self.Left_Frame.pack(side = LEFT, fill = BOTH, pady = (62,0))
    def right_frame(self):
        self.Right_Frame = Frame(self.master, bg = 'red')
        self.Right_Frame.pack(side = RIGHT, fill = BOTH, expand = True)
#------------------------------Buttons---------------------------------------       
    def add_buttons(self):
        self.button1 = Button(self.Left_Frame, text = 'Home', name = 'home', fg = 'orange', bg = 'black', height = 4, width = 18, activebackground = 'orange', activeforeground = 'black', command = None )
        self.button1.configure(font=('Arial', 12))
        self.button1.pack()
        
        self.button2 = Button(self.Left_Frame, text = 'Customer Table', name = 'customerTable', fg = 'orange', bg = 'black', height = 4, width = 18, activebackground = 'orange', activeforeground = 'black')
        self.button2.configure(font=('Arial', 12))
        self.button2.pack()
        
        self.button3 = Button(self.Left_Frame, text = 'Order Table', name = 'orderTable', fg = 'orange', bg = 'black',height = 4, width = 18, activebackground = 'orange', activeforeground = 'black')
        self.button3.configure(font=('Arial', 12))
        self.button3.pack()
        
        self.button4 = Button(self.Left_Frame, text = 'Exit',name = 'exit', fg = 'orange', bg = 'black', height = 4, width = 18, activebackground = 'orange', activeforeground = 'black', command = self.iExit)
        self.button4.configure(font=('Arial', 12))
        self.button4.pack(side = 'bottom')

        self.button5 = Button(self.Left_Frame, text = 'Order Line Table',name = 'orderLineTable', fg = 'orange', bg = 'black', height = 4, width = 18, activebackground = 'orange', activeforeground = 'black')
        self.button5.configure(font=('Arial', 12))
        self.button5.pack()

        self.button6  = Button(self.Left_Frame, text = 'Product Table', name = 'productTable', fg = 'orange', bg = 'black', height = 4, width = 18, activebackground = 'orange', activeforeground = 'black', command  = None)
        self.button6.configure(font=('Arial', 12))
        self.button6.pack()

        self.button7  = Button(self.Left_Frame, text = 'Driver Table', name = 'driverTable', fg = 'orange', bg = 'black', height = 4, width = 18, activebackground = 'orange', activeforeground = 'black', command  = None)
        self.button7.configure(font=('Arial', 12))
        self.button7.pack()

        


        
        
#------------------------------Bind Commands-----------------------------------     
        self.button1.bind('<Enter>', self.button_hover1)
        self.button1.bind('<Leave>', self.button_hover_leave1)
        
        self.button2.bind('<Enter>', self.button_hover2)
        self.button2.bind('<Leave>', self.button_hover_leave2)
        
        self.button3.bind('<Enter>', self.button_hover3)
        self.button3.bind('<Leave>', self.button_hover_leave3)
        
        self.button4.bind('<Enter>', self.button_hover4)
        self.button4.bind('<Leave>', self.button_hover_leave4)

        self.button5.bind('<Enter>', self.button_hover5)
        self.button5.bind('<Leave>', self.button_hover_leave5)

        self.button6.bind('<Enter>', self.button_hover6)
        self.button6.bind('<Leave>', self.button_hover_leave6)

        self.button7.bind('<Enter>', self.button_hover7)
        self.button7.bind('<Leave>', self.button_hover_leave7)


   

        
#-------------------Hover/ Leave Functions------------------------------
    def button_hover1(self, event):
        self.button1['bg'] = 'white'
    def button_hover_leave1(self, event):
        self.button1['bg'] = 'black'  
    def button_hover2(self, event):
        self.button2['bg'] = 'white'
    def button_hover_leave2(self, event):
        self.button2['bg'] = 'black' 
    def button_hover3(self, event):
        self.button3['bg'] = 'white'  
    def button_hover_leave3(self, event):
        self.button3['bg'] = 'black'  
    def button_hover4(self, event):
        self.button4['bg'] = 'white'    
    def button_hover_leave4(self, event): 
        self.button4['bg'] = 'black'
    def button_hover5(self, event):
        self.button5['bg'] = 'white'    
    def button_hover_leave5(self, event): 
        self.button5['bg'] = 'black'
    def button_hover6(self, event):
        self.button6['bg'] = 'white'    
    def button_hover_leave6(self, event): 
        self.button6['bg'] = 'black'
    def button_hover7(self, event):
        self.button7['bg'] = 'white'    
    def button_hover_leave7(self, event): 
        self.button7['bg'] = 'black'
       
#---------------------- Pages -----------------------------------
    def home_page(self):
        self.home_label = Label(self.Right_Frame, text = 'Home Page', relief = RAISED, font = ('Calibri', 18, 'bold'), fg = 'black', bg = 'red')
        self.home_label.place(x = 360, y = 50)
        
    def displayRecordTreeView(self):
        x0 = self.Right_Frame.winfo_screenwidth()/2


        # Data frame - frame used to place the scrollbars and treeview
        self.dataFrame = Frame(self.Right_Frame)
        self.dataFrame.config(bg='#d6b919', relief = 'ridge', bd = 10)
        self.dataFrame.place(x = x0, y = 200, height = 200, width = 575, anchor = 'center')
       
      



        titleLabel1 = Label(self.Right_Frame, text = "Records",font = ("Calibri",20,"bold"), \
                           fg = "black",bg='#d6b919', relief = 'ridge', bd = 5,width = 15)
        titleLabel1.place(x = x0, y = 50, anchor = 'center')

        #Configure the treeview  
        self.myTree = ttk.Treeview(self.dataFrame)

        #Configure scrollbars on the frame
        xscrollbar = Scrollbar(self.dataFrame, orient=HORIZONTAL, command = self.myTree.xview)
        yscrollbar = Scrollbar(self.dataFrame, orient=VERTICAL, command = self.myTree.yview)

        xscrollbar.pack(side = BOTTOM, fill = X)    
        yscrollbar.pack(side = RIGHT, fill = Y)

        self.myTree.configure(xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)

        #Now pack the tree and the frame correctly
        self.myTree.pack()

      

        #Now time for displaying titles and set the treeview
        conn = sqlite3.connect('test.db')
        try:
            cur = conn.execute("Select * from Company order by ID desc")
            row = cur.fetchone()
        except:
           return 

        self.myTree['columns'] = ("Name", "Age", "Address", "Salary")
        self.myTree.heading("#0", text = "ID",anchor = "w")
        self.myTree.column("#0", anchor = "w", width = 45, minwidth=45, stretch=0)

        self.myTree.heading("Name", text = "Name")
        self.myTree.column("Name", anchor="center", width=100, minwidth=100, stretch=0)

        self.myTree.heading("Age", text = "Age")
        self.myTree.column("Age", anchor="center", width=100, minwidth=100, stretch=0)

        self.myTree.heading("Address", text = "Address")
        self.myTree.column("Address", anchor="center", width=100, minwidth=100, stretch=0)

        self.myTree.heading("Salary", text = "Salary")
        self.myTree.column("Salary", anchor="center", width=190, minwidth=100, stretch=0)

        #add data to the treeview
        while row is not None:
            self.myTree.insert('','0',text=row[0], \
                              values=(row[0],row[1],row[2],row[3]))
            row = cur.fetchone()

        Button2 = Button(self.Right_Frame, text = "Display Selected Record", font = 20, fg = 'purple', \
                             command = None).place(x = 575 , y = 350)
        Button3 = Button(self.Right_Frame, text = "Delete Record", font = 20, fg = 'purple', \
                             command = None).place(x = 775, y  = 350)
        Button4 = Button(self.Right_Frame, text = 'Delete all selected records', font = 20, fg = 'purple', command = None).place(x= 900, y= 350)

        
        



    
if __name__ == '__main__':   
    root = Tk()
    app = MainMenu(root)
    root.mainloop()
