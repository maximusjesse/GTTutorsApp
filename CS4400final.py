from tkinter import *
import urllib.request
import pymysql

class Gui():

#########################################################################
#This is the initial login window
    
    def __init__(self,win):
        self.LoginPage()
        
    def LoginPage(self):
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
                messagebox.showwarning("Success", "You have successfully logged in.")
                win.withdraw()
                self.win2=Toplevel()
                self.MainMenu()
                    
            cursor.close()
            self.db.commit()
            self.db.close()

##############################################################################                

    def MainMenu(self):
        #Figure 2

        win.title('GTT Main Menu')
        l1=Label(self.win2,text='Academic Year 2014')
        l1.grid(row=0,column=0,sticky=W,pady=20, padx=30)
        l2=Label(self.win2,text='Student Options')
        l2.grid(row=2,column=0,sticky=W,pady=10, padx=30)
        l3=Label(self.win2,text='Tutor Options')
        l3.grid(row=4,column=0,sticky=W,pady=10, padx=30)
        l4=Label(self.win2,text='Professor Options')
        l4.grid(row=6,column=0,sticky=W,pady=10, padx=30)
        l5=Label(self.win2,text='Administrator Options')
        l5.grid(row=8,column=0,sticky=W,pady=10, padx=30)

        b1=Button(self.win2,text='Search/Schedule Tutor',command=self.Search)
        b1.grid(row=3,column=0,sticky=W,padx=60)
        b2=Button(self.win2,text='Rate A Tutor',command=self.RateTutor)
        b2.grid(row=3,column=1,sticky=W,padx=20)
        b3=Button(self.win2,text='Apply',command=self.Apply)
        b3.grid(row=5,column=0,sticky=W,padx=60)
        b4=Button(self.win2,text='Find my Schedule',command=self.FindSched)
        b4.grid(row=5,column=1,sticky=W)
        b5=Button(self.win2,text='Add Recommendation',command=self.AddRec)
        b5.grid(row=7,column=0,sticky=W,padx=60)
        b6=Button(self.win2,text='Summary 1',command=self.Summary1)
        b6.grid(row=9,column=0,sticky=W,padx=60)
        b7=Button(self.win2,text='Summary 2',command=self.Summary2)
        b7.grid(row=9,column=1,sticky=W)
        b8=Button(self.win2,text='Exit',command=self.Exit)
        b8.grid(row=10,column=0, sticky=W,pady=50,padx=30,ipadx=20)

##############################################################################                
    #Code needed for figure 3 to function
    def scroll(self, *args):
        self.list1.yview(*args)
        self.list2.yview(*args)

    def clicked(self):
        a=self.ee.get()
        aa=self.eee.get()
        print (a)
        print(aa)

    def savefromtable2(self):
        s=self.var.get()
        ss=self.var2.get()
        sss=self.var3.get()
        self.mylist.append((s,ss+sss))
        print(self.mylist)

    def ok(self):
        self.clicked()
        self.savefromtable2()

    def TutCancel(self):
        self.win3.withdraw()
        self.win2=Toplevel()
        self.MainMenu()

    def AvailableTutorPage(self):
        #Figure 3 Begins
        #need tables

        self.win3.title('Available Tutors')
        l1=Label(self.win3,text='Course')
        l1.grid(row=0,column=0,sticky=W)

        e1 = Entry(self.win3, relief=RIDGE)
        e2= Entry(self.win3, relief=RIDGE)
        e1.grid(row=0, column=1, sticky=NSEW)
        e1.insert(END, 'School')
        e1.config(state="readonly")
        e2.grid(row=0, column=2, sticky=NSEW)
        e2.insert(END, 'Number')
        e2.config(state="readonly")

        #first table
        self.ee=Entry(self.win3, relief=RIDGE)
        self.ee.grid(row=1, column=1)
        self.eee=Entry(self.win3, relief=RIDGE)
        self.eee.grid(row=1, column=2, sticky=EW)

        l3=Label(self.win3,text='Availability: Note- tutor session can only be schedule for 1 hour per week for a given course')
        l3.grid(row=4,column=0,columnspan=7, sticky=W)

        #second table
        e3 = Entry(self.win3, relief=RIDGE)
        e3.grid(row=5, column=1, sticky=NSEW)
        e3.insert(END, 'Day')
        e3.config(state="readonly")
        e4= Entry(self.win3, relief=RIDGE)
        e4.grid(row=5, column=2, sticky=NSEW)
        e4.insert(END, 'Time')
        e4.config(state="readonly")
        e44= Entry(self.win3, relief=RIDGE)
        e44.grid(row=5, column=3, sticky=NSEW)
        e44.insert(END, 'AM/PM')
        e44.config(state="readonly")

        self.mylist=[]
        self.mylist2=[]
        self.var=StringVar()
        self.var.set("M")
        O=OptionMenu(self.win3, self.var, "M", "T", "W", "R", "F")
        O.grid(row=10, column=1)

        self.var2=StringVar()
        self.var2.set("1")
        O2=OptionMenu(self.win3, self.var2, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
        O2.grid(row=10, column=2)

        self.var3=StringVar()
        self.var3.set("AM")
        O3=OptionMenu(self.win3, self.var3, "AM", "PM")
        O3.grid(row=10, column=3)
        
        b1=Button(self.win3,width=8, text='OK', command=self.ok)
        b1.grid(row=12)

        #third table
        l5=Label(self.win3,text='Available Tutors')
        l5.grid(row=13,column=3)

        e5 = Entry(self.win3, relief=RIDGE)
        e5.grid(row=14, column=0, sticky=NSEW)
        e5.insert(END, 'First Name')
        e5.config(state="readonly")
        e6= Entry(self.win3, relief=RIDGE)
        e6.grid(row=14, column=1, sticky=NSEW)
        e6.insert(END, 'Last Name')
        e6.config(state="readonly")
        e7 = Entry(self.win3, relief=RIDGE)
        e7.grid(row=14, column=2, sticky=NSEW)
        e7.insert(END, 'Email')
        e7.config(state="readonly")
        e8= Entry(self.win3, relief=RIDGE)
        e8.grid(row=14, column=3, sticky=NSEW)
        e8.insert(END, 'Avg Prof Rating')
        e8.config(state="readonly")
        e9 = Entry(self.win3, relief=RIDGE)
        e9.grid(row=14, column=4, sticky=NSEW)
        e9.insert(END, '# Professors')
        e9.config(state="readonly")
        e10= Entry(self.win3, relief=RIDGE)
        e10.grid(row=14, column=5, sticky=NSEW)
        e10.insert(END, 'Avg Student Rating')
        e10.config(state="readonly")
        e11= Entry(self.win3, relief=RIDGE)
        e11.grid(row=14, column=6, sticky=NSEW)
        e11.insert(END, '# Students')
        e11.config(state="readonly")

        rowss = []
        for i in range(5):
            colu = []
            e = Entry(relief=RIDGE)
            for j in range(7):
                e = Entry(self.win3,relief=RIDGE)
                e.grid(row=i+15, sticky=NSEW)
                e.insert(END, '%d' %i)
                e.grid(column=j, sticky=NSEW)
                e.insert(END, '%d' %j)
                colu.append(e)
            rowss.append(colu)

        l6=Label(self.win3,text='                                               ')
        l6.grid(row=20,column=0, columnspan=10)
        b2=Button(self.win3,width=20, text='Schedule a Tutor', command=self.SchTutor)
        b2.grid(row=21, column=0, columnspan= 2, sticky=W)
        b3=Button(self.win3,width=20, text='Cancel', command=self.TutCancel)
        b3.grid(row=21, column=2, sticky=W)
        l7=Label(self.win3,text='                                               ')
        l7.grid(row=22,column=0, columnspan=10)

        
##############################################################################                

    def ScheduleTutorPage(self):
        #Figure 4

        self.win4.title('Schedule a Tutor')
        l1=Label(self.win4,text='Select a Tutor your Course')
        l1.grid(row=0,column=0,sticky=EW)

        ##Need code for a table here

        l2=Label( self.win4,text='NOTE: Only one box under the select column may be checked')
        l2.grid(row=2,column=0,sticky=W,pady=20, padx=30)

        b2=Button( self.win4, text="Ok")
        b2.grid(row=3,column=0,sticky=W,ipadx=5,pady=20,padx=30)
        b3=Button( self.win4, text="Cancel", width=5)
        b3.grid(row=3,column=0,sticky=W,pady=20,padx=100)

        
##############################################################################                


    def TutorEvalPage(self):
        #Figure 5
        #needs list of courses

        self.win5.title('Student Tutor Evaluation')

        self.var=IntVar()
   
        l1=Label(self.win5,text='Course')
        l1.grid(row=0,column=0,sticky=W,pady=20, padx=30)
        l2=Label(self.win5,text='Tutor Name')
        l2.grid(row=0,column=1,sticky=E)
        l3=Label(self.win5,text='Descriptive Evaluation')
        l3.grid(row=1,column=0,sticky=W,pady=20, padx=30)
        l4=Label(self.win5,text='Numeric Evaluation')
        l4.grid(row=3,column=0,sticky=W,pady=20, padx=30)

        e1=Entry(self.win5, state='normal',width=40)
        e1.grid(row=0,column=2,sticky=W)
        t1=Text(self.win5,width=60,height=10,bd=5)
        t1.grid(row=2,column=0,columnspan=2,padx=20)


        c4=Radiobutton(self.win5,state='normal',text='4 Highly Recommend',variable=self.var,value=4)
        c4.grid(row=4,column=0,sticky=W,padx=30)
        c3=Radiobutton(self.win5,state='normal',text='3 Recommend',variable=self.var,value=3)
        c3.grid(row=5,column=0,sticky=W,padx=30)
        c2=Radiobutton(self.win5,state='normal',text='2 Recommend with reservation',variable=self.var,value=2)
        c2.grid(row=6,column=0,sticky=W,padx=30)
        c1=Radiobutton(self.win5,state='normal',text='1 Do not recommend',variable=self.var,value=1)
        c1.grid(row=7,column=0,sticky=W,padx=30)

        b2=Button(self.win5, text="Ok")
        b2.grid(row=8,column=0,sticky=W,ipadx=10,pady=20,padx=30)

    def EvalOk(self):
        pass

        

##############################################################################                

    def TutorAppPage(self):
        
        ##Figure 6
        ll1= Label (self.win6,text="Student Information")
        ll1.grid(row=0, column=0, sticky=W)
        L1= Label(self.win6,text="Georgia Tech ID:")
        L1. grid(row=1, column=0, sticky=W)
        L2= Label(self.win6,text="First Name")
        L2. grid(row=2, column=0, sticky=W)
        L3= Label(self.win6,text="Email")
        L3.grid(row=3, column=0, sticky=W)
        L4=Label(self.win6,text="GPA")
        L4.grid(row=4, column=0, sticky=W)
        e1= Entry(self.win6)
        e1.grid(row=1, column=0, sticky=E,padx=20)
        e2=Entry(self.win6)
        e2.grid(row=2, column=0, sticky=E,padx=20)
        e3=Entry(self.win6)
        e3.grid(row=3, column=0, sticky=E,padx=20)
        e4=Entry(self.win6)
        e4.grid(row=4, column=0, sticky=E,padx=20)
       
        L4= Label(self.win6,text="Last Name")
        L4.grid(row=1, column=1, sticky=W, padx=50)
        L5=Label(self.win6,text="Telephone")
        L5.grid(row=2, column=1, sticky=W, padx=50)
        e5=Entry(self.win6)
        e5.grid(row=1, column=1,padx=80)
        e6=Entry(self.win6)
        e6.grid(row=2, column=1,padx=80)

        self.v = StringVar()
        
        r1= Radiobutton(self.win6, text="Undergraduate", variable=self.v, value="u")
        r1.grid(row=3, column=1, sticky=W,padx=100)
        r2=Radiobutton(self.win6, text="Graduate", variable=self.v, value="g")
        r2.grid(row=4, column=1, sticky=W, padx=100)
        self.v.set("u")

        L6= Label(self.win6,text="Courses for Tutoring")
        L6.grid(row=7, column=0, sticky=W,pady=10)
        L7= Label(self.win6,text="Check the GTA box if you have been a graduate TA for the course.")
        L7.grid(row=8, column=0, columnspan=3, sticky=W,pady=10)

        e7 = Entry(self.win6,relief=RIDGE)
        e7.grid(row=9, column=0, sticky=EW)
        e7.insert(END, 'School')
        e7.config(state="readonly")
        e8= Entry(self.win6,relief=RIDGE)
        e8.grid(row=9, column=1, sticky=EW)
        e8.insert(END, 'Number')
        e8.config(state="readonly")
        e9= Entry(self.win6,relief=RIDGE)
        e9.grid(row=9, column=2, sticky=EW)
        e9.insert(END, 'GTA')
        e9.config(state="readonly")

        #connects to the database and returns list for courses
        self.Connect()
        cursor=self.db.cursor()
        sql="SELECT * FROM Course"
        cursor.execute(sql)
        courses=[]
        for x in cursor:
            courses.append(x)
        print(courses)
            
        #if self.v.get()=='u':
        for i in range(7):
            e = Entry(relief=RIDGE)
            for j in range(3):
                if j<2:
                    e = Entry(relief=RIDGE)
                    e.grid(row=i+10, sticky=NSEW)
                    e.insert(END, '%d' %i)
                    e.grid(column=j+1, sticky=NSEW)
                    e.insert(END, '%d' %j)
                if j==2:
                    self.v2=IntVar()
                    r1= Checkbutton(win, variable=self.v2)
                    r1.grid(row=i+10, column=j+1, sticky=EW)
        
        #else:
        #    pass

        
        L7= Label(self.win6,text="Available Days/Time")
        L7.grid(row=20, column=0, sticky=W,pady=10)

        f1=LabelFrame(self.win6, text='Monday',width=650, height=60)
        f1.grid(row=21, sticky=W, columnspan=3)
        f2=LabelFrame(self.win6, text='Tuesday',width=650, height=60)
        f2.grid(row=22, sticky=W, columnspan=3)
        f3=LabelFrame(self.win6, text='Wednesday',width=650, height=60)
        f3.grid(row=23, sticky=W, columnspan=3)
        f4=LabelFrame(self.win6, text='Thursday',width=650, height=60)
        f4.grid(row=24, sticky=W, columnspan=3)
        f5=LabelFrame(self.win6, text='Friday',width=650, height=60)
        f5.grid(row=25, sticky=W, columnspan=3)

        #Stuff for the checkboxes
        self.v1=IntVar()
        self.v2=IntVar()
        self.v3=IntVar()
        self.v4=IntVar()
        self.v5=IntVar()
        self.v6=IntVar()
        self.v7=IntVar()
        self.v8=IntVar()
        self.v9=IntVar()
        self.v10=IntVar()
        self.v11=IntVar()
        self.v12=IntVar()
        self.v13=IntVar()
        self.v14=IntVar()
        self.v15=IntVar()
        self.v16=IntVar()
        self.v17=IntVar()
        self.v18=IntVar()
        self.v19=IntVar()
        self.v20=IntVar()
        self.v21=IntVar()
        self.v22=IntVar()
        self.v23=IntVar()
        self.v24=IntVar()
        self.v25=IntVar()
        self.v26=IntVar()
        self.v27=IntVar()
        self.v28=IntVar()
        self.v29=IntVar()
        self.v30=IntVar()
        self.v31=IntVar()
        self.v32=IntVar()
        self.v33=IntVar()
        self.v34=IntVar()
        self.v35=IntVar()
        self.v36=IntVar()
        self.v37=IntVar()
        self.v38=IntVar()
        self.v39=IntVar()
        self.v40=IntVar()


        c1 = Checkbutton(self.win6, text = "9am",variable=self.v1)
        c1.grid(row=21,sticky=W, columnspan=4,padx=3)
        c2 = Checkbutton(self.win6, text = "10am",variable=self.v2)
        c2.grid(row=21,sticky=W, columnspan=4,padx=80)
        c3 = Checkbutton(self.win6, text = "11am",variable=self.v3)
        c3.grid(row=21,sticky=W, columnspan=4,padx=160)
        c4 = Checkbutton(self.win6, text = "12pm",variable=self.v4)
        c4.grid(row=21,sticky=W, columnspan=4,padx=240)
        c5 = Checkbutton(self.win6, text = "1pm",variable=self.v5)
        c5.grid(row=21,sticky=W, columnspan=4,padx=320)
        c6 = Checkbutton(self.win6, text = "2pm",variable=self.v6)
        c6.grid(row=21,sticky=W, columnspan=4,padx=400)
        c7 = Checkbutton(self.win6, text = "3pm",variable=self.v7)
        c7.grid(row=21,sticky=W, columnspan=4,padx=480)
        c8 = Checkbutton(self.win6, text = "4pm",variable=self.v8)
        c8.grid(row=21,sticky=W, columnspan=4,padx=560)

        tc1 = Checkbutton(self.win6, text = "9am",variable=self.v9)
        tc1.grid(row=22,sticky=W, columnspan=4,padx=3)
        tc2 = Checkbutton(self.win6, text = "10am",variable=self.v10)
        tc2.grid(row=22,sticky=W, columnspan=4,padx=80)
        tc3 = Checkbutton(self.win6, text = "11am",variable=self.v11)
        tc3.grid(row=22,sticky=W, columnspan=4,padx=160)
        tc4 = Checkbutton(self.win6, text = "12pm",variable=self.v12)
        tc4.grid(row=22,sticky=W, columnspan=4,padx=240)
        tc5 = Checkbutton(self.win6, text = "1pm",variable=self.v13)
        tc5.grid(row=22,sticky=W, columnspan=4,padx=320)
        tc6 = Checkbutton(self.win6, text = "2pm",variable=self.v14)
        tc6.grid(row=22,sticky=W, columnspan=4,padx=400)
        tc7 = Checkbutton(self.win6, text = "3pm",variable=self.v15)
        tc7.grid(row=22,sticky=W, columnspan=4,padx=480)
        tc8 = Checkbutton(self.win6, text = "4pm",variable=self.v16)
        tc8.grid(row=22,sticky=W, columnspan=4,padx=560)

        wc1 = Checkbutton(self.win6, text = "9am",variable=self.v17)
        wc1.grid(row=23,sticky=W, columnspan=4,padx=3)
        wc2 = Checkbutton(self.win6, text = "10am",variable=self.v18)
        wc2.grid(row=23,sticky=W, columnspan=4,padx=80)
        wc3 = Checkbutton(self.win6, text = "11am",variable=self.v19)
        wc3.grid(row=23,sticky=W, columnspan=4,padx=160)
        wc4 = Checkbutton(self.win6, text = "12pm",variable=self.v20)
        wc4.grid(row=23,sticky=W, columnspan=4,padx=240)
        wc5 = Checkbutton(self.win6, text = "1pm",variable=self.v21)
        wc5.grid(row=23,sticky=W, columnspan=4,padx=320)
        wc6 = Checkbutton(self.win6, text = "2pm",variable=self.v22)
        wc6.grid(row=23,sticky=W, columnspan=4,padx=400)
        wc7 = Checkbutton(self.win6, text = "3pm",variable=self.v23)
        wc7.grid(row=23,sticky=W, columnspan=4,padx=480)
        wc8 = Checkbutton(self.win6, text = "4pm",variable=self.v24)
        wc8.grid(row=23,sticky=W, columnspan=4,padx=560)

        rc1 = Checkbutton(self.win6, text = "9am",variable=self.v25)
        rc1.grid(row=24,sticky=W, columnspan=4,padx=3)
        rc2 = Checkbutton(self.win6, text = "10am",variable=self.v26)
        rc2.grid(row=24,sticky=W, columnspan=4,padx=80)
        rc3 = Checkbutton(self.win6, text = "11am",variable=self.v27)
        rc3.grid(row=24,sticky=W, columnspan=4,padx=160)
        rc4 = Checkbutton(self.win6, text = "12pm",variable=self.v28)
        rc4.grid(row=24,sticky=W, columnspan=4,padx=240)
        rc5 = Checkbutton(self.win6, text = "1pm",variable=self.v29)
        rc5.grid(row=24,sticky=W, columnspan=4,padx=320)
        rc6 = Checkbutton(self.win6, text = "2pm",variable=self.v30)
        rc6.grid(row=24,sticky=W, columnspan=4,padx=400)
        rc7 = Checkbutton(self.win6, text = "3pm",variable=self.v31)
        rc7.grid(row=24,sticky=W, columnspan=4,padx=480)
        rc8 = Checkbutton(self.win6, text = "4pm",variable=self.v32)
        rc8.grid(row=24,sticky=W, columnspan=4,padx=560)

        fc1 = Checkbutton(self.win6, text = "9am",variable=self.v33)
        fc1.grid(row=25,sticky=W, columnspan=4,padx=3)
        fc2 = Checkbutton(self.win6, text = "10am",variable=self.v34)
        fc2.grid(row=25,sticky=W, columnspan=4,padx=80)
        fc3 = Checkbutton(self.win6, text = "11am",variable=self.v35)
        fc3.grid(row=25,sticky=W, columnspan=4,padx=160)
        fc4 = Checkbutton(self.win6, text = "12pm",variable=self.v36)
        fc4.grid(row=25,sticky=W, columnspan=4,padx=240)
        fc5 = Checkbutton(self.win6, text = "1pm",variable=self.v37)
        fc5.grid(row=25,sticky=W, columnspan=4,padx=320)
        fc6 = Checkbutton(self.win6, text = "2pm",variable=self.v38)
        fc6.grid(row=25,sticky=W, columnspan=4,padx=400)
        fc7 = Checkbutton(self.win6, text = "3pm",variable=self.v39)
        fc7.grid(row=25,sticky=W, columnspan=4,padx=480)
        fc8 = Checkbutton(self.win6, text = "4pm",variable=self.v40)
        fc8.grid(row=25,sticky=W, columnspan=4,padx=560)
        
                
        b1=Button(self.win6, text='OK', width=5, command=self.OkButton)
        b1.grid(row=26, sticky=W, pady=10)


    def OkButton(self):
        self.datelist=[]
        if self.v1.get()==1:
            self.datelist.append(['Monday','9am'])
        if self.v2.get()==1:
            self.datelist.append(['Monday','10am'])
        if self.v3.get()==1:
            self.datelist.append(['Monday','11am'])
        if self.v4.get()==1:
            self.datelist.append(['Monday','12pm'])
        if self.v5.get()==1:
            self.datelist.append(['Monday','1pm'])
        if self.v6.get()==1:
            self.datelist.append(['Monday','2pm'])
        if self.v7.get()==1:
            self.datelist.append(['Monday','3pm'])
        if self.v8.get()==1:
            self.datelist.append(['Monday','4pm'])
        if self.v9.get()==1:
            self.datelist.append(['Tuesday','9am'])
        if self.v10.get()==1:
            self.datelist.append(['Tuesday','10am'])
        if self.v11.get()==1:
            self.datelist.append(['Tuesday','11am'])
        if self.v12.get()==1:
            self.datelist.append(['Tuesday','12pm'])
        if self.v13.get()==1:
            self.datelist.append(['Tuesday','1pm'])
        if self.v14.get()==1:
            self.datelist.append(['Tuesday','2pm'])
        if self.v15.get()==1:
            self.datelist.append(['Tuesday','3pm'])
        if self.v16.get()==1:
            self.datelist.append(['Tuesday','4pm'])
        if self.v17.get()==1:
            self.datelist.append(['Wednesday','9am'])
        if self.v18.get()==1:
            self.datelist.append(['Wednesday','10am'])
        if self.v19.get()==1:
            self.datelist.append(['Wednesday','11am'])
        if self.v20.get()==1:
            self.datelist.append(['Wednesday','12pm'])
        if self.v21.get()==1:
            self.datelist.append(['Wednesday','1pm'])
        if self.v22.get()==1:
            self.datelist.append(['Wednesday','2pm'])
        if self.v23.get()==1:
            self.datelist.append(['Wednesday','3pm'])
        if self.v24.get()==1:
            self.datelist.append(['Wednesday','4pm'])
        if self.v25.get()==1:
            self.datelist.append(['Thursday','9am'])
        if self.v26.get()==1:
            self.datelist.append(['Thursday','10am'])
        if self.v27.get()==1:
            self.datelist.append(['Thursday','11am'])
        if self.v28.get()==1:
            self.datelist.append(['Thursday','12pm'])
        if self.v29.get()==1:
            self.datelist.append(['Thursday','1pm'])
        if self.v30.get()==1:
            self.datelist.append(['Thursday','2pm'])
        if self.v31.get()==1:
            self.datelist.append(['Thursday','3pm'])
        if self.v32.get()==1:
            self.datelist.append(['Thursday','4pm'])
        if self.v33.get()==1:
            self.datelist.append(['Friday','9am'])
        if self.v34.get()==1:
            self.datelist.append(['Friday','10am'])
        if self.v35.get()==1:
            self.datelist.append(['Friday','11am'])
        if self.v36.get()==1:
            self.datelist.append(['Friday','12pm'])
        if self.v37.get()==1:
            self.datelist.append(['Friday','1pm'])
        if self.v38.get()==1:
            self.datelist.append(['Friday','2pm'])
        if self.v39.get()==1:
            self.datelist.append(['Friday','3pm'])
        if self.v40.get()==1:
            self.datelist.append(['Friday','4pm'])
        print(self.datelist)

        


############################################################################## 

    def ProfRecPage(self):
        
        #Figure 8
        self.win7.title('Professor Recommendation')
        var4=IntVar()
        var3=IntVar()
        var2=IntVar()
        var1=IntVar()

        l1=Label(self.win7,text='Student GTID')
        l1.grid(row=0,column=0,sticky=W,pady=20, padx=30)
        l2=Label(self.win7,text='Descriptive Evaluation')
        l2.grid(row=1,column=0,sticky=W,pady=20, padx=30)
        l3=Label(self.win7,text='Numeric Evaluation')
        l3.grid(row=3,column=0,sticky=W,pady=20, padx=30)

        e1=Entry(self.win7, state='normal',width=30)
        e1.grid(row=0,column=0,sticky=E)
        t1=Text(self.win7,width=60,height=10,bd=5)
        t1.grid(row=2,column=0,columnspan=2,padx=20)

        c4=Checkbutton(self.win7,state='normal',text='4 Highly Recommend',variable=var4)
        c4.grid(row=4,column=0,sticky=W,padx=30)
        c3=Checkbutton(self.win7,state='normal',text='3 Recommend',variable=var3)
        c3.grid(row=5,column=0,sticky=W,padx=30)
        c2=Checkbutton(self.win7,state='normal',text='2 Recommend with reservation',variable=var2)
        c2.grid(row=6,column=0,sticky=W,padx=30)
        c1=Checkbutton(self.win7,state='normal',text='1 Do not recommend',variable=var1)
        c1.grid(row=7,column=0,sticky=W,padx=30)

        b2=Button(self.win7, text="Ok")
        b2.grid(row=8,column=0,sticky=W,ipadx=10,pady=20,padx=30)
        
    def Search(self):
        self.win2.withdraw()
        self.win3=Toplevel()
        self.AvailableTutorPage()

    def SchTutor(self):
        self.win3.withdraw()
        self.win4=Toplevel()
        self.ScheduleTutorPage()

    def RateTutor(self):
        self.win2.withdraw()
        self.win5=Toplevel()
        self.TutorEvalPage()

    def Apply(self):
        self.win2.withdraw()
        self.win6=Toplevel()
        self.TutorAppPage()
        

    def FindSched(self):
        pass

    def AddRec(self):
        self.win2.withdraw()
        self.win7=Toplevel()
        self.ProfRecPage()

    def Summary1(self):
        pass

    def Summary2(self):
        pass

    def Exit(self):
        self.win2.destroy()
        

win = Tk()
myObj=Gui(win)
win.mainloop()
