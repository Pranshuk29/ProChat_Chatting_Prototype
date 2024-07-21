from tkinter import*
'''from tkinter.ttk import*'''
import tkinter.ttk as tak
from PIL import* #Image,ImageDraw,ImageFont
import time

#DISPLAY RESOLUTION=1600 X 900
ddict1={}#empty dict later to store single user details
ddict2={}#empty dict later to store unm, nm, pw, security answer
ddict3={}#empty dict later to store chats
val=[]#list to store unm,fnm,lnm,pw
lstt=['theCAP','Wa44nda','thehulk4u','EDITH','ddE1','lok_i','Jk45r','Vs^n']#default contact list based on interests
#*******************************************************************************************************************
#5th page(main mssging screen)
def newmain():
    p=Tk(className=' प्रो-CHAT ')
    #p.geometry('1100x700')
    h=Frame(p).pack()

    ima1=PhotoImage(file='Screenshot (98).png')

    cc1=Canvas(h,height=700,width=1100)#main canvas
    cc1.create_image(0,0,image=ima1,anchor='nw')
    cc1.pack()
    cc2=Canvas(h,bg='black',width=320,height=540)
    cc2.place(x=1020,y=120)#contact canvas

    cc1.create_text(500,70,text="Let's Connect!!",font=('jokerman',40,'bold','underline'),fill='white')
    ccc=Canvas(h,bg='black')#moving text canvas
    ccc.place(x=260,y=150)
    
    def clearval():#change to get same contact list for next sign in
        val.clear()
        lstt=['theCAP','Wa44nda','thehulk4u','EDITH','ddE1','lok_i','Jk45r','Vs^n']
    bckbttn=Button(h,cursor='hand2',text='LOG OUT',font=('arial',8,'bold'),bg='black',fg='white',relief='raised',\
                   command=lambda:[clearval(),p.destroy(),SignUp()])
    bckbttn.place(x=260,y=20)

    def shift():
        x1,y1,x2,y2 = ccc.bbox("marquee")
        if(x2<0 or y1<0): #reset the coordinates
            x1 = ccc.winfo_width()
            y1 = ccc.winfo_height()//2
            ccc.coords("marquee",x1,y1)
        else:
            ccc.move("marquee", -2, 0)
        ccc.after(1000//fps,shift)
    text_var="Basic Widgets:-"
    text=ccc.create_text(0,-2000,text=text_var,font=('elephant',20,'bold'),fill='white',tags=("marquee",),anchor='w')
    x1,y1,x2,y2 = ccc.bbox("marquee")
    width = x2-x1
    height = y2-y1
    ccc['width']=width
    ccc['height']=height
    fps=40
    shift()

    import webbrowser#for widgets
    new=1
    ur1="https://weather.com/en-IN/weather/tenday/l/Jodhpur+Rajasthan?canonicalCityId=705dbd593b81c3882065475ccaf1c970644905bcadd355934c98f88063203684"
    ur2="https://www.timeanddate.com/calendar/"
    ur3="https://www.clocktab.com/"
    ur4="https://www.google.co.in/maps/@26.3043082,73.0523224,14z?hl=en&authuser=0"
    ur5="https://www.calculator.net/"
    def openw():#weather
        webbrowser.open(ur1,new=new)
    bt=Button(h,cursor='hand2',width=10,text="Weather",font=('elephant',15,'bold'),bg='navy',fg='white',command=lambda:[openw()])
    bt.place(x=260,y=200)
    
    def opencal():#calendar
        webbrowser.open(ur2,new=new)
    bt2=Button(h,cursor='hand2',width=10,text="Calendar",font=('elephant',15,'bold'),bg='navy',fg='white',command=lambda:[opencal()])
    bt2.place(x=260,y=260)

    def openclo():#clock
        webbrowser.open(ur3,new=new)
    bt3=Button(h,cursor='hand2',width=10,text="Clock",font=('elephant',15,'bold'),bg='navy',fg='white',command=lambda:[openclo()])
    bt3.place(x=260,y=320)

    def openmap():#maps
        webbrowser.open(ur4,new=new)
    bt4=Button(h,cursor='hand2',width=10,text="Maps",font=('elephant',15,'bold'),bg='navy',fg='white',command=lambda:[openmap()])
    bt4.place(x=260,y=380)

    def calc():#calculator
        webbrowser.open(ur5,new=new)
    bt5=Button(h,cursor='hand2',width=10,text="Calculator",font=('elephant',15,'bold'),bg='navy',fg='white',command=lambda:[calc()])
    bt5.place(x=260,y=440)


    cc2.create_text(165,20,text='Your Contact List:-',font=('elephant',20,'bold'),fill='powder blue')#contact list head

    #lstt=['Steve','Wanda','Bruce','Tony','Dwayne','Smith','Jack','Nancy']#default contact list based on interests

    cmb=tak.Combobox(h,width=16,values=lstt,height=4,font=('blackadder itc',25))#combo box
    cmb.current(0)#preset Steve
    cmb.place(x=1069,y=200)


    def chat():#chat box
        cann=Canvas(h,bg='grey2',height=477,width=495)#canvas for chatbox
        cann.place(x=506,y=150)
        chtbx=Label(h,text='CHAT-BOX',font=('elephant',19),foreground='seagreen2',background='grey2')#chatbox
        chtbx.place(x=670,y=155)
        name=Label(h,text=str(cmb.get()),font=('elephant',18),foreground='khaki1',background='grey2',width=10)#name
        name.place(x=668,y=190)

        chatlist=[]#empty list to store chats

        messages = Text(p,width=55,bg='thistle2',height=20)#chat code
        messages.place(x=530,y=220)

        input_user = StringVar()
        input_field = Entry(p,bg='thistle2',text=input_user,width=33,font=('Baskerville Old face',15,'bold'))
        input_field.place(x=533,y=558)
        input_field.insert(0,'Type Here')

        def loadchat():#loading previous chats from file
            f4=open("chats.txt",'a+')
            f4.seek(0,0)
            chtlst=f4.readlines()
            #print('chtlist',chtlst)
            f4.close()
            for i in chtlst:
                print(i.split())
                if i.split('**')[0]==val[0][:-1] and i.split('**')[2][:-1]==cmb.get():#sender to receiver format in file 'chats'
                    #print('yhi h',i)
                    for kk in range(len(i.split('**'))):
                        if kk>2:
                            loadcht=i.split('**')[kk]
                            #print(loadcht)
                            messages.insert(INSERT,(' '*(55-len(loadcht)))+'%s\n'%loadcht)
                elif i.split('**')[0]==cmb.get() and i.split('**')[2][:-1]==val[0][:-1]:#receiver to sender format
                    for kk in range(len(i.split('**'))):
                        if kk>2:
                            loadcht=i.split('**')[kk]
                            #print(loadcht)
                            messages.insert(INSERT,'%s\n'%loadcht)               
        loadchat()

        def clearddict3():#remove deleted chat
            del ddict3[cmb.get()[2::]]
            print(ddict3)

        def Enter_pressed(event):
            input_get = input_field.get()
            chatlist.append(input_field.get())#adding chats to chatlist
            ddict3.update({cmb.get()[2::]:chatlist})#adding chat to ddict3
            print(input_get)
            print('dd',ddict3)
            messages.insert(INSERT,(' '*(55-len(input_get)))+'%s\n\n' % input_get)
            input_user.set('')
            def savechat():#to save chats in file 'chats'
                f4=open("chats.txt",'a+')
                f4.write(val[0][:-1]+'**to**'+cmb.get()+':**'+input_get+'\n')
                f4.write(cmb.get()+'**from**'+val[0][:-1]+':**'+input_get+'\n')
                f4.close()
            savechat()#calling to save chat     
            return "break"
         
        frame = Frame(p)    
        input_field.bind("<Return>", Enter_pressed)
        frame.place(x=400,y=280)

        L=Label(h,text='Press Enter To\nSend Message',foreground='khaki1',background='grey2',width=20,font=('baskerville old face',10,'bold'))
        L.place(x=818,y=556)

  
    def newlyadd():#to show details of new contacts
        st=cmb.get()#contact in combobox
        f3=open("contacts.txt",'r')
        ll2=f3.readlines()
        f3.close()
        for i in ll2:
            a=i.split(':')
            if a[1].split(',')[0]==st:
                ll=Label(h,text=a[1].split(',')[1][:-1]+"'s"+" Details:-\n\nNAME:   "+a[1].split(',')[1]+"\n   USERNAME:   "+st,
                         font=('elephant',15),bg='black',fg='white',width=20)
                ll.place(x=1030,y=350)
                c3=Button(h,cursor='hand2',text='CHAT!!',command=lambda:[chat(),c3.destroy()],font=('elephant',15),bg='navy',fg='white')#chat button
                c3.place(x=1140,y=500)
                break
        
        

    def addcontct():#to add required contacts
        pop=Tk(className=' ADD CONTACT')
        pop.geometry('500x500')
        op=Frame(p).pack()
    
        cc=Canvas(pop,width=1000,height=500,bg='pink')#main canvas
        #cc.create_image(0,0,image=imm,anchor='nw')image setup
        cc.pack()
        cc.create_text(140,200,text='USERNAME: ',font=('cooper black',12),fill='blue2')
        

        def adtocombo(u,n):#adding new contact to combo's list 'lstt'
            if u not in lstt:
                lstt.append(u)
            
        def addnew(a,b):#adding new contact to file 'contacts'
            f3=open("contacts.txt",'a+')
            f3.write(val[0][:-1]+':'+a+','+b+'\n')
            f3.close()
            print('contact added')
            adtocombo(a,b)

        def addbtn(u,nm):#add button pops
            btn=Button(pop,cursor='hand2',text='ADD',command=lambda:[addnew(u,nm),pop.destroy(),p.destroy(),newmain()],
                       font=('elephant',10),bg='navy',fg='white')
            btn.place(x=270,y=290)

        def focshift(event):#to shift focus to i2
            def i2appear(uname,name):#i2 appears
                cc.create_text(140,250,text='NAME: ',font=('cooper black',12),fill='blue2')
                i2=Entry(pop,font=('Baskerville Old face',12,'bold'))#nm
                i2.place(x=200,y=240)
                i2.focus_set()
                def chknm(event):#to check if name is correct
                    if name==i2.get():
                        prsnt=Label(pop,text='  \tGOOD TO GO!! \t\t',font=('arial',8,'bold'),background='pink',foreground='dark blue')
                        prsnt.place(x=240,y=265)
                        addbtn(uname,name)
                    else:
                        nprsntt=Label(pop,text=' INCORRECT NAME  ',font=('arial',8,'bold'),foreground='red',background='pink')
                        nprsntt.place(x=240,y=265)
                    
                i2.bind("<Return>",chknm)
            f=open("prochat.txt",'a+')
            f.seek(0,0)
            ggg=f.readlines()
            for nn in ggg:
                if nn.split()[0]==i1.get():
                    prsnt=Label(pop,text='  \tGOOD TO GO!! \t\t',font=('arial',8,'bold'),background='pink',foreground='dark blue')
                    prsnt.place(x=240,y=215)
                    i2appear(nn.split()[0],nn.split()[1])
                    break
            else:
                nprsntt=Label(pop,text=' NO SUCH USER EXISTS  ',font=('arial',8,'bold'),foreground='red',background='pink')
                nprsntt.place(x=240,y=215)
            f.close()
            #i2.bind("<Return>",addbtn)
        i1 = Entry(pop,font=('Baskerville Old face',12,'bold'))#unm
        i1.place(x=200,y=190)
        i1.focus_set()
        i1.bind("<Return>",focshift)#to set focus on i2 after enter pressed

        
        pop.mainloop()

    add=Button(h,cursor='hand2',text='Add Contact',command=lambda:[addcontct()],font=('elephant',11),bg='navy',fg='white')#add contact button
    add.place(x=1130,y=590)
   

    def stev():#steve details
        ll=Label(h,text="Steve's Details:-\n\nNAME:   Steve\n   USERNAME:   theCAP",font=('elephant',15),bg='black',fg='white',width=20)
        ll.place(x=1030,y=350)
        c1=Button(h,cursor='hand2',text='CHAT!!',command=lambda:[chat(),c1.destroy()],font=('elephant',15),bg='navy',fg='white')#chat button
        c1.place(x=1140,y=500)
        
    def wand():#wanda details
        ll=Label(h,text="Wanda's Details:-\n\nNAME:   Wanda\n   USERNAME:   Wa44nda",font=('elephant',15),bg='black',fg='white',width=20)
        ll.place(x=1030,y=350)
        c2=Button(h,cursor='hand2',text='CHAT!!',command=lambda:[chat(),c2.destroy()],font=('elephant',15),bg='navy',fg='white')#chat button
        c2.place(x=1140,y=500)
        
    def bruce():#bruce details
        ll=Label(h,text="Bruce's Details:-\n\nNAME:   Bruce\n   USERNAME:   thehulk4u",font=('elephant',15),bg='black',fg='white',width=20)
        ll.place(x=1030,y=350)
        c3=Button(h,cursor='hand2',text='CHAT!!',command=lambda:[chat(),c3.destroy()],font=('elephant',15),bg='navy',fg='white')#chat button
        c3.place(x=1140,y=500)
         
    def dwayne():#dwayne detials
        ll=Label(h,text="Dwayne' Details:-\n\nNAME:   Dwayne\n   USERNAME:   ddE1",font=('elephant',15),bg='black',fg='white',width=20)
        ll.place(x=1030,y=350)
        c4=Button(h,cursor='hand2',text='CHAT!!',command=lambda:[chat(),c4.destroy()],font=('elephant',15),bg='navy',fg='white')#chat button
        c4.place(x=1140,y=500)
        
    def tony():#tony details
        ll=Label(h,text="Tony's Details:-\n\nNAME:   Tony\n   USERNAME:   EDITH!!",font=('elephant',15),bg='black',fg='white',width=20)
        ll.place(x=1030,y=350)
        c5=Button(h,cursor='hand2',text='CHAT!!',command=lambda:[chat(),c5.destroy()],font=('elephant',15),bg='navy',fg='white')#chat button
        c5.place(x=1140,y=500)
        
    def smith():#smith details
        ll=Label(h,text="Smith's Details:-\n\nNAME:   Smith\n   USERNAME:   lok_i",font=('elephant',15),bg='black',fg='white',width=20)
        ll.place(x=1030,y=350)
        c6=Button(h,cursor='hand2',text='CHAT!!',command=lambda:[chat(),c6.destroy()],font=('elephant',15),bg='navy',fg='white')#chat button
        c6.place(x=1140,y=500)
        
    def jack():#jack details
        ll=Label(h,text="Jack's Details:-\n\nNAME:   Jack\n   USERNAME:   Jk45r",font=('elephant',15),bg='black',fg='white',width=20)
        ll.place(x=1030,y=350)
        c7=Button(h,cursor='hand2',text='CHAT!!',command=lambda:[chat(),c7.destroy()],font=('elephant',15),bg='navy',fg='white')#chat button
        c7.place(x=1140,y=500)
        
    def nancy():#nancy details
        ll=Label(h,text="Nancy's Details:-\n\nNAME:   Nancy\n   USERNAME:   Vs^n",font=('elephant',15),bg='black',fg='white',width=20)
        ll.place(x=1030,y=350)
        c8=Button(h,cursor='hand2',text='CHAT!!',command=lambda:[chat(),c8.destroy()],font=('elephant',15),bg='navy',fg='white')#chat button
        c8.place(x=1140,y=500)
        
    def chkcombo():#checking selected contact
        if cmb.get()=='theCAP':
            stev()
        elif cmb.get()=='Wa44nda':
            wand()
        elif cmb.get()=='thehulk4u':
            bruce()
        elif cmb.get()=='ddE1':
            dwayne()
        elif cmb.get()=='EDITH':
            tony()
        elif cmb.get()=='lok_i':
            smith()
        elif cmb.get()=='Jk45r':
            jack()
        elif cmb.get()=='Vs^n':
            nancy()
        else:
            newlyadd()
    bb=Button(h,text="OK",width=10,command=lambda:[chkcombo()],bg='navy',fg='white',cursor='hand2',font=('Times New Roman',10))#combo box
    bb.place(x=1130,y=280)

    p.mainloop()
#****************************************************************************************************************************************
#4th page(welcome)
def main():
    lstt=[]#to save interests later
    print(ddict1)
    z=Tk(className=' प्रो-CHAT ')
    #z.geometry('1100x700')
    j=Frame(z).pack()

    img=PhotoImage(file='Screenshot (775).png')

    cc1=Canvas(j,height=700,width=1200)
    cc1.create_image(0,0,image=img,anchor='nw')
    cc1.pack()

    b4=Button(j,cursor='hand2',text='<<GO BACK',font=('arial',8,'bold'),bg='light cyan',command=lambda: [z.destroy(),SignUp()]).place(x=245,y=40)#bck btn

    cc1.create_text(320,200,text="Hi,",font=('blackadder itc',50,'bold'),fill='black')
    
    f=open("prochat.txt",'a+')#opening the file to get name after 'hi'
    f.seek(0,0)
    lst=f.readlines()
    print(lst)
    st=lst[len(lst)-1]
    ss=st.split()
    a=ss[1]
    b=ss[0]
    f.close()
        
    cc1.create_text(500,200,text=a,font=('blackadder itc',50,'bold'),fill='black')
    cc1.create_text(570,300,text="We would Like to know your Interests to Suggest You People with\nSimilar Interests across the Globe. "\
                    "Please choose your Interests from the\n  ones Given Here:-",font=('blackadder itc',25,'bold'),fill='black')

    progress = tak.Progressbar(z,orient = HORIZONTAL,length = 250, mode = 'determinate')#loading bar
    def bar():#loading bar
        progress.place(x=580,y=610)
        cc1.create_text(330,620,text='LOADING...',font=('cooper black',12),fill='blue')
        #import time#already imported    
        progress['value'] = 0
        z.update_idletasks() 
        time.sleep(1) 
    
        progress['value'] = 25
        z.update_idletasks() 
        time.sleep(1) 
        
        progress['value'] = 50
        z.update_idletasks() 
        time.sleep(1) 
    
        progress['value'] = 75
        z.update_idletasks() 
        time.sleep(1) 

        progress['value'] = 100
                
        z.destroy(),newmain()

    def cont():#continue & adding interests to 'interests'
        f2=open("interests.txt",'a+')
        f2.write(b+':'+str(lstt)+'\n')
        f2.close()
        bar()

    def createlstt(st):#to create list of interests chosen
        lstt.append(st)
        cntb=Button(j,cursor='hand2',text='CONTINUE>>',font=('arial',9,'bold'),bg='light cyan',relief='raised',command=lambda:[cont()])#continue button
        cntb.place(x=1000,y=600)

    ca=Canvas(j,width=230,height=240,bg='light cyan').place(x=595,y=357)
    b1=Checkbutton(j,font=('arial',8,'bold'),cursor='hand2',text='Physics',command=lambda:[createlstt('Physics')],bg='light cyan').place(x=600,y=360)#buttons for choice
    b2=Checkbutton(j,font=('arial',9,'bold'),cursor='hand2',text='Mathematics',command=lambda:[createlstt('Mathematics')],bg='light cyan').place(x=600,y=400)
    b3=Checkbutton(j,font=('arial',9,'bold'),cursor='hand2',text='Chemistry',command=lambda:[createlstt('Chemistry')],bg='light cyan').place(x=600,y=440)
    b4=Checkbutton(j,font=('arial',9,'bold'),cursor='hand2',text='Astrology',command=lambda:[createlstt('Astrology')],bg='light cyan').place(x=600,y=480)
    b5=Checkbutton(j,font=('arial',9,'bold'),cursor='hand2',text='Arts',command=lambda:[createlstt('Arts')],bg='light cyan').place(x=600,y=520)
    b6=Checkbutton(j,font=('arial',9,'bold'),cursor='hand2',text='Culture',command=lambda:[createlstt('Culture')],bg='light cyan').place(x=600,y=560)
    b7=Checkbutton(j,font=('arial',9,'bold'),cursor='hand2',text='Politics',command=lambda:[createlstt('Politics')],bg='light cyan').place(x=710,y=360)
    b8=Checkbutton(j,font=('arial',9,'bold'),cursor='hand2',text='Hollywood',command=lambda:[createlstt('Hollywood')],bg='light cyan').place(x=710,y=400)
    b9=Checkbutton(j,font=('arial',9,'bold'),cursor='hand2',text='TV',command=lambda:[createlstt('TV')],bg='light cyan').place(x=710,y=440)
    b10=Checkbutton(j,font=('arial',9,'bold'),cursor='hand2',text='Bollywood',command=lambda:[createlstt('Bollywood')],bg='light cyan').place(x=710,y=480)
    b11=Checkbutton(j,font=('arial',9,'bold'),cursor='hand2',text='Music',command=lambda:[createlstt('Music')],bg='light cyan').place(x=710,y=520)
    b12=Checkbutton(j,font=('arial',9,'bold'),cursor='hand2',text='Sports',command=lambda:[createlstt('Sports')],bg='light cyan').place(x=710,y=560)

    z.mainloop()#end of 4th screen
#***************************************************************************************************************************************************************************************
#3rd page(sign in)
def SignIn():
    q=Tk(className=' SIGN IN ')
    #q.geometry('1000x700')
    t=Frame(q).pack()
    
    ii=PhotoImage(file='Screenshot (88).png')

    c8=Canvas(t,height=800,width=1200)#maincanvas3
    c8.create_image(0,0,image=ii,anchor='nw')
    c8.pack()

    c8.create_text(600,100,text='SIGN IN',font=('jokerman',50,'underline'),fill='blue2')#sign in heading

    b4=Button(t,cursor='hand2',text='<<GO BACK',font=('arial',8,'bold'),bg='turquoise',command=lambda: [q.destroy(),SignUp()]).place(x=240,y=42)#backbutton2

    c8.create_text(300,200,text='USERNAME:',font=('cooper black',20,'bold'),fill='indigo')#unm pw
    c8.create_text(300,300,text='PASSWORD:',font=('cooper black',20,'bold'),fill='indigo')
    
    #entries
    u5=Entry(t,width=20,font=('Baskerville Old Face',20,'bold'))#unm
    u5.place(x=630,y=180)
    u5.focus_set()
    u6=Entry(t,width=20,font=('Baskerville Old Face',20,'bold'))#pwd
    u6.place(x=630,y=280)


    def Nxt():#submit sign in
        ss=Button(t,cursor='hand2',text='NEXT>>',font=('algerian',16,'bold'),bg='lightblue1',fg='black',relief='raised',
                  command=lambda:[q.destroy(),newmain()])
        ss.place(x=1170,y=550)
        
    def chngpwd():#fgtpwd bttn clicked
        st=''#to store new pwd of i2
        pop=Tk(className=' CHANGE PASSWORD')
        pop.geometry('500x500')
        op=Frame(q).pack()
        cc=Canvas(pop,width=1000,height=500,bg='pink')
        cc.pack()
        cc.create_text(140,200,text='OLD PASSWORD: ',font=('cooper black',12),fill='blue2')

        
        
        def invld():#old pwd invalid
            nprsntt=Label(pop,text=' INCORRECT PASSWORD, RETRY  ',font=('arial',8,'bold'),foreground='red',background='pink')
            nprsntt.place(x=240,y=215)

        def nxtt():#ok btn after new pwd set
            btn=Button(pop,cursor='hand2',text='OK',command=lambda:[pop.destroy()],font=('elephant',10),bg='navy',fg='white')
            btn.place(x=270,y=290)
            
            
        def chkpw(event):#cheking old pwd in file
            f=open("prochat.txt",'a+')
            print(f.tell())#current location of pointer
            f.seek(0,0)
            llt=f.readlines()
            f.close()
            for i in llt:
                if i.split()[3]==i1.get():
                    pos=llt.index(i)
                    prsnt=Label(pop,text='  \tGOOD TO GO!! \t\t',font=('arial',8,'bold'),background='pink',foreground='dark blue')
                    prsnt.place(x=240,y=215)
                    cc.create_text(140,250,text='NEW PASSWORD: ',font=('cooper black',12),fill='blue2')
                    def valid(enter):#old pwd valid
                        a=i.replace(i1.get(),i2.get())
                        llt[llt.index(i)]=a
                        f=open("prochat.txt",'w')
                        f.writelines(llt)
                        f.close()
                        nxtt()
                    i2=Entry(pop,font=('Baskerville Old face',12,'bold'))#nm
                    i2.place(x=240,y=240)
                    i2.focus_set()
                    i2.bind("<Return>",valid)
                    break
            else:
                invld()         
            
        i1 = Entry(pop,font=('Baskerville Old face',12,'bold'))#unm
        i1.place(x=240,y=190)
        i1.focus_set()
        
        i1.bind("<Return>",chkpw)#after enter pressed check old pw
        
        pop.mainloop()

    def captcha2():#captcha
        def chkcap1(event):#Captcha check
            cap=startentry.get()
            print(cap)
            if st1!=cap:
                inv=Label(t,text='INVALID CAPTCHA!! TRY AGAIN',font=('arial',9,'bold'),background='pink',foreground='red',width=30)
                inv.place(x=630,y=610)
            else:
                Nxt()
                val=Label(t,text='GOOD TO GO!!',font=('arial',9,'bold'),background='pink',foreground='dark blue',width=30)
                val.place(x=630,y=610)            

                
        st1=''#captcha generatn
        import random as rand
        for i in range(2):
            st1+=chr(rand.randint(65,91))
        for j in range(2):
            st1+=chr(rand.randint(48,58))
        for k in range(3):
            st1+=chr(rand.randint(97,123))
        c8.create_text(290,535,text='CAPTCHA:' ,font=('cooper black',20,'bold'),fill='indigo')
        lq=Label(t,text=st1,font=('Curlz mt',20,'bold'),foreground='navy',background='cadetblue2',width=10)
        lq.place(x=630,y=515)
        
        c8.create_text(268,580,text='ENTER:' ,font=('cooper black',20,'bold'),fill='indigo')
        startentry=Entry(t,width=20,font=('Baskerville Old Face',20,'bold'))
        startentry.place(x=630,y=565)
        startentry.focus_set()
        startentry.bind("<Return>",chkcap1)
        b2=Button(t,cursor='hand2',text='Reload CAPTCHA',bg='light cyan',font=('arial',11,'bold'),command=lambda:[captcha2()])#reload captcha
        b2.place(x=930,y=565) 

    def invldunm():#username invalid
        nprsnt=Label(t,text='    ENTERED USERNAME DOES NOT EXIST, RETRY  ',font=('arial',9,'bold'),background='pink',foreground='red')
        nprsnt.place(x=630,y=220)
        #ret=Button(t,cursor='hand2',text='RETRY',font=('arial',8,'bold'),command=lambda:[nprsnt.destroy(),button1(),ret.destroy()])
        #ret.place(x=880,y=220)

    def invldpwd():#pwd invalid
        nprsntt=Label(t,text='\tINCORRECT PASSWORD, RETRY\t',font=('arial',9,'bold'),foreground='red',background='pink')
        nprsntt.place(x=630,y=320)

    def fgtpwd():#forgot pwd clicked
        f=open("prochat.txt",'a+')
        f.seek(0,0)
        llt=f.readlines()
        f.close()
        for i in llt:
            if i.split()[0]==u5.get():
                secqtn=i.split('(')[1].partition(':')[0]
                ans=i.split('(')[1].partition(':')[2][:-2]
                break

        def chkans(event):#checking entered answer
            rec=enn.get()
            if rec!=ans:
                err=Label(t,text='WRONG ANSWER!!..RE-ENTER',font=('arial',9,'bold'),background='pink',foreground='red',width=30)
                err.place(x=630,y=480)
            else:
                val.extend([i.split()[0],i.split()[1],i.split()[2],i.split()[3],i.split()[4]])#adding unm,fnm,lnm,pw to val for add contact later
                gtg=Label(t,text='GOOD TO GO!!',font=('arial',9,'bold'),background='pink',foreground='blue2',width=30)
                gtg.place(x=630,y=480)
                captcha2()        
            
            
        c8.create_text(390,420,text=secqtn,font=('Baskerville Old Face',20,'bold'),fill='green')
        c8.create_text(300,460,text='Your Answer: ',font=('Baskerville Old Face',20,'bold'),fill='indigo')
        enn=Entry(t,width=20,font=('Baskerville Old Face',20,'bold'))#entry for secqtn answer
        enn.place(x=630,y=440)
        enn.bind("<Return>",chkans)
        
    def unmm(event):#unm check
        unm=u5.get()
        f=open("prochat.txt",'a+')
        f.seek(0,0)
        llt=f.readlines()
        f.close()
        for i in llt:
            if i.split()[0]==unm:
                prsnt=Label(t,text='\t           GOOD TO GO!! \t                ',font=('arial',9,'bold'),background='pink',foreground='dark blue')
                prsnt.place(x=630,y=220)
                fgtpw=Button(t,cursor='hand2',text='FORGOT PASSWORD?',font=('cooper black',15),bg='light cyan',fg='indigo',relief='raised',
                             command=lambda:[fgtpwd(),fgtpw.destroy()])
                fgtpw.place(x=630,y=360)
                chngpw=Button(t,cursor='hand2',text='CHANGE PASSWORD?',font=('cooper black',10),bg='light cyan',fg='indigo',relief='raised',
                              command=lambda:[chngpwd()])#chng pw btn
                chngpw.place(x=1020,y=370)
                u6.focus_set()
                break

        else:
            invldunm()
                
    def pwdd(event):#pwd check
        pwd=u6.get()
        f=open("prochat.txt",'a+')
        f.seek(0,0)
        llt=f.readlines()
        f.close()
        for i in llt:
            if i.split()[3]==pwd:
                prsnt=Label(t,text='\t           GOOD TO GO!! \t                ',font=('arial',9,'bold'),background='pink',foreground='dark blue')
                prsnt.place(x=630,y=320)
                val.extend([i.split()[0],i.split()[1],i.split()[2],i.split()[3],i.split()[4]])#adding unm,fnm,lnm,pw to val for add contact later
                captcha2()#calling captcha fxn
                break
        else:
            invldpwd()
            
    u5.bind("<Return>",unmm)
    u6.bind("<Return>",pwdd)
    q.mainloop()#end of 3rd page

#***************************************************************************************************************************************************************************************
#2nd page(sign up)
def SignUp():
    n=Tk(className=" SIGN UP ")
    #n.geometry("1000x700")
    g=Frame(n).pack()

    im1=PhotoImage(file='Screenshot (81).png')#main image
    
    cc=Canvas(g,width=1200,height=700)#main canvas
    cc.create_image(0,0,image=im1,anchor='nw')
    cc.pack()
    cc.create_text(530,100,text='SIGN UP',font=('Curlz MT',50,'bold','underline'),fill='grey1')
    cc.create_text(340,200,text='USERNAME: ',font=('cooper black',20),fill='blue2')
    cc.create_text(340,250,text='FIRST NAME: ',font=('cooper black',20),fill='blue2')
    cc.create_text(340,300,text='LAST NAME: ',font=('cooper black',20),fill='blue2')
    cc.create_text(340,350,text='PASSWORD: ',font=('cooper black',20),fill='blue2')
    
    bck1=Button(g,cursor='hand2',relief='solid',bg='turquoise',font=('arial',8,'bold'),text='<<GO BACK',
                command=lambda: [n.destroy(),Welcome()]).place(x=230,y=33)#backbutton1
     
    def unm(event):#entering and adding unm,fnm,lnm,pw
        c=0
        unm=i1.get()
        f=open("prochat.txt",'a+')#UNM ALREADY EXISTS CHECK
        f.seek(0,0)
        ltt=f.readlines()
        print('ltt',ltt)
        f.close()
        for i in ltt:
            print('i',i)
            if i.split()[0]==unm:
                print('already exists')
                ll=Label(n,text='USERNAME TAKEN, TRY A NEW ONE',font=('arial',9,'bold'),foreground='red',background='pink')
                ll.place(x=975,y=195)
                c=1
                break
        if c==0:
            ll=Label(n,text='               GOOD CHOICE !!                     ',font=('arial',9,'bold'),foreground='dark blue',background='pink')
            ll.place(x=975,y=195)
            val.append(unm+' ')
        i2.focus_set()
    def fnm(event):
        fnm=i2.get()
        val.append(fnm+' ')
        i3.focus_set()
    def lnm(event):
        lnm=i3.get()
        val.append(lnm+' ')
        i4.focus_set()
    def pw(event):
        pw=i4.get()
        val.append(pw+' ')
        f=open("prochat.txt",'a+')#opening the file
        f.writelines(val)#writing list val of record into file
        f.close()
        secqtn()

    i1 = Entry(n,font=('Baskerville Old face',20,'bold'))#unm
    i1.place(x=680,y=185)
    i1.focus_set()#cursor at i1
    i2=Entry(n,font=('Baskerville Old face',20,'bold'))#fnm
    i2.place(x=680,y=235)
    i3=Entry(n,font=('Baskerville Old face',20,'bold'))#lnm
    i3.place(x=680,y=285)
    i4=Entry(n,font=('Baskerville Old face',20,'bold'))#pw
    i4.place(x=680,y=335)
    '''input_field1.insert(0,"type here")#for type here
    input_field2.insert(0)
    input_field3.insert(0)'''
    i1.bind("<Return>",unm)#calling fxns here
    i2.bind("<Return>",fnm)
    i3.bind("<Return>",lnm)
    i4.bind("<Return>",pw)

    
    def Nxt():#submit sign up
        ss=Button(g,cursor='hand2',text='NEXT>>',font=('algerian',15,'bold'),relief='solid',background='lightblue1',foreground='black',
                  command=lambda:[n.destroy(),main()]).place(x=600,y=600)
        
    def captcha1():#captcha
        def chkcap(event):#Captcha check
            cap=startentry.get()
            print(cap)
            if st1!=cap:
                inv=Label(g,text='INVALID CAPTCHA!! TRY AGAIN',font=('arial',9,'bold'),background='pink',foreground='red')
                inv.place(x=940,y=600)
            
            else:
                Nxt()
                val=Label(g,text='GOOD TO GO!!',font=('arial',9,'bold'),background='pink',foreground='dark blue',width=25)
                val.place(x=940,y=600)
                
        st1=''#captcha generatn
        import random as rand
        for i in range(2):
            st1+=chr(rand.randint(65,91))
        for j in range(2):
            st1+=chr(rand.randint(48,58))
        for k in range(3):
            st1+=chr(rand.randint(97,123))
        cc.create_text(657,550,text='CAPTCHA:',font=('cooper black',15,'bold'),fill='blue2')
       
        ll=Label(g,text=st1,font=('Curlz mt',20,'bold'),foreground='navy',background='medium sea green',width=10)
        ll.place(x=940,y=520)
        
        cc.create_text(645,580,text='ENTER:',font=('cooper black',15,'bold'),fill='blue2')
        startentry=Entry(g,width=15,font=('arial',12,'bold'))
        startentry.place(x=940,y=570)
        startentry.focus_set()
        startentry.bind("<Return>",chkcap)
        b2=Button(g,cursor='hand2',text='Reload CAPTCHA',font=('arial',10,'bold'),background='light cyan',relief='solid',
                  command=lambda:[captcha1()])#reload captcha
        b2.place(x=940,y=625)

    def secqtn():#qtns
        def setup(event):
            ii5=i5.get()
            cmbb=cmb.get()
            secqn=cmbb+':'+ii5
            f=open("prochat.txt",'a+')#opening the file
            f.write('('+secqn+')\n')#writing list val of record into file
            f.close()
            print('secqtn and ans added')
            captcha1()
            
        cc.create_text(340,450,text='SECURITY QUESTION:',font=('cooper black',17),fill='blue2')
        cc.create_text(340,500,text='YOUR ANSWER:',font=('cooper black',15),fill='blue2')
        lst=["--Select--", "What is your Father's Name?","What is your Mother's Name?","What is your Mobile Number?","What is your House Number?",
             'Which is your Favourite City?']#sec qtn
        cmb=tak.Combobox(n,width=26,values=lst,height=5,font=('cooper black',13))#combo box for secqtn
        cmb.current(0)
        cmb.place(x=680,y=435)
        cmb.focus_set()
        i5=Entry(n,width=25,font=('Baskerville Old face',15,'bold'))#sec ans
        i5.place(x=680,y=480)
        i5.bind("<Return>",setup)#run setup() on pressing enter

    cc.create_text(170,590,text='Already a user?',font=('cooper black',20,'bold'),fill='blue2')
    b3=Button(g,cursor='hand2',text='Click here to Sign In',bg='light cyan',font=('arial',11,'bold'),relief='solid',
              command=lambda:[n.destroy(),SignIn()]).place(x=260,y=620)
    
   
    n.mainloop()#end of 2nd page

#***************************************************************************************************************************************************************************************


#1st page(welcome)
def Welcome():#first
    r=Tk(className=' प्रो-CHAT™©')#Tk
    #r.geometry('1150x700')
    f=Frame(r).pack()

    pic1=PhotoImage(file='Screenshot (64).png') #PICTURE
    pic2=PhotoImage(file='Screenshot (78).png')

    c5=Canvas(f,width=1150,height=700)#main canvas
    c5.create_image(0,0,image=pic1,anchor='nw')#main bg
    c5.create_image(50,380,image=pic2,anchor='nw')#wooden
    c5.pack()
    c5.create_text(400,250,text='WELCOME TO',font=('cooper black',40),fill='blue2')
    c5.create_text(800,250,text=" PRo-CHAT™  ",font=('cooper black',40),fill='spring green4')
    c5.create_text(165,400,text="Privacy Policy:- ",font=('cooper black',20),fill='alice blue')
    c5.create_text(570,525,text="\n⭐PRo-CHAT is a free software developed to enable users to perform various tasks like \n    "\
                   "chatting & much more.\n\n⭐While this software takes utmost care of your Privacy, it asks for Personal Information like\n      "\
                   "your Username & Password etc. It is informed that any such Personal Information is well\n      secured & its mischievous use is "\
                   "impossible in wake of the security offered by the Creator.\n\n⭐Please select 'I agree' to continue to the software only if "\
                   "you have read & accepted the\n      Privacy Policy",font=('cooper black',15),fill='alice blue')
    
    def submit():#submit
        b1=Button(r,text='SUBMIT',cursor='hand2',font=('cooper black',12),bg='lightskyblue2',fg='blue2',relief='solid',width=10,height=2,
                  command=lambda:[r.destroy(),SignUp()])
        b1.place(x=900,y=625)
    v=StringVar(f,"0")#agree
    values={"I AGREE":"1"}
    for (text,value) in values.items():
        Radiobutton(f,bg='lightskyblue2',cursor='hand2',relief='solid',fg='blue2',text=text,font=('cooper black',12),width=8,height=1,
                    variable=v,value=value,command=lambda:[submit()]).place(x=612,y=650)  
    r.mainloop()#end of 1st page
    
Welcome()#end of first
