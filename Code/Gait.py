from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import djfsd

selected_tuple=[1]
cardet=[1,0,0,0,0]
carplate=0
neglected_tuple=[1,0,0,0,0,0]

def new_rider(A,B,C,D,E,F,G):
    djfsd.insert(A,B,C,D,E,F,G)

def update_pdetails(R,A,B,C):
    djfsd.update_p(R,A,B,C)

    print(R,A,B,C)

def update_tdetails(R,A,B,C):
    djfsd.update_t(R,A,B,C)

    print(R,A,B,C)

def view_command(R):
    list1.delete(0,END)
    for row in djfsd.view(R):
        list1.insert(END,row)

def view_select_riders_command(R):
    list2.delete(0,END)
    for row in djfsd.view_selected(R):
        list2.insert(END,row)

def view_select_riders_comm1(R):
    list1.delete(0, END)
    for row in djfsd.view_selected(R):
        list1.insert(END, row)

def search_command(R,N,P,G,De,Da,Pick,Rg):
    list1.delete(0,END)
    for row in djfsd.search(R,N,P,G,De,Da,Pick,Rg):
        list1.insert(END,row)

def same_year_comm(De,Da,Pi,R,Reg):
    list1.delete(0,END)
    for row in djfsd.same_year(De,Da,Pi,R,Reg):
        list1.insert(END,row)

def get_selected(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    selected_tuple=selected_tuple[0:4]
    e1.delete(0,END)
    e1.insert(END,selected_tuple[0])
    e2.delete(0, END)
    e2.insert(END,selected_tuple[1])
    e3.delete(0, END)
    e3.insert(END,selected_tuple[2])
    e4.delete(0, END)
    e4.insert(END,selected_tuple[3])

def gets_selected(event):
    global cardet,carplate
    index=list3.curselection()[0]
    cardet=list3.get(index)
    carplate=cardet[-1]
    ctype.delete(0,END)
    ctype.insert(END,cardet[1])
    maxseat.delete(0, END)
    maxseat.insert(END,int(cardet[2]))
    ac.delete(0, END)
    ac.insert(END,cardet[3])
    ppkm.delete(0, END)
    ppkm.insert(END,cardet[4])

def select_rider_comm(Register):
    print(str(Register))
    djfsd.selected(str(Register),str(selected_tuple[0]))

def unselect_rider_comm(Register):
    print(str(Register))
    djfsd.selected('',str(selected_tuple[0]))

def find_later(Reg):
    djfsd.later(Reg)
    App.destroy()

def view_all_cars():
    list3.delete(0, END)
    for row in djfsd.view_cars():
        list3.insert(END, row)

def search_cars_comm(A,B,C,D):
    list3.delete(0, END)
    for row in djfsd.search_cars(A,B,C,D):
        list3.insert(END, row)

def sort_list(n):
    """
    function to sort listbox items case insensitive
    """
    temp_list = list(list3.get(0, END))
    temp_list.sort(key= lambda x:x[n])
    print(temp_list)
    # delete contents of present listbox
    list3.delete(0, END)
    # load listbox with sorted data
    for item in temp_list:
        list3.insert(END, item)

def popup(A,B,C,D,E,F,Reg):
    templist1= list(list3.get(0,END))
    templist2=[]
    global neglected_tuple
    for x in templist1:
        x=x[1:5]
        templist2.append(x)

    y=(A,B,C,D)
    print(templist2)

    if y not in templist2:
        tkinter.messagebox.showinfo('Return', "Booking Can't be made until you select a car. Please Return And Select a Car")

    else:
        MsgBox = tkinter.messagebox.askquestion ('Booking Confirmation','Once a car is booked, it cannot be cancelled, Are you sure you want to book?',icon = 'warning')
        if MsgBox == 'yes':
            djfsd.book_car(F,Reg)
            show_framess(E)
            get_info(F)


class CabShare(Tk):

    def __init__(self):
        Tk.__init__(self)
        icon=PhotoImage("YOLOBOY.icns")
        self.tk.call('wm','iconphoto',self._w,icon)
        Tk.wm_title(self, "CabShare - VIT")
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames= {}

        for F in (StartPage,StartPage):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nesw")

        self.show_frame(StartPage)

def show_frame(Homepage):
    global Name,Register,Phone,Destination,Gender,Date,Time,GroupCode
    GroupCode=str(GroupCode.get())
    Name=str(Name.get())
    Register=str(Register.get())
    Phone=int(Phone.get())
    Gender=str(Gender.get())
    Destination=str(Destination.get())
    Date=str(Date.get())
    Time=float(Time.get())
    print(Name)
    App.geometry("670x360")
    Homepage.tkraise()
    Homepage.grid(row=0,column=0,sticky="nesw")
    return [Name,Register,Phone,Destination,Gender,Date,Time]

def show_frames(Homepage):
    App.geometry("950x320")
    Homepage.tkraise()
    Homepage.grid(row=0, column=0, sticky="nesw")

def show_framess(Homepage):
    App.geometry("670x360")
    Homepage.tkraise()
    Homepage.grid(row=0, column=0, sticky="nesw")

def get_info(A):
    global neglected_tuple
    neglected_tuple=djfsd.get_information(A)
    neglected_tuple=neglected_tuple[0]
    print(neglected_tuple)

def delete_user(A):
    djfsd.delete(A)
    App.destroy()

def edit_pdetails(A):
    Ap=Tk()
    Str=Frame(Ap)
    Str.grid(row=0,column=0,sticky='nesw')
    AA= StringVar()
    aa = Label(Str, text="Name")
    aa.grid(row=1, column=1)
    aa_entry = Entry(Str)
    aa_entry.grid(row=1, column=2)
    BB = IntVar()
    bb = Label(Str, text="Phone")
    bb.grid(row=2, column=1)
    bb_entry = Entry(Str)
    bb_entry.grid(row=2, column=2)
    CC = StringVar()
    cc = Label(Str, text="Gender")
    cc.grid(row=3, column=1)
    cc_entry = Entry(Str)
    cc_entry.grid(row=3, column=2)
    Add_to_db1 = ttk.Button(Str, text="Update Details",
                           command=lambda: update_pdetails(A,str(aa_entry.get()),int(bb_entry.get()),str(cc_entry.get())))
    Add_to_db1.grid(row=4, column=1)

    Ap.mainloop()

def edit_tdetails(A):
    Ap=Tk()
    Str=Frame(Ap)
    Str.grid(row=0,column=0,sticky='nesw')
    AA= StringVar()
    aa = Label(Str, text="Destination")
    aa.grid(row=1, column=1)
    aa_entry = Entry(Str)
    aa_entry.grid(row=1, column=2)
    BB = IntVar()
    bb = Label(Str, text="Date")
    bb.grid(row=2, column=1)
    bb_entry = Entry(Str)
    bb_entry.grid(row=2, column=2)
    CC = StringVar()
    cc = Label(Str, text="Pickup-Time (Max) ")
    cc.grid(row=3, column=1)
    cc_entry = Entry(Str)
    cc_entry.grid(row=3, column=2)
    Add_to_db1 = ttk.Button(Str, text="Update Details",
                           command=lambda: update_tdetails(A,str(aa_entry.get()),str(bb_entry.get()),float(cc_entry.get())))
    Add_to_db1.grid(row=4, column=1)

    Ap.mainloop()

def show_inst1():
    Ap=Tk()
    Str=Frame(Ap)
    Str.grid(row=0,column=0,sticky='nesw')
    ins1=Label(Str, text='Welcome To CabShare - VIT!')
    ins1.grid(row=0,column=1)
    ins2 = Label(Str, text='If You Are New, Please Fill up all information besides the Groupcode;\n Click the "Add To List" Button;\n Then Click "Find Rider" To Move on with our Process ')
    ins2.grid(row=1, column=1)
    ins1 = Label(Str, text='If you are a old user, Simply enter your register number and click FIND RIDER')
    ins1.grid(row=0, column=1)
    Ap.mainloop()

def show_inst2():
    Ap = Tk()
    Str = Frame(Ap)
    Str.grid(row=0, column=0, sticky='nesw')
    ins1 = Label(Str, text='Welcome To CabShare - VIT!')
    ins1.grid(row=0, column=1)
    ins2 = Label(Str,
                 text='Click on "View All" To reveal all the college students who will be travelling on the same date or around the same time as you\n You can swiftly Search through the list Using our Provided Search Filters\n')
    ins2.grid(row=1, column=1)
    ins3= Label(Str, text='Do Understand that our Search Filters will match a rider for you if they meet any one of your required criteria\n Clicking on View All or Same-Year Students resets all of your filters')
    ins3.grid(row=2, column=1)
    ins4 = Label(Str, text='On finding a suitable partner, Contact him/her via the phone number provided when you select her\n After agreeing, click on the decided partner and select the "SELECT RIDER" Button')
    ins4.grid(row=3, column=1)
    ins5 = Label(Str, text='Do Make sure YOU SELECT YOURSELF INTO THE GROUP AS WELL\n If you do not find any or enough partners to ride with, click on "Find Later" To come back at a later time to continue your search')
    ins5.grid(row=4, column=1)
    ins6 = Label(Str, text='Once you Click on FIND LATER, your made up group will be dispersed since we cannot allow anyone to hold onto to others without booking a trip')
    ins6.grid(row=5, column=1)
    ins7 = Label(Str, text='Once you\'re done froming the group, click on the SELECT CAR Button to move forward with the booking process')
    ins7.grid(row=6, column=1)
    Ap.mainloop()

def show_inst3():
    Ap=Tk()
    Str=Frame(Ap)
    Str.grid(row=0,column=0,sticky='nesw')
    ins1=Label(Str, text='Welcome To CabShare - VIT!')
    ins1.grid(row=0,column=1)
    ins2 = Label(Str, text='You can view your selected group and available cars by selecting the VIEW YOUR GROUP and VIEW ALL CARS respectively')
    ins2.grid(row=1, column=1)
    ins3 = Label(Str, text='If you still have to make any changes to your group, you can go back by simply clicking on the CHANGE RIDERS button')
    ins3.grid(row=2, column=1)
    ins4 = Label(Str, text='The Filters in the Car Selection process work in the similar way the Rider Selection Filters did')
    ins4.grid(row=3, column=1)
    ins5 = Label(Str, text='Click on the Car and SELECT BOOK Car to book the car\n The Car will arrive on the earliest time given by the group members')
    ins5.grid(row=4, column=1)
    ins6 = Label(Str, text='So ask your group members to change their pick-up time if you want to change the pick-up time\n To change or delete ider details check the Delete/Update Details\n CAR ONCE BOOKED WILL NOT BE CANCELLED')
    ins6.grid(row=5, column=1)

    Ap.mainloop()

def show_inst4():
    Ap=Tk()
    Str=Frame(Ap)
    Str.grid(row=0,column=0,sticky='nesw')
    ins1=Label(Str, text='Welcome To CabShare - VIT!')
    ins1.grid(row=0,column=1)
    ins2 = Label(Str, text='To delete details, Click on USER > DELETE USER;\n To UPDATE personal details CLICK USER>EDIT PERSONAL DETAILS;\n To UPDATE Trip Details CLICK TRIP>EDIT TRIP DETAILS ')
    ins2.grid(row=1, column=1)
    Ap.mainloop()

App=Tk()



App.wm_title("CabShare - VIT")
#Making The First Fame
StartPage=Frame(App)
StartPage.grid(row=0, column=0,sticky="nesw")
   #Logo
icon=PhotoImage(file="CabShared.gif")
label=Label(StartPage,image=icon)
label.image =icon
label.grid(row=0,columnspan=8,sticky=W+E)
   #Making Labels and Entries
person=Label(StartPage,text="Personal Details",bg="green")
person.grid(row=1,columnspan=8,sticky="nesw")

regno=Label(StartPage,text="Regno")
regno.grid(row=2,column=0)
Register=StringVar()
regno_entry=Entry(StartPage,textvariable=Register)
regno_entry.grid(row=2,column=1)

Name=StringVar()
name=Label(StartPage,text="Name")
name.grid(row=2,column=2)
name_entry=Entry(StartPage,textvariable=Name)
name_entry.grid(row=2,column=3)

Phone=IntVar()
phone=Label(StartPage,text="Phone No")
phone.grid(row=2,column=4)
phone_entry=Entry(StartPage,textvariable=Phone)
phone_entry.grid(row=2,column=5)

Gender=StringVar()
gender=Label(StartPage, text="Gender")
gender.grid(row=2,column=6)
gender_entry=Entry(StartPage, textvariable=Gender)
gender_entry.grid(row=2,column=7)

Trip=Label(StartPage, text="Trip Details",bg="blue")
Trip.grid(row=3,columnspan=8,sticky="nesw")

Destination=StringVar()
dest=Label(StartPage,text="Destination")
dest.grid(row=4,column=0)
dest_entry=Entry(StartPage, textvariable=Destination)
dest_entry.grid(row=4,column=1)

Date=StringVar()
date=Label(StartPage,text="Date(YYYY-MM-DD)")
date.grid(row=4,column=2)
date_entry=Entry(StartPage, textvariable=Date)
date_entry.grid(row=4,column=3)


Time=DoubleVar()
time=Label(StartPage,text="Max PickUp Time (24-Hr Format)")
time.grid(row=4,column=4)
time_entry=Entry(StartPage, textvariable=Time)
time_entry.grid(row=4,column=5)

GroupCode=StringVar()
gc=Label(StartPage,text="GroupCode (Leave Alone If New)")
gc.grid(row=4,column=6)
gc_entry=Entry(StartPage, textvariable=GroupCode)
gc_entry.grid(row=4,column=7)

#Button To move to new page
NxtPage=ttk.Button(StartPage,text="Find Your Rider", command=lambda:show_frame(Homepage))
NxtPage.grid(row=5,column=5)
Add_to_db=ttk.Button(StartPage,text="Add To List", command=lambda:new_rider(Register.get(),Name.get(),Phone.get(),Gender.get(),
                                                                            Destination.get(),Date.get(),Time.get()))
Add_to_db.grid(row=5,column=3)

Trip=Label(StartPage, text="Check Instructions For Help",bg="Red")
Trip.grid(row=6,columnspan=8,sticky="nesw")



#HOME PAGE
Homepage=Frame(App)
 #LABELS AND ENTRIES
l0=Label(Homepage,text="SEARCHING FILTERS", bg="red")
l0.grid(row=0,column=0,columnspan=20,sticky="nesw")

l1=Label(Homepage,text="Register No.")
l1.grid(row=1,column=0)

l2=Label(Homepage,text="Name")
l2.grid(row=1,column=2)

l3=Label(Homepage,text="Phone")
l3.grid(row=2,column=0)

l1=Label(Homepage,text="Gender")
l1.grid(row=2,column=2)

R=StringVar()
e1=Entry(Homepage,textvariable=R)
e1.grid(row=1,column=1)

N=StringVar()
e2=Entry(Homepage,textvariable=N)
e2.grid(row=1,column=3)

P=IntVar()
e3=Entry(Homepage,textvariable=P)
e3.grid(row=2,column=1)

G=StringVar()
e4=Entry(Homepage,textvariable=G)
e4.grid(row=2,column=3)

 #DB VIEWER AND SCROLL BAR
pbook=Label(Homepage,text="LIVE PHONEBOOK (Reg No, Name, Phone No, Gender, Destination, Time)",bg="red")
pbook.grid(row=3,column=0,columnspan=20,sticky="nesw")
list1=Listbox(Homepage,height=10,width=35)
list1.grid(row=5,column=0,rowspan=10,columnspan=5)

sb1=Scrollbar(Homepage)
sb1.grid(row=9,column=5)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected)


b1=Button(Homepage,text="View all", width=12, command=lambda:view_command(Register))
b1.grid(row=6, column=6)

b2=Button(Homepage,text="Search Riders", width=12, command=lambda : search_command(R.get(),N.get(),P.get(),G.get(),Destination,Date,Time,Register))
b2.grid(row=1, column=6,rowspan=1)

b3=Button(Homepage,text="Select Rider", width=12, command=lambda: select_rider_comm(Register))
b3.grid(row=7, column=6)

b4=Button(Homepage,text="Show Rider Group", width=12, command= lambda : view_select_riders_comm1(Register))
b4.grid(row=8, column=6)

b5=Button(Homepage,text="Select Car", width=12, command=lambda : show_frames(Finalize),bg='green')
b5.grid(row=10, column=6)

b6=Button(Homepage,text="Unselect Rider", width=12, command=lambda :unselect_rider_comm(R.get()))
b6.grid(row=9,column=6)

b7=Button(Homepage,text="Find Later", width=12, command=lambda : find_later(Register))
b7.grid(row=11,column=6)

b8=Button(Homepage,text="Search Same Year", width=12, command=lambda : same_year_comm(Destination,Date,Time,str(Register[0:2]),Register))
b8.grid(row=2, column=6,rowspan=1)

#SELECT CAR
Finalize=Frame(App)

L1=Label(Finalize,text="Car Type")
L1.grid(row=1,column=0)
L2=Label(Finalize,text="Max Seat")
L2.grid(row=1,column=2)
L3=Label(Finalize,text="AC")
L3.grid(row=2,column=0)
L4=Label(Finalize,text="Price")
L4.grid(row=2,column=2)

CType=StringVar()
ctype=Entry(Finalize,textvariable=CType)
ctype.grid(row=1,column=1)

MaxSeat=IntVar()
maxseat=Entry(Finalize,textvariable=MaxSeat)
maxseat.grid(row=1,column=3)

AC=StringVar()
ac=Entry(Finalize,textvariable=AC)
ac.grid(row=2,column=1)

PPKM=DoubleVar()
ppkm=Entry(Finalize,textvariable=PPKM)
ppkm.grid(row=2,column=3)

faltu_label1=Label(Finalize,text='Rider Group',bg='Yellow')
faltu_label1.grid(row=3,column=0,columnspan=4,sticky=W+E)

faltu_label2=Label(Finalize,text='Cars List(Car Model,Car-Type,Seats,AC,Price)',bg='Green')
faltu_label2.grid(row=3,column=4,columnspan=4,sticky=W+E)

faltu_label3=Label(Finalize,text='Search Query/Info',bg='Red')
faltu_label3.grid(row=0,column=0,columnspan=8,sticky=W+E)


list2=Listbox(Finalize,height=10,width=27)
list2.grid(row=4,column=0,rowspan=10,columnspan=2,sticky='W')

sb2=Scrollbar(Finalize)
sb2.grid(row=9,column=2,sticky='W')

list2.configure(yscrollcommand=sb2.set)
sb2.configure(command=list2.yview)

B1=ttk.Button(Finalize,text='View Your Group',width=12,command=lambda : view_select_riders_command(Register))
B1.grid(row=4,column=3,rowspan=3,sticky="NS")

B2=ttk.Button(Finalize,text='Change Riders',width=12,command=lambda : show_framess(Homepage))
B2.grid(row=8,column=3,rowspan=3,sticky="NS")

B3=ttk.Button(Finalize,text='View All Cars',width=12,command=lambda : view_all_cars())
B3.grid(row=4,column=7,rowspan=3,sticky="NS")

B4=ttk.Button(Finalize,text='Search Cars',width=12,command=lambda : search_cars_comm(CType.get(),MaxSeat.get(),AC.get(),PPKM.get()))
B4.grid(row=1,column=4,rowspan=2,columnspan=2,sticky="NS")

B5=ttk.Button(Finalize,text='Book Car',width=12,command=lambda: popup(CType.get(),MaxSeat.get(),AC.get(),PPKM.get(),Lastpage,carplate,Register))
B5.grid(row=1,column=7,rowspan=2,columnspan=2,sticky="NS")

B6=ttk.Button(Finalize,text='Sort By Price',width=12,command=lambda : sort_list(-2))
B6.grid(row=7,column=7,rowspan=3,sticky="NS")

B7=ttk.Button(Finalize,text='Sort By Seats',width=12,command=lambda : sort_list(2))
B7.grid(row=10,column=7,rowspan=3,sticky="NS")

list3=Listbox(Finalize,height=10,width=30)
list3.grid(row=4,column=4,rowspan=10,sticky='W')

sb3=Scrollbar(Finalize)
sb3.grid(row=9,column=6,sticky='NESW')

list3.configure(yscrollcommand=sb3.set)
sb3.configure(command=list3.yview,troughcolor="red")

list3.bind('<<ListboxSelect>>', gets_selected)

Lastpage=Frame(App)

Button1=ttk.Button(Lastpage,text='SHOW DETAILS',width=20,command= lambda : show_detail())
Button1.grid(row=10,column=0,rowspan=3,sticky="NSEW")

Button2=ttk.Button(Lastpage,text='DONE',width=20,command= lambda : App.destroy())
Button2.grid(row=10,column=1,rowspan=3,sticky="NSEW")

def show_detail():
    global neglected_tuple,cardet

    D_NAME = neglected_tuple[0]
    dname1 = Label(Lastpage, text='Driver Name')
    dname1.grid(row=1, column=0)
    dname2 = Label(Lastpage, text=D_NAME)
    dname2.grid(row=1, column=1)

    D_PHONE = neglected_tuple[1]
    dphone1 = Label(Lastpage, text='Driver Contact No:')
    dphone1.grid(row=2, column=0)
    dphone2 = Label(Lastpage, text=D_PHONE)
    dphone2.grid(row=2, column=1)

    D_PLATE = neglected_tuple[2]
    dplate1 = Label(Lastpage, text='Car Plate No:')
    dplate1.grid(row=3, column=0)
    dplate2 = Label(Lastpage, text=D_PLATE)
    dplate2.grid(row=3, column=1)

    C_MODEL = cardet[0]
    cmodel1 = Label(Lastpage, text='Car Model:')
    cmodel1.grid(row=4, column=0)
    cmodel2 = Label(Lastpage, text=C_MODEL)
    cmodel2.grid(row=4, column=1)

    C_AC = cardet[3]
    cac1 = Label(Lastpage, text='AC:')
    cac1.grid(row=5, column=0)
    cac2 = Label(Lastpage, text=C_AC)
    cac2.grid(row=5, column=1)

menu=Menu(App)
App.config(menu=menu)
subMenu=Menu(menu)
menu.add_cascade(label='User', menu=subMenu)
subMenu.add_command(label='Delete User',command= lambda: delete_user(Register))
subMenu.add_separator()
subMenu.add_command(label='Edit Personal Details', command= lambda: edit_pdetails(Register))
subMenu1=Menu(menu)
menu.add_cascade(label='Trip', menu=subMenu1)
subMenu1.add_command(label='Edit Trip Details', command= lambda: edit_tdetails(Register))
subMenu2=Menu(menu)
menu.add_cascade(label='Instructions', menu=subMenu2)
subMenu2.add_command(label='Signup/Login Instructions',command=lambda: show_inst1())
subMenu2.add_separator()
subMenu2.add_command(label="Group Formation Process",command=lambda : show_inst2())
subMenu2.add_separator()
subMenu2.add_command(label='Car Selection/Booking Process',command=lambda: show_inst3())
subMenu2.add_separator()
subMenu2.add_command(label='Deletion/Updation Instruction',command=lambda: show_inst4())
App.mainloop()
