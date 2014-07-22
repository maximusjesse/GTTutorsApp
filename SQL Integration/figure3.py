from tkinter import *
win=Tk()

class project:
    
     #Code needed for figure 3 to function
    def scroll(self, *args):
        self.list2.yview(*args)
        self.list3.yview(*args)
        self.list4.yview(*args)
        self.list5.yview(*args)
        self.list6.yview(*args)
        self.list7.yview(*args)

    def clicked(self):
        a=self.ee.get()
        aa=self.eee.get()
        print (a)
        print(aa)

    def savefromtable2(self):
        import time
        day=self.var.get()
        hour=self.var2.get()
        ampm=self.var3.get()
        timeString=time.strftime('%H',time.strptime(hour,'%I'))
        self.listbox.delete(0,len(self.mylist))
        self.mylist.append((day,timeString, ampm))
        print (self.mylist)

        for i in self.mylist:
            self.listbox.insert(END, i)

    def ok(self):
        self.clicked()
        self.savefromtable2()

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

        ##### Scroll NEEDS THIS
        s = Scrollbar(self.win3)
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

        listt=[['emily', 'dong', 'edong7@gatech.edu', '9', '3', '15', '3'],['yan', 'zheng', 'yzheng@gatech.edu', '9', '2', '10', '2'], ['emily', 'dong', 'edong7@gatech.edu', '9', '3', '15', '3'], ['emily', 'dong', 'edong7@gatech.edu', '9', '3', '15', '3'], ['emily', 'dong', 'edong7@gatech.edu', '9', '3', '15', '3'], ['emily', 'dong', 'edong7@gatech.edu', '9', '3', '15', '3'], ['emily', 'dong', 'edong7@gatech.edu', '9', '3', '15', '3']]


        l6=Label(self.win3,text='                                               ')
        l6.grid(row=20,column=0, columnspan=10)
        b2=Button(self.win3,width=20, text='Schedule a Tutor')
        b2.grid(row=30, column=0, columnspan= 2, sticky=W)
        b3=Button(self.win3,width=20, text='Cancel')
        b3.grid(row=30, column=2, sticky=W)
        l7=Label(self.win3,text='                                               ')
        l7.grid(row=22,column=0, columnspan=10)
        
        for i in range(5):
            e = Entry(relief=RIDGE)
            for j in range(7):
                
                self.list2.insert(END, "%s" %listt[j][i+1])
                self.list2.grid(row=15, column=1, sticky=EW)
                self.list3.insert(END, "%s" %listt[j][i+2])
                self.list4.insert(END, "%s" %listt[j][i+3])
                self.list5.insert(END, "%s" %listt[j][i+4])
                self.list6.insert(END, "%s" %listt[j][i+5])
                self.list7.insert(END, "%s" %listt[j][i+6])
            return


        
win.title("table")
myObj=project(win)
win.mainloop()
