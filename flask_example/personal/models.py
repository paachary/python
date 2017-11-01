from personal import db
import datetime

from sqlalchemy import UniqueConstraint, ForeignKey, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata

class Personalinfo(Base, db.Model):
    __tablename__ = 'personal_personalinfo'
    __table_args__ = (
        UniqueConstraint('first_name', 'middle_name', 'last_name'),
    )

    id = db.Column(db.Integer, primary_key=True, server_default=text(
        "nextval('personal_personalinfo_id_seq'::regclass)")
        )
    gender = db.Column(db.String(2), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(500), nullable=False)
    last_name = db.Column(db.String(500), nullable=False)
    middle_name = db.Column(db.String(500), nullable=False)
    emailid = db.Column(db.String(500), nullable=False)
#    dob = db.Column(datetime)


class Addressinfo(Base, db.Model):
    __tablename__ = 'personal_addressinfo'
#    __table_args__ = (
#        UniqueConstraint('person_id', 'address_type'),
#    )

    id = db.Column(db.Integer, primary_key=True, server_default=text(
        "nextval('personal_addressinfo_id_seq'::regclass)")
 )
    address_type = db.Column(db.String(1), nullable=False)
    door = db.Column(db.Integer, nullable=False)
    street = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    person_id = db.Column(ForeignKey('personal_personalinfo.id',
                                  deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    pin = db.Column(db.Integer, nullable=False)

    person = relationship('Personalinfo')


class Bankdebitdetail(Base, db.Model):
    __tablename__ = 'personal_bankdebitdetails'

    id = db.Column(db.Integer, primary_key=True, server_default=text(
        "nextval('personal_bankdebitdetails_id_seq'::regclass)"))
    debit_dt = db.Column(db.Date, nullable=False)
    debit_type = db.Column(db.String(2), nullable=False)
    debit_desc = db.Column(db.String(2000), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    remarks = db.Column(db.String(2000), nullable=False)
    bankmembership_id = db.Column(ForeignKey(
        'personal_bankmembership.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    bankmembership = relationship('Bankmembership')


class Bankinfo(Base, db.Model):
    __tablename__ = 'personal_bankinfo'
    __table_args__ = (
        UniqueConstraint('name', 'branch'),
    )

    id = db.Column(db.Integer, primary_key=True, server_default=text(
        "nextval('personal_bankinfo_id_seq'::regclass)"))
    name = db.Column(db.String(2000), nullable=False)
    branch = db.Column(db.String(2000))
    address = db.Column(db.String(2000), nullable=False)
    phone_nbr = db.Column(db.String(15), nullable=False)
    bnk_abbr_name = db.Column(db.String(200))
    brn_abbr_name = db.Column(db.String(200))


class Bankmembership(Base, db.Model):
    __tablename__ = 'personal_bankmembership'
    __table_args__ = (
        UniqueConstraint('person_id', 'bank_id', 'acct_type', 'acctnbr'),
    )

    id = db.Column(db.Integer, primary_key=True, server_default=text(
        "nextval('personal_bankmembership_id_seq'::regclass)"))
    acct_type = db.Column(db.String(2), nullable=False)
    bank_id = db.Column(ForeignKey('personal_bankinfo.id', deferrable=True,
                                   initially='DEFERRED'), nullable=False, index=True)
    person_id = db.Column(ForeignKey('personal_personalinfo.id',
                                     deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    acctnbr = db.Column(db.String(15), nullable=False)

    bank = relationship('Bankinfo')
    person = relationship('Personalinfo')


class Phoneinfo(Base, db.Model):
    __tablename__ = 'personal_phoneinfo'
    __table_args__ = (
        UniqueConstraint('person_id', 'phone_type', 'phone_nbr'),
    )

    id = db.Column(db.Integer, primary_key=True, server_default=text(
        "nextval('personal_phoneinfo_id_seq'::regclass)"))
    phone_type = db.Column(db.String(1), nullable=False)
    person_id = db.Column(ForeignKey('personal_personalinfo.id',
                                     deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    phone_nbr = db.Column(db.String(15), nullable=False)

    person = relationship('Personalinfo')
