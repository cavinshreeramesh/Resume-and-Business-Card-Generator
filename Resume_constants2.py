import tkinter as tk

#creating a window
window = tk.Tk()  

name = "Kyle J Shanks"

addressline1 = "My Place Drive"
addressline2 = "Astoria, New York 11105"

phoneno = "1-800-CALLPLZ"
email = "emailsareforsquares@gmail.com"

twitter = "twitter"
pinterest = "pinterest"
linkedin = "linkedin"

skill1 = "HTML"
skill2 = "CSS (Stylus)"
skill3 = "JavaScript & jQuery"
skill4 = "Killer Taste"

education1 = "Advanced potion making"
education2 = "Degree in popping and locking" 
education3 = "Knitting game on point" #make it optional

position = "Front-End Developer"
desc = "Retro DIY quinoa, mixtape williamsburg master cleanse bushwick tumblr chillwave dreamcatcher hella wolf paleo. Knausgaard semiotics truffaut cornhole hoodie, YOLO meggings gochujang tofu. Locavore ugh kale chips iPhone biodiesel typewriter freegan, kinfolk brooklyn kitsch man bun. Austin neutra etsy, lumbersexual paleo cornhole sriracha kinfolk meggings kickstarter."

job1 = "First job description"
job1desc = "Plaid gentrify put a bird on it, pickled XOXO farm-to-table irony raw denim messenger bag leggings. Hoodie PBR&B photo booth, vegan chillwave meh paleo freegan ramps. Letterpress shabby chic fixie semiotics. Meditation sriracha banjo pour-over. Gochujang pickled hashtag mixtape cred chambray. Freegan microdosing VHS, 90's bicycle rights aesthetic hella PBR&B."

job2 = "Second Job Description"
job2desc = "Beard before they sold out photo booth distillery health goth. Hammock franzen green juice meggings, ethical sriracha tattooed schlitz mixtape man bun stumptown swag whatever distillery blog. Affogato iPhone normcore, meggings actually direct trade lomo plaid franzen shoreditch. Photo booth pug paleo austin, pour-over banh mi scenester vice food truck slow-carb. Street art kogi normcore, vice everyday carry crucifix thundercats man bun raw denim echo park pork belly helvetica vinyl."

job3 ="Third Job Description"
job3desc = "Next level roof party lo-fi fingerstache skateboard, kogi tumblr. Shabby chic put a bird on it chambray, 3 wolf moon swag beard brooklyn post-ironic taxidermy art party microdosing keffiyeh marfa. Put a bird on it 3 wolf moon cliche helvetica knausgaard. Mumblecore fingerstache lomo, artisan freegan keffiyeh paleo kinfolk kale chips street art blog flannel."

title = tk.Label(window, text="Resume Details",width=20,font=("bold", 20))  
title.place(x=625,y=53)  

name_lbl = tk.Label(window, text="FullName",width=20,font=("bold", 15))  
name_lbl.place(x=415,y=130)  
name_entry = tk.Text(window, height = 2, width = 50)  
name_entry.place(x=830,y=130) 

def f8():
    global job1
    job1 = job1_entry.get(1.0, "end-1c") 
    global job1desc
    job1desc = job1desc_entry.get(1.0, "end-1c") 
    global job2
    job2 = job2_entry.get(1.0, "end-1c") 
    global job2desc
    job2desc = job2desc_entry.get(1.0, "end-1c") 
    global job3
    job3 = job3_entry.get(1.0, "end-1c") 
    global job3desc
    job3desc = job3desc_entry.get(1.0, "end-1c") 
    
    window.quit()

def f7():
    global position
    position = position_entry.get(1.0, "end-1c") 
    global desc
    desc = decs_entry.get(1.0, "end-1c") 
    position_lbl.destroy()
    position_entry.destroy()
    decs_lbl.destroy()
    decs_entry.destroy()
    button7.destroy()

    global job1_lbl,job1_entry,job1desc_lbl,job1desc_entry
    global job2_lbl,job2_entry,job2desc_lbl,job2desc_entry
    global job3_lbl,job3_entry,job3desc_lbl,job3desc_entry
    job1_lbl = tk.Label(window, text="Job Title",width=20,font=("bold", 15))  
    job1_lbl.place(x=415,y=130)  
    job1_entry = tk.Text(window, height = 2, width = 50)  
    job1_entry.place(x=830,y=130) 

    job1desc_lbl = tk.Label(window, text="Job Description",width=20,font=("bold", 15))  
    job1desc_lbl.place(x=415,y=180)  
    job1desc_entry = tk.Text(window, height = 2, width = 50)  
    job1desc_entry.place(x=830,y=180) 

    job2_lbl = tk.Label(window, text="Job Title",width=20,font=("bold", 15))  
    job2_lbl.place(x=415,y=220)  
    job2_entry = tk.Text(window, height = 2, width = 50)  
    job2_entry.place(x=830,y=220) 

    job2desc_lbl = tk.Label(window, text="Job Description",width=20,font=("bold", 15))  
    job2desc_lbl.place(x=415,y=280)  
    job2desc_entry = tk.Text(window, height = 2, width = 50)  
    job2desc_entry.place(x=830,y=280) 

    job3_lbl = tk.Label(window, text="Job Title",width=20,font=("bold", 15))  
    job3_lbl.place(x=415,y=330)  
    job3_entry = tk.Text(window, height = 2, width = 50)  
    job3_entry.place(x=830,y=330) 

    job3desc_lbl = tk.Label(window, text="Job Description",width=20,font=("bold", 15))  
    job3desc_lbl.place(x=415,y=380)  
    job3desc_entry = tk.Text(window, height = 2, width = 50)  
    job3desc_entry.place(x=830,y=380) 

    global button8
    button8 = tk.Button(window, text = "Submit",  command = f8) 
    button8.place(x=750,y=430) 

def f6():
    global education1
    education1 = education1_entry.get(1.0, "end-1c") 
    global education2
    education2 = education2_entry.get(1.0, "end-1c") 
    global education3
    education3 = education3_entry.get(1.0, "end-1c") 
    education1_entry.destroy()
    education1_lbl.destroy()
    education2_entry.destroy()
    education2_lbl.destroy()
    education3_entry.destroy()
    education3_lbl.destroy()
    button6.destroy()

    global position_lbl,position_entry,decs_lbl,decs_entry
    position_lbl = tk.Label(window, text="Position",width=20,font=("bold", 15))  
    position_lbl.place(x=415,y=130)  
    position_entry = tk.Text(window, height = 2, width = 50)  
    position_entry.place(x=830,y=130) 

    decs_lbl = tk.Label(window, text="Description",width=20,font=("bold", 15))  
    decs_lbl.place(x=415,y=180)  
    decs_entry = tk.Text(window, height = 2, width = 50)  
    decs_entry.place(x=830,y=180) 

    global button7
    button7 = tk.Button(window, text = "Next",  command = f7) 
    button7.place(x=750,y=230) 

def f5():
    global skill1
    skill1 = skill1_entry.get(1.0, "end-1c") 
    global skill2
    skill2 = skill2_entry.get(1.0, "end-1c") 
    global skill3
    skill3 = skill3_entry.get(1.0, "end-1c") 
    global skill4
    skill4 = skill4_entry.get(1.0, "end-1c") 
    skill1_lbl.destroy()
    skill1_entry.destroy()
    skill2_lbl.destroy()
    skill2_entry.destroy()
    skill3_lbl.destroy()
    skill3_entry.destroy()
    skill4_lbl.destroy()
    skill4_entry.destroy()
    button5.destroy()

    global education1_entry,education1_lbl, education2_entry,education2_lbl, education3_entry,education3_lbl
    education1_lbl = tk.Label(window, text="High School Education",width=20,font=("bold", 15))  
    education1_lbl.place(x=415,y=130)  
    education1_entry = tk.Text(window, height = 2, width = 50)  
    education1_entry.place(x=830,y=130) 

    education2_lbl = tk.Label(window, text="Undergraduate Degree",width=20,font=("bold", 15))  
    education2_lbl.place(x=415,y=180)  
    education2_entry = tk.Text(window, height = 2, width = 50)  
    education2_entry.place(x=830,y=180) 

    education3_lbl = tk.Label(window, text="Postgraduate Degree",width=20,font=("bold", 15))  
    education3_lbl.place(x=415,y=230)  
    education3_entry = tk.Text(window, height = 2, width = 50)  
    education3_entry.place(x=830,y=230) 

    global button6
    button6 = tk.Button(window, text = "Next",  command = f6) 
    button6.place(x=750,y=280) 

def f4():
    global twitter
    twitter = twitter_entry.get(1.0, "end-1c") 
    global pinterest
    pinterest = pinterest_entry.get(1.0, "end-1c") 
    global linkedin
    linkedin = linkedin_entry.get(1.0, "end-1c") 
    twitter_lbl.destroy()
    twitter_entry.destroy()
    pinterest_lbl.destroy()
    pinterest_entry.destroy()
    linkedin_lbl.destroy()
    linkedin_entry.destroy()
    button4.destroy()

    global skill1_lbl,skill1_entry,skill2_lbl,skill2_entry,skill3_lbl,skill3_entry,skill4_lbl,skill4_entry
    skill1_lbl = tk.Label(window, text="Skill 1",width=20,font=("bold", 15))  
    skill1_lbl.place(x=415,y=130)  
    skill1_entry = tk.Text(window, height = 2, width = 50)  
    skill1_entry.place(x=830,y=130) 

    skill2_lbl = tk.Label(window, text="Skill 2",width=20,font=("bold", 15))  
    skill2_lbl.place(x=415,y=180)  
    skill2_entry = tk.Text(window, height = 2, width = 50)  
    skill2_entry.place(x=830,y=180) 

    skill3_lbl = tk.Label(window, text="Skill 3",width=20,font=("bold", 15))  
    skill3_lbl.place(x=415,y=230)  
    skill3_entry = tk.Text(window, height = 2, width = 50)  
    skill3_entry.place(x=830,y=230) 

    skill4_lbl = tk.Label(window, text="Skill 4",width=20,font=("bold", 15))  
    skill4_lbl.place(x=415,y=280)  
    skill4_entry = tk.Text(window, height = 2, width = 50)  
    skill4_entry.place(x=830,y=280) 

    global button5
    button5 = tk.Button(window, text = "Next",  command = f5) 
    button5.place(x=750,y=330) 

def f3():
    global phoneno
    phoneno = phoneno_entry.get(1.0, "end-1c") 
    global email
    email = email_entry.get(1.0, "end-1c") 
    phoneno_lbl.destroy()
    phoneno_entry.destroy()
    email_lbl.destroy()
    email_entry.destroy()
    button3.destroy()

    global twitter_lbl,twitter_entry,pinterest_lbl,pinterest_entry,linkedin_lbl,linkedin_entry
    twitter_lbl = tk.Label(window, text="twitter",width=20,font=("bold", 15))  
    twitter_lbl.place(x=415,y=130)  
    twitter_entry = tk.Text(window, height = 2, width = 50)  
    twitter_entry.place(x=830,y=130) 

    pinterest_lbl = tk.Label(window, text="Pinterest",width=20,font=("bold", 15))  
    pinterest_lbl.place(x=415,y=180)  
    pinterest_entry = tk.Text(window, height = 2, width = 50)  
    pinterest_entry.place(x=830,y=180) 

    linkedin_lbl = tk.Label(window, text="Linkedin",width=20,font=("bold", 15))  
    linkedin_lbl.place(x=415,y=230)  
    linkedin_entry = tk.Text(window, height = 2, width = 50)  
    linkedin_entry.place(x=830,y=230) 

    global button4
    button4 = tk.Button(window, text = "Next",  command = f4) 
    button4.place(x=750,y=280) 

def f2():
    global addressline1
    addressline1 = addressline1_entry.get(1.0, "end-1c") 
    global addressline2
    addressline2 = addressline2_entry.get(1.0, "end-1c")
    addressline1_lbl.destroy()
    addressline1_entry.destroy()
    addressline2_lbl.destroy()
    addressline2_entry.destroy()
    button2.destroy()

    global phoneno_lbl
    phoneno_lbl = tk.Label(window, text="Phone Number",width=20,font=("bold", 15))  
    phoneno_lbl.place(x=415,y=130)  
    global phoneno_entry
    phoneno_entry = tk.Text(window, height = 2, width = 50)  
    phoneno_entry.place(x=830,y=130) 

    global email_lbl
    email_lbl = tk.Label(window, text="Email",width=20,font=("bold", 15))  
    email_lbl.place(x=415,y=180)  
    global email_entry
    email_entry = tk.Text(window, height = 2, width = 50)  
    email_entry.place(x=830,y=180) 

    global button3
    button3 = tk.Button(window, text = "Next",  command = f3) 
    button3.place(x=750,y=230) 


def f1():
    global name
    name = name_entry.get(1.0, "end-1c") 
    name_lbl.destroy()
    name_entry.destroy()
    button1.destroy()

    global addressline1_lbl 
    addressline1_lbl = tk.Label(window, text="Address Line 1",width=20,font=("bold", 15))  
    addressline1_lbl.place(x=415,y=130)  
    global addressline1_entry
    addressline1_entry = tk.Text(window, height = 2, width = 50)  
    addressline1_entry.place(x=830,y=130)    

    global addressline2_lbl
    addressline2_lbl = tk.Label(window, text="Address Line 2",width=20,font=("bold", 15))   
    addressline2_lbl.place(x=415,y=180)
    global addressline2_entry  
    addressline2_entry = tk.Text(window, height = 2, width = 50)  
    addressline2_entry.place(x=830,y=180) 

    global button2
    button2 = tk.Button(window, text = "Next",  command = f2) 
    button2.place(x=750,y=230) 

button1 = tk.Button(window, text = "Next",  command = f1) 
button1.place(x=750,y=180)  

window.mainloop()
