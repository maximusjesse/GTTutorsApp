
from tkinter import *
import urllib.request
import pymysql




class Gui():

#########################################################################
#This is the initial login window


    def __init__(self,win):

        #Figure 1

        url = "http://espn.go.com/i/teamlogos/ncaa/med/trans/59.gif"
        response = urllib.request.urlopen(url)
        myPicture = response.read()
        import base64
        b64_data = base64.encodebytes(myPicture)

        self.photo = PhotoImage(data=b64_data)

        l = Label(win, image=self.photo)
        l.grid(row=0,columnspan=3,sticky=EW)

        win.title('GTT Login')

        l1=Label(win,text='Enter GTID')
        l1.grid(row=1,column=0,sticky=E)
        l2=Label(win,text='Enter Password')
        l2.grid(row=3,column=0,sticky=E)


        self.e1=Entry(win,state='normal', width=30)
        self.e1.grid(row=1,column=1)
        self.e2=Entry(win,state='normal', width=30)
        self.e2.grid(row=3,column=1)

        l3=Label(win,text='')
        l3.grid(row=4,column=0,sticky=W)

        l4=Label(win,text='')
        l4.grid(row=2,column=0,sticky=W)

        b1=Button(win,text='Ok', width=15, command=self.Login)
        b1.grid(row=5,columnspan=2)
        
#############################################################################
#Connects to the database 

    def Connect(self):
        try:
            self.db=pymysql.connect(host='academic-mysql.cc.gatech.edu',db='cs4400_Group_14',user='cs4400_Group_14',passwd='GdGw3XSz')
            return(self.db)
        except:
            messagebox.showwarning('Error','Could not connect. Please try again.')
        
#############################################################################

    def Login(self):
        gtid=self.e1.get() #Retrieves GTID from e1
        pw=self.e2.get() #Retrieves password from e2
        self.Connect() #connects to database

        if gtid == "":
                messagebox.showwarning("GTID?", "Please enter a username.")
        elif pw == "":
                messagebox.showwarning("Password?", "Please enter a password.")
        
        else:
            cursor = self.db.cursor()
            sql1 = "SELECT * FROM User WHERE Gtid = %s and Password = %s"
            cursor.execute(sql1,(gtid,pw))
            userNameList = []
            
            for item in cursor:
                userNameList.append(item)
            
            if len(userNameList) == 0 or userNameList[0][0] == '' or userNameList[0][0] == None:
                messagebox.showerror("Fail to Login","You've entered an unrecognizable username/password combination! Please try again!")
            else:
                messagebox.showinfo("Logged In","You've successfully logged in!")
                self.win.quit()
                self.MainMenu()
                    
            cursor.close()
            self.db.commit()
            self.db.close()


##############################################################################                

    def MainMenu(self):

        #Figure 2

        win.title('GTT Main Menu')

        l1=Label(win,text='Academic Year 2014')
        l1.grid(row=0,column=0,sticky=W,pady=20, padx=30)

        l2=Label(win,text='Student Options')
        l2.grid(row=2,column=0,sticky=W,pady=10, padx=30)

        l3=Label(win,text='Tutor Options')
        l3.grid(row=4,column=0,sticky=W,pady=10, padx=30)

        l4=Label(win,text='Professor Options')
        l4.grid(row=6,column=0,sticky=W,pady=10, padx=30)

        l5=Label(win,text='Administrator Options')
        l5.grid(row=8,column=0,sticky=W,pady=10, padx=30)

        b1=Button(win,text='Search/Schedule Tutor',command=self.Search)
        b1.grid(row=3,column=0,sticky=W,padx=60)
        b2=Button(win,text='Rate A Tutor',command=self.RateTutor)
        b2.grid(row=3,column=1,sticky=W,padx=20)
        b3=Button(win,text='Apply',command=self.Apply)
        b3.grid(row=5,column=0,sticky=W,padx=60)
        b4=Button(win,text='Find my Schedule',command=self.FindSched)
        b4.grid(row=5,column=1,sticky=W)
        b5=Button(win,text='Add Recommendation',command=self.AddRec)
        b5.grid(row=7,column=0,sticky=W,padx=60)
        b6=Button(win,text='Summary 1',command=self.Summary1)
        b6.grid(row=9,column=0,sticky=W,padx=60)
        b7=Button(win,text='Summary 2',command=self.Summary2)
        b7.grid(row=9,column=1,sticky=W)
        b8=Button(win,text='Exit',command=self.Exit)
        b8.grid(row=10,column=0, sticky=W,pady=50,padx=30,ipadx=20)

##############################################################################                


    def AvailableTutorPage(self):
        #Figure 3
        #need tables

        win.title('Available Tutors')
        
        l1=Label(win,text='Course')
        l1.grid(row=0,column=0,sticky=W,pady=20, padx=30)

        l2=Label(win,text='Availability Note: Tutor sessions can only be scheduled for 1 hour per week for a given course')
        l2.grid(row=1,column=0,sticky=W,pady=20, padx=30)

        l3=Label(win,text='Available Tutors')
        l3.grid(row=4,column=0, sticky=EW)

        b1=Button(win, text="Ok", width=5)
        b1.grid(row=3,column=0,sticky=W,pady=20, padx=30)
        b2=Button(win, text="Schedule a Tutor")
        b2.grid(row=6,column=0,sticky=W,pady=20, padx=30)
        b3=Button(win, text="Cancel", width=5)
        b3.grid(row=6,column=0,sticky=W,pady=20,padx=200)
        ##Need code for two tables here

        
##############################################################################                


    def ScheduleTutorPage(self):
        #Figure 4

        win.title('Schedule a Tutor')

        l1=Label(win,text='Select a Tutor your Course')
        l1.grid(row=0,column=0,sticky=EW)

        ##Need code for a table here

        l2=Label(win,text='NOTE: Only one box under the select column may be checked')
        l2.grid(row=2,column=0,sticky=W,pady=20, padx=30)

        b2=Button(win, text="Ok")
        b2.grid(row=3,column=0,sticky=W,ipadx=5,pady=20,padx=30)
        b3=Button(win, text="Cancel", width=5)
        b3.grid(row=3,column=0,sticky=W,pady=20,padx=100)

        
##############################################################################                


    def TutorEvalPage(self):
        #Figure 5
        #needs list of courses

        win.title('Student Tutor Evaluation')

        var4=IntVar()
        var3=IntVar()
        var2=IntVar()
        var1=IntVar()

        l1=Label(win,text='Course')
        l1.grid(row=0,column=0,sticky=W,pady=20, padx=30)
        l2=Label(win,text='Tutor Name')
        l2.grid(row=0,column=1,sticky=E)
        l3=Label(win,text='Descriptive Evaluation')
        l3.grid(row=1,column=0,sticky=W,pady=20, padx=30)
        l4=Label(win,text='Numeric Evaluation')
        l4.grid(row=3,column=0,sticky=W,pady=20, padx=30)

        e1=Entry(win, state='normal',width=40)
        e1.grid(row=0,column=2,sticky=W)
        t1=Text(win,width=60,height=10,bd=5)
        t1.grid(row=2,column=0,columnspan=2,padx=20)


        c4=Checkbutton(win,state='normal',text='4 Highly Recommend',variable=var4)
        c4.grid(row=4,column=0,sticky=W,padx=30)
        c3=Checkbutton(win,state='normal',text='3 Recommend',variable=var3)
        c3.grid(row=5,column=0,sticky=W,padx=30)
        c2=Checkbutton(win,state='normal',text='2 Recommend with reservation',variable=var2)
        c2.grid(row=6,column=0,sticky=W,padx=30)
        c1=Checkbutton(win,state='normal',text='1 Do not recommend',variable=var1)
        c1.grid(row=7,column=0,sticky=W,padx=30)

        b2=Button(win, text="Ok")
        b2.grid(row=8,column=0,sticky=W,ipadx=10,pady=20,padx=30)

##############################################################################                

    def 






############################################################################## 

    def ProfRecPage(self):
        
        #Figure 8
        win.title('Professor Recommendation')
        var4=IntVar()
        var3=IntVar()
        var2=IntVar()
        var1=IntVar()

        l1=Label(win,text='Student GTID')
        l1.grid(row=0,column=0,sticky=W,pady=20, padx=30)
        l2=Label(win,text='Descriptive Evaluation')
        l2.grid(row=1,column=0,sticky=W,pady=20, padx=30)
        l3=Label(win,text='Numeric Evaluation')
        l3.grid(row=3,column=0,sticky=W,pady=20, padx=30)

        e1=Entry(win, state='normal',width=30)
        e1.grid(row=0,column=0,sticky=E)
        t1=Text(win,width=60,height=10,bd=5)
        t1.grid(row=2,column=0,columnspan=2,padx=20)


        c4=Checkbutton(win,state='normal',text='4 Highly Recommend',variable=var4)
        c4.grid(row=4,column=0,sticky=W,padx=30)
        c3=Checkbutton(win,state='normal',text='3 Recommend',variable=var3)
        c3.grid(row=5,column=0,sticky=W,padx=30)
        c2=Checkbutton(win,state='normal',text='2 Recommend with reservation',variable=var2)
        c2.grid(row=6,column=0,sticky=W,padx=30)
        c1=Checkbutton(win,state='normal',text='1 Do not recommend',variable=var1)
        c1.grid(row=7,column=0,sticky=W,padx=30)

        b2=Button(win, text="Ok")
        b2.grid(row=8,column=0,sticky=W,ipadx=10,pady=20,padx=30)
        
            

            

    def Search(self):
        pass

    def RateTutor(self):
        pass

    def Apply(self):
        pass

    def FindSched(self):
        pass

    def AddRec(self):
        pass

    def Summary1(self):
        pass

    def Summary2(self):
        pass

    def Exit(self):
        pass
        
            
        
    
                  

        
        









win = Tk()
myObj=Gui(win)
win.mainloop()
