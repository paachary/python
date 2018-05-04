from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class PersonalInfo(Base):
    __tablename__ = 'personal_personalinfo'
    __table_args__ = (
        UniqueConstraint('first_name', 'middle_name', 'last_name'),
    )

    id = Column(Integer, primary_key=True)
    gender = Column(String(2), nullable=False)
    age = Column(Integer, nullable=False)
    first_name = Column(String(500), nullable=False)
    last_name = Column(String(500), nullable=False)
    middle_name = Column(String(500), nullable=False)
    emailid = Column(String(500), nullable=False)
    phoneinfo = relationship("PersonalPhoneinfo", back_populates="person")
    address = relationship("PersonalAddressinfo", back_populates="person")
    bank_membership = relationship("PersonalBankmembership",
                                   back_populates="person")


class PersonalPhoneinfo(Base):
    __tablename__ = 'personal_phoneinfo'
    __table_args__ = (
        UniqueConstraint('person_id', 'phone_type', 'phone_nbr'),
    )
    id = Column(Integer, primary_key=True)
    phone_type = Column(String(1), nullable=False)
    person_id = Column(ForeignKey('personal_personalinfo.id', deferrable=True,
                       initially='DEFERRED'), nullable=False, index=True)
    phone_nbr = Column(String(15), nullable=False)
    person = relationship('PersonalInfo', back_populates="phoneinfo")


class PersonalAddressinfo(Base):
    __tablename__ = 'personal_addressinfo'
    __table_args__ = (
        UniqueConstraint('person_id', 'address_type'),
    )

    id = Column(Integer, primary_key=True)
    address_type = Column(String(1), nullable=False)
    door = Column(Integer, nullable=False)
    street = Column(String(200), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    person_id = Column(ForeignKey('personal_personalinfo.id', deferrable=True,
                       initially='DEFERRED'), nullable=False, index=True)
    pin = Column(Integer, nullable=False)
    person = relationship('PersonalInfo', back_populates="address")


class PersonalBankmembership(Base):
    __tablename__ = 'personal_bankmembership'
    __table_args__ = (
        UniqueConstraint('person_id', 'bank_id', 'acct_type', 'acctnbr'),
    )
    id = Column(Integer, primary_key=True)
    acct_type = Column(String(2), nullable=False)
    bank_id = Column(ForeignKey('personal_bankinfo.id', deferrable=True,
                     initially='DEFERRED'), nullable=False, index=True)
    person_id = Column(ForeignKey('personal_personalinfo.id', deferrable=True,
                       initially='DEFERRED'), nullable=False, index=True)
    acctnbr = Column(String(15), nullable=False)
    bank = relationship('PersonalBankInfo', back_populates="bank_info")
    person = relationship('PersonalInfo', back_populates="bank_membership")


class PersonalBankInfo(Base):
    __tablename__ = 'personal_bankinfo'
    __table_args__ = (
        UniqueConstraint('name', 'branch'),
    )
    id = Column(Integer, primary_key=True)
    name = Column(String(2000), nullable=False)
    branch = Column(String(2000))
    address = Column(String(2000), nullable=False)
    phone_nbr = Column(String(15), nullable=False)
    bnk_abbr_name = Column(String(200))
    brn_abbr_name = Column(String(200))
    bank_info = relationship("PersonalBankmembership", back_populates="bank")
