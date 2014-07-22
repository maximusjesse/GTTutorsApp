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
            return(self.db)
        except:
            messagebox.showwarning('Error','Could not connect. Please try again.')
        
#############################################################################

    def Login(self):
        self.gtid=self.e1.get() #Retrieves GTID from e1
        pw=self.e2.get() #Retrieves password from e2
        self.Connect() #connects to database

        if self.gtid == "":
                messagebox.showwarning("GTID?", "Please enter a username.")
        elif pw == "":
                messagebox.showwarning("Password?", "Please enter a password.")
        
        else:
            cursor = self.db.cursor()
            sql1 = "SELECT * FROM User WHERE Gtid = %s and Password = %s"
            cursor.execute(sql1,(self.gtid,pw))
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
        self.list2.yview(*args)
        self.list3.yview(*args)
        self.list4.yview(*args)
        self.list5.yview(*args)
        self.list6.yview(*args)
        self.list7.yview(*args)

    def clicked(self):
        self.a=self.ee.get()
        self.aa=self.eee.get()

    def savefromtable2(self):
        import time
        day=self.var.get()
        hour=self.var2.get()
        ampm=self.var3.get()
        timeString=time.strftime('%H',time.strptime(hour,'%I'))
        
        timeString2=time.strftime('%H:%M:%S',time.strptime(hour+ampm,'%I%p'))
       
        self.listbox.delete(0,len(self.mylist))
        self.mylist.append((day,hour, ampm))

        query= "Select Name, Email, ProfAvgRating, ProfNumRatings, StuAvgRating, StuNumRatings FROM (SELECT *FROM Figure3 WHERE %s=Figure3.School AND %s=Figure3.Number AND %s=Figure3.Weekday AND %s=Figure3.Time) A"
        db=pymysql.connect(host='academic-mysql.cc.gatech.edu',db='cs4400_Group_14',user='cs4400_Group_14',passwd='GdGw3XSz')
        cursor = db.cursor()        
        test=cursor.execute(query,(self.a, str(self.aa), day, str(timeString2)))
        test=cursor.fetchall()

        for i in self.mylist:
            self.listbox.insert(END, i)
            self.thelist.append(i)

        s = Scrollbar(win)
        s.grid(row=12, column=8, rowspan=15, sticky=W)

        self.list2 = Listbox(self.win3, yscrollcommand = s.set )
        self.list2.grid(row=15, column=1, sticky=EW)

        self.list3 = Listbox(self.win3, yscrollcommand = s.set )
        self.list3.grid(row=15, column=2, sticky=EW)
        self.list4 = Listbox(self.win3, yscrollcommand = s.set )
        self.list4.grid(row=15, column=3, sticky=EW)
        self.list5 = Listbox(self.win3, yscrollcommand = s.set )
        self.list5.grid(row=15, column=4, sticky=EW)

        self.list6 = Listbox(self.win3, yscrollcommand = s.set )
        self.list6.grid(row=15, column=5, sticky=EW)
        self.list7 = Listbox(self.win3, yscrollcommand = s.set )
        self.list7.grid(row=15, column=6, sticky=EW)

        s.config( command=self.scroll )

        leng=len(test)
        i=0
        e = Entry(win, relief=RIDGE)
        for j in range(leng):
            self.list2.insert(END, "%s" %test[j][0])
            self.list3.insert(END, "%s" %test[j][1])
            self.list4.insert(END, "%s" %test[j][2])
            self.list5.insert(END, "%s" %test[j][3])
            self.list6.insert(END, "%s" %test[j][4])
            self.list7.insert(END, "%s" %test[j][5])
        return


    def ok(self):
        self.clicked()
        self.thelist=[]
        self.savefromtable2()
        print(self.thelist)

    def cancel3(self):
        self.win3.withdraw()
        self.win2=Toplevel()
        self.MainMenu()
        

#########FIGURE 3 BEGINS###################
    def AvailableTutorPage(self):
        self.win3.title('Available Tutors')
        l1=Label(self.win3,text='Course')
        l1.grid(row=0,column=0,sticky=W)

        self.e1 = Entry(self.win3, relief=RIDGE)
        self.e2= Entry(self.win3, relief=RIDGE)
        self.e1.grid(row=0, column=1, sticky=NSEW)
        self.e1.insert(END, 'School')
        self.e1.config(state="readonly")
        self.e2.grid(row=0, column=2, sticky=NSEW)
        self.e2.insert(END, 'Number')
        self.e2.config(state="readonly")

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
        ######### Listbox appears
        self.listbox = Listbox(self.win3)
        self.listbox.grid(row=10, column=4, rowspan=3, padx=20)


        #third table
        l5=Label(self.win3,text='Available Tutors')
        l5.grid(row=13,column=3)
      
        e6 = Entry(self.win3, relief=RIDGE)
        e6.grid(row=14, column=1, sticky=NSEW)
        e6.insert(END, 'Name')
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


        l6=Label(self.win3,text='                                               ')
        l6.grid(row=20,column=0, columnspan=10)
        b2=Button(self.win3,width=20, text='Schedule a Tutor', command=self.SchTutor)
        b2.grid(row=30, column=0, columnspan= 2, sticky=W)
        b3=Button(self.win3,width=20, text='Cancel',command=self.cancel3)
        b3.grid(row=30, column=2, sticky=W)
        l7=Label(self.win3,text='                                               ')
        l7.grid(row=22,column=0, columnspan=10)

##############################################################################                

    def ScheduleTutorPage(self):
        #Figure 4

        self.win4.title('Schedule a Tutor')
        L1= Label(self.win4, text='Select your Tutor')
        L1.grid(row=0, column=2, columnspan=2, sticky=EW)

        e2= Entry(self.win4, relief=RIDGE)
        e2.grid(row=1, column=1, sticky=NSEW)
        e2.insert(END, 'Name')
        e2.config(state="readonly")
        e3= Entry(self.win4, relief=RIDGE, width=20)
        e3.grid(row=1, column=2, sticky=NSEW)
        e3.insert(END, 'Email')
        e3.config(state="readonly")
        e4= Entry(self.win4, relief=RIDGE)
        e4.grid(row=1, column=3, sticky=NSEW)
        e4.insert(END, 'Day')
        e4.config(state="readonly")
        e5= Entry(self.win4, relief=RIDGE)
        e5.grid(row=1, column=4, sticky=NSEW)
        e5.insert(END, 'Time')
        e5.config(state="readonly")
        e6= Entry(self.win4, relief=RIDGE)
        e6.grid(row=1, column=5, sticky=NSEW)
        e6.insert(END, 'Select')
        e6.config(state="readonly")
        ahh=[]
        
        da=len(self.thelist)
        import time
        db=pymysql.connect(host='academic-mysql.cc.gatech.edu',db='cs4400_Group_14',user='cs4400_Group_14',passwd='GdGw3XSz')
        cursor = db.cursor()

        self.b=[]
        c=[]        

        for i in range (da):
            #print(self.thelist[i][1]+self.thelist[i][2])
            t=time.strftime('%H:%M:%S',time.strptime(self.thelist[i][1]+self.thelist[i][2],'%I%p'))
            hey= "Select Name, Email, Weekday, Time FROM (SELECT * FROM Figure3 WHERE %s=Figure3.School AND %s=Figure3.Number AND %s=Figure3.Weekday AND %s=Figure3.Time) A"
            testing=cursor.execute(hey, (self.a, self.aa, str(self.thelist[i][0]), t))

            cur=cursor.fetchone()
            
            while cur is not None:
                self.b.append(cur)
                cur=cursor.fetchone()
            
        print(self.b)

        ra=len(self.b)
       

        for i in range(ra):
            e = Entry(self.win4, relief=RIDGE)
            for j in range(5):
                if j<4:
                    e = Entry(self.win4, relief=RIDGE)
                    e.grid(row=i+2, column=j+1, sticky=NSEW)
                    e.insert(END, self.b[i][j])
                    print(self.b[i][j])

        self.v=IntVar()
        for i in range(ra):
            r=Checkbutton(self.win4, variable=self.v, onvalue=i)
            r.grid(row=i+2, column=5)
        

        L1= Label(self.win4, text='NOTE: Only 1 box under the Select column may be checked')
        L1.grid(row=25, column=3, columnspan=2, sticky=EW)

        B1=Button(self.win4, text="OK", width=15, command=self.okpage)
        B1.grid(row=26, column=1)
        B2=Button(self.win4, text="Cancel", width=15)
        B2.grid(row=26, column=3, sticky=W)

    def okpage(self):
        self.checker=[]
        k=self.v.get()
        self.checker.append(k)
        self.tupler=self.b[k]
        print(self.tupler)
        db=pymysql.connect(host='academic-mysql.cc.gatech.edu',db='cs4400_Group_14',user='cs4400_Group_14',passwd='GdGw3XSz')
        cursor2 = db.cursor()
        gt=self.gtid
        query2="Update TutorTimeSlots Set TuteeID=%s Where TutorID= (Select StudentID FROM Student Where Name=%s) AND Time=%s"
        print(self.tupler[2])
        cursor2.execute(query2, (gt, self.tupler[0], str(self.tupler[3])))
        
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

        self.Connect()
        sql="SELECT * FROM Course"
        cursor=self.db.cursor()
        cursor.execute(sql)
        course=[]
        for x in cursor:
            course.append(x)
        #print(course)
        newcourse=[]
        for tup in course:
            y=str(tup[0])+' '+str(tup[1])
            newcourse.append(y)
        #print(newcourse)
        self.sv=StringVar()
        o=OptionMenu(self.win5,self.sv,*newcourse)
        o.grid(row=0, column=0,sticky=W, padx=150)
        

        self.e1=Entry(self.win5, state='normal',width=40)
        self.e1.grid(row=0,column=2,sticky=W)
        self.t1=Text(self.win5,width=60,height=10,bd=5)
        self.t1.grid(row=2,column=0,columnspan=2,padx=20)


        c4=Radiobutton(self.win5,state='normal',text='4 Highly Recommend',variable=self.var,value=4)
        c4.grid(row=4,column=0,sticky=W,padx=30)
        c3=Radiobutton(self.win5,state='normal',text='3 Recommend',variable=self.var,value=3)
        c3.grid(row=5,column=0,sticky=W,padx=30)
        c2=Radiobutton(self.win5,state='normal',text='2 Recommend with reservation',variable=self.var,value=2)
        c2.grid(row=6,column=0,sticky=W,padx=30)
        c1=Radiobutton(self.win5,state='normal',text='1 Do not recommend',variable=self.var,value=1)
        c1.grid(row=7,column=0,sticky=W,padx=30)

        b2=Button(self.win5, text="Ok", command=self.TutorEvalPageOk)
        b2.grid(row=8,column=0,sticky=W,ipadx=10,pady=20,padx=30)
        b3=Button(self.win5, text="Cancel", command=self.TutorEvalPageCancel)
        b3.grid(row=8,column=0,sticky=E,ipadx=10,pady=20,padx=30)

    def TutorEvalPageOk(self):
        self.finalc=self.sv.get()
        #print(self.finalc)
        sep=self.finalc.split()
        
        school=sep[0]
        num=sep[1]        
        tutor=self.e1.get()
        ev=self.t1.get(1.0,END)
        nev=self.var.get()    
        stud=self.gtid
        
        query = "INSERT INTO Rates VALUES (%s,%s,%s,%s,%s,%s,'null')"
        query2="SELECT * FROM Student WHERE Name=%s"
        self.Connect()
        cursor1 = self.db.cursor()
        cursor1.execute(query2,(tutor))
        cursor2 = self.db.cursor()
        alist=[]
        for item in cursor1:
            alist.append(item)
        if len(alist)==0 or alist[0]=='' or alist[0]==None:
            messagebox.showerror("Invalid Tutor Name","You've entered an invalid tutor name. Please try again.")
        else:
            tutid=alist[0][0]
            print(stud, tutid, school, num, nev, ev)
            cursor2.execute(query,(stud,tutid,school,num,nev,ev))
            cursor1.close()
            cursor2.close()
            self.db.commit()
            self.db.close()
            self.win5.withdraw()
            self.win2=Toplevel()
            self.MainMenu()

    def TutorEvalPageCancel(self):
            self.win5.withdraw()
            self.win2=Toplevel()
            self.MainMenu()

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
        
        for i in range(6):
            self.v2=IntVar()
            e = Entry(self.win6, relief=RIDGE)
            for j in range(3):
                if j<2:
                    e = Entry(self.win6, relief=RIDGE)
                    e.grid(row=i+10, sticky=NSEW)
                    e.insert(END, '%d' %i)
                    e.grid(column=j, sticky=NSEW)
                    e.insert(END, '%d' %j)

        for i in range(6):
            r1= Checkbutton(self.win6, variable=self.v2, onvalue=i)
            r1.grid(row=i+10, column=j, sticky=EW)

        L7= Label(self.win6,text="Available Days/Time")
        L7.grid(row=17, column=0, sticky=W,pady=10)

        f1=LabelFrame(self.win6, text='Monday',width=650, height=60)
        f1.grid(row=18, sticky=W, columnspan=3)
        f2=LabelFrame(self.win6, text='Tuesday',width=650, height=60)
        f2.grid(row=19, sticky=W, columnspan=3)
        f3=LabelFrame(self.win6, text='Wednesday',width=650, height=60)
        f3.grid(row=20, sticky=W, columnspan=3)
        f4=LabelFrame(self.win6, text='Thursday',width=650, height=60)
        f4.grid(row=21, sticky=W, columnspan=3)
        f5=LabelFrame(self.win6, text='Friday',width=650, height=60)
        f5.grid(row=22, sticky=W, columnspan=3)

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
        c1.grid(row=18,sticky=W, columnspan=4,padx=3)
        c2 = Checkbutton(self.win6, text = "10am",variable=self.v2)
        c2.grid(row=18,sticky=W, columnspan=4,padx=80)
        c3 = Checkbutton(self.win6, text = "11am",variable=self.v3)
        c3.grid(row=18,sticky=W, columnspan=4,padx=160)
        c4 = Checkbutton(self.win6, text = "12pm",variable=self.v4)
        c4.grid(row=18,sticky=W, columnspan=4,padx=240)
        c5 = Checkbutton(self.win6, text = "1pm",variable=self.v5)
        c5.grid(row=18,sticky=W, columnspan=4,padx=320)
        c6 = Checkbutton(self.win6, text = "2pm",variable=self.v6)
        c6.grid(row=18,sticky=W, columnspan=4,padx=400)
        c7 = Checkbutton(self.win6, text = "3pm",variable=self.v7)
        c7.grid(row=18,sticky=W, columnspan=4,padx=480)
        c8 = Checkbutton(self.win6, text = "4pm",variable=self.v8)
        c8.grid(row=18,sticky=W, columnspan=4,padx=560)

        tc1 = Checkbutton(self.win6, text = "9am",variable=self.v9)
        tc1.grid(row=19,sticky=W, columnspan=4,padx=3)
        tc2 = Checkbutton(self.win6, text = "10am",variable=self.v10)
        tc2.grid(row=19,sticky=W, columnspan=4,padx=80)
        tc3 = Checkbutton(self.win6, text = "11am",variable=self.v11)
        tc3.grid(row=19,sticky=W, columnspan=4,padx=160)
        tc4 = Checkbutton(self.win6, text = "12pm",variable=self.v12)
        tc4.grid(row=19,sticky=W, columnspan=4,padx=240)
        tc5 = Checkbutton(self.win6, text = "1pm",variable=self.v13)
        tc5.grid(row=19,sticky=W, columnspan=4,padx=320)
        tc6 = Checkbutton(self.win6, text = "2pm",variable=self.v14)
        tc6.grid(row=19,sticky=W, columnspan=4,padx=400)
        tc7 = Checkbutton(self.win6, text = "3pm",variable=self.v15)
        tc7.grid(row=19,sticky=W, columnspan=4,padx=480)
        tc8 = Checkbutton(self.win6, text = "4pm",variable=self.v16)
        tc8.grid(row=19,sticky=W, columnspan=4,padx=560)

        wc1 = Checkbutton(self.win6, text = "9am",variable=self.v17)
        wc1.grid(row=20,sticky=W, columnspan=4,padx=3)
        wc2 = Checkbutton(self.win6, text = "10am",variable=self.v18)
        wc2.grid(row=20,sticky=W, columnspan=4,padx=80)
        wc3 = Checkbutton(self.win6, text = "11am",variable=self.v19)
        wc3.grid(row=20,sticky=W, columnspan=4,padx=160)
        wc4 = Checkbutton(self.win6, text = "12pm",variable=self.v20)
        wc4.grid(row=20,sticky=W, columnspan=4,padx=240)
        wc5 = Checkbutton(self.win6, text = "1pm",variable=self.v21)
        wc5.grid(row=20,sticky=W, columnspan=4,padx=320)
        wc6 = Checkbutton(self.win6, text = "2pm",variable=self.v22)
        wc6.grid(row=20,sticky=W, columnspan=4,padx=400)
        wc7 = Checkbutton(self.win6, text = "3pm",variable=self.v23)
        wc7.grid(row=20,sticky=W, columnspan=4,padx=480)
        wc8 = Checkbutton(self.win6, text = "4pm",variable=self.v24)
        wc8.grid(row=20,sticky=W, columnspan=4,padx=560)

        rc1 = Checkbutton(self.win6, text = "9am",variable=self.v25)
        rc1.grid(row=21,sticky=W, columnspan=4,padx=3)
        rc2 = Checkbutton(self.win6, text = "10am",variable=self.v26)
        rc2.grid(row=21,sticky=W, columnspan=4,padx=80)
        rc3 = Checkbutton(self.win6, text = "11am",variable=self.v27)
        rc3.grid(row=21,sticky=W, columnspan=4,padx=160)
        rc4 = Checkbutton(self.win6, text = "12pm",variable=self.v28)
        rc4.grid(row=21,sticky=W, columnspan=4,padx=240)
        rc5 = Checkbutton(self.win6, text = "1pm",variable=self.v29)
        rc5.grid(row=21,sticky=W, columnspan=4,padx=320)
        rc6 = Checkbutton(self.win6, text = "2pm",variable=self.v30)
        rc6.grid(row=21,sticky=W, columnspan=4,padx=400)
        rc7 = Checkbutton(self.win6, text = "3pm",variable=self.v31)
        rc7.grid(row=21,sticky=W, columnspan=4,padx=480)
        rc8 = Checkbutton(self.win6, text = "4pm",variable=self.v32)
        rc8.grid(row=21,sticky=W, columnspan=4,padx=560)

        fc1 = Checkbutton(self.win6, text = "9am",variable=self.v33)
        fc1.grid(row=22,sticky=W, columnspan=4,padx=3)
        fc2 = Checkbutton(self.win6, text = "10am",variable=self.v34)
        fc2.grid(row=22,sticky=W, columnspan=4,padx=80)
        fc3 = Checkbutton(self.win6, text = "11am",variable=self.v35)
        fc3.grid(row=22,sticky=W, columnspan=4,padx=160)
        fc4 = Checkbutton(self.win6, text = "12pm",variable=self.v36)
        fc4.grid(row=22,sticky=W, columnspan=4,padx=240)
        fc5 = Checkbutton(self.win6, text = "1pm",variable=self.v37)
        fc5.grid(row=22,sticky=W, columnspan=4,padx=320)
        fc6 = Checkbutton(self.win6, text = "2pm",variable=self.v38)
        fc6.grid(row=22,sticky=W, columnspan=4,padx=400)
        fc7 = Checkbutton(self.win6, text = "3pm",variable=self.v39)
        fc7.grid(row=22,sticky=W, columnspan=4,padx=480)
        fc8 = Checkbutton(self.win6, text = "4pm",variable=self.v40)
        fc8.grid(row=22,sticky=W, columnspan=4,padx=560)

        b1=Button(self.win6, text='OK', width=5, command=self.OkButton)
        b1.grid(row=22, column=10, sticky=W, pady=10)

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

    def scroll(self, *args):
        self.list17.yview(*args)
        self.list27.yview(*args)
        self.list37.yview(*args)
        self.list47.yview(*args)
        self.list57.yview(*args)

    def FindSchedPage(self):
        #Figure 7
        self.win7.title('Find Tutor Schedule')
        l1= Label(self.win7, text='Enter Tutor GTID')
        l1.grid(row=0, column=0,pady=50, padx=10)
        l2= Label(self.win7, text='Tutor Schedule')
        l2.grid(row=1, column=2,sticky=EW)
        self.te=Entry(self.win7, state='normal')
        self.te.grid(row=0,column=1,sticky=E,pady=50, padx=10)

        e1= Entry(self.win7, relief=RIDGE)
        e1.grid(row=2, column=0, sticky=NSEW)
        e1.insert(END, 'Day')
        e1.config(state="readonly")
        
        e2= Entry(self.win7, relief=RIDGE, width=20)
        e2.grid(row=2, column=1, sticky=NSEW)
        e2.insert(END, 'Time')
        e2.config(state="readonly")
        e3= Entry(self.win7, relief=RIDGE)
        e3.grid(row=2, column=2, sticky=NSEW)
        e3.insert(END, 'Name')
        e3.config(state="readonly")
        e4= Entry(self.win7, relief=RIDGE)
        e4.grid(row=2, column=3, sticky=NSEW)
        e4.insert(END, 'Email')
        e4.config(state="readonly")
        e5= Entry(self.win7, relief=RIDGE)
        e5.grid(row=2, column=4, sticky=NSEW)
        e5.insert(END, 'Course')
        e5.config(state="readonly")

        b1=Button(self.win7, text="OK", width=5,command=self.FindSchedPageOk1)
        b1.grid(row=0, column=2,pady=50, padx=10, sticky=W)

    def FindSchedPageOk1(self):
        tutid=self.te.get()
        query='SELECT Day, Time, Name, Email, Course FROM TutorSchedule WHERE StudentID=%s'
        self.Connect()
        alist=[]
        cursor = self.db.cursor()
        cursor.execute(query,(tutid))

        for x in cursor:
            alist.append(x)
        if len(alist)==0:
            messagebox.showerror("Invalid Tutor ID","You've entered an invalid tutor ID. Please try again.")
        else:

            print(alist)
            s = Scrollbar(self.win7)
            s.grid(row=3, column=5, rowspan=15, sticky=W)

            self.list17 = Listbox(self.win7, yscrollcommand = s.set )
            self.list17.grid(row=3, column=0, sticky=EW)
            self.list27 = Listbox(self.win7, yscrollcommand = s.set )
            self.list27.grid(row=3, column=1, sticky=EW)
            self.list37 = Listbox(self.win7, yscrollcommand = s.set )
            self.list37.grid(row=3, column=2, sticky=EW)
            self.list47 = Listbox(self.win7, yscrollcommand = s.set )
            self.list47.grid(row=3, column=3, sticky=EW)
            self.list57 = Listbox(self.win7, yscrollcommand = s.set )
            self.list57.grid(row=3, column=4, sticky=EW)

            button2=Button(self.win7, text='Ok', width=10, command=self.FindSchedPageOk2) #supposed to go back to main menu)
            button2.grid(row=20, column=5, padx=15)

            s.config( command=self.scroll )
            i=0
            for j in range(len(alist)): 
                self.list17.insert(END, "%s" %alist[j][0])
                self.list27.insert(END, "%s" %alist[j][1])
                self.list37.insert(END, "%s" %alist[j][2])
                self.list47.insert(END, "%s" %alist[j][3])
                self.list57.insert(END, "%s" %alist[j][4])
            return
        
    def FindSchedPageOk2(self):
        self.win7.withdraw()
        self.win2=Toplevel()
        self.MainMenu()
        


############################################################################## 



    def ProfRecPage(self):
        
        #Figure 8
        self.win8.title('Professor Recommendation')
        
        self.var2=IntVar()

        l1=Label(self.win8,text='Student GTID')
        l1.grid(row=0,column=0,sticky=W,pady=20, padx=30)
        l2=Label(self.win8,text='Descriptive Evaluation')
        l2.grid(row=1,column=0,sticky=W,pady=20, padx=30)
        l3=Label(self.win8,text='Numeric Evaluation')
        l3.grid(row=3,column=0,sticky=W,pady=20, padx=30)

        self.e1=Entry(self.win8, state='normal',width=30)
        self.e1.grid(row=0,column=0,sticky=E)
        self.t1=Text(self.win8,width=60,height=10,bd=5)
        self.t1.grid(row=2,column=0,columnspan=2,padx=20)

        c4=Radiobutton(self.win8,state='normal',text='4 Highly Recommend',variable=self.var2,value=4)
        c4.grid(row=4,column=0,sticky=W,padx=30)
        c3=Radiobutton(self.win8,state='normal',text='3 Recommend',variable=self.var2,value=3)
        c3.grid(row=5,column=0,sticky=W,padx=30)
        c2=Radiobutton(self.win8,state='normal',text='2 Recommend with reservation',variable=self.var2,value=2)
        c2.grid(row=6,column=0,sticky=W,padx=30)
        c1=Radiobutton(self.win8,state='normal',text='1 Do not recommend',variable=self.var2,value=1)
        c1.grid(row=7,column=0,sticky=W,padx=30)

        b2=Button(self.win8, text="Ok", command=self.ProfRecOk)
        b2.grid(row=8,column=0,sticky=W,ipadx=10,pady=20,padx=30)
        b3=Button(self.win8, text="Cancel", command=self.ProfRecCancel)
        b3.grid(row=8,column=0,sticky=E,ipadx=10,pady=20,padx=30)

    def ProfRecOk(self):
        tutor=self.e1.get()
        rec=self.t1.get(1.0,END)
        num=self.var2.get()
        prof=self.gtid
        query = "INSERT INTO Recommends VALUES (%s, %s, %s, %s)"
        query2="SELECT * FROM Tutor WHERE Tutor.TutorID=%s"
        self.Connect()
        alist=[]
        cursor1 = self.db.cursor()
        cursor1.execute(query2,(tutor))
        cursor2 = self.db.cursor()
        for item in cursor1:
            alist.append(item)
            
        if len(alist)==0 or alist[0]=='' or alist[0]==None:
            messagebox.showerror("Invalid Tutor ID","You've entered an invalid tutor ID. Please try again.")

        else:
            cursor2.execute(query,(tutor,prof,num,rec))
            cursor1.close()
            cursor2.close()
            self.db.commit()
            self.db.close()
            self.win8.withdraw()
            self.win2=Toplevel()
            self.MainMenu()

    def ProfRecCancel(self):
            self.win8.withdraw()
            self.win2=Toplevel()
            self.MainMenu()

##############################################################################


    def scroll9(self, *args):
        self.list19.yview(*args)
        self.list29.yview(*args)
        self.list39.yview(*args)
        self.list49.yview(*args)
        
    def Summary1Page(self):

        #Figure 9
        
        L1= Label(self.win9, text='Academic Year 2014')
        L1.grid(row=0, column=0, columnspan=2, sticky=W, pady=10)

        self.cv1=IntVar()
        self.cv2=IntVar()
        self.cv3=IntVar()

        c1=Checkbutton(self.win9,variable=self.cv1)
        c1.grid(row=0, column=1, sticky=E)
        c2=Checkbutton(self.win9,variable=self.cv2)
        c2.grid(row=0, column=2, sticky=E)
        c3=Checkbutton(self.win9,variable=self.cv3)
        c3.grid(row=0, column=3, sticky=E)
        l1= Label(self.win9, text="Fall")
        l1.grid(row=0, column=2, sticky=W)
        l2=Label(self.win9, text="Spring")
        l2.grid(row=0, column=3, sticky=W)
        l3=Label(self.win9, text="Summer")
        l3.grid(row=0, column=4, sticky=W)
                

        e1 = Entry(self.win9,relief=RIDGE)
        e1.grid(row=1, column=0, sticky=NSEW)
        e1.insert(END, 'Course')
        e1.config(state="readonly")
        e2= Entry(self.win9,relief=RIDGE)
        e2.grid(row=1, column=1, sticky=NSEW)
        e2.insert(END, 'Semester')
        e2.config(state="readonly")
        e3= Entry(self.win9,relief=RIDGE)
        e3.grid(row=1, column=2, sticky=NSEW)
        e3.insert(END, '# Students')
        e3.config(state="readonly")
        e4= Entry(self.win9,relief=RIDGE)
        e4.grid(row=1, column=3, sticky=NSEW)
        e4.insert(END, '# Tutors')
        e4.config(state="readonly")

        button1=Button(self.win9, text='Ok', width=10, command=self.populate)
        button1.grid(row=0, column=5, padx=15)
                
        
    def populate(self):
        s = Scrollbar(self.win9)
        s.grid(row=2, column=4, rowspan=15, sticky=W)

        self.list19 = Listbox(self.win9, yscrollcommand = s.set )
        self.list19.grid(row=2, column=0, sticky=EW)

        self.list29 = Listbox(self.win9, yscrollcommand = s.set )
        self.list29.grid(row=2, column=1, sticky=EW)
        self.list39 = Listbox(self.win9, yscrollcommand = s.set )
        self.list39.grid(row=2, column=2, sticky=EW)
        self.list49 = Listbox(self.win9, yscrollcommand = s.set )
        self.list49.grid(row=2, column=3, sticky=EW)


        button2=Button(self.win9, text='Ok', width=10,command=self.Sum1Exit) #supposed to go back to main menu)
        button2.grid(row=20, column=0, padx=15)

        query='SELECT * FROM Summary'
        self.Connect()
        llist=[]
        cursor = self.db.cursor()
        cursor.execute(query)
        for x in cursor:
            llist.append(x)

        print(llist)
        mlist=[]
        if self.cv1.get()==1:
            for x in llist:
                if x[1]=='Fall':
                    mlist.append(x)
                else:
                    pass
        if self.cv2.get()==1:
            for y in llist:
                if y[1]=='Spring':
                    mlist.append(y)
                else:
                    pass
        if self.cv3.get()==1:
            for z in llist:
                if z[1]=='Summer':
                    mlist.append(z)
                else:
                    pass
        for n in llist:
            if n[1]=='Total':
                mlist.append(n)
            
        print(mlist)
        
        s.config( command=self.scroll9 )
        for i in range(len(mlist)):
            for j in range(len(mlist)):
                self.list19.insert(END, "%s" %mlist[j][i])
                self.list29.insert(END, "%s" %mlist[j][i+1])
                self.list39.insert(END, "%s" %mlist[j][i+2])
                self.list49.insert(END, "%s" %mlist[j][i+3])
                    
            return
        
    def Sum1Exit(self):
        self.win9.withdraw()
        self.win2=Toplevel()
        self.MainMenu()

        

##############################################################################        

    def scroll0(self, *args):
        self.list10.yview(*args)
        self.list20.yview(*args)
        self.list30.yview(*args)
        self.list40.yview(*args)
        self.list50.yview(*args)
        self.list60.yview(*args)
        
    def Summary2Page(self):

        #Figure 10
        
        L1= Label(self.win10, text='Academic Year 2014')
        L1.grid(row=0, column=0, columnspan=2, sticky=W, pady=10)

        self.cv10=IntVar()
        self.cv20=IntVar()
        self.cv30=IntVar()

        c1=Checkbutton(self.win10,variable=self.cv10)
        c1.grid(row=0, column=1, sticky=E)
        c2=Checkbutton(self.win10,variable=self.cv20)
        c2.grid(row=0, column=2, sticky=E)
        c3=Checkbutton(self.win10,variable=self.cv30)
        c3.grid(row=0, column=3, sticky=E)
        l1= Label(self.win10, text="Fall")
        l1.grid(row=0, column=2, sticky=W)
        l2=Label(self.win10, text="Spring")
        l2.grid(row=0, column=3, sticky=W)
        l3=Label(self.win10, text="Summer")
        l3.grid(row=0, column=4, sticky=W)
                

        e1 = Entry(self.win10,relief=RIDGE)
        e1.grid(row=1, column=0, sticky=NSEW)
        e1.insert(END, 'Course')
        e1.config(state="readonly")
        e2= Entry(self.win10,relief=RIDGE)
        e2.grid(row=1, column=1, sticky=NSEW)
        e2.insert(END, 'Semester')
        e2.config(state="readonly")
        e3= Entry(self.win10,relief=RIDGE)
        e3.grid(row=1, column=2, sticky=NSEW)
        e3.insert(END, 'TA')
        e3.config(state="readonly")
        e4= Entry(self.win10,relief=RIDGE)
        e4.grid(row=1, column=3, sticky=NSEW)
        e4.insert(END, 'Avg Rating')
        e4.config(state="readonly")
        e5= Entry(self.win10,relief=RIDGE)
        e5.grid(row=1, column=4, sticky=NSEW)
        e5.insert(END, 'non TA')
        e5.config(state="readonly")
        e6= Entry(self.win10,relief=RIDGE)
        e6.grid(row=1, column=5, sticky=NSEW)
        e6.insert(END, 'Avg Rating')
        e6.config(state="readonly")

        button1=Button(self.win10, text='Ok', width=10, command=self.populate10)
        button1.grid(row=0, column=5, padx=15)
                
        
    def populate10(self):
        s = Scrollbar(self.win10)
        s.grid(row=2, column=4, rowspan=15, sticky=W)

        self.list10 = Listbox(self.win10, yscrollcommand = s.set )
        self.list10.grid(row=2, column=0, sticky=EW)
        self.list20 = Listbox(self.win10, yscrollcommand = s.set )
        self.list20.grid(row=2, column=1, sticky=EW)
        self.list30 = Listbox(self.win10, yscrollcommand = s.set )
        self.list30.grid(row=2, column=2, sticky=EW)
        self.list40 = Listbox(self.win10, yscrollcommand = s.set )
        self.list40.grid(row=2, column=3, sticky=EW)
        self.list50 = Listbox(self.win10, yscrollcommand = s.set )
        self.list50.grid(row=2, column=4, sticky=EW)
        self.list60 = Listbox(self.win10, yscrollcommand = s.set )
        self.list60.grid(row=2, column=5, sticky=EW)


        button2=Button(self.win10, text='Ok', width=10,command=self.Sum2Exit) #supposed to go back to main menu)
        button2.grid(row=20, column=0, padx=15)

        query='SELECT * FROM Summary2'
        self.Connect()
        llist=[]
        cursor = self.db.cursor()
        cursor.execute(query)
        for x in cursor:
            llist.append(x)

        
        mlist=[]
        if self.cv10.get()==1:
            for x in llist:
                if x[1]=='Fall':
                    mlist.append(x)
                else:
                    pass
        if self.cv20.get()==1:
            for y in llist:
                if y[1]=='Spring':
                    mlist.append(y)
                else:
                    pass
        if self.cv30.get()==1:
            for z in llist:
                if z[1]=='Summer':
                    mlist.append(z)
                else:
                    pass
        print(mlist)
        
        s.config( command=self.scroll0 )
        for i in range(len(mlist)):
            for j in range(len(mlist)):
                self.list10.insert(END, "%s" %mlist[j][i])
                self.list20.insert(END, "%s" %mlist[j][i+1])
                self.list30.insert(END, "%s" %mlist[j][i+2])
                self.list40.insert(END, "%s" %mlist[j][i+3])
                self.list50.insert(END, "%s" %mlist[j][i+4])
                self.list60.insert(END, "%s" %mlist[j][i+5])
            return
        
    def Sum2Exit(self):
        self.win10.withdraw()
        self.win2=Toplevel()
        self.MainMenu()





##############################################################################        
        

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
        self.win2.withdraw()
        self.win7=Toplevel()
        self.FindSchedPage()

    def AddRec(self):
        self.win2.withdraw()
        self.win8=Toplevel()
        self.ProfRecPage()

    def Summary1(self):
        self.win2.withdraw()
        self.win9=Toplevel()
        self.Summary1Page()

    def Summary2(self):
        self.win2.withdraw()
        self.win10=Toplevel()
        self.Summary2Page()

    def Exit(self):
        self.win2.destroy()
        

win = Tk()
myObj=Gui(win)
win.mainloop()
