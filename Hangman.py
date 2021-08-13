#Hangman
from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox as mb
root=Tk()
root.title("Hangman")

def firstscreen():
    global first,picture
    first=Canvas(root,width=1200,height=700)
    first.pack()
    hang=Image.open('frontpage.jpg')
    hang=hang.resize((1200,700),Image.ANTIALIAS)
    picture=ImageTk.PhotoImage(hang)
    first.create_image(0,0,anchor=NW,image=picture)
    first.create_text(800,180,text="Hangman",fill="white",font=('century schoolbook',60,'bold'),tag='heading')
    first.create_text(1000,670,text="Pooja Premnath",fill="white",font=('century schoolbook',15,'bold'),tag='heading')
    play= Button(text='Play', command=change, bg='azure', fg='black', font=('century schoolbook', 11,'bold'))
    play.config(height=2,width=25)
    first.create_window(800,350, window=play)
    ending= Button(text='Quit', command=end, bg='azure', fg='black', font=('century schoolbook', 11,'bold'))
    ending.config(height=2,width=25)
    first.create_window(800,430, window=ending)
    
def screen():
    global canvas,pic,letter,submit,homepic,word,wordlength
    canvas=Canvas(root,width=1200,height=700)
    canvas.pack()
    image=Image.open('bg2.jpg')
    image=image.resize((1200,700),Image.ANTIALIAS)
    pic=ImageTk.PhotoImage(image)
    canvas.create_image(0,0,anchor=NW,image=pic)
    home=Image.open('home.png')
    home=home.resize((50,50),Image.ANTIALIAS)
    homepic=ImageTk.PhotoImage(home)
    homebtn= Button(command=gametohomescreen,image=homepic)
    homebtn.config(height=40,width=40)
    canvas.create_window(40,40, window=homebtn)
    f=open('hangman_words.txt','r')
    lines=f.readlines()
    word=random.choice(lines)
    print(word)
    wordlength=len(word)
    x=100
    for i in range(wordlength-1):
        canvas.create_line(x,490,x+40,490,width=5)
        x+=60
    B = Label(root, text="Guessed Alphabets", width=44,height=1, borderwidth=3, relief="solid",font=('century schoolbook',30,'bold'))
    B.pack()
    canvas.create_window(600,540,window=B)
    canvas.create_text(160,595,text="Incorrect Guesses:",fill="black",font=('century schoolbook',20,'bold'))
    canvas.create_polygon(300,580,380,580,380,610,300,610,fill='red2')
    canvas.create_text(650,595,text="Correct Guesses:",fill="black",font=('century schoolbook',20,'bold'))
    canvas.create_polygon(800,580,880,580,880,610,800,610,fill='black')
    canvas.create_text(600,50,text="Hangman",fill="black",font=('century schoolbook',60,'bold'))
    canvas.create_text(600,110,text="Try to find the word, by guessing alphabets. For every wrong alphabet, a body part is added to the gallows.",fill='firebrick1',font=('century schoolbook',15,'bold'))
    canvas.create_text(600,140,text="You have 10 tries, before the man is hung.",fill='firebrick1',font=('century schoolbook',15,'bold'))
    canvas.create_line(1000,200,1100,200,width=3)
    canvas.create_line(1000,200,1000,240,width=3)
    canvas.create_line(1100,200,1100,420,width=3)
    canvas.create_line(1080,420,1120,420,width=3)
    canvas.create_line(980,240,1020,240,width=3)
    canvas.create_text(200,250,text="Enter a letter",font=('century schoolbook',30,'bold'))
    letter=Entry(root,font="Calibri 30")
    letter.configure(width=5)
    canvas.create_window(400,250,window=letter)
    submit= Button(text='Submit', command=gameplay, bg='azure', fg='black', font=('century schoolbook', 11,'bold'))
    submit.config(height=2,width=15)
    canvas.create_window(550,250, window=submit)
    
    
def hangman_body():
    global canvas,attempt
    if attempt==1:
        canvas.create_oval(975,240,1025,300,width=3)
    if attempt==2:
        canvas.create_line(1000,300,1000,380,width=3)
    if attempt==3:
        canvas.create_line(1000,380,960,430,width=3)
    if attempt==4:
        canvas.create_line(1000,380,1040,430,width=3)
    if attempt==5:
        canvas.create_line(1000,340,1040,320,width=3)
    if attempt==6:
        canvas.create_line(1000,340,960,320,width=3)
    if attempt==7:
        canvas.create_oval(990,265,994,269,fill='black')
    if attempt==8:
        canvas.create_oval(1005,265,1009,269,fill='black')
    if attempt==9:
        canvas.create_polygon(1000,270,994,275,1006,275,width=3)
    if attempt==10:
        canvas.create_line(994,285,1006,285,width=2)
        submit= Button(text='Submit', command=gameplay, bg='azure', fg='black', font=('century schoolbook', 11,'bold'),state=DISABLED)
        submit.config(height=2,width=15)
        canvas.create_window(550,250, window=submit)
        canvas.create_text(370,340,text="You've run out of chances.",fill="Red",font=('Lucida Handwriting',20,'bold'),tag='loser')
        canvas.create_text(370,380,text="Better luck next time!",fill="Red",font=('Lucida Handwriting',20,'bold'),tag='loser')
        canvas.delete('present')
        canvas.delete('invalid')
        playagain= Button(text='Play Again', command=reload, bg='SlateBlue2', fg='white', font=('century schoolbook', 11,'bold'))
        playagain.config(height=2,width=15)
        canvas.create_window(1050,600, window=playagain)
        quitgame= Button(text='Quit', command=mb, bg='SlateBlue2', fg='white', font=('century schoolbook', 11,'bold'))
        quitgame.config(height=2,width=15)
        canvas.create_window(1050,670, window=quitgame)  
        
def gameplay():
    global canvas,wordlength,word,letter,attempt,alphabetlist,length
    alphabet=letter.get()
    if alphabet.isalpha()==False:
        canvas.delete('present')
        canvas.delete('invalid')
        canvas.create_text(350,320,text="Invalid Input,Try Again",fill="purple1",font=('century schoolbook',20,'bold'),tag='invalid')
    elif len(alphabet)>1:
        canvas.delete('present')
        canvas.delete('invalid')
        canvas.create_text(350,320,text="Invalid Input,Try Again",fill="purple1",font=('century schoolbook',20,'bold'),tag='invalid')
    else:
        if alphabet in alphabetlist:
            canvas.delete('invalid')
            canvas.create_text(350,320,text="You've already guessed this alphabet.",fill="purple1",font=('century schoolbook',20,'bold'),tag='present')
           
        else:
            canvas.delete('invalid')
            canvas.delete('present')
            alphabetlist.append(alphabet)
            
            if alphabet in word:
                for j in range(len(word)):
                    if word[j]==alphabet:
                        k,v=d.get(j)
                        canvas.create_text(k,v,text=word[j],fill="navy",font=('century schoolbook',30,'bold'),tag='alpha')
                        length+=1
                    if length==wordlength-1:
                        win()
                        break        
            else:
                attempt+=1
                hangman_body()                    
    xl=120
    for i in alphabetlist:
        if i in word:
            canvas.create_text(xl,650,text=i.upper(),fill="black",font=('century schoolbook',20,'bold'),tag='blank')
        else:
            canvas.create_text(xl,650,text=i.upper(),fill="red",font=('century schoolbook',20,'bold'),tag='blank')

        xl+=40    
    letter.delete(0,END)
    
def win():
    global canvas,submit
    print('word found')
    submit= Button(text='Submit', command=gameplay, bg='azure', fg='black', font=('century schoolbook', 11,'bold'),state=DISABLED)
    submit.config(height=2,width=15)
    canvas.create_window(550,250, window=submit)
    canvas.delete('present')
    canvas.delete('invalid')
    canvas.create_text(370,340,text="You Win!",fill="magenta2",font=('Lucida Handwriting',60,'bold'),tag='winner')
    playagain= Button(text='Play Again', command=reload, bg='SlateBlue2', fg='white', font=('century schoolbook', 11,'bold'))
    playagain.config(height=2,width=15)
    canvas.create_window(1050,600, window=playagain)
    quitgame= Button(text='Quit', command=end, bg='SlateBlue2', fg='white', font=('century schoolbook', 11,'bold'))
    quitgame.config(height=2,width=15)
    canvas.create_window(1050,670, window=quitgame)  

def reload():
    global length, alphabetlist,attempt
    canvas.delete('blank')
    canvas.delete('present')
    canvas.delete('invalid')
    canvas.delete('alpha')
    canvas.delete('loser')
    canvas.pack_forget()
    length=0
    alphabetlist=[]
    attempt=0
    screen()
    
    
def end():
    if mb.askyesno('Quit Game','Do you really want to quit the game?'):
        root.destroy()

def change():
    first.pack_forget()
    screen()

def gametohomescreen():
    if mb.askyesno('Home Screen','Do you want to go back to the Home Screen? Your progress will be lost'):
        global length, alphabetlist,attempt
        canvas.delete('blank')
        canvas.delete('present')
        canvas.delete('invalid')
        canvas.delete('alpha')
        canvas.delete('loser')
        canvas.pack_forget()
        length=0
        alphabetlist=[]
        attempt=0
        firstscreen()
d={}
xcoordinate=120
ycoordinate=465
for i in range(0,15):
    d[i]=(xcoordinate,ycoordinate)
    xcoordinate+=60
firstscreen()
length=0
alphabetlist=[]
attempt=0
