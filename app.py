from tkinter import * 
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:

    def __init__(self):

        #create a database object
        self.dbo=Database()
        self.apio=API()

        self.root=Tk()
        self.root.title("NLP App")
        self.root.iconbitmap("resources/favicon.ico")
        self.root.geometry("350x600")
        self.root.configure(bg="#D9F7FF")
        self.login_gui()
        self.root=mainloop()

    def login_gui(self):
        self.clear()
        heading=Label(self.root,text="NLPApp",bg="#D9F7FF",fg="black")
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,"bold"))

        Label1=Label(self.root,text="Enter email",bg="#D9F7FF",fg="black")
        Label1.pack(pady=(10,10))

        self.input1=Entry(self.root,width=50)
        self.input1.pack(pady=(10,10),ipady=4)

        Label2=Label(self.root,text="Enter Password",bg="#D9F7FF",fg="black")
        Label2.pack(pady=(10,10))

        self.input2=Entry(self.root,width=50,show="*")
        self.input2.pack(pady=(10,10),ipady=4)

        login_button=Button(self.root,text="login",width=20,height=1,command=self.perform_login)
        login_button.pack(pady=(10,10),ipady=4)

        Label3=Label(self.root,text="Not a member?",bg="#D9F7FF",fg="black")
        Label3.pack(pady=(20,10))

        register_button=Button(self.root,text="Register Now",width=20,height=1,command=self.register_gui)
        register_button.pack(pady=(5,10))

    def register_gui(self):
        self.clear()
        heading=Label(self.root,text="NLPApp",bg="#D9F7FF",fg="black")
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,"bold"))

        Label1=Label(self.root,text="Enter name",bg="#D9F7FF",fg="black")
        Label1.pack(pady=(10,10))

        self.input1=Entry(self.root,width=50)
        self.input1.pack(pady=(10,10),ipady=4)

        Label2=Label(self.root,text="Enter Email",bg="#D9F7FF",fg="black")
        Label2.pack(pady=(10,10))

        self.input2=Entry(self.root,width=50)
        self.input2.pack(pady=(10,10),ipady=4)

        Label3=Label(self.root,text="Enter password",bg="#D9F7FF",fg="black")
        Label3.pack(pady=(10,10))

        self.input3=Entry(self.root,width=50,show="*")
        self.input3.pack(pady=(10,10),ipady=4)


        login_button=Button(self.root,text="Register",width=20,height=1,command=self.perform_registration)
        login_button.pack(pady=(10,10),ipady=4)

        Label3=Label(self.root,text="Alrady a member?",bg="#D9F7FF",fg="black")
        Label3.pack(pady=(20,10))

        register_button=Button(self.root,text="Login Now",width=20,height=1,command=self.login_gui)
        register_button.pack(pady=(5,10))


    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        #fetch data from gui
        name=self.input1.get()
        email=self.input2.get()
        password=self.input3.get()
        response=self.dbo.add_data(name,email,password)
        if response==1:
            messagebox.showinfo("Success","registration successful you can login now")
        else:
            messagebox.showerror("Error","email already exists")

    def perform_login(self):
        #fetch data from gui
        email=self.input1.get()
        password=self.input2.get()
        response=self.dbo.search(email,password)
        if response==1:
            messagebox.showinfo("Success","Login successful")
            self.home_gui()
        else:
            messagebox.showerror("Error","Incorrect Email/Password")

    def home_gui(self):
        self.clear()

        heading=Label(self.root,text="NLPApp",bg="#D9F7FF",fg="black")
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,"bold"))

        sentiment_button=Button(self.root,text="Sentiment_Analysis",width=30,height=2,command=self.sentiment_gui)
        sentiment_button.pack(pady=(10,10),ipady=4)

        ner_button=Button(self.root,text="Named Entity Recognisation",width=30,height=2,command=self.perform_registration)
        ner_button.pack(pady=(10,10),ipady=4)

        emotion_button=Button(self.root,text="Emotion Prediction",width=30,height=2,command=self.perform_registration)
        emotion_button.pack(pady=(10,10),ipady=4)

        logout_button=Button(self.root,text="Logout Button",width=15,height=1,command=self.login_gui)
        logout_button.pack(pady=(10,10),ipady=4)

    def sentiment_gui(self):

        self.clear()

        heading=Label(self.root,text="NLPApp",bg="#D9F7FF",fg="black")
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,"bold"))

        heading1=Label(self.root,text="Sentiment Analysis",bg="#D9F7FF",fg="black")
        heading1.pack(pady=(10,20))
        heading1.configure(font=('verdana',20))

        label1=Label(self.root,text="Enter the text",bg="#D9F7FF",fg="black")
        label1.pack(pady=(10,10))

        self.sentiment_input=Entry(self.root,width=50)
        self.sentiment_input.pack(pady=(10,10),ipady=4)

        sentiment_button=Button(self.root,text="Analyze Sentiment",width=15,height=1,command=self.do_sentiment_analysis)
        sentiment_button.pack(pady=(10,10),ipady=4)

        self.sentiment_result=Label(self.root,text="",bg="#D9F7FF",fg="black")
        self.sentiment_result.pack(pady=(10,10))

        goback_button=Button(self.root,text="Go back",width=10,height=1,command=self.home_gui)
        goback_button.pack(pady=(10,10),ipady=4)

    def do_sentiment_analysis(self):

        text=self.sentiment_input.get()
        result=self.apio.sentiment_analysis(text)

        print(result["score"],"The emotion is : ", result["sentiment"])
        self.sentiment_result["text"]=result








nlp=NLPApp()