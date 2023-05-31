from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data2.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Booking(db.Model):

    __tablename__ = 'booking_info'

    id = db.Column(db.Integer,nullable=False,primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(320),nullable=False)
    row = db.Column(db.String(6),nullable=False)
    numbert = db.Column(db.Integer,nullable=False)
    paymentm = db.Column(db.String(20),nullable=False)
    

    def __init__(self,name,email,row,numbert,paymentm) -> None:
        self.name=name
        self.email=email
        self.row=row
        self.numbert=numbert
        self.paymentm=paymentm
        

class Payment(db.Model):

    __tablename__='Payment'

    id = db.Column(db.Integer,nullable=False,primary_key=True)
    namec = db.Column(db.String(80),nullable=True)
    cardno = db.Column(db.BigInteger,nullable=True)
    expirey = db.Column(db.Integer,nullable=True)
    cvv = db.Column(db.Integer,nullable=True)
    message = db.Column(db.Text,nullable=True)

    def __init__(self,namec,cardno,expirey,cvv,message) -> None:
        self.namec=namec
        self.cardno=cardno
        self.expirey=expirey
        self.cvv=cvv
        self.message=message
       
#db.drop_all()
db.create_all()
db.session.commit()