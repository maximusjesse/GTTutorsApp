
from tkinter import *
import urllib.request
from re import findall
import pymysql
import sqlite3

class Gui():

    def __init__(self,win):

        self.page1=win
        self.TutorsPage(win)
        self.page2=Toplevel()
        self.page2.withdraw()

    def LoginPage(self,win):

        url = "http://espn.go.com/i/teamlogos/ncaa/med/trans/59.gif"
        response = urllib.request.urlopen(url)
        myPicture = response.read()
        import base64
        b64_data = base64.encodebytes(myPicture)

        self.photo = PhotoImage(data=b64_data)

        l = Label(win, image=self.photo)
        l.grid(row=0,columnspan=3,sticky=EW)
        
        l1=Label(win,text='Enter GTID')
        l1.grid(row=1,column=0,sticky=E)
        l2=Label(win,text='Enter Password')
        l2.grid(row=3,column=0,sticky=E)


        self.e1=Entry(win,state='normal', width=30)
        self.e1.grid(row=1,column=1)
        self.e2=Entry(win,state='normal', width=30)
        self.e2.grid(row=3,column=1)

        win.title('GTT Login')

        l3=Label(win,text='')
        l3.grid(row=4,column=0,sticky=W)

        l4=Label(win,text='')
        l4.grid(row=2,column=0,sticky=W)

        b1=Button(win,text='Ok', width=15, command=self.Login)
        b1.grid(row=5,columnspan=2)

    def MainMenu(self,win):

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

    def TutorsPage(self,win):
        l1=Label(win,text='Course')
        l1.grid(row=0,column=0,sticky=W,pady=20, padx=30)

        l2=Label(win,text='Availability Note: Tutor sessions can only be scheduled for 1 hour per week for a given course')
        l2.grid(row=1,column=0,sticky=W,pady=20, padx=30)

        t1=Treeview(win)
        t1.pack()


    def Connect(self):
        db=pymysql.connect(host='academic-mysql.cc.gatech.edu',db='cs4400',user='yzheng88',passwd='BCBgVE2V')
            return(db)
        except:
            messagebox.showwarning('Error','Could not connect. Please try again.')
        

    def Login(self):
        user=self.e1.get()
        p1=self.e2.get()
        db=self.Connect()
        try:
            cursor = db.cursor()
            sql = "SELECT * from User where GTID=%s and Password=%s"
            cursor.execute(sql,(user,p1))
            aList=[]
            for item in cursor:
                aList.append(item)                
            bList=[]
            for items in aList:
                bList.append(items[0])
        finally:
            db.close()
        if len(bList)==0:
            messagebox.showwarning('Error','Incorrect GTID or password. Please try again.')
        else:
            win.destroy()
            

            

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
