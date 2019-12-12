#M&P(CR7) game Created By Sajad.CR7 / Copyright@2015
from tkinter import*
from random import*
import time
#for restart button
T = 2
T2 = 2
#For scoreboard
I = 0
I2 = 0
#window
a = Tk()
a.geometry('1000x800')
a.configure(background = 'goldenrod')
a.title('M&P(CR7)')
#for copyright
EE = Label(a,text='By : Sajad.CR7 / My-Website : www.CR7group.blog.ir / Copyright@2015 ',bg='goldenrod',font='thoma 15 bold')
EE.place(x=50,y=760)
#Butttons for tas
tas = Button(a,text='Click',width = 6,height =4,bg = 'yellow',fg='black')
tas.place(x=840,y=720)
tas2 = Button(a,text='Click',width = 6,height =4,fg = 'yellow',bg='black')
tas2.place(x=940,y=720)
#Buttons and Labels for main menu
L1=Label(a,text='--------- ',bg='goldenrod')
L1.place(x=940,y=580)
L2=Label(a,text='--------- ',bg='goldenrod')
L2.place(x=940,y=470)
L3=Label(a,text='--------- ',bg='goldenrod')
L3.place(x=940,y=360)
L4=Label(a,text='--------- ',bg='goldenrod')
L4.place(x=940,y=250)
L6=Label(a,text='------------ ',bg='goldenrod')
L6.place(x=820,y=250)
L7=Label(a,text='------------ ',bg='goldenrod')
L7.place(x=820,y=360)
L8=Label(a,text='------------ ',bg='goldenrod')
L8.place(x=820,y=470)
L9=Label(a,text='------------ ',bg='goldenrod')
L9.place(x=820,y=580)
l1=Label(a,text='|',bg='goldenrod')
l1.place(x=910,y=570)
l2=Label(a,text='|',bg='goldenrod')
l2.place(x=910,y=550)
l3=Label(a,text='|',bg='goldenrod')
l3.place(x=910,y=530)
l4=Label(a,text='|',bg='goldenrod')
l4.place(x=910,y=510)
l5=Label(a,text='|',bg='goldenrod')
l5.place(x=910,y=490)
l6=Label(a,text='|',bg='goldenrod')
l6.place(x=910,y=470)
l7=Label(a,text='|',bg='goldenrod')
l7.place(x=910,y=450)
l8=Label(a,text='|',bg='goldenrod')
l8.place(x=910,y=430)
l9=Label(a,text='|',bg='goldenrod')
l9.place(x=910,y=410)
l10=Label(a,text='|',bg='goldenrod')
l10.place(x=910,y=390)
l11=Label(a,text='|',bg='goldenrod')
l11.place(x=910,y=370)
l12=Label(a,text='|',bg='goldenrod')
l12.place(x=910,y=350)
l13=Label(a,text='|',bg='goldenrod')
l13.place(x=910,y=330)
l14=Label(a,text='|',bg='goldenrod')
l14.place(x=910,y=310)
l15=Label(a,text='|',bg='goldenrod')
l15.place(x=910,y=290)
l16=Label(a,text='|',bg='goldenrod')
l16.place(x=910,y=270)
l17=Label(a,text='|',bg='goldenrod')
l17.place(x=910,y=250)
l18=Label(a,text='|',bg='goldenrod')
l18.place(x=910,y=230)
l19=Label(a,text='|',bg='goldenrod')
l19.place(x=910,y=210)
l20=Label(a,text='|',bg='goldenrod')
l20.place(x=910,y=190)
l21=Label(a,text='|',bg='goldenrod')
l21.place(x=910,y=170)
tasl=Label(a,text='Tas P1 :   ',bg='goldenrod')
tasl.place(x=840,y=650)
tasl2=Label(a,text='Tas P2 :   ',bg='goldenrod')
tasl2.place(x=940,y=650)
ex = Button(a,text='Exit',width = 6,height =4,bg = 'red')
ex.place(x=940,y=500)
ab = Button(a,text='About',width = 6,height =4,bg = 'red')
ab.place(x=940,y=390)
he = Button(a,text='Other',width = 6,height =4,bg = 'red')
he.place(x=940,y=280)
Pa = Button(a,text='Pause',width = 8,height =4,bg = 'red')
Pa.place(x=820,y=170)
sc = Button(a,text='ScoreBoard',width = 8,height =4,bg = 'red')
sc.place(x=820,y=280)
ap = Button(a,text='Update',width = 8,height =4,bg = 'red')
ap.place(x=820,y=390)
se = Button(a,text='Setting',width = 8,height =4,bg = 'red')
se.place(x=820,y=500)
Re = Button(a,text='Restart',width = 6,height =4,bg = 'red')
Re.place(x=940,y=170)
#Buttons for line of game
b0 = Button(a,bg='white',width=10)
b0.place(x=650,y=720)
b1 = Button(a,bg='white',width=10)
b1.place(x=550,y=720)
b2 = Button(a,bg='white',width=10)
b2.place(x=450,y=720)
b3 = Button(a,bg='white',width=10)
b3.place(x=350,y=720)
b4 = Button(a,bg='white',width=10)
b4.place(x=250,y=720)
b5 = Button(a,bg='white',width=10)
b5.place(x=150,y=720)
b6 = Button(a,bg='white',width=10)
b6.place(x=50,y=720)
b7 = Button(a,bg='white',width=10)
b7.place(x=50,y=570)
b8 = Button(a,bg='white',width=10)
b8.place(x=150,y=570)
b9 = Button(a,bg='white',width=10)
b9.place(x=250,y=570)
b10 = Button(a,bg='white',width=10)
b10.place(x=350,y=570)
b11 = Button(a,bg='white',width=10)
b11.place(x=450,y=570)
b12 = Button(a,bg='white',width=10)
b12.place(x=550,y=570)
b13 = Button(a,bg='white',width=10)
b13.place(x=650,y=570)
b14 = Button(a,bg='white',width=10)
b14.place(x=650,y=420)
b15 = Button(a,bg='white',width=10)
b15.place(x=550,y=420)
b16 = Button(a,bg='white',width=10)
b16.place(x=450,y=420)
b17 = Button(a,bg='white',width=10)
b17.place(x=350,y=420)
b18 = Button(a,bg='white',width=10)
b18.place(x=250,y=420)
b19 = Button(a,bg='white',width=10)
b19.place(x=150,y=420)
b20 = Button(a,bg='white',width=10)
b20.place(x=50,y=420)
b21 = Button(a,bg='white',width=10)
b21.place(x=50,y=270)
b22 = Button(a,bg='white',width=10)
b22.place(x=150,y=270)
b23 = Button(a,bg='white',width=10)
b23.place(x=250,y=270)
b24 = Button(a,bg='white',width=10)
b24.place(x=350,y=270)
b25 = Button(a,bg='white',width=10)
b25.place(x=450,y=270)
b26 = Button(a,bg='white',width=10)
b26.place(x=550,y=270)
b27 = Button(a,bg='white',width=10)
b27.place(x=650,y=270)
b28 = Button(a,bg='white',width=10)
b28.place(x=650,y=120)
b29 = Button(a,bg='white',width=10)
b29.place(x=550,y=120)
b30 = Button(a,bg='white',width=10)
b30.place(x=450,y=120)
b31 = Button(a,bg='white',width=10)
b31.place(x=350,y=120)
b32 = Button(a,bg='white',width=10)
b32.place(x=250,y=120)
b33 = Button(a,bg='white',width=10)
b33.place(x=150,y=120)
b34 = Button(a,text='The End',bg='green',width=10,height=3)
b34.place(x=50,y=90)
#Buttons for players
a1 = Button(a,text='P1',bg='black',fg='white',width=2,height=5)
a1.place(x=750,y=630)
a2 = Button(a,text='P2',bg='white',fg='black',width=2,height=5)
a2.place(x=780,y=630)
#Labels for snake 1
s0 = Label(a,text='/',fg='black',bg='goldenrod')
s0.place(x=180,y=690)
s1 = Label(a,text='/',fg='black',bg='goldenrod')
s1.place(x=190,y=690)
s2 = Label(a,text='/',fg='black',bg='goldenrod')
s2.place(x=190,y=670)
s3 = Label(a,text='/',fg='black',bg='goldenrod')
s3.place(x=200,y=670)
s4 = Label(a,text='/',fg='black',bg='goldenrod')
s4.place(x=200,y=650)
s5 = Label(a,text='/',fg='black',bg='goldenrod')
s5.place(x=210,y=650)
s6 = Label(a,text='/',fg='black',bg='goldenrod')
s6.place(x=210,y=630)
s7 = Label(a,text='/',fg='black',bg='goldenrod')
s7.place(x=220,y=630)
s8 = Label(a,text='/',fg='black',bg='goldenrod')
s8.place(x=220,y=610)
s9 = Label(a,text='/',fg='black',bg='goldenrod')
s9.place(x=230,y=610)
s10 = Label(a,text='/',fg='black',bg='goldenrod')
s10.place(x=230,y=590)
s11 = Label(a,text='/',fg='black',bg='goldenrod')
s11.place(x=240,y=590)
s12 = Label(a,text='/',fg='black',bg='goldenrod')
s12.place(x=250,y=540)
s13 = Label(a,text='/',fg='black',bg='goldenrod')
s13.place(x=260,y=540)
s14 = Label(a,text='/',fg='black',bg='goldenrod')
s14.place(x=260,y=520)
s15 = Label(a,text='/',fg='black',bg='goldenrod')
s15.place(x=270,y=520)
s16 = Label(a,text='/',fg='black',bg='goldenrod')
s16.place(x=270,y=500)
s17 = Label(a,text='/',fg='black',bg='goldenrod')
s17.place(x=280,y=500)
s18 = Label(a,text='/',fg='black',bg='goldenrod')
s18.place(x=280,y=480)
s19 = Label(a,text='/',fg='black',bg='goldenrod')
s19.place(x=290,y=480)
s20 = Label(a,text='/',fg='black',bg='goldenrod')
s20.place(x=290,y=460)
s21 = Label(a,text='/',fg='black',bg='goldenrod')
s21.place(x=300,y=460)
#Labels for snake 2
s_0 = Label(a,text='|',fg='black',bg='goldenrod')
s_0.place(x=580,y=300)
s_1 = Label(a,text='|',fg='black',bg='goldenrod')
s_1.place(x=590,y=300)
s_2 = Label(a,text='|',fg='black',bg='goldenrod')
s_2.place(x=580,y=320)
s_3 = Label(a,text='|',fg='black',bg='goldenrod')
s_3.place(x=590,y=320)
s_4 = Label(a,text='|',fg='black',bg='goldenrod')
s_4.place(x=580,y=340)
s_5 = Label(a,text='|',fg='black',bg='goldenrod')
s_5.place(x=590,y=340)
s_6 = Label(a,text='|',fg='black',bg='goldenrod')
s_6.place(x=580,y=360)
s_7 = Label(a,text='|',fg='black',bg='goldenrod')
s_7.place(x=590,y=360)
s_8 = Label(a,text='|',fg='black',bg='goldenrod')
s_8.place(x=580,y=380)
s_9 = Label(a,text='|',fg='black',bg='goldenrod')
s_9.place(x=590,y=380)
s_10 = Label(a,text='|',fg='black',bg='goldenrod')
s_10.place(x=580,y=400)
s_11 = Label(a,text='|',fg='black',bg='goldenrod')
s_11.place(x=590,y=400)
s_12 = Label(a,text='|',fg='black',bg='goldenrod')
s_12.place(x=580,y=450)
s_13 = Label(a,text='|',fg='black',bg='goldenrod')
s_13.place(x=590,y=450)
s_14 = Label(a,text='|',fg='black',bg='goldenrod')
s_14.place(x=580,y=470)
s_15 = Label(a,text='|',fg='black',bg='goldenrod')
s_15.place(x=590,y=470)
s_16 = Label(a,text='|',fg='black',bg='goldenrod')
s_16.place(x=580,y=490)
s_17 = Label(a,text='|',fg='black',bg='goldenrod')
s_17.place(x=590,y=490)
s_18 = Label(a,text='|',fg='black',bg='goldenrod')
s_18.place(x=580,y=510)
s_19 = Label(a,text='|',fg='black',bg='goldenrod')
s_19.place(x=590,y=510)
s_20 = Label(a,text='|',fg='black',bg='goldenrod')
s_20.place(x=580,y=530)
s_21 = Label(a,text='|',fg='black',bg='goldenrod')
s_21.place(x=590,y=530)
s_22 = Label(a,text='|',fg='black',bg='goldenrod')
s_22.place(x=580,y=550)
s_23 = Label(a,text='|',fg='black',bg='goldenrod')
s_23.place(x=590,y=550)
#Labels for snake 3
s__0 = Label(a,text='|',fg='black',bg='goldenrod')
s__0.place(x=280,y=150)
s__1 = Label(a,text='|',fg='black',bg='goldenrod')
s__1.place(x=290,y=150)
s__2 = Label(a,text='|',fg='black',bg='goldenrod')
s__2.place(x=280,y=170)
s__3 = Label(a,text='|',fg='black',bg='goldenrod')
s__3.place(x=290,y=170)
s__4 = Label(a,text='|',fg='black',bg='goldenrod')
s__4.place(x=280,y=190)
s__5 = Label(a,text='|',fg='black',bg='goldenrod')
s__5.place(x=290,y=190)
s__6 = Label(a,text='|',fg='black',bg='goldenrod')
s__6.place(x=280,y=210)
s__7 = Label(a,text='|',fg='black',bg='goldenrod')
s__7.place(x=290,y=210)
s__8 = Label(a,text='|',fg='black',bg='goldenrod')
s__8.place(x=280,y=230)
s__9 = Label(a,text='|',fg='black',bg='goldenrod')
s__9.place(x=290,y=230)
s__10 = Label(a,text='|',fg='black',bg='goldenrod')
s__10.place(x=280,y=250)
s__11 = Label(a,text='|',fg='black',bg='goldenrod')
s__11.place(x=290,y=250)
#Labels for snake 4
s___0 = Label(a,text='|',fg='black',bg='goldenrod')
s___0.place(x=680,y=300)
s___1 = Label(a,text='|',fg='black',bg='goldenrod')
s___1.place(x=690,y=300)
s___2 = Label(a,text='|',fg='black',bg='goldenrod')
s___2.place(x=680,y=320)
s___3 = Label(a,text='|',fg='black',bg='goldenrod')
s___3.place(x=690,y=320)
s___4 = Label(a,text='|',fg='black',bg='goldenrod')
s___4.place(x=680,y=340)
s___5 = Label(a,text='|',fg='black',bg='goldenrod')
s___5.place(x=690,y=340)
s___6 = Label(a,text='|',fg='black',bg='goldenrod')
s___6.place(x=680,y=360)
s___7 = Label(a,text='|',fg='black',bg='goldenrod')
s___7.place(x=690,y=360)
s___8 = Label(a,text='|',fg='black',bg='goldenrod')
s___8.place(x=680,y=380)
s___9 = Label(a,text='|',fg='black',bg='goldenrod')
s___9.place(x=690,y=380)
s___10 = Label(a,text='|',fg='black',bg='goldenrod')
s___10.place(x=680,y=400)
s___11 = Label(a,text='|',fg='black',bg='goldenrod')
s___11.place(x=690,y=400)
s___12 = Label(a,text='|',fg='black',bg='goldenrod')
s___12.place(x=680,y=450)
s___13 = Label(a,text='|',fg='black',bg='goldenrod')
s___13.place(x=690,y=450)
s___14 = Label(a,text='|',fg='black',bg='goldenrod')
s___14.place(x=680,y=470)
s___15 = Label(a,text='|',fg='black',bg='goldenrod')
s___15.place(x=690,y=470)
s___16 = Label(a,text='|',fg='black',bg='goldenrod')
s___16.place(x=680,y=490)
s___17 = Label(a,text='|',fg='black',bg='goldenrod')
s___17.place(x=690,y=490)
s___18 = Label(a,text='|',fg='black',bg='goldenrod')
s___18.place(x=680,y=510)
s___19 = Label(a,text='|',fg='black',bg='goldenrod')
s___19.place(x=690,y=510)
s___20 = Label(a,text='|',fg='black',bg='goldenrod')
s___20.place(x=680,y=530)
s___21 = Label(a,text='|',fg='black',bg='goldenrod')
s___21.place(x=690,y=530)
s___22 = Label(a,text='|',fg='black',bg='goldenrod')
s___22.place(x=680,y=550)
s___23 = Label(a,text='|',fg='black',bg='goldenrod')
s___23.place(x=690,y=550)
s___24 = Label(a,text='|',fg='black',bg='goldenrod')
s___24.place(x=680,y=600)
s___25 = Label(a,text='|',fg='black',bg='goldenrod')
s___25.place(x=690,y=600)
s___26 = Label(a,text='|',fg='black',bg='goldenrod')
s___26.place(x=680,y=620)
s___27 = Label(a,text='|',fg='black',bg='goldenrod')
s___27.place(x=690,y=620)
s___28 = Label(a,text='|',fg='black',bg='goldenrod')
s___28.place(x=680,y=640)
s___29 = Label(a,text='|',fg='black',bg='goldenrod')
s___29.place(x=690,y=640)
s___30 = Label(a,text='|',fg='black',bg='goldenrod')
s___30.place(x=680,y=660)
s___31 = Label(a,text='|',fg='black',bg='goldenrod')
s___31.place(x=690,y=660)
s___32 = Label(a,text='|',fg='black',bg='goldenrod')
s___32.place(x=680,y=680)
s___33 = Label(a,text='|',fg='black',bg='goldenrod')
s___33.place(x=690,y=680)
s___34 = Label(a,text='|',fg='black',bg='goldenrod')
s___34.place(x=680,y=700)
s___35 = Label(a,text='|',fg='black',bg='goldenrod')
s___35.place(x=690,y=700)
s___36 = Label(a,text='|',fg='black',bg='goldenrod')
s___36.place(x=680,y=250)
s___37 = Label(a,text='|',fg='black',bg='goldenrod')
s___37.place(x=690,y=250)
s___38 = Label(a,text='|',fg='black',bg='goldenrod')
s___38.place(x=680,y=230)
s___39 = Label(a,text='|',fg='black',bg='goldenrod')
s___39.place(x=690,y=230)
s___40 = Label(a,text='|',fg='black',bg='goldenrod')
s___40.place(x=690,y=210)
s___41 = Label(a,text='|',fg='black',bg='goldenrod')
s___41.place(x=680,y=210)
s___42 = Label(a,text='|',fg='black',bg='goldenrod')
s___42.place(x=690,y=190)
s___43 = Label(a,text='|',fg='black',bg='goldenrod')
s___43.place(x=680,y=190)
s___44 = Label(a,text='|',fg='black',bg='goldenrod')
s___44.place(x=690,y=170)
s___45 = Label(a,text='|',fg='black',bg='goldenrod')
s___45.place(x=680,y=170)
s___46 = Label(a,text='|',fg='black',bg='goldenrod')
s___46.place(x=690,y=150)
s___47 = Label(a,text='|',fg='black',bg='goldenrod')
s___47.place(x=680,y=150)
#Enter boxes and Button for player's name
n1=Entry(a,width=15)
n2=Entry(a,width=15)
n1.place(x=900,y=10)
n2.place(x=900,y=40)
Ln1 = Label(a,text='Enter your name as player 1 :',bg='goldenrod')
Ln1.place(x=720,y=10)
Ln2 = Label(a,text='Enter your name as player 2 :',bg='goldenrod')
Ln2.place(x=720,y=40)
Ok = Button(a,text='submit',bg='yellowgreen',width=8)
Ok.place(x=900,y=70)
#submit player's name
q1 = 'P1'
q2 = 'P2'
def pn(x):
    global q1
    global q2
    global i
    q1 = n1.get()
    q2 = n2.get()
Ok.bind('<Button-1>',pn)
#Menu's Tabeh
def about(x):
    w = Tk()
    w.geometry('400x250')
    w.title('About')
    Lw0 = Label(w,text='M&P(CR7) version 1.0')
    Lw1 = Label(w,text='This Program is a Snakes and Ladders game but')
    Lw2 = Label(w,text='This is very very exactly')
    Lw3 = Label(w,text='in this game just have snake')
    Lw4 = Label(w,text='and there isnt any Ladder in this game')
    Lw5 = Label(w,text='You can change your name and')
    Lw6 = Label(w,text='you can just play multiplayer ')
    Lw7 = Label(w,text='this game created by Me(Sajad.Cr7)/Copyright@2015')
    Lw8 = Label(w,text='E-mail : sajadalipour1380@gmail.com')
    Lw9 = Label(w,text='Web-site : www.CR7group.blog.ir')
    Lw10 = Label(w,text='if you like this program follow my instagram : sajadalipourcr7')
    Lw0.pack()
    Lw1.pack()
    Lw2.pack()
    Lw3.pack()
    Lw4.pack()
    Lw5.pack()
    Lw6.pack()
    Lw7.pack()
    Lw8.pack()
    Lw9.pack()
    Lw10.pack()
def other(x):
    w2 = Tk()
    w2.geometry('250x100')
    w2.title('Other')
    Lw20 = Label(w2,text='My other program is :')
    Lw21 = Label(w2,text='Calculator(CR7)')
    Lw22 = Label(w2,text='You can get more information in my site :')
    Lw23 = Label(w2,text='www.CR7group.blog.ir')
    Lw20.pack()
    Lw21.pack()
    Lw22.pack()
    Lw23.pack()
def exi(x):
    a.destroy()
def pause(x):
    u2 = Tk()
    u2.geometry('400x400')
    u2.title('Pause')
    Lu = Label(u2,text = 'Pause Menu',font = ' thoma 20')
    Lu.place(x=130,y=10)
    Lu2 = Label(u2,text='Resume',font='thoma 25 bold',bg = 'yellow')
    Lu2.place(x=135,y=200)
    def resume(x):
        u2.destroy()
    Lu2.bind('<Button-1>',resume)
def setting(x):
    u3 = Tk()
    u3.geometry('400x400')
    u3.title('Setting')
    Lu_1 = Label(u3,text='Setting' , font='thoma 15',fg='black')
    Lu_1.place(x=170,y=10)
    Lu_2 = Label(u3,text='Set Background Color :' , font='thoma 10',fg='black')
    Lu_2.place(x=120,y=80)
    Lu_3 = Label(u3,text='Change Difficulty :',font='thoma 10',fg='black')
    Lu_3.place(x=120,y=180)
    Bu_1 = Button(u3,text='yellow',bg = 'yellow',fg='black',width='8')
    Bu_1.place(x=80,y=120)
    Bu_2 = Button(u3,text='orange',bg = 'orange',fg='black',width='8')
    Bu_2.place(x=160,y=120)
    Bu_3 = Button(u3,text='blue',bg = 'blue',fg='black',width='8')
    Bu_3.place(x=240,y=120)
    Bu_4 = Button(u3,text='Normal',width='8')
    Bu_4.place(x=160,y=220)
    Lu_5 = Label(u3,text='Cheat code :',font='thoma 10',fg='black')
    Lu_5.place(x=120,y=270)
    ent_1 = Entry(u3,bg='white')
    ent_1.place(x=120,y=300)
    B_ent = Button(u3,text='Ok',bg='black',fg='red')
    B_ent.place(x=280,y=300)
    Lu_6 = Label(u3,text='You Can Buy Cheat code in my site : ',fg='black')
    Lu_6.place(x=120,y=340)
    Lu_7 = Label(u3,text='WWW.CR7group.blog.ir',fg='black')
    Lu_7.place(x=120,y=365)
    def yellow(x):
        a.configure(background='yellow')
    def orange(x):
        a.configure(background='goldenrod')
    def blue(x):
        a.configure(background='blue')
    def cheat(x):
        q = ent_1.get()
        if q=='pioneer' or q=='PIONEER':
            u4=Tk()
            u4.geometry('350x100')
            u4.title('Cheat code')
            u4L0=Label(u4,text='This is correct !')
            u4L1=Label(u4,text='Now you can win the game everytime with this button !')
            u4L0.pack()
            u4L1.pack()
            u4b = Button(u4,text='Win',fg='green',bg='black')
            u4b.place(x=155 , y=60)
            def wi(x):
                u5=Tk()
                u5.geometry('100x100')
                u5L=Label(u5,text='You win!')
                u5L.pack()
            u4b.bind('<Button-1>',wi)
    B_ent.bind('<Button-1>',cheat)
    Bu_1.bind('<Button-1>',yellow)
    Bu_2.bind('<Button-1>',orange)
    Bu_3.bind('<Button-1>',blue)
def upto(x):
    u6 = Tk()
    u6.geometry('350x100')
    u6.title('Update')
    Lu6_0 = Label(u6,text = 'You Can get new updates of M&P(CR7) game in my site : ')
    Lu6_0.pack()
    Lu6_1 = Label(u6,text = 'WWW.CR7group.blog.ir ')
    Lu6_1.place(x=100,y=30)
def score(x):
    global I
    global I2
    Q = Tk()
    Q.geometry('300x200')
    Q.title('Scoreboard')
    Q.configure(background='cyan2')
    f1 = Label(Q,text=str(q1) + ' Wins ' + ' : ' + str(I),font='thoma 15',bg='cyan2')
    f2 = Label(Q,text=str(q2) + ' Wins ' + ' : ' + str(I2),font='thoma 15',bg='cyan2')
    f1.place(x=100,y=50)
    f2.place(x=100,y=100)
se.bind('<Button-1>',setting)
Pa.bind('<Button-1>',pause)
ab.bind('<Button-1>',about)
he.bind('<Button-1>',other)
ex.bind('<Button-1>',exi)
ap.bind('<Button-1>',upto)
sc.bind('<Button-1>',score)
#Main tavabeh
x_1 = 750
y_1=630
def Restart(x):
    R = Tk()
    R.geometry('250x100')
    R.title('Restart')
    Rt = Label(R,text='Are you sure want to restart the game?')
    Rt.pack()
    Rb = Button(R,text='Yes')
    Rn = Button(R,text='No')
    global T
    global T2
    def rb(x):
        a1.place(x = 750 , y = 630)
        a2.place(x = 780 , y = 630)
        global T
        global T2
        T2 = 1
        T = 1
        R.destroy()
    def rn(x):
        R.destroy()
    Rn.place(x=160,y=50)
    Rb.place(x=60,y=50)
    Rb.bind('<Button-1>',rb)
    Rn.bind('<Button-1>',rn)
Re.bind('<Button-1>',Restart)
def cl(x):
    global I
    global q1
    global q2
    global r
    global r2
    global r3
    global r4
    global i
    global x_1
    global y_1
    global T
    r = random()
    r2 = r * 5
    r3 = int(r2)
    r4 = r3+1
    time.sleep(0.2)
    #For restart
    if T == 1 :
        x_1 = 750
        y_1 = 630
        T = 0
    #For r4 == 1 P1
    if x_1<750 and y_1==30 and r4 == 1:
        x_1 = x_1 - r4*100
        if x_1 <= 50 and y_1 == 30:
            y = Tk()
            y.geometry('250x100')
            y.title('Win!')
            win = Label(y,text=str(q1) + ' win !')
            win.pack()
            win2 = Label(y,text='You can see score board in the menu')
            win2.pack()
            I = I + 1
    if x_1<750 and y_1==180 and r4 == 1:
        if x_1==650:
            y_1=y_1 - 150
            x_1 = x_1 - 100
        x_1 = x_1 + r4*100

    if x_1<750 and y_1==330 and r4 == 1:
        if x_1==50:
            y_1=y_1 - 150
            x_1 = x_1 + 100
        x_1 = x_1 - r4*100
    if x_1<750 and y_1==480 and r4 == 1:
        if x_1==650:
            y_1 = y_1-150
            x_1=x_1-100
        x_1 = x_1 + r4*100
    if x_1<=750 and y_1==630 and r4 == 1:
        if x_1==50:
            y_1 = y_1 - 150
            x_1=x_1+100
        x_1 = x_1 - r4*100
    #For r4 == 2 P1
    if x_1<750 and y_1==30 and r4 == 2:
        x_1 = x_1 - r4*100
        if x_1<=50  and y_1 == 30:
            y = Tk()
            y.geometry('250x100')
            y.title('Win!')
            win = Label(y,text=str(q1) + ' win !')
            win.pack()
            win2 = Label(y,text='You can see score board in the menu')
            win2.pack()
            I = I + 1
    if x_1 == 550 and y_1==180 and r4 == 2:
        x_1 = 650
        y_1 = y_1 - 150
    if x_1<750 and y_1==180 and r4 == 2:
        if x_1==650:
            y_1=y_1 - 150
            x_1 = x_1 - 300
        x_1 = x_1 + r4*100
    if x_1 == 50 and y_1==330 and r4 == 2:
        x_1 = 150
        y_1 = y_1 - 150
    if x_1<750 and y_1==330 and r4 == 2:
        if x_1==150:
            y_1=y_1 - 150
            x_1 = x_1 + 100
        x_1 = x_1 - r4*100
    if x_1 == 550 and y_1==480 and r4 == 2:
        x_1 = 650
        y_1 = y_1 - 150
    if x_1<750 and y_1==480 and r4 == 2:
        if x_1==650:
            y_1 = y_1-150
            x_1=x_1-300
        x_1 = x_1 + r4*100
    if x_1 == 50 and y_1==630 and r4 == 2:
        x_1 = 150
        y_1 = y_1 - 150
    if x_1<=750 and y_1==630 and r4 == 2 :
        if x_1==150:
            y_1 = y_1 - 150
            x_1=x_1+100
        x_1 = x_1 - r4*100
    #For r4 == 3 P1
    if x_1<750 and y_1==30 and r4 == 3:
        x_1 = x_1 - r4*100
        if x_1<=50  and y_1 == 30:
            y = Tk()
            y.geometry('250x100')
            y.title('Win!')
            win = Label(y,text=str(q1) + ' win !')
            win.pack()
            win2 = Label(y,text='You can see score board in the menu')
            win2.pack()
            I = I + 1
    if x_1 == 450 and y_1==180 and r4 == 3:
        x_1 = 650
        y_1 = y_1 - 150
    if x_1 == 650 and y_1==180 and r4 == 3:
        x_1 = 450
        y_1 = y_1 - 150
    if x_1<750 and y_1==180 and r4 == 3:
        if x_1==550:
            y_1=y_1 - 150
            x_1 = 250
        x_1 = x_1 + r4*100
    if x_1 == 150 and y_1==330 and r4 == 3:
        x_1 = 150
        y_1 = y_1 - 150
    if x_1 == 250 and y_1==330 and r4 == 3:
        x_1 = 50
        y_1 = y_1 - 150
    if x_1<750 and y_1==330 and r4 == 3:
        if x_1==50:
            y_1=y_1 - 150
            x_1 = 550
        x_1 = x_1 - r4*100
    if x_1 == 650 and y_1==480 and r4 == 3:
        x_1 = 450
        y_1 = y_1 - 150
    if x_1 == 550 and y_1==480 and r4 == 3:
        x_1 = 550
        y_1 = y_1 - 150
    if x_1<750 and y_1==480 and r4 == 3:
        if x_1==450:
            y_1 = y_1-150
            x_1=350
        x_1 = x_1 + r4*100
    if x_1 == 250 and y_1==630 and r4 == 3:
        x_1 = 50
        y_1 = y_1 - 150
    if x_1 == 50 and y_1==630 and r4 == 3:
        x_1 = 250
        y_1 = y_1 - 150
    if x_1<=750 and y_1==630 and r4 == 3 :
        if x_1==150:
            y_1 = y_1 - 150
            x_1 = 450
        x_1 = x_1 - r4*100
    #For r4 == 4 P1
    if x_1<750 and y_1==30 and r4 == 4:
        x_1 = x_1 - r4*100
        if x_1<=50  and y_1 == 30:
            y = Tk()
            y.geometry('250x100')
            y.title('Win!')
            win = Label(y,text=str(q1) + ' win !')
            win.pack()
            win2 = Label(y,text='You can see score board in the menu')
            win2.pack()
            I = I + 1
    if x_1==550 and y_1==180 and r4 == 4:
        x_1 = 450
        y_1 = y_1 - 150
    if x_1 == 450 and y_1==180 and r4 == 4:
        x_1 = 550
        y_1 = y_1 - 150
    if x_1 == 350 and y_1==180 and r4 == 4:
        x_1 = 650
        y_1 = y_1 - 150
    if x_1<750 and y_1==180 and r4 == 4:
        if x_1==650:
            y_1=y_1 - 150
            x_1 = -50
        x_1 = x_1 + r4*100
    if x_1==250 and y_1==330 and r4 == 4:
        x_1 = 150
        y_1 = y_1 - 150
    if x_1 == 350 and y_1==330 and r4 == 4:
        x_1 = 50
        y_1 = y_1 - 150
    if x_1 == 50 and y_1==330 and r4 == 4:
        x_1 = 350
        y_1 = y_1 - 150
    if x_1<750 and y_1==330 and r4 == 4:
        if x_1==150:
            y_1=y_1 - 150
            x_1 = 650
        x_1 = x_1 - r4*100
    if x_1==350 and y_1==480 and r4 == 4:
        x_1 = 650
        y_1 = y_1 - 150
    if x_1 == 650 and y_1==480 and r4 == 4:
        x_1 = 350
        y_1 = y_1 - 150
    if x_1 == 550 and y_1==480 and r4 == 4:
        x_1 = 450
        y_1 = y_1 - 150
    if x_1<750 and y_1==480 and r4 == 4:
        if x_1==450:
            y_1 = y_1-150
            x_1=150
        x_1 = x_1 + r4*100
    if x_1==50 and y_1==630 and r4 == 4:
        x_1 = 350
        y_1 = y_1 - 150
    if x_1 == 150 and y_1==630 and r4 == 4:
        x_1 = 250
        y_1 = y_1 - 150
    if x_1 == 250 and y_1==630 and r4 == 4:
        x_1 = 150
        y_1 = y_1 - 150
    if x_1<=750 and y_1==630 and r4 == 4 :
        if x_1==350:
            y_1 = y_1 - 150
            x_1 = 450
        x_1 = x_1 - r4*100
    #For r4 == 5 P1
    if x_1<750 and y_1==30 and r4 == 5:
        x_1 = x_1 - r4*100
        if x_1<=50  and y_1 == 30:
            y = Tk()
            y.geometry('250x100')
            y.title('Win!')
            win = Label(y,text=str(q1) + ' win !')
            win.pack()
            win2 = Label(y,text='You can see score board in the menu')
            win2.pack()
            I = I + 1
    if x_1==250 and y_1==180 and r4==5:
        x_1 = 650
        y_1 = y_1 - 150
    if x_1==650 and y_1==180 and r4 == 5:
        x_1 = 250
        y_1 = y_1 - 150
    if x_1 == 550 and y_1==180 and r4 == 5:
        x_1 = 350
        y_1 = y_1 - 150
    if x_1 == 450 and y_1==180 and r4 == 5:
        x_1 = 450
        y_1 = y_1 - 150
    if x_1<750 and y_1==180 and r4 == 5:
        if x_1==350:
            y_1=y_1 - 150
            x_1 = 50
        x_1 = x_1 + r4*100
    if x_1==250 and y_1==330 and r4==5:
        x_1 = 250
        y_1 = y_1 - 150
    if x_1==350 and y_1==330 and r4 == 5:
        x_1 = 150
        y_1 = y_1 - 150
    if x_1 == 450 and y_1==330 and r4 == 5:
        x_1 = 50
        y_1 = y_1 - 150
    if x_1 == 50 and y_1==330 and r4 == 5:
        x_1 = 450
        y_1 = y_1 - 150
    if x_1<750 and y_1==330 and r4 == 5:
        if x_1==150:
            y_1=y_1 - 150
            x_1 = 850
        x_1 = x_1 - r4*100
    if x_1==650 and y_1 == 480 and r4==5:
        x_1 = 250
        y_1 = y_1 - 150
    if x_1==550 and y_1==480 and r4 == 5:
        x_1 = 350
        y_1 = y_1 - 150
    if x_1 == 450 and y_1==480 and r4 == 5:
        x_1 = 450
        y_1 = y_1 - 150
    if x_1 == 350 and y_1==480 and r4 == 5:
        x_1 = 550
        y_1 = y_1 - 150
    if x_1<750 and y_1==480 and r4 == 5:
        if x_1==250:
            y_1 = y_1-150
            x_1=150
        x_1 = x_1 + r4*100
    if x_1==350 and y_1==630 and r4==5:
        x_1 = 150
        y_1 = y_1 - 150
    if x_1==450 and y_1==630 and r4 == 5:
        x_1 = 50
        y_1 = y_1 - 150
    if x_1 == 50 and y_1==630 and r4 == 5:
        x_1 = 450
        y_1 = y_1 - 150
    if x_1 == 150 and y_1==630 and r4 == 5:
        x_1 = 350
        y_1 = y_1 - 150
    if x_1<=750 and y_1==630 and r4 == 5 :
        if x_1==250:
            y_1 = y_1 - 150
            x_1 = 750
        x_1 = x_1 - r4*100
    #For snakes
    #snake 1
    if x_1==250 and y_1==330:
        time.sleep(0.5)
        x_1 = 150
        y_1 = 630
    #snake 2
    if x_1==550 and y_1 == 180:
        time.sleep(0.5)
        x_1 = 550
        y_1 = 480
    #snake 3
    if x_1==250 and y_1==30:
        time.sleep(0.5)
        x_1 = 250
        y_1 = 180
    #snake 4
    if x_1 == 650 and y_1==30:
        time.sleep(0.5)
        x_1 = 650
        y_1=630
    #For Change the turn
    a1.place(x=x_1,y=y_1)
    A1 = Label(a,text=str(q2) + ' it is your turn ',fg='black',bg='goldenrod')
    A1.place(x=50,y=10)
    tas02 = Label(a,text=r4,bg='goldenrod')
    tas02.place(x=860,y=680)
x_2 = 780
y_2 = 630
def cl2(x):
    global I2
    global q1
    global q2
    global r_
    global r_2
    global r_3
    global r_4
    global i
    global x_2
    global y_2
    global T2
    r_ = random()
    r_2 = r_ * 5
    r_3 = int(r_2)
    r_4 = r_3+1
    time.sleep(0.2)
    #For restart
    if T2 == 1 :
        x_2 = 780
        y_2 = 630
        T2 = 2
    #For r_4 == 1 P2
    if x_2<780 and y_2==30 and r_4 == 1:
        x_2 = x_2 - r_4*100
        if x_2 <= 80 and y_2 == 30:
            y = Tk()
            y.geometry('250x100')
            y.title('Win!')
            win = Label(y,text=str(q1) + ' win !')
            win.pack()
            win2 = Label(y,text='You can see score board in the menu')
            win2.pack()
            I2 = I2 + 1
    if x_2<780 and y_2==180 and r_4 == 1:
        if x_2==680:
            y_2=y_2 - 150
            x_2 = x_2 - 100
        x_2 = x_2 + r_4*100

    if x_2<780 and y_2==330 and r_4 == 1:
        if x_2==80:
            y_2=y_2 - 150
            x_2 = x_2 + 100
        x_2 = x_2 - r_4*100
    if x_2<780 and y_2==480 and r_4 == 1:
        if x_2==680:
            y_2 = y_2-150
            x_2=x_2-100
        x_2 = x_2 + r_4*100
    if x_2<=780 and y_2==630 and r_4 == 1:
        if x_2==80:
            y_2 = y_2 - 150
            x_2=x_2+100
        x_2 = x_2 - r_4*100
    #For r_4 == 2 P2
    if x_2<780 and y_2==30 and r_4 == 2:
        x_2 = x_2 - r_4*100
        if x_2<=80  and y_2 == 30:
            y = Tk()
            y.geometry('250x100')
            y.title('Win!')
            win = Label(y,text=str(q1) + ' win !')
            win.pack()
            win2 = Label(y,text='You can see score board in the menu')
            win2.pack()
            I2 = I2 + 1
    if x_2 == 580 and y_2==180 and r_4 == 2:
        x_2 = 680
        y_2 = y_2 - 150
    if x_2<780 and y_2==180 and r_4 == 2:
        if x_2==680:
            y_2=y_2 - 150
            x_2 = x_2 - 300
        x_2 = x_2 + r_4*100
    if x_2 == 80 and y_2==330 and r_4 == 2:
        x_2 = 180
        y_2 = y_2 - 150
    if x_2<780 and y_2==330 and r_4 == 2:
        if x_2==180:
            y_2=y_2 - 150
            x_2 = x_2 + 100
        x_2 = x_2 - r_4*100
    if x_2 == 580 and y_2==480 and r_4 == 2:
        x_2 = 680
        y_2 = y_2 - 150
    if x_2<780 and y_2==480 and r_4 == 2:
        if x_2==680:
            y_2 = y_2-150
            x_2=x_2-300
        x_2 = x_2 + r_4*100
    if x_2 == 80 and y_2==630 and r_4 == 2:
        x_2 = 180
        y_2 = y_2 - 150
    if x_2<=780 and y_2==630 and r_4 == 2 :
        if x_2==180:
            y_2 = y_2 - 150
            x_2=x_2+100
        x_2 = x_2 - r_4*100
    #For r_4 == 3 P2
    if x_2<780 and y_2==30 and r_4 == 3:
        x_2 = x_2 - r_4*100
        if x_2<=80  and y_2 == 30:
            y = Tk()
            y.geometry('250x100')
            y.title('Win!')
            win = Label(y,text=str(q1) + ' win !')
            win.pack()
            win2 = Label(y,text='You can see score board in the menu')
            win2.pack()
            I2 = I2 + 1
    if x_2 == 480 and y_2==180 and r_4 == 3:
        x_2 = 680
        y_2 = y_2 - 150
    if x_2 == 680 and y_2==180 and r_4 == 3:
        x_2 = 480
        y_2 = y_2 - 150
    if x_2<780 and y_2==180 and r_4 == 3:
        if x_2==580:
            y_2=y_2 - 150
            x_2 = 280
        x_2 = x_2 + r_4*100
    if x_2 == 180 and y_2==330 and r_4 == 3:
        x_2 = 180
        y_2 = y_2 - 150
    if x_2 == 280 and y_2==330 and r_4 == 3:
        x_2 = 80
        y_2 = y_2 - 150
    if x_2<780 and y_2==330 and r_4 == 3:
        if x_2==80:
            y_2=y_2 - 150
            x_2 = 580
        x_2 = x_2 - r_4*100
    if x_2 == 680 and y_2==480 and r_4 == 3:
        x_2 = 480
        y_2 = y_2 - 150
    if x_2 == 580 and y_2==480 and r_4 == 3:
        x_2 = 580
        y_2 = y_2 - 150
    if x_2<780 and y_2==480 and r_4 == 3:
        if x_2==480:
            y_2 = y_2-150
            x_2=380
        x_2 = x_2 + r_4*100
    if x_2 == 280 and y_2==630 and r_4 == 3:
        x_2 = 80
        y_2 = y_2 - 150
    if x_2 == 80 and y_2==630 and r_4 == 3:
        x_2 = 280
        y_2 = y_2 - 150
    if x_2<=780 and y_2==630 and r_4 == 3 :
        if x_2==180:
            y_2 = y_2 - 150
            x_2 = 480
        x_2 = x_2 - r_4*100
    #For r_4 == 4 P2
    if x_2<780 and y_2==30 and r_4 == 4:
        x_2 = x_2 - r_4*100
        if x_2<=80  and y_2 == 30:
            y = Tk()
            y.geometry('250x100')
            y.title('Win!')
            win = Label(y,text=str(q1) + ' win !')
            win.pack()
            win2 = Label(y,text='You can see score board in the menu')
            win2.pack()
            I2 = I2 + 1
    if x_2==580 and y_2==180 and r_4 == 4:
        x_2 = 480
        y_2 = y_2 - 150
    if x_2 == 480 and y_2==180 and r_4 == 4:
        x_2 = 580
        y_2 = y_2 - 150
    if x_2 == 380 and y_2==180 and r_4 == 4:
        x_2 = 680
        y_2 = y_2 - 150
    if x_2<780 and y_2==180 and r_4 == 4:
        if x_2==680:
            y_2=y_2 - 150
            x_2 = -20
        x_2 = x_2 + r_4*100
    if x_2==280 and y_2==330 and r_4 == 4:
        x_2 = 180
        y_2 = y_2 - 150
    if x_2 == 380 and y_2==330 and r_4 == 4:
        x_2 = 80
        y_2 = y_2 - 150
    if x_2 == 80 and y_2==330 and r_4 == 4:
        x_2 = 380
        y_2 = y_2 - 150
    if x_2<780 and y_2==330 and r_4 == 4:
        if x_2==180:
            y_2=y_2 - 150
            x_2 = 680
        x_2 = x_2 - r_4*100
    if x_2==380 and y_2==480 and r_4 == 4:
        x_2 = 680
        y_2 = y_2 - 150
    if x_2 == 680 and y_2==480 and r_4 == 4:
        x_2 = 380
        y_2 = y_2 - 150
    if x_2 == 580 and y_2==480 and r_4 == 4:
        x_2 = 480
        y_2 = y_2 - 150
    if x_2<780 and y_2==480 and r_4 == 4:
        if x_2==480:
            y_2 = y_2-150
            x_2=180
        x_2 = x_2 + r_4*100
    if x_2==80 and y_2==630 and r_4 == 4:
        x_2 = 380
        y_2 = y_2 - 150
    if x_2 == 180 and y_2==630 and r_4 == 4:
        x_2 = 280
        y_2 = y_2 - 150
    if x_2 == 280 and y_2==630 and r_4 == 4:
        x_2 = 180
        y_2 = y_2 - 150
    if x_2<=780 and y_2==630 and r_4 == 4 :
        if x_2==380:
            y_2 = y_2 - 150
            x_2 = 480
        x_2 = x_2 - r_4*100
    #For r_4 == 5 P2
    if x_2<780 and y_2==30 and r_4 == 5:
        x_2 = x_2 - r_4*100
        if x_2<=80  and y_2 == 30:
            y = Tk()
            y.geometry('250x100')
            y.title('Win!')
            win = Label(y,text=str(q1) + ' win !')
            win.pack()
            win2 = Label(y,text='You can see score board in the menu')
            win2.pack()
            I2 = I2 + 1
    if x_2==280 and y_2==180 and r_4==5:
        x_2 = 680
        y_2 = y_2 - 150
    if x_2==680 and y_2==180 and r_4 == 5:
        x_2 = 280
        y_2 = y_2 - 150
    if x_2 == 580 and y_2==180 and r_4 == 5:
        x_2 = 380
        y_2 = y_2 - 150
    if x_2 == 480 and y_2==180 and r_4 == 5:
        x_2 = 480
        y_2 = y_2 - 150
    if x_2<780 and y_2==180 and r_4 == 5:
        if x_2==380:
            y_2=y_2 - 150
            x_2 = 80
        x_2 = x_2 + r_4*100
    if x_2==280 and y_2==330 and r_4==5:
        x_2 = 280
        y_2 = y_2 - 150
    if x_2==380 and y_2==330 and r_4 == 5:
        x_2 = 180
        y_2 = y_2 - 150
    if x_2 == 480 and y_2==330 and r_4 == 5:
        x_2 = 80
        y_2 = y_2 - 150
    if x_2 == 80 and y_2==330 and r_4 == 5:
        x_2 = 480
        y_2 = y_2 - 150
    if x_2<780 and y_2==330 and r_4 == 5:
        if x_2==180:
            y_2=y_2 - 150
            x_2 = 880
        x_2 = x_2 - r_4*100
    if x_2==680 and y_2 == 480 and r_4==5:
        x_2 = 280
        y_2 = y_2 - 150
    if x_2==580 and y_2==480 and r_4 == 5:
        x_2 = 380
        y_2 = y_2 - 150
    if x_2 == 480 and y_2==480 and r_4 == 5:
        x_2 = 480
        y_2 = y_2 - 150
    if x_2 == 380 and y_2==480 and r_4 == 5:
        x_2 = 580
        y_2 = y_2 - 150
    if x_2<780 and y_2==480 and r_4 == 5:
        if x_2==280:
            y_2 = y_2-150
            x_2=180
        x_2 = x_2 + r_4*100
    if x_2==380 and y_2==630 and r_4==5:
        x_2 = 180
        y_2 = y_2 - 150
    if x_2==480 and y_2==630 and r_4 == 5:
        x_2 = 80
        y_2 = y_2 - 150
    if x_2 == 80 and y_2==630 and r_4 == 5:
        x_2 = 480
        y_2 = y_2 - 150
    if x_2 == 180 and y_2==630 and r_4 == 5:
        x_2 = 380
        y_2 = y_2 - 150
    if x_2<=780 and y_2==630 and r_4 == 5 :
        if x_2==280:
            y_2 = y_2 - 150
            x_2 = 780
        x_2 = x_2 - r_4*100
    #For snakes
    #snake 1
    if x_2==280 and y_2==330:
        time.sleep(0.5)
        x_2 = 180
        y_2 = 630
    #snake 2
    if x_2==580 and y_2 == 180:
        time.sleep(0.5)
        x_2 = 580
        y_2 = 480
    #snake 3
    if x_2==280 and y_2==30:
        time.sleep(0.5)
        x_2 = 280
        y_2 = 180
    #snake 4
    if x_2 == 680 and y_2==30:
        time.sleep(0.5)
        x_2 = 680
        y_2=630
    #For Change the turn
    a2.place(x=x_2,y=y_2)
    A2 = Label(a,text=str(q1) + ' it is your turn ',fg='black',bg='goldenrod')
    A2.place(x=50,y=10)
    tas_2 = Label(a,text=r_4,bg='goldenrod')
    tas_2.place(x=960,y=680)
tas.bind('<Button-1>',cl)
tas2.bind('<Button-1>',cl2)
a.mainloop()
