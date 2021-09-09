import tkinter as tk
from tkinter import *
from response import bot_name, response
from os import sys
import os
import tkinter
from tkinter import font
from tkinter.font import BOLD
from PIL import ImageTk, Image
from tkinter import messagebox
import pyttsx3


engine = pyttsx3.init()

a = None
def bot():
    BG_GRAY = "#ABB2B9"
    BG_COLOR = "#17202A"
    TEXT_COLOR = "#EAECEE"

    FONT = "Helvetica 14"
    FONT_BOLD = "Helvetica 13 bold"
    class ChatApplication:
        def __init__(self):
            self.window = Tk()
            self._setup_main_window()

        def run(self):
            self.window.mainloop()

        def _setup_main_window(self):
            
            self.window.title("KlayBot")
            self.window.resizable(width=False, height=False)
            self.window.configure(width=1300, height=650, bg= "#1e1e1e")
            
            # head label
            head_label = Label(self.window, bg="#1e1e1e",anchor='w',justify="left", fg=TEXT_COLOR,text="Klay: Hello " + contents +", I am KlayBot and I have skills and capabilities to help make you feel better.\nPress OK to continue...", font=("Courier New", 14))
            head_label.pack()
            head_label.place(x=0, y = 10)
            

            

            # tiny divider
            #line = Label(self.window, width=50, bg=BG_GRAY)
            #line.place(relwidth=1, rely=0.07, relheight=0.012)

            # text widget
            self.text_widget = Text(self.window, width=20, height=2, bg="#1e1e1e", fg=TEXT_COLOR,
                                    font=FONT, padx=5, pady=5)
            self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
            self.text_widget.configure(cursor="arrow", state=DISABLED, insertbackground="red")

            # scroll bar
            scrollbar = Scrollbar(self.text_widget)
            scrollbar.place(relheight=1, relx=0.984)
            scrollbar.configure(command=self.text_widget.yview, background='#36393f')

            # bottom label
            bottom_label = Label(self.window, bg="#252526", height=80)
            bottom_label.place(relwidth=1, rely=0.825)
                
            # message entry box
            self.msg_entry = Entry(bottom_label, bg="#36393f", fg=TEXT_COLOR, font=FONT)
            self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
            self.msg_entry.focus()
            self.msg_entry.bind("<Return>", self._on_enter_pressed)

            # send button
            send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                                command=lambda: self._on_enter_pressed(NONE))
            send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

        def _on_enter_pressed(self, event):
            msg = self.msg_entry.get()
            self._insert_message(msg, "You")

        def _insert_message(self, msg, sender):
            global a
            if not msg:
                return
            if msg == "discard":
                a=msg
            if "bye" in msg.lower():
                if a == "discard":
                    
                    os.remove('Transcript.txt')
                sys.exit()   
            content = response(msg)
            self.msg_entry.delete(0, END)
            msg1 = f"{sender}: {msg}\n\n"
            self.text_widget.configure(cursor="arrow", state=NORMAL, wrap=WORD)
            self.text_widget.insert(END, msg1)
            self.text_widget.configure(cursor="arrow", state=DISABLED, wrap=WORD)
            
            
            
            
            msg2 = f"{bot_name}: {content}\n\n"
            self.text_widget.configure(cursor="arrow", state=NORMAL)
            
            self.text_widget.insert(END, msg2)
            self.text_widget.configure(cursor="arrow", state=DISABLED)

            self.text_widget.see(END)
            message = msg1 +"\n"+msg2
            
            with open("Transcript.txt","a") as file:
                file.write(message)
            
            
         

    if __name__ == "__main__":
        app = ChatApplication()
    app.run()

def voicebot(x):
    BG_GRAY = "#ABB2B9"
    BG_COLOR = "#17202A"
    TEXT_COLOR = "#EAECEE"
    FONT = "Helvetica 14"
    FONT_BOLD = "Helvetica 13 bold"
    class ChatApplication:
        def __init__(self):
            self.window = Tk()
            self._setup_main_window()

        def run(self):
            self.window.mainloop()

        def _setup_main_window(self):
            self.window.title("KlayBot")
            self.window.resizable(width=False, height=False)
            self.window.configure(width=1300, height=650, bg="#1e1e1e")
            head_label = Label(self.window, bg="#1e1e1e",anchor='w',justify="left", fg=TEXT_COLOR,text="Klay: Hello " + contents +",I am KlayBot and I have skills and capabilities to help you make you feel better.\nPress OK to continue...", font=("Courier New", 14))
            head_label.pack()
            head_label.place(x=0, y = 10)

            # tiny divider
            #line = Label(self.window, width=50, bg=BG_GRAY)
            #line.place(relwidth=1, rely=0.07, relheight=0.012)


            # text widget
            self.text_widget = Text(self.window, width=20, height=2,fg=TEXT_COLOR,bg="#1e1e1e",
                                    font=FONT, padx=5, pady=5)
            self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
            self.text_widget.configure(cursor="arrow", state=DISABLED)

            # scroll bar
            scrollbar = Scrollbar(self.text_widget)
            scrollbar.place(relheight=1, relx=0.984)
            scrollbar.configure(command=self.text_widget.yview, background='#36393f')

            # bottom label
            bottom_label = Label(self.window, bg="#252526", height=80)
            bottom_label.place(relwidth=1, rely=0.825)
                
            # message entry box
            self.msg_entry = Entry(bottom_label, bg="#36393f", fg=TEXT_COLOR, font=FONT)
            self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
            self.msg_entry.focus()
            self.msg_entry.bind("<Return>", self._on_enter_pressed)

            # send button
            send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                                command=lambda: self._on_enter_pressed(NONE))
            send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

        def _on_enter_pressed(self, event):
            msg = self.msg_entry.get()
            self._insert_message(msg, "You")

        def _insert_message(self, msg, sender):
            global a
            if not msg:
                return
            if msg == "discard":
                a=msg
            if "bye" in msg.lower():
                if a == "discard":
                    
                    os.remove('Transcript.txt') 
                sys.exit()   
            content = response(msg)
            self.msg_entry.delete(0, END)
            msg1 = f"{sender}: {msg}\n\n"
            self.text_widget.configure(cursor="arrow", state=NORMAL)
            self.text_widget.insert(END, msg1)
            self.text_widget.configure(cursor="arrow", state=DISABLED)
            
            
            
            
            msg2 = f"{bot_name}: {content}\n\n"
            self.text_widget.configure(cursor="arrow", state=NORMAL)
            self.text_widget.insert(END, msg2)
            self.text_widget.configure(cursor="arrow", state=DISABLED)

            self.text_widget.see(END)
            message = msg1 +"\n"+msg2
            
            with open("Transcript.txt","a") as file:
                file.write(message)
            
            rate = engine.getProperty('rate')
            voices = engine.getProperty('voices')
            engine.setProperty('rate', 175)
            engine.setProperty('voice', voices[x].id)
            
            engine.say(content)
            engine.runAndWait()
            engine.stop()

            

    if __name__ == "__main__":
        app = ChatApplication()
    app.run()
    
def voice_final():
    male = (f"{male_value.get()}")
    female = (f"{female_value.get()}")
    print("Happy conversation! Just remember, my devs are always with you, headover to discord.gg/klayspg")
    with open("./vars/male.txt","w") as m:
        m.write(male)
    with open("./vars/female.txt","w") as f:
        f.write(female)
    male_file = open("./vars/male.txt")
    male_file_no = male_file.read()
    male_file = int(male_file_no)
    female_file = open("./vars/female.txt")
    female_file_no = female_file.read()
    female_file = int(female_file_no)
    if male_file == 1 and female_file == 0:
        voicebot(2)
        # rate = engine.getProperty('rate')
        # voices = engine.getProperty('voices')
        # engine.setProperty('rate', 175)
        # engine.setProperty('voice', voices[0].id)
            
        # engine.say("Klay: Hello,"+contents+" I am KlayBot and I have skills and capabilities to help make you feel better.\nPress OK to continue...")
        
        # engine.stop()

    if male_file == 0 and female_file == 1:
        voicebot(1)
        # rate = engine.getProperty('rate')
        # voices = engine.getProperty('voices')
        # engine.setProperty('rate', 175)
        # engine.setProperty('voice', voices[1].id)
            
        # engine.say("Klay: Hello,"+contents+" I am KlayBot and I have skills and capabilities to help make you feel better.\nPress OK to continue...")
        # engine.stop()
    if male_file == 0 and female_file == 0:
        messagebox.showerror('Choice error', 'Hey, choose atleast one type of voice ( ͡° ͜ʖ ͡°)')    
    if male_file == 1 and female_file == 1:
        messagebox.showerror('Choice error', 'Hey, choose at max one type of voice ( ͡° ͜ʖ ͡°)')    


def voice_choice():
    global male_value
    global female_value
    
    mywindow = Toplevel()

    mywindow.title("Voice type")
    mywindow.geometry("450x150")
    mywindow.resizable(False,False)

    male_value = IntVar()
    female_value = IntVar()
    

    title=Label(mywindow,text="Please choice voice type:",font=("Terminal",15),fg="#C85417").place(x=80,y=20)
    male_check = Checkbutton(mywindow, text="Male",font=("Terminal", 13), height=2, width = 10,variable=male_value)
    
    male_check.place(x=60, y= 60)
    female_check = Checkbutton(mywindow, text="Female",font=("Terminal", 13), height=2, width = 10,variable=female_value)
    female_check.place(x=220, y= 60)
    submit_button=Button(mywindow, text="Submit",fg="black",font=("Courier New",18),command=voice_final).place(x=160,y=100)
    
    
    mywindow.mainloop()


    

def getvals():
    global contents
    name = (f"{namevalue.get()} ")
    age = (f"{agevalue.get()} ")
    ver = (f"{verificationvalue.get()}")
    voice = (f"{voicevalue.get()}")
    text = (f"{textvalue.get()}")
    with open("./vars/ver.txt", "w") as i:
        i.write(ver)
    with open("./assets/age.txt", "w") as f:
        f.write(age)
    with open("./assets/name.txt","w") as n:
        n.write(name)
    with open("./vars/voice.txt","w") as n:
        n.write(voice)
    with open("./assets/text.txt","w") as n:
        n.write(text)
    file = open("./assets/age.txt")
    file = file.read()
    try:
        file = int(file)
    except:
        messagebox.showerror('Type error', 'Breh, Age is a number!')
    folder = open("./vars/ver.txt")
    folder = folder.read()
    folder = int(folder)
    v = open("./vars/voice.txt")
    v = v.read()
    v = int(v)
    t = open("./assets/text.txt")
    t = t.read()
    t = int(t)
    f = open("./assets/name.txt")
    contents = f.read()
    if file >= 15 and file <= 25 and folder == 1:
        if t == 1 and v == 0:
            bot()
        elif t ==0 and v == 1:
            voice_choice()
        else:
            messagebox.showerror('Choice error', 'Hey! Choose either of the ways you wanna comunicate :/')
    if folder != 1:
        messagebox.showerror('Error', 'Please accept the T&C to continue...')

    if file < 15 or file > 25:
        messagebox.showerror('Age error', 'We currently dont support age groups more than 25 or under 15.')

class Login:
    def __init__(self,root):
        global namevalue
        global agevalue
        global verificationvalue
        global voicevalue
        global textvalue
        self.root=root
        self.root.title("Klay Bot")
        self.root.geometry("1068x600+100+50")
        self.root.resizable(False,False)

        image1 = Image.open("./assets/bg3.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test)
        label1.image = test

        
        
    # Position image
        label1.place(x=450, y=-175)
        

        FONT_BOLD = "Helvetica 13 bold"
        FONT = "Helvetica 14"
        
        
    #Frame
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=0,y=0,height=1200,width=500)


        namevalue = StringVar()
        agevalue = StringVar()
        verificationvalue = IntVar()
        textvalue = IntVar()
        voicevalue = IntVar()
     
    #Warning
        title=Label(Frame_login,text="Klaybot",font=("Terminal",35),fg="#C85417",bg="white").place(x=130,y=50)
        title=Label(Frame_login,text='KlayBot is not a crisis service. KlayBot is a ',font=("Courier New",11,"bold"),fg="#808080",bg="white").place(x=40,y=130)
        title=Label(Frame_login,text='self-help tool that is not intended to be a ',font=("Courier New",11,"bold"),fg="#808080",bg="white").place(x=60,y=155)
        title=Label(Frame_login,text='medical intervention. No human is monitoring your ',font=("Courier New",11,"bold"),fg="#808080",bg="white").place(x=60,y=180)
        title=Label(Frame_login,text='live conversations with KlayBot. If you are in a ',font=("Courier New",11,"bold"),fg="#808080",bg="white").place(x=40,y=205)
        title=Label(Frame_login,text='crisis, type ',font=("Courier New",11,"bold"),fg="#808080",bg="white").place(x=60,y=230)
        title=Label(Frame_login,text='"SOS" ',font=("Courier New",11,"bold"),fg="red",bg="white").place(x=175,y=230)
        title=Label(Frame_login,text='in the app and KlayBot will',font=("Courier New",11,"bold"),fg="#808080",bg="white").place(x=228,y=230)
        title=Label(Frame_login,text='suggest external resources that you can use.',font=("Courier New",11,"bold"),fg="#808080",bg="white").place(x=60,y=255)
        title=Label(Frame_login,text='⊂(◉‿◉)つ',font=("Courier New",19,"bold"),fg="#808080",bg="white").place(x=180,y=285)

    #name and age
        title=Label(Frame_login,text="Name",font=("Courier New",11,"bold"),fg="#000000",bg="white").place(x=40,y=335)
        self_txt_user=Entry(Frame_login,font=("Terminal",11),bg="lightgray",textvariable=namevalue)
        self_txt_user.place(x=150,y=340,width=190,height=20)
        title=Label(Frame_login,text="Age",font=("Courier New",11,"bold"),fg="#000000",bg="white").place(x=40,y=375)
        self_txt_pass=Entry(Frame_login,font=("Terminal",11),bg="lightgray",textvariable=agevalue)
        self_txt_pass.place(x=150,y=385,width=190,height=20)
    
    #text
        title=Label(Frame_login,text="Way of communication:",font=("Terminal",12,"bold"),fg="#000000",bg="white").place(x=80,y=420)

        checkbutton_variable = IntVar()
    #voice
        voice_check = Checkbutton(text="Voice (Beta)",font=("Terminal", 9),bg = "white", height=2, width = 10,variable=voicevalue)
        voice_check.place(x=120, y= 460)
    
    #text
        text_check = Checkbutton(text="Text",font=("Terminal", 9),bg = "white", height=2, width = 10,variable=textvalue)
        text_check.place(x=240, y= 460)
    
    #T&C
        verification = Checkbutton(text="I have read and agree to the T&C",font=("Terminal", 9),bg = "white", height=2, width = 50,variable=verificationvalue)
        verification.place(x=20, y= 500)
        
      
    #Submit
        submit_button=Button(Frame_login,text="Submit",fg="black",bg="#FFFFFF",font=("Courier New",18),command=getvals).place(x=170,y=550)
        

root = Tk()

root.iconbitmap('./assets/logo.ico')



obj = Login(root)
root.mainloop()
