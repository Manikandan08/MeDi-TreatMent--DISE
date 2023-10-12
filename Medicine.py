from tkinter import *
from tkinter import messagebox
import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='',database='doctor')
mycursor=mydb.cursor()


w=Tk()
w.geometry("1530x700")
w.title("SIGN UP PAGE")
w.configure(bg="Purple")

def med():
    k=Tk()
    k.geometry("1500x700")
    k.title("MAIN PAGE")
    k.configure(bg="Green")
    for i in lb.curselection():
        global dis
        dis=lb.get(i)
    if dis=="Acne":
        l=Label(k,text="ACNE :",font="cambria 20",fg="Black",bg="Green")
        l.place(x=50,y=100)
        l=Label(k,text="Treatment :",font="cambria 15",fg="White",bg="Green")
        l.place(x=80,y=200)
        a="""Retinoids and retinoid-like drugs: Drugs that contain retinoic acids or tretinoin are often useful for moderate acne. These come as creams, gels and lotions. Examples include tretinoin 
(Avita, Retin-A, others), adapalene (Differin) and tazarotene (Tazorac, Avage, others). You apply this medication in the evening, beginning with three times a week, then daily as your
skin becomes used to it. It prevents plugging of hair follicles. Do not apply tretinoin at the same time as benzoyl peroxide.

Dapsone: Dapsone (Aczone) 5% gel twice daily is recommended for inflammatory acne, especially in women with acne. Side effects include redness and dryness.

Antibiotics: These work by killing excess skin bacteria and reducing redness and inflammation. For the first few months of treatment, you may use both a retinoid and an antibiotic,
with the antibiotic applied in the morning and the retinoid in the evening. The antibiotics are often combined with benzoyl peroxide to reduce the likelihood of developing antibiotic 
resistance. Examples include clindamycin with benzoyl peroxide (Benzaclin, Duac, others) and erythromycin with benzoyl peroxide (Benzamycin). Topical antibiotics alone aren't recommended."""
        l=Label(k,text=a,font="helvetica 13",fg="Black",bg="Green")
        l.place(x=80,y=300)
        b=Button(k,text="Exit",font="Pacifico 15 bold",fg="White",bg="Black",command=perform)
        b.place(x=750,y=550)

    elif dis=="AIDS/HIV":
        l=Label(k,text="AIDS/HIV :",font="cambria 20",fg="Black",bg="Green")
        l.place(x=50,y=100)
        l=Label(k,text="Treatment :",font="cambria 15",fg="White",bg="Green")
        l.place(x=80,y=200)
        b="""HIV treatment involves taking highly effective medicines called antiretroviral therapy (ART) that work to control the virus. ART is recommended for everyone with HIV, and people with HIV
should start ART as soon as possible after diagnosis, even on that same day.

lamivudine (3TC)
tenofovir disoproxil fumarate (tenofovir DF, TDF)
zidovudine (azidothymidine, AZT, ZDV)"""
        l=Label(k,text=b,font="helvetica 13",fg="Black",bg="Green")
        l.place(x=80,y=300)
        b=Button(k,text="Exit",font="Pacifico 15 bold",fg="White",bg="Black",command=perform)
        b.place(x=750,y=550)

    elif dis=="Anxiety":
        l=Label(k,text="Anxiety :",font="cambria 20",fg="Black",bg="Green")
        l.place(x=50,y=100)
        l=Label(k,text="Treatment :",font="cambria 15",fg="White",bg="Green")
        l.place(x=80,y=200)
        c="""The two main treatments for anxiety disorders are psychotherapy and medications. 

Psychotherapy: Cognitive behavioral therapy (CBT) is the most effective form of psychotherapy for anxiety disorders. Generally a short-term treatment, CBT focuses on teaching you specific
skills to improve your symptoms and gradually return to the activities you've avoided because of anxiety.

Medications: Several types of medications are used to help relieve symptoms, depending on the type of anxiety disorder you have and whether you also have other mental or physical health 
issues. For example:

                     Certain antidepressants are also used to treat anxiety disorders.
                     An anti-anxiety medication called buspirone may be prescribed.
                     In limited circumstances, your doctor may prescribe other types of medications, such as sedatives, also called benzodiazepines, or beta blockers. These medications are 
for short-term relief of anxiety symptoms and are not intended to be used long term."""
        l=Label(k,text=c,font="helvetica 13",fg="Black",bg="Green")
        l.place(x=80,y=300)
        b=Button(k,text="Exit",font="Pacifico 15 bold",fg="White",bg="Black",command=perform)
        b.place(x=750,y=550)

    elif dis=="Cancer":
        l=Label(k,text="Cancer :",font="cambria 20",fg="Black",bg="Green")
        l.place(x=50,y=100)
        l=Label(k,text="Treatment :",font="cambria 15",fg="White",bg="Green")
        l.place(x=80,y=200)
        d="""Cancer can be treated by surgery, chemotherapy, radiation therapy, hormonal therapy, targeted therapy (including immunotherapy such as monoclonal antibody therapy) and synthetic lethality, 
most commonly as a series of separate treatments (e.g. chemotherapy before surgery). The choice of therapy depends upon the location and grade of the tumor and the stage of the disease, 
as well as the general state of the patient (performance status). Cancer genome sequencing helps in determining which cancer the patient exactly has for determining the best therapy for 
the cancer. A number of experimental cancer treatments are also under development. Under current estimates, two in five people will have cancer at some point in their lifetime.

Complete removal of the cancer without damage to the rest of the body (that is, achieving cure with near-zero adverse effects) is the ideal, if rarely achieved, goal of treatment and is 
often the goal in practice. Sometimes this can be accomplished by surgery, but the propensity of cancers to invade adjacent tissue or to spread to distant sites by microscopic metastasis 
often limits its effectiveness; and chemotherapy and radiotherapy can have a negative effect on normal cells."""
        l=Label(k,text=d,font="helvetica 13",fg="Black",bg="Green")
        l.place(x=80,y=300)
        b=Button(k,text="Exit",font="Pacifico 15 bold",fg="White",bg="Black",command=perform)
        b.place(x=750,y=550)

    elif dis=="Colds&Flu":
        l=Label(k,text="Colds&Flu :",font="cambria 20",fg="Black",bg="Green")
        l.place(x=50,y=100)
        l=Label(k,text="Treatment :",font="cambria 15",fg="White",bg="Green")
        l.place(x=80,y=200)
        f="""Hydration:

Austin's number one recommendation for recovering quickly from a cold or flu virus is staying hydrated.
"When you're hydrated, your body has a natural ability to flush germs out of your system," she says.
She recommends 64 ounces of fluid a day, but talk to your doctor about your specific needs. Some people, such as those with congestive heart failure, should drink less water.

Vitamin C

While vitamin C hasn't been proven to prevent cold symptoms, some studies have indicated it can shorten the lifespan of a cold. Plus, it boosts your overall health, including your immune 
system.
Austin recommends getting the vitamin through your diet. The fresher the food, the better. Think oranges, rather than orange juice or supplements. Overdoing it on vitamin C supplements
(not dietary vitamin C) can lead to upset stomach and kidney stones."""
        l=Label(k,text=f,font="helvetica 13",fg="Black",bg="Green")
        l.place(x=80,y=300)
        b=Button(k,text="Exit",font="Pacifico 15 bold",fg="White",bg="Black",command=perform)
        b.place(x=750,y=550)

    elif dis=="Diabetes":
        l=Label(k,text="Diabetes :",font="cambria 20",fg="Black",bg="Green")
        l.place(x=50,y=100)
        l=Label(k,text="Treatment :",font="cambria 15",fg="White",bg="Green")
        l.place(x=80,y=200)
        g="""Treatment for type 1 diabetes involves insulin injections or the use of an insulin pump, frequent blood sugar checks, and carbohydrate counting. For some people with type 1 diabetes, 
pancreas transplant or islet cell transplant may be an option.

Treatment of type 2 diabetes mostly involves lifestyle changes, monitoring of your blood sugar, along with oral diabetes drugs, insulin or both.
Monitoring your blood sugar:
          Besides daily blood sugar monitoring, your provider will likely recommend regular A1C testing to measure your average blood sugar level for the past 2 to 3 months.
Insulin:
          An insulin pump also may be an option. The pump is a device about the size of a small cellphone worn on the outside of your body. A tube connects the reservoir of insulin to a 
tube (catheter) that's inserted under the skin of your abdomen."""
        l=Label(k,text=g,font="helvetica 13",fg="Black",bg="Green")
        l.place(x=80,y=300)
        b=Button(k,text="Exit",font="Pacifico 15 bold",fg="White",bg="Black",command=perform)
        b.place(x=750,y=550)

    elif dis=="Diarrhea":
        l=Label(k,text="Diarrhea :",font="cambria 20",fg="Black",bg="Green")
        l.place(x=50,y=100)
        l=Label(k,text="Treatment :",font="cambria 15",fg="White",bg="Green")
        l.place(x=80,y=200)
        h="""Drink plenty of liquids, including water, broths and juices. Avoid caffeine and alcohol.
Add semisolid and low-fiber foods gradually as your bowel movements return to normal. Try soda crackers, toast, eggs, rice or chicken.
Avoid certain foods such as dairy products, fatty foods, high-fiber foods or highly seasoned foods for a few days.
Ask about anti-diarrheal medications. Over-the-counter anti-diarrheal medications, such as loperamide and bismuth subsalicylate, might help reduce the number of watery bowel movements and control severe symptoms."""
        l=Label(k,text=h,font="helvetica 13",fg="Black",bg="Green")
        l.place(x=80,y=300)
        b=Button(k,text="Exit",font="Pacifico 15 bold",fg="White",bg="Black",command=perform)
        b.place(x=750,y=550)

    elif dis=="Heart Disease":
        l=Label(k,text="Heart Disease :",font="cambria 20",fg="Black",bg="Green")
        l.place(x=50,y=100)
        l=Label(k,text="Treatment :",font="cambria 15",fg="White",bg="Green")
        l.place(x=80,y=200)
        i="""Electrocardiogram (ECG or EKG):
An ECG is a quick and painless test that records the electrical signals in the heart. It can tell if the heart is beating too fast or too slowly.
Holter monitoring.
A Holter monitor is a portable ECG device that's worn for a day or more to record the heart's activity during daily activities. This test can detect irregular heartbeats that aren't found during a regular ECG exam.
Echocardiogram.
This noninvasive exam uses sound waves to create detailed images of the heart in motion. It shows how blood moves through the heart and heart valves. An echocardiogram can help determine if a valve is narrowed or leaking.
Exercise tests or stress tests.
These tests often involve walking on a treadmill or riding a stationary bike while the heart is monitored. Exercise tests help reveal how the heart responds to physical activity and whether heart disease symptoms occur during exercise. If you can't exercise, you might be given medications."""
        l=Label(k,text=i,font="helvetica 13",fg="Black",bg="Green")
        l.place(x=80,y=300)
        b=Button(k,text="Exit",font="Pacifico 15 bold",fg="White",bg="Black",command=perform)
        b.place(x=750,y=550)

    elif dis=="Pneumonia":
        l=Label(k,text="Pneumonia :",font="cambria 20",fg="Black",bg="Green")
        l.place(x=50,y=100)
        l=Label(k,text="Treatment :",font="cambria 15",fg="White",bg="Green")
        l.place(x=80,y=200)
        j="""Antibiotics.
These medicines are used to treat bacterial pneumonia. It may take time to identify the type of bacteria causing your pneumonia and to choose the best antibiotic to treat it. If your symptoms don't improve, your doctor may recommend a different antibiotic.
Cough medicine.
This medicine may be used to calm your cough so that you can rest. Because coughing helps loosen and move fluid from your lungs, it's a good idea not to eliminate your cough completely. In addition, you should know that very few studies have looked at whether over-the-counter cough medicines lessen coughing caused by pneumonia. If you want to try a cough suppressant, use the lowest dose that helps you rest.
Fever reducers/pain relievers.
You may take these as needed for fever and discomfort. These include drugs such as aspirin, ibuprofen (Advil, Motrin IB, others) and acetaminophen (Tylenol, others)."""
        l=Label(k,text=j,font="helvetica 13",fg="Black",bg="Green")
        l.place(x=80,y=300)
        b=Button(k,text="Exit",font="Pacifico 15 bold",fg="White",bg="Black",command=perform)
        b.place(x=750,y=550)

    elif dis=="Stroke":
        l=Label(k,text="Stroke :",font="cambria 20",fg="Black",bg="Green")
        l.place(x=50,y=100)
        l=Label(k,text="Treatment :",font="cambria 15",fg="White",bg="Green")
        l.place(x=80,y=200)
        m="""Emergency IV medication. Therapy with drugs that can break up a clot has to be given within 4.5 hours from when symptoms first started if given intravenously. The sooner these drugs are given, the better. Quick treatment not only improves your chances of survival but also may reduce complications.

An IV injection of recombinant tissue plasminogen activator (TPA) — also called alteplase (Activase) or tenecteplase (TNKase) — is the gold standard treatment for ischemic stroke. An injection of TPA is usually given through a vein in the arm within the first three hours. Sometimes, TPA can be given up to 4.5 hours after stroke symptoms started.

This drug restores blood flow by dissolving the blood clot causing the stroke. By quickly removing the cause of the stroke, it may help people recover more fully from a stroke. Your doctor will consider certain risks, such as potential bleeding in the brain, to determine whether TPA is appropriate for you."""
        l=Label(k,text=m,font="helvetica 13",fg="Black",bg="Green")
        l.place(x=80,y=300)
        b=Button(k,text="Exit",font="Pacifico 15 bold",fg="White",bg="Black",command=perform)
        b.place(x=750,y=550)

    elif dis=="Covid 19":
        l=Label(k,text="Covid 19 :",font="cambria 20",fg="Black",bg="Green")
        l.place(x=50,y=100)
        l=Label(k,text="Treatment :",font="cambria 15",fg="White",bg="Green")
        l.place(x=80,y=200)
        n="""Monoclonal Antibodies
Manufactured in a laboratory, monoclonal antibodies are proteins that in some cases, can help your body fight infectious disease. Monoclonal antibody treatment is given by infusing the material into the bloodstream.
Mask: The caregiver should wear a triple layer medical mask. N95 mask may be considered when in the same room with the ill person.
Hand hygiene: Hand hygiene must be ensured following contact with ill person or patient’s immediate environment.
Exposure to patient/patient’s environment: Avoid direct contact with body fluids of the patient, particularly oral or respiratory secretions. Use disposable gloves while handling the patient. Perform hand hygiene before and after removing gloves."""
        l=Label(n,text=m,font="helvetica 13",fg="Black",bg="Green")
        l.place(x=80,y=300)
        b=Button(k,text="Exit",font="Pacifico 15 bold",fg="White",bg="Black",command=perform)
        b.place(x=750,y=550)

    elif dis=="Insomnia":
        l=Label(k,text="Insomnia :",font="cambria 20",fg="Black",bg="Green")
        l.place(x=50,y=100)
        l=Label(k,text="Treatment :",font="cambria 15",fg="White",bg="Green")
        l.place(x=80,y=200)
        o="""Stimulus control therapy.
This method helps remove factors that condition your mind to resist sleep. For example, you might be coached to set a consistent bedtime and wake time and avoid naps, use the bed only for sleep and sex, and leave the bedroom if you can't go to sleep within 20 minutes, only returning when you're sleepy.
Relaxation techniques.
Progressive muscle relaxation, biofeedback and breathing exercises are ways to reduce anxiety at bedtime. Practicing these techniques can help you control your breathing, heart rate, muscle tension and mood so that you can relax.
Sleep restriction.
This therapy decreases the time you spend in bed and avoids daytime naps, causing partial sleep deprivation, which makes you more tired the next night. Once your sleep has improved, your time in bed is gradually increased.
Remaining passively awake.
Also called paradoxical intention, this therapy for learned insomnia is aimed at reducing the worry and anxiety about being able to get to sleep by getting in bed and trying to stay awake rather than expecting to fall asleep."""
        l=Label(n,text=o,font="helvetica 13",fg="Black",bg="Green")
        l.place(x=80,y=300)
        b=Button(k,text="Exit",font="Pacifico 15 bold",fg="White",bg="Black",command=perform)
        b.place(x=750,y=550)

##########################################################################################################################################################################################################       

def login():
    email=e1.get()
    password=e2.get()
    if email==e1 and password==e2:
        return true
    messagebox.showinfo("","Login Success")
    
    global s
    s=Tk()
    s.geometry("1500x700")
    s.title("LOGIN PAGE")
    s.configure(bg="sky blue")
    l=Label(s,text="HEALTH CARE",font="Pacifico 25 bold",bg="sky blue",fg="Black")
    l.place(x=640,y=50)
    l=Label(s,text="Earth greatest grass for good. Place for divide evening yielding them that. Creeping beginning over gathered brought.",font="Shadowsintolight 15",bg="sky blue",fg="White")
    l.place(x=260,y=150)
    Frame(s,width=1050,height=6,bg="Black").place(x=250,y=180)
    l=Label(s,text="SYMPTOMS :",font="cambria 20",fg="Black",bg="Sky blue")
    l.place(x=530,y=250)
    global entry
    entry=Entry(s,fg="White",bg="Sky blue",font="helvetica 15",border=0)
    entry.place(x=690,y=255)
    Frame(s,width=260,height=2,bg="White").place(x=685,y=285)

    def update(data):
        lb.delete(0, END)

        for item in data:
            lb.insert(END, item)

    def fillout(y):
        entry.delete(0, END)
        entry.insert(0, lb.get(ACTIVE))

    def check(y):
        typed=entry.get()

        if typed=="":
            data=diseases
        else:
            data=[]
            for item in diseases:
                if typed.lower() in item.lower():
                    data.append(item)

        update(data)

    b=Button(s,text="Search",font="Pacifico 15 bold",border=0,fg="White",bg="Black",command=med)
    b.place(x=1000,y=255)

    global lb            
    lb=Listbox(s,width=40,fg="White",bg="Black",font="cambria 15")
    lb.place(x=580,y=400)
    diseases=["Acne","AIDS/HIV","Anxiety","Cancer","Colds&Flu","Diabetes","Diarrhea","Heart Disease","Pneumonia","Stroke","Covid 19","Insomnia"]
    update(diseases)

    lb.bind("<<ListboxSelect>>",fillout)

    entry.bind("<KeyRelease>",check)

    b=Button(s,text="Search",font="Pacifico 15 bold",border=0,fg="White",bg="Black",command=med)
    b.place(x=1000,y=255)


def perform():
    name1=e1.get()
    dob1=e2.get()
    mobile1=e3.get()
    email1=e4.get()
    password1=e5.get()
    sql="insert into signup (name,dob,mobile,email,password) VALUES (%s ,%s ,%s ,%s ,%s)"
    val=(name1,dob1,mobile1,email1,password1)
    mycursor.execute(sql,val)
    mydb.commit()
    print(name)
    print(dob)
    print(mobile)
    print(email)
    print(password)
-    

    
    h=Tk()
    h.geometry("1500x700")
    h.title("LOGIN PAGE")
    h.configure(bg="Black")
    l=Label(h,text="LOGIN",font="serif 35",fg="Wheat",bg="Black")
    l.place(x=700,y=80)
    f=Frame(h,width=450,height=350,bg="White")
    f.place(x=560,y=220)
    l=Label(h,text="Email:", font=("times new roman", 18, "bold"), bg="White",fg="Black")
    l.place(x=600, y=290)
    e6=Entry(h,fg="Black",font="Helvetica 15",border=0)
    e6.place(x=730,y=290)
    Frame(h,width=260,height=2,bg="Black").place(x=720,y=320)
    i=Label(h,text="Password:", font=("times new roman", 18, "bold"), bg="White",fg="Black")
    i.place(x=600, y=370)
    e7=Entry(h,fg="Black",font="Helvetica 15",border=0)
    e7.place(x=730,y=370)
    Frame(h,width=260,height=2,bg="Black").place(x=720,y=400)
    b=Button(h,text="Login",width=35,fg="Black",bg="Dark blue",command=login)
    b.place(x=660,y=450)
    b1=Button(h,text="Cancel",width=35,fg="Black",bg="Red",command=h.destroy)
    b1.place(x=660,y=500)


l=Label(w,text="SIGN UP",font="serif 30",bg="Purple")
l.place(x=700,y=30)
f=Frame(w,width=450,height=600,bg="White")
f.place(x=560,y=130)
name=Label(w,text="Name:", font=("times new roman", 18, "bold"), bg="White",fg="Black")
name.place(x=590, y=170)
e1=Entry(w,fg="Black",font="Helvetica 15",border=0)
e1.place(x=730,y=170)
Frame(w,width=260,height=2,bg="Black").place(x=720,y=200)
dob=Label(w,text="D.O.B:", font=("times new roman", 18, "bold"), bg="White",fg="Black")
dob.place(x=590, y=250)
e2=Entry(w,fg="Black",font="Helvetica 15",border=0)
e2.place(x=730,y=250)
Frame(w,width=260,height=2,bg="Black").place(x=720,y=280)
mobile=Label(w,text="Mobile. No:", font=("times new roman", 18, "bold"), bg="White",fg="Black")
mobile.place(x=590, y=330)
e3=Entry(w,fg="Black",font="Helvetica 15",border=0)
e3.place(x=730,y=330)
Frame(w,width=260,height=2,bg="Black").place(x=720,y=360)
email=Label(w,text="Email:", font=("times new roman", 18, "bold"), bg="White",fg="Black")
email.place(x=590, y=410)
e4=Entry(w,fg="Black",font="Helvetica 15",border=0)
e4.place(x=730,y=410)
Frame(w,width=260,height=2,bg="Black").place(x=720,y=440)
password=Label(w,text="Password:", font=("times new roman", 18, "bold"), bg="White",fg="Black")
password.place(x=590, y=490)
e5=Entry(w,fg="Black",font="Helvetica 15",border=0)
e5.place(x=730,y=490)
Frame(w,width=260,height=2,bg="Black").place(x=720,y=520)
b=Button(w,text="SIGN UP",width=35,fg="White",bg="Black",font="Pacifico 10 bold",command=perform)
b.place(x=640,y=600)
l=Label(w,text="Already a member?",fg="Black",bg="White",border=0,font="Chakrapetch 10")
l.place(x=690,y=670)
b1=Button(w,text="Sign In",border=0,bg="White",fg="Red",font="Chakrapetch 10",command=perform)
b1.place(x=810,y=666)






    



        
    
        
