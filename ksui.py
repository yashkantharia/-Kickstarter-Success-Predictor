import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle

#loading models
model_classification = pickle.load(open('catboost_classification.sav', 'rb'))
model_duration = pickle.load(open('catboost_duration.sav', 'rb'))
model_goal = pickle.load(open('catboost_goal.sav', 'rb'))
model_nl = pickle.load(open('catboost_name_length.sav', 'rb'))
model_bl = pickle.load(open('catboost_blurb_length.sav', 'rb'))


#UI
window = tk.Tk()
window.title("KICKSTARTER SUCCESS PREDICTOR")
window.geometry("600x350")



#------Calling Functions------------------
def retrieve_input():
    global ip_mc, ip_sc, ip_country, ip_goal, ip_duration, ip_state, ip_city, ip_currency, ip_name, ip_blurb
    global ip_name_length, ip_blurb_length, prediction, predicted_duration, predicted_goal, predicted_nl, predicted_bl
    ip_mc = v0.get()
    ip_sc = v1.get()
    ip_country = v2.get()
    ip_goal = float(tb1.get("1.0","end-1c"))
    ip_duration= int(tb2.get("1.0","end-1c"))
    ip_state = tb3.get("1.0","end-1c")
    ip_city = tb4.get("1.0","end-1c")
    ip_currency= v3.get()
    ip_name = tb5.get("1.0","end-1c")
    ip_blurb = tb6.get("1.0","end-1c")
    
    if (type(ip_mc)!='str' or type(ip_sc)!='str' or type(ip_goal)!='float' or type(ip_duration)!='int' or type(ip_name)!='str' or type(ip_blurb)!='str'):
       
         #name length
        words1 = ip_name.split()
        ip_name_length = len(words1)
        
        words2 = ip_blurb.split()
        ip_blurb_length = len(words2)
        
        print(ip_name_length)
        print(ip_blurb_length)
        ipdata = { 'currency':[ip_currency],'main_category':[ip_mc], 'sub_category':[ip_sc],'duration':[ip_duration],'goal_usd':[ip_goal],'city': [ip_city],'state': [ip_state], 'country': [ip_country], 'blurb_length':[ip_blurb_length], 'name_length': [ip_name_length]}
        testip =pd.DataFrame(data=ipdata)
        prediction = int(model_classification.predict(testip))
        
        ip_pred_duration_data ={ 'currency':[ip_currency],'main_category':[ip_mc], 'sub_category':[ip_sc],'goal_usd':[ip_goal],'city': [ip_city],'state': [ip_state], 'country': [ip_country], 'blurb_length':[ip_blurb_length], 'name_length': [ip_name_length]}
        duration_ip = pd.DataFrame(data=ip_pred_duration_data)
        predicted_duration = int(model_duration.predict(duration_ip))
        
        ip_pred_goal_data = { 'currency':[ip_currency],'main_category':[ip_mc], 'sub_category':[ip_sc],'duration':[ip_duration],'city': [ip_city],'state': [ip_state], 'country': [ip_country], 'blurb_length':[ip_blurb_length], 'name_length': [ip_name_length]}
        goal_ip = pd.DataFrame(data=ip_pred_goal_data)
        predicted_goal = int(model_goal.predict(goal_ip))
        
        ip_bl_data= { 'currency':[ip_currency],'main_category':[ip_mc], 'sub_category':[ip_sc],'duration':[ip_duration],'goal_usd':[ip_goal],'city': [ip_city],'state': [ip_state], 'country': [ip_country], 'name_length': [ip_name_length]}
        bl_ip =pd.DataFrame(data=ip_bl_data)
        predicted_bl = int(model_bl.predict(bl_ip))
        
        ip_nl_data = { 'currency':[ip_currency],'main_category':[ip_mc], 'sub_category':[ip_sc],'duration':[ip_duration],'goal_usd':[ip_goal],'city': [ip_city],'state': [ip_state], 'country': [ip_country], 'blurb_length':[ip_blurb_length], 'name_length': [ip_name_length]}
        nl_ip =pd.DataFrame(data=ip_nl_data)
        predicted_nl = int(model_nl.predict(nl_ip))
        
        #prediction output
        if prediction ==1:
            pred_output = ttk.Label(text="Successful")
        else:
            pred_output = ttk.Label(text="Unsuccessful")
        pred_output.grid(column=4, row=13, pady=5)
    
    else:
        messagebox.showwarning("Warning!","Incorrect input format")
    




def genrep():
    global ip_mc, ip_sc, ip_country, ip_goal, ip_duration, ip_state, ip_city, ip_currency, ip_name, ip_blurb
    global ip_name_length, ip_blurb_length, prediction, predicted_duration, predicted_goal, predicted_nl, predicted_bl
    repwindow = tk.Toplevel(window)
    repwindow.title("REPORT")
    sug = tk.Label(repwindow,text="REPORT")
    repwindow.geometry("350x100")
    lr1 = ttk.Label(repwindow,text="Parameter")
    lr1.grid(column=0 , row=0, padx=5 )
    lr2 = ttk.Label(repwindow,text="Predicted value")
    lr2.grid(column=5 , row=0, padx=5 )
    lr3 = ttk.Label(repwindow,text="Input Values")
    lr3.grid(column=10 , row=0, padx=5 )
    lr4 = ttk.Label(repwindow,text="Difference")
    lr4.grid(column=15 , row=0, padx=5 )
    
    p1 = ttk.Label(repwindow,text="Goal")
    p1.grid(column=0 , row=3, padx=5 )
    p2 = ttk.Label(repwindow,text="Duration")
    p2.grid(column=0 , row=6, padx=5 )
    p3 = ttk.Label(repwindow,text="Blurb Length")
    p3.grid(column=0 , row=9, padx=5 )
    p4 = ttk.Label(repwindow,text="Name Length")
    p4.grid(column=0 , row=11, padx=5 )
    
    #prediction
    pred_goal_op = ttk.Label(repwindow,text= predicted_goal)
    pred_goal_op.grid(column=5 , row=3, padx=5 ,pady=1 )
    
    pred_duration_op = ttk.Label(repwindow,text= predicted_duration)
    pred_duration_op.grid(column=5 , row=6, padx=5,pady=1 )
    
    pred_bl_op = ttk.Label(repwindow,text= predicted_bl)
    pred_bl_op.grid(column=5 , row=9, padx=5 ,pady=1)
    
    pred_nl_op = ttk.Label(repwindow, text =predicted_nl)
    pred_nl_op.grid(column=5 , row= 11, padx=5,pady=1)
    
    #inputvalues
    ip_goal_op = ttk.Label(repwindow,text=(ip_goal))
    ip_goal_op.grid(column=10 , row=3, padx=5,pady=1 )
    
    ip_duration_op = ttk.Label(repwindow,text=ip_duration)
    ip_duration_op.grid(column=10 , row=6, padx=5,pady=1 )
    
    ip_bl_op = ttk.Label(repwindow,text=ip_blurb_length)
    ip_bl_op.grid(column=10 , row=9, padx=5 ,pady=1)
    
    ip_nl_op = ttk.Label(repwindow,text=ip_name_length)
    ip_nl_op.grid(column=10 , row=11, padx=5,pady=1 )
    
    #diff
    diff_goal_op = ttk.Label(repwindow,text=(predicted_goal - ip_goal))
    diff_goal_op.grid(column=15 , row=3, padx=5 ,pady=1)
    
    diff_duration_op = ttk.Label(repwindow,text=(predicted_duration - ip_duration))
    diff_duration_op.grid(column=15 , row=6, padx=5 ,pady=1)
    
    diff_bl_op = ttk.Label(repwindow,text=(predicted_bl - ip_blurb_length))
    diff_bl_op.grid(column=15 , row=9, padx=5,pady=1 )
    
    diff_nl_op = ttk.Label(repwindow,text=(predicted_nl -ip_name_length))
    diff_nl_op.grid(column=15 , row=11, padx=5 ,pady=1)
    
    sug.pack()


#~~~~~~~~~~~~~~~INPUTS~~~~~~~~~~~~~~~~~~~~~~~
#---LABELS--
lab1 = ttk.Label(text="Main Category")
lab1.grid(column=0 , row=0, padx=5 ,pady=1)

lab2 = ttk.Label(text="Sub-Category")
lab2.grid(column=4 , row=0, padx=5 ,pady=1)

lab3 = ttk.Label(text="Goal (in USD)")
lab3.grid(column=8 , row=0, padx=5 ,pady=1)

lab4 = ttk.Label(text="Duration (in days)")
lab4.grid(column=12 , row=0, padx=5 ,pady=1)

lab5 = ttk.Label(text="Country")
lab5.grid(column=0 , row=3, padx=5 ,pady=1)

lab6 = ttk.Label(text="State")
lab6.grid(column=4 , row=3, padx=5,pady=1 )

lab7 = ttk.Label(text="City")
lab7.grid(column=8 , row=3, padx=5 ,pady=1)

lab8 = ttk.Label(text="Currency")
lab8.grid(column=12 , row=3, padx=5 ,pady=1)

lab9 = ttk.Label(text="Name of Campaign:")
lab9.grid(column=0 , row=7, padx=5 ,pady=1)

lab10 = ttk.Label(text="Short Description:")
lab10.grid(column=0 , row=10, padx=5 ,pady=1)
#--------INPUT FIELDS-------
#---DROPDOWN----
v0 = tk.StringVar(window)
 # default value
v1 = tk.StringVar(window)
v2 = tk.StringVar(window)
v3 = tk.StringVar(window)
 # default value
a=0
sc=[['Drama', 'Documentary', 'Horror', 'Experimental', 'Shorts', 'Fantasy', 'Television', 'Movie Theaters', 'Thrillers', 'Music Videos', 'Comedy', 'Narrative Film', 'Animation', 'Family', 'Webseries', 'Romance', 'Action', 'Festivals', 'Film & Video', 'Science Fiction'], ['Makerspaces', 'DIY Electronics', '3D Printing', 'Flight', 'Web', 'Apps', 'Sound', 'Technology', 'Space Exploration', 'Fabrication Tools', 'Hardware', 'Software', 'Gadgets', 'Robots', 'Wearables', 'Camera Equipment'], ['Chiptune', 'Classical Music', 'Punk', 'Hip-Hop', 'Jazz', 'Rock', 'Blues', 'Indie Rock', 'Metal', 'Comedy', 'Music', 'World Music', 'Pop', 'R&B', 'Latin', 'Country & Folk', 'Kids', 'Electronic Music', 'Faith'], ['Journalism', 'Video', 'Web', 'Photo', 'Audio', 'Print'], ['Zines', 'Literary Spaces', 'Publishing', 'Fiction', 'Art Books', 'Literary Journals', "Children's Books", 'Comedy', 'Young Adult', 'Poetry', 'Nonfiction', 'Academic', 'Calendars', 'Anthologies', 'Radio & Podcasts', 'Periodicals', 'Letterpress', 'Translations'], ['Ready-to-wear', 'Jewelry', 'Pet Fashion', 'Footwear', 'Fashion', 'Accessories', 'Apparel', 'Couture', 'Childrenswear'], ['Printing', 'DIY', 'Candles', 'Crafts', 'Crochet', 'Knitting', 'Taxidermy', 'Weaving', 'Woodworking', 'Embroidery', 'Glass', 'Stationery', 'Pottery', 'Quilts'], ['Mobile Games', 'Gaming Hardware', 'Video Games', 'Live Games', 'Playing Cards', 'Tabletop Games', 'Puzzles', 'Games'], ['Webcomics', 'Events', 'Graphic Novels', 'Comics', 'Anthologies', 'Comic Books'], ['Theater', 'Plays', 'Immersive', 'Musical', 'Spaces', 'Comedy', 'Festivals', 'Experimental'], ['Public Art', 'Textiles', 'Video Art', 'Painting', 'Sculpture', 'Installations', 'Digital Art', 'Art', 'Ceramics', 'Conceptual Art', 'Performance Art', 'Mixed Media', 'Illustration'], ['Nature', 'Animals', 'Places', 'Photobooks', 'Photography', 'People', 'Fine Art'], ['Performances', 'Dance', 'Workshops', 'Spaces', 'Residencies'], ['Interactive Design', 'Graphic Design', 'Typography', 'Design', 'Civic Design', 'Product Design', 'Architecture'], ['Cookbooks', 'Farms', 'Food', 'Food Trucks', 'Vegan', 'Community Gardens', 'Small Batch', 'Events', "Farmer's Markets", 'Spaces', 'Restaurants', 'Drinks', 'Bacon']]

def opm(v=v0.get):
    print(v)
    if v=='film & video':
        a=0
    elif v=='technology':
        a=1
    elif v=='music':
        a=2
    elif v=='journalism':
        a=3
    elif v=='publishing':
        a=4
    elif v=='fashion':
        a=5
    elif v=='crafts':
        a=6
    elif v=='games':
        a=7
    elif v=='comics':
        a=8
    elif v=='theater':
        a=9
    elif v=='art':
        a=10
    elif v== 'photography':
        a=11
    elif v=='dance':
        a=12
    elif v=='design':
        a=13
    elif v=='food':
        a=14

    d2 = ttk.OptionMenu(window, v1, 'select',*sc[a])
    d2.grid(column=4, row=1, padx=5,pady=1)

d1 = ttk.OptionMenu(window, v0, 'select','film & video', 'technology', 'music', 'journalism', 'publishing', 'fashion', 'crafts', 'games', 'comics', 'theater', 'art', 'photography', 'dance', 'design', 'food', command=opm)
d1.grid(column=0, row=1, padx=5,pady=1)



d3 = ttk.OptionMenu(window, v2, 'NO', 'AT', 'CH', 'DK', 'SG', 'MX', 'GB', 'IT', 'SE', 'HK', 'BE', 'LU', 'ES', 'IE', 'NZ', 'DE', 'AU', 'CA', 'NL', 'FR', 'JP', 'US')
d3.grid(column=0, row=5, padx=5,pady=1)

d4 = ttk.OptionMenu(window, v3, 'MXN', 'SGD', 'CAD', 'JPY', 'SEK', 'AUD', 'GBP', 'NOK', 'CHF', 'HKD', 'EUR', 'NZD', 'DKK', 'USD')
d4.grid(column=12, row=5, padx=5,pady=1)



#Textboxes
tb1 = tk.Text(window, height=1 ,width=10)
tb1.grid(column=8, row=1, padx=5,pady=1)

tb2 = tk.Text(window, height=1 ,width=10)
tb2.grid(column=12, row=1, padx=5,pady=1)

tb3= tk.Text(window, height=1 ,width=10)
tb3.grid(column=4, row=5, padx=5,pady=1)

tb4= tk.Text(window, height=1 ,width=10)
tb4.grid(column=8, row=5, padx=5,pady=1)

tb5= tk.Text(window, height=1 ,width=30)
tb5.grid(column=0, row=8, padx=5,pady=1)

tb6= tk.Text(window, height=3 ,width=30)
tb6.grid(column=0, row=11, padx=5,pady=1)

#------BUTTON------
but1 = ttk.Button(text="Submit", command =lambda: retrieve_input())
but1.grid(column=4, row= 12, pady=5)

#~~~~~~~~~~~~~~~~Output~~~~~~~~~~~~~~~~~~~~~

lab4 = ttk.Label(text="Prediction:")
lab4.grid(column=0 , row=13, pady=5 )

pred_output = ttk.Label(text="")
pred_output.grid(column=4, row=14, pady=5)

#----Advanced Output Buttons---

but3 = ttk.Button(text="Generate Report!", command = lambda: genrep())
but3.grid(column=4, row=15 , pady=5)


window.mainloop()
