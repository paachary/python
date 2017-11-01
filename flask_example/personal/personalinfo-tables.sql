class PersonalAddressinfo(Base):
    __tablename__ = 'personal_addressinfo'
    __table_args__ = (
        UniqueConstraint('person_id', 'address_type'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('personal_addressinfo_id_seq'::regclass)"))
    address_type = Column(String(1), nullable=False)
    door = Column(Integer, nullable=False)
    street = Column(String(200), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    person_id = Column(ForeignKey('personal_personalinfo.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    pin = Column(Integer, nullable=False)

    person = relationship('PersonalPersonalinfo')


class PersonalBankdebitdetail(Base):
    __tablename__ = 'personal_bankdebitdetails'

    id = Column(Integer, primary_key=True, server_default=text("nextval('personal_bankdebitdetails_id_seq'::regclass)"))
    debit_dt = Column(Date, nullable=False)
    debit_type = Column(String(2), nullable=False)
    debit_desc = Column(String(2000), nullable=False)
    amount = Column(Integer, nullable=False)
    remarks = Column(String(2000), nullable=False)
    bankmembership_id = Column(ForeignKey('personal_bankmembership.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    bankmembership = relationship('PersonalBankmembership')


class PersonalBankinfo(Base):
    __tablename__ = 'personal_bankinfo'
    __table_args__ = (
        UniqueConstraint('name', 'branch'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('personal_bankinfo_id_seq'::regclass)"))
    name = Column(String(2000), nullable=False)
    branch = Column(String(2000))
    address = Column(String(2000), nullable=False)
    phone_nbr = Column(String(15), nullable=False)
    bnk_abbr_name = Column(String(200))
    brn_abbr_name = Column(String(200))


class PersonalBankmembership(Base):
    __tablename__ = 'personal_bankmembership'
    __table_args__ = (
        UniqueConstraint('person_id', 'bank_id', 'acct_type', 'acctnbr'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('personal_bankmembership_id_seq'::regclass)"))
    acct_type = Column(String(2), nullable=False)
    bank_id = Column(ForeignKey('personal_bankinfo.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    person_id = Column(ForeignKey('personal_personalinfo.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    acctnbr = Column(String(15), nullable=False)

    bank = relationship('PersonalBankinfo')
    person = relationship('PersonalPersonalinfo')


class PersonalPersonalinfo(Base):
    __tablename__ = 'personal_personalinfo'
    __table_args__ = (
        UniqueConstraint('first_name', 'middle_name', 'last_name'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('personal_personalinfo_id_seq'::regclass)"))
    gender = Column(String(2), nullable=False)
    age = Column(Integer, nullable=False)
    first_name = Column(String(500), nullable=False)
    last_name = Column(String(500), nullable=False)
    middle_name = Column(String(500), nullable=False)
    emailid = Column(String(500), nullable=False)
    dob = Column(Date)


class PersonalPhoneinfo(Base):
    __tablename__ = 'personal_phoneinfo'
    __table_args__ = (
        UniqueConstraint('person_id', 'phone_type', 'phone_nbr'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('personal_phoneinfo_id_seq'::regclass)"))
    phone_type = Column(String(1), nullable=False)
    person_id = Column(ForeignKey('personal_personalinfo.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    phone_nbr = Column(String(15), nullable=False)

    person = relationship('PersonalPersonalinfo')