from personal import db

personal_bankmembership = db.Table('personal_bankmembership',
                          db.Column('bank_id', db.Integer, db.ForeignKey(
                                       'personal_bankinfo.id')),
                          db.Column('person_id', db.Integer, db.ForeignKey(
                                       'personal_personalinfo.id')),
                          db.Column('acct_type', db.String(2)),
                          db.Column('acctnbr', db.String(15)))

class Personalinfo(db.Model):
    __tablename__ = 'personal_personalinfo'
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(2), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(500), nullable=False)
    last_name = db.Column(db.String(500), nullable=False)
    middle_name = db.Column(db.String(500), nullable=False)
    emailid = db.Column(db.String(500), nullable=False)
    _banks = db.relationship('Bankinfo', backref='persons', secondary=personal_bankmembership)
    _addresses = db.relationship('Addressinfo', backref='_persons')

class Addressinfo(db.Model):
    __tablename__ = 'personal_addressinfo'
    id = db.Column(db.Integer, primary_key=True)
    address_type = db.Column(db.String(1), nullable=False)
    door = db.Column(db.Integer, nullable=False)
    street = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    pin = db.Column(db.Integer, nullable=False)
    person_id = db.Column(db.ForeignKey('personal_personalinfo.id'))
    personAddress= db.relationship('Personalinfo', backref='addresses')

class Bankinfo(db.Model):
    __tablename__ = 'personal_bankinfo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(2000), nullable=False)
    branch = db.Column(db.String(2000))
    address = db.Column(db.String(2000), nullable=False)
    phone_nbr = db.Column(db.String(15), nullable=False)
    bnk_abbr_name = db.Column(db.String(200))
    brn_abbr_name = db.Column(db.String(200))
    person = db.relationship('Personalinfo', backref='banks', secondary=personal_bankmembership)
