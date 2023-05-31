import os
import re
import time
from flask import Flask,render_template,redirect,request
from flask.helpers import get_load_dotenv, total_seconds
from modelapp2 import db,Booking,Payment

top1 = 50
middle1 = 50
bottom1 = 50

top2 = 50
middle2 = 50
bottom2 = 50

top3 = 50
middle3 = 50
bottom3 = 50

top4 = 50
middle4 = 50
bottom4 = 50

app = Flask(__name__,template_folder='templates')
app.secret_key = 'super secret key'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/form1',methods=['GET','POST'])
def form1():
    global top1
    global middle1
    global bottom1
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        row=request.form['row']
        numbert=request.form['tickets']
        paymentm=request.form['payment']
 
        numbert = int(numbert)

        if row == 'Top' and top1-numbert>=0:
            amt = int(numbert)*300
            top1-=numbert
            b = 'Tickets booked in top row'
        elif row=='Middle'and middle1-numbert>=0:
            amt = int(numbert)*250
            middle1-=numbert
            b = 'Tickets booked in middle row'
        elif row=='Bottom' and bottom1-numbert>=0:
            amt = int(numbert)*200
            bottom1-=numbert   
            b = 'Tickets booked in bottom row'
        elif row=='Top' and top1==0 or top1-numbert<0 and middle1>0 or bottom1>0:
            if middle1>0 and middle1-numbert>0:
                b='We have booked your seats in the middle row as top was full, Sorry for the inconvinenece caused'
                amt = int(numbert)*250
                middle1-=numbert
            elif bottom1>0 and bottom1-numbert>0:
                b='We have booked your seats in the bottom row as top was full, Sorry for the inconvinenece caused'
                amt = int(numbert)*200
                bottom1-=numbert
            else:
                b='We are not having enough vacant seats, Sorry'
        elif row =='Middle' and middle1==0 or middle1-numbert<0 and top1>0 or bottom1>0:
            if top1>0 and top1-numbert>0 :
                b='We have booked your seats in the top row as middle was full at cost of middle row seats'
                amt = int(numbert)*250
                top1-=numbert
            elif bottom1>0 and bottom1-numbert>0:
                b='We have booked your seats in the bottom row as middle was full, Sorry for the inconvinenece caused'
                amt = int(numbert)*200
                bottom1-=numbert
            else:
                b='We are not having enough vacant seats, Sorry'
        elif row == 'Bottom' and bottom1==0 or bottom1-numbert<0 and top1>0 or middle1>0:
            if top1>0 and top1-numbert>0 :
                b='We have booked your seats in the top row as bottom was full at cost of bottom row seats'
                amt = int(numbert)*200
                top1-=numbert
            elif middle1>0 and middle1-numbert>0:
                b='We have booked your seats in the middle row as bottom was full at cost of bottom row seats'
                amt = int(numbert)*200
                bottom1-=numbert
            else:
                b='We are not having enough vacant seats, Sorry'
        else:
            b='We are not having enough vacant seats, Sorry'

        #print(top1)

        if str(paymentm)=='Debit Card' or 'Credit Card':
            m=1
        elif str(paymentm)=="Cash":
            m=2

        
        book=Booking(name=name,email=email,row=row,numbert=numbert,paymentm=paymentm)

        db.session.add(book)
        db.session.commit()
        return render_template('payform.html',amt=amt,m=paymentm,b=b)      
    else:
        return render_template('form2.html', mn = 'Shang Chi', t='11.00 am to 1.45 pm')

@app.route('/form2',methods=['GET','POST'])
def form2():
    global top2
    global middle2
    global bottom2
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        row=request.form['row']
        numbert=request.form['tickets']
        paymentm=request.form['payment']
 
        numbert = int(numbert)

        if row == 'Top' and top2-numbert>=0:
            amt = int(numbert)*300
            top2-=numbert
            b = 'Tickets booked in top row'
        elif row=='Middle'and middle2-numbert>=0:
            amt = int(numbert)*250
            middle2-=numbert
            b = 'Tickets booked in middle row'
        elif row=='Bottom' and bottom2-numbert>=0:
            amt = int(numbert)*200
            bottom2-=numbert   
            b = 'Tickets booked in bottom row'
        elif row=='Top' and top2==0 or top2-numbert<0 and middle2>0 or bottom2>0:
            if middle2>0 and middle2-numbert>0:
                b='We have booked your seats in the middle row as top was full, Sorry for the inconvinenece caused'
                amt = int(numbert)*250
                middle2-=numbert
            elif bottom2>0 and bottom2-numbert>0:
                b='We have booked your seats in the bottom row as top was full, Sorry for the inconvinenece caused'
                amt = int(numbert)*200
                bottom2-=numbert
            else:
                b='We are not having enough vacant seats, Sorry'
        elif row =='Middle' and middle2==0 or middle2-numbert<0 and top2>0 or bottom2>0:
            if top2>0 and top2-numbert>0 :
                b='We have booked your seats in the top row as middle was full at cost of middle row seats'
                amt = int(numbert)*250
                top2-=numbert
            elif bottom2>0 and bottom2-numbert>0:
                b='We have booked your seats in the bottom row as middle was full, Sorry for the inconvinenece caused'
                amt = int(numbert)*200
                bottom2-=numbert
            else:
                b='We are not having enough vacant seats, Sorry'
        elif row == 'Bottom' and bottom2==0 or bottom2-numbert<0 and top2>0 or middle2>0:
            if top2>0 and top2-numbert>0 :
                b='We have booked your seats in the top row as bottom was full at cost of bottom row seats'
                amt = int(numbert)*200
                top2-=numbert
            elif middle2>0 and middle2-numbert>0:
                b='We have booked your seats in the middle row as bottom was full at cost of bottom row seats'
                amt = int(numbert)*200
                bottom2-=numbert
            else:
                b='We are not having enough vacant seats, Sorry'
        else:
            b='We are not having enough vacant seats, Sorry'

        #print(top2)

        if str(paymentm)=='Debit Card' or 'Credit Card':
            m=1
        elif str(paymentm)=="Cash":
            m=2

        
        book=Booking(name=name,email=email,row=row,numbert=numbert,paymentm=paymentm)

        db.session.add(book)
        db.session.commit()
        return render_template('payform.html',amt=amt,m=paymentm,b=b)      
    else:
        return render_template('form2.html',  mn = 'Black Widow', t = '2 pm to 4:15 pm')

@app.route('/form3',methods=['GET','POST'])
def form3():
    global top3
    global middle3
    global bottom3
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        row=request.form['row']
        numbert=request.form['tickets']
        paymentm=request.form['payment']
 
        numbert = int(numbert)

        if row == 'Top' and top3-numbert>=0:
            amt = int(numbert)*300
            top3-=numbert
            b = 'Tickets booked in top row'
        elif row=='Middle'and middle3-numbert>=0:
            amt = int(numbert)*250
            middle3-=numbert
            b = 'Tickets booked in middle row'
        elif row=='Bottom' and bottom3-numbert>=0:
            amt = int(numbert)*200
            bottom3-=numbert   
            b = 'Tickets booked in bottom row'
        elif row=='Top' and top3==0 or top3-numbert<0 and middle3>0 or bottom3>0:
            if middle3>0 and middle3-numbert>0:
                b='We have booked your seats in the middle row as top was full, Sorry for the inconvinenece caused'
                amt = int(numbert)*250
                middle3-=numbert
            elif bottom3>0 and bottom3-numbert>0:
                b='We have booked your seats in the bottom row as top was full, Sorry for the inconvinenece caused'
                amt = int(numbert)*200
                bottom3-=numbert
            else:
                b='We are not having enough vacant seats, Sorry'
        elif row =='Middle' and middle3==0 or middle3-numbert<0 and top3>0 or bottom3>0:
            if top3>0 and top3-numbert>0 :
                b='We have booked your seats in the top row as middle was full at cost of middle row seats'
                amt = int(numbert)*250
                top3-=numbert
            elif bottom3>0 and bottom3-numbert>0:
                b='We have booked your seats in the bottom row as middle was full, Sorry for the inconvinenece caused'
                amt = int(numbert)*200
                bottom3-=numbert
            else:
                b='We are not having enough vacant seats, Sorry'
        elif row == 'Bottom' and bottom3==0 or bottom3-numbert<0 and top3>0 or middle3>0:
            if top3>0 and top3-numbert>0 :
                b='We have booked your seats in the top row as bottom was full at cost of bottom row seats'
                amt = int(numbert)*200
                top3-=numbert
            elif middle3>0 and middle3-numbert>0:
                b='We have booked your seats in the middle row as bottom was full at cost of bottom row seats'
                amt = int(numbert)*200
                bottom3-=numbert
            else:
                b='We are not having enough vacant seats, Sorry'
        else:
            b='We are not having enough vacant seats, Sorry'

        #print(top3)

        if str(paymentm)=='Debit Card' or 'Credit Card':
            m=1
        elif str(paymentm)=="Cash":
            m=2

        
        book=Booking(name=name,email=email,row=row,numbert=numbert,paymentm=paymentm)

        db.session.add(book)
        db.session.commit()
        return render_template('payform.html',amt=amt,m=paymentm,b=b)      
    else:
        return render_template('form2.html',  mn = 'Fast And Furious 9' , t = '5:00 pm to 8:00 pm')

@app.route('/form4',methods=['GET','POST'])
def form4():
    global top4
    global middle4
    global bottom4
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        row=request.form['row']
        numbert=request.form['tickets']
        paymentm=request.form['payment']
 
        numbert = int(numbert)

        if row == 'Top' and top4-numbert>=0:
            amt = int(numbert)*300
            top4-=numbert
            b = 'Tickets booked in top row'
        elif row=='Middle'and middle4-numbert>=0:
            amt = int(numbert)*250
            middle4-=numbert
            b = 'Tickets booked in middle row'
        elif row=='Bottom' and bottom4-numbert>=0:
            amt = int(numbert)*200
            bottom4-=numbert   
            b = 'Tickets booked in bottom row'
        elif row=='Top' and top4==0 or top4-numbert<0 and middle4>0 or bottom4>0:
            if middle4>0 and middle4-numbert>0:
                b='We have booked your seats in the middle row as top was full, Sorry for the inconvinenece caused'
                amt = int(numbert)*250
                middle4-=numbert
            elif bottom4>0 and bottom4-numbert>0:
                b='We have booked your seats in the bottom row as top was full, Sorry for the inconvinenece caused'
                amt = int(numbert)*200
                bottom4-=numbert
            else:
                b='We are not having enough vacant seats, Sorry'
        elif row =='Middle' and middle4==0 or middle4-numbert<0 and top4>0 or bottom4>0:
            if top4>0 and top4-numbert>0 :
                b='We have booked your seats in the top row as middle was full at cost of middle row seats'
                amt = int(numbert)*250
                top4-=numbert
            elif bottom4>0 and bottom4-numbert>0:
                b='We have booked your seats in the bottom row as middle was full, Sorry for the inconvinenece caused'
                amt = int(numbert)*200
                bottom4-=numbert
            else:
                b='We are not having enough vacant seats, Sorry'
        elif row == 'Bottom' and bottom4==0 or bottom4-numbert<0 and top4>0 or middle4>0:
            if top4>0 and top4-numbert>0 :
                b='We have booked your seats in the top row as bottom was full at cost of bottom row seats'
                amt = int(numbert)*200
                top4-=numbert
            elif middle4>0 and middle4-numbert>0:
                b='We have booked your seats in the middle row as bottom was full at cost of bottom row seats'
                amt = int(numbert)*200
                bottom4-=numbert
            else:
                b='We are not having enough vacant seats, Sorry'
        else:
            b='We are not having enough vacant seats, Sorry'

        #print(top4)

        if str(paymentm)=='Debit Card' or 'Credit Card':
            m=1
        elif str(paymentm)=="Cash":
            m=2

        
        book=Booking(name=name,email=email,row=row,numbert=numbert,paymentm=paymentm)

        db.session.add(book)
        db.session.commit()
        return render_template('payform.html',amt=amt,m=paymentm,b=b)      
    else:
        return render_template('form2.html',  mn = 'Bell Bottom' , t='8:15 pm to 10:30pm')



@app.route('/paymentform',methods=['GET','POST'])
def pform():
    if request.method=='POST':
        namec=request.form['name-card']
        cardno=request.form['number-card']
        expirey=request.form['month-card']
        cvv=request.form['cvv']
        message=request.form['Message']

        payment = Payment(namec=namec,cardno=cardno,expirey=expirey,cvv=cvv,message=message)

        db.session.add(payment)
        db.session.commit()
        return render_template('thankyou.html')
    else:
        return render_template('payform.html')

@app.route('/paymentformcash',methods=['GET','POST'])
def pformcash():
    if request.method=='POST':
        namec=None
        cardno=None
        expirey=None
        cvv=None
        message=request.form['Message']

        payment = Payment(namec=namec,cardno=cardno,expirey=expirey,cvv=cvv,message=message)

        db.session.add(payment)
        db.session.commit()
        return render_template('thankyou.html')
    else:
        return render_template('payform.html')

@app.route('/bhome',methods=['GET','POST'])
def bhome():
    if request.method=='POST':
        return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)