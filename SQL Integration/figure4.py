from tkinter import *
win=Tk()

class project:
    def ScheduleTutorPage(self):
        #Figure 4

         L1= Label(win, text='Select your Tutor for CS 4400')
         L1.grid(row=0, column=3, columnspan=2, sticky=EW)

         e1 = Entry(relief=RIDGE)
         e1.grid(row=1, column=1, sticky=NSEW)
         e1.insert(END, 'First Name')
         e1.config(state="readonly")
         e2= Entry(relief=RIDGE)
         e2.grid(row=1, column=2, sticky=NSEW)
         e2.insert(END, 'Last Name')
         e2.config(state="readonly")
         e2= Entry(relief=RIDGE)
         e2.grid(row=1, column=3, sticky=NSEW)
         e2.insert(END, 'Email')
         e2.config(state="readonly")
         e2= Entry(relief=RIDGE)
         e2.grid(row=1, column=4, sticky=NSEW)
         e2.insert(END, 'Day')
         e2.config(state="readonly")
         e2= Entry(relief=RIDGE)
         e2.grid(row=1, column=5, sticky=NSEW)
         e2.insert(END, 'Time')
         e2.config(state="readonly")
         e2= Entry(relief=RIDGE)
         e2.grid(row=1, column=6, sticky=NSEW)
         e2.insert(END, 'Select')
         e2.config(state="readonly")

        
        for i in range(6):
            e = Entry(relief=RIDGE)
            for j in range(6):
                if j<5:
                    e = Entry(relief=RIDGE)
                    e.grid(row=i+2, sticky=NSEW)
                    e.insert(END, '%d' %i)
                    e.grid(column=j+1, sticky=NSEW)
                    e.insert(END, '%d' %j)
                if j==4:
                    self.v=IntVar()

                    r1= Radiobutton(win, variable=self.v, value=i+2)
                    r1.grid(row=i+2, column=j+2)

        L1= Label(win, text='NOTE: Only 1 box under the Select column may be checked')
        L1.grid(row=9, column=3, columnspan=2, sticky=EW)

        B1=Button(win, text="OK", width=15)
        B1.grid(row=10, column=1)
        B2=Button(win, text="Cancel", width=15)
        B2.grid(row=10, column=3, sticky=W)
                        
win.title("table")
myObj=project(win)
win.mainloop()
