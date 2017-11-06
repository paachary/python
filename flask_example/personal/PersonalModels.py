import json
from datetime import datetime
from uuid import uuid4, UUID
from personal import ma, db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import Schema, fields

### Code generation tool for extracting existing tables into a model

#sqlacodegen postgresql://polldb_user:polldb_user@localhost:5432/polldb --outfile PersonalModels.py

# coding: utf-8
from sqlalchemy import Boolean, CheckConstraint, Column, Date, DateTime, ForeignKey, Integer, SmallInteger, String, Text, UniqueConstraint, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

from sqlalchemy.ext.declarative import DeclarativeMeta

"""
class OutputMixin(object):
    print("PRAX:: in OutputMixin ")
    RELATIONSHIPS_TO_DICT = False

    def __iter__(self):
        return self.to_dict().iteritems()

    def to_dict(self, rel=None, backref=None):
        if rel is None:
            rel = self.RELATIONSHIPS_TO_DICT
        res = {column.key: getattr(self, attr)
               for attr, column in self.__mapper__.c.items()}
        if rel:
            for attr, relation in self.__mapper__.relationships.items():
                # Avoid recursive loop between to tables.
                if backref == relation.table:
                    continue
                value = getattr(self, attr)
                if value is None:
                    res[relation.key] = None
                elif isinstance(value.__class__, DeclarativeMeta):
                    res[relation.key] = value.to_dict(backref=self.__table__)
                else:
                    res[relation.key] = [i.to_dict(backref=self.__table__)
                                         for i in value]
        return res

    def to_json(self, rel=None):
        def extended_encoder(x):
            if isinstance(x, datetime):
                return x.isoformat()
            if isinstance(x, UUID):
                return str(x)
        if rel is None:
            rel = self.RELATIONSHIPS_TO_DICT
        return json.dumps(self.to_dict(rel), default=extended_encoder)
"""
class AbPermission(Base):
    __tablename__ = 'ab_permission'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)


class AbPermissionView(Base):
    __tablename__ = 'ab_permission_view'

    id = Column(Integer, primary_key=True)
    permission_id = Column(ForeignKey('ab_permission.id'))
    view_menu_id = Column(ForeignKey('ab_view_menu.id'))

    permission = relationship('AbPermission')
    view_menu = relationship('AbViewMenu')


class AbPermissionViewRole(Base):
    __tablename__ = 'ab_permission_view_role'

    id = Column(Integer, primary_key=True)
    permission_view_id = Column(ForeignKey('ab_permission_view.id'))
    role_id = Column(ForeignKey('ab_role.id'))

    permission_view = relationship('AbPermissionView')
    role = relationship('AbRole')


class AbRegisterUser(Base):
    __tablename__ = 'ab_register_user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    username = Column(String(64), nullable=False, unique=True)
    password = Column(String(256))
    email = Column(String(64), nullable=False)
    registration_date = Column(DateTime)
    registration_hash = Column(String(256))


class AbRole(Base):
    __tablename__ = 'ab_role'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, unique=True)


class AbUser(Base):
    __tablename__ = 'ab_user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    username = Column(String(64), nullable=False, unique=True)
    password = Column(String(256))
    active = Column(Boolean)
    email = Column(String(64), nullable=False, unique=True)
    last_login = Column(DateTime)
    login_count = Column(Integer)
    fail_login_count = Column(Integer)
    created_on = Column(DateTime)
    changed_on = Column(DateTime)
    created_by_fk = Column(ForeignKey('ab_user.id'))
    changed_by_fk = Column(ForeignKey('ab_user.id'))

    parent = relationship('AbUser', remote_side=[id], primaryjoin='AbUser.changed_by_fk == AbUser.id')
    parent1 = relationship('AbUser', remote_side=[id], primaryjoin='AbUser.created_by_fk == AbUser.id')


class AbUserRole(Base):
    __tablename__ = 'ab_user_role'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('ab_user.id'))
    role_id = Column(ForeignKey('ab_role.id'))

    role = relationship('AbRole')
    user = relationship('AbUser')


class AbViewMenu(Base):
    __tablename__ = 'ab_view_menu'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)


class AuthGroup(Base):
    __tablename__ = 'auth_group'

    id = Column(Integer, primary_key=True, server_default=text("nextval('auth_group_id_seq'::regclass)"))
    name = Column(String(80), nullable=False, unique=True)


class AuthGroupPermission(Base):
    __tablename__ = 'auth_group_permissions'
    __table_args__ = (
        UniqueConstraint('group_id', 'permission_id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('auth_group_permissions_id_seq'::regclass)"))
    group_id = Column(ForeignKey('auth_group.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    permission_id = Column(ForeignKey('auth_permission.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    group = relationship('AuthGroup')
    permission = relationship('AuthPermission')


class AuthPermission(Base):
    __tablename__ = 'auth_permission'
    __table_args__ = (
        UniqueConstraint('content_type_id', 'codename'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('auth_permission_id_seq'::regclass)"))
    name = Column(String(255), nullable=False)
    content_type_id = Column(ForeignKey('django_content_type.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    codename = Column(String(100), nullable=False)

    content_type = relationship('DjangoContentType')


class AuthUser(Base):
    __tablename__ = 'auth_user'

    id = Column(Integer, primary_key=True, server_default=text("nextval('auth_user_id_seq'::regclass)"))
    password = Column(String(128), nullable=False)
    last_login = Column(DateTime(True))
    is_superuser = Column(Boolean, nullable=False)
    username = Column(String(150), nullable=False, unique=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(254), nullable=False)
    is_staff = Column(Boolean, nullable=False)
    is_active = Column(Boolean, nullable=False)
    date_joined = Column(DateTime(True), nullable=False)


class AuthUserGroup(Base):
    __tablename__ = 'auth_user_groups'
    __table_args__ = (
        UniqueConstraint('user_id', 'group_id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('auth_user_groups_id_seq'::regclass)"))
    user_id = Column(ForeignKey('auth_user.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    group_id = Column(ForeignKey('auth_group.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    group = relationship('AuthGroup')
    user = relationship('AuthUser')


class AuthUserUserPermission(Base):
    __tablename__ = 'auth_user_user_permissions'
    __table_args__ = (
        UniqueConstraint('user_id', 'permission_id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('auth_user_user_permissions_id_seq'::regclass)"))
    user_id = Column(ForeignKey('auth_user.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    permission_id = Column(ForeignKey('auth_permission.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    permission = relationship('AuthPermission')
    user = relationship('AuthUser')

class Benefit(Base):
    __tablename__ = 'benefit'

    id = Column(Integer, primary_key=True, server_default=text("nextval('benefit_id_seq'::regclass)"))
    name = Column(String(50), nullable=False, unique=True)


class BenefitsEmployee(Base):
    __tablename__ = 'benefits_employee'

    id = Column(Integer, primary_key=True, server_default=text("nextval('benefits_employee_id_seq'::regclass)"))
    benefit_id = Column(ForeignKey('benefit.id'))
    employee_id = Column(ForeignKey('employee.id'))

    benefit = relationship('Benefit')
    employee = relationship('Employee')


class Contact(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True, server_default=text("nextval('contact_id_seq'::regclass)"))
    name = Column(String(150), nullable=False, unique=True)
    address = Column(String(564))
    birthday = Column(Date)
    personal_phone = Column(String(20))
    personal_celphone = Column(String(20))
    contact_group_id = Column(ForeignKey('contact_group.id'), nullable=False)
    gender_id = Column(ForeignKey('gender.id'), nullable=False)

    contact_group = relationship('ContactGroup')
    gender = relationship('Gender')


class ContactGroup(Base):
    __tablename__ = 'contact_group'

    id = Column(Integer, primary_key=True, server_default=text("nextval('contact_group_id_seq'::regclass)"))
    name = Column(String(50), nullable=False, unique=True)


class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True, server_default=text("nextval('department_id_seq'::regclass)"))
    name = Column(String(50), nullable=False, unique=True)


class DjangoAdminLog(Base):
    __tablename__ = 'django_admin_log'
    __table_args__ = (
        CheckConstraint('action_flag >= 0'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('django_admin_log_id_seq'::regclass)"))
    action_time = Column(DateTime(True), nullable=False)
    object_id = Column(Text)
    object_repr = Column(String(200), nullable=False)
    action_flag = Column(SmallInteger, nullable=False)
    change_message = Column(Text, nullable=False)
    content_type_id = Column(ForeignKey('django_content_type.id', deferrable=True, initially='DEFERRED'), index=True)
    user_id = Column(ForeignKey('auth_user.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    content_type = relationship('DjangoContentType')
    user = relationship('AuthUser')


class DjangoContentType(Base):
    __tablename__ = 'django_content_type'
    __table_args__ = (
        UniqueConstraint('app_label', 'model'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('django_content_type_id_seq'::regclass)"))
    app_label = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)


class DjangoMigration(Base):
    __tablename__ = 'django_migrations'

    id = Column(Integer, primary_key=True, server_default=text("nextval('django_migrations_id_seq'::regclass)"))
    app = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    applied = Column(DateTime(True), nullable=False)


class DjangoSession(Base):
    __tablename__ = 'django_session'

    session_key = Column(String(40), primary_key=True, index=True)
    session_data = Column(Text, nullable=False)
    expire_date = Column(DateTime(True), nullable=False, index=True)


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, server_default=text("nextval('employee_id_seq'::regclass)"))
    full_name = Column(String(150), nullable=False)
    address = Column(String(250), nullable=False)
    fiscal_number = Column(Integer, nullable=False)
    employee_number = Column(Integer, nullable=False)
    department_id = Column(ForeignKey('department.id'), nullable=False)
    function_id = Column(ForeignKey('function.id'), nullable=False)
    begin_date = Column(Date)
    end_date = Column(Date)

    department = relationship('Department')
    function = relationship('Function')


class EmployeeHistory(Base):
    __tablename__ = 'employee_history'

    id = Column(Integer, primary_key=True, server_default=text("nextval('employee_history_id_seq'::regclass)"))
    department_id = Column(ForeignKey('department.id'), nullable=False)
    employee_id = Column(ForeignKey('employee.id'), nullable=False)
    begin_date = Column(Date)
    end_date = Column(Date)

    department = relationship('Department')
    employee = relationship('Employee')


class Function(Base):
    __tablename__ = 'function'

    id = Column(Integer, primary_key=True, server_default=text("nextval('function_id_seq'::regclass)"))
    name = Column(String(50), nullable=False, unique=True)


class Gender(Base):
    __tablename__ = 'gender'

    id = Column(Integer, primary_key=True, server_default=text("nextval('gender_id_seq'::regclass)"))
    name = Column(String(50), nullable=False, unique=True)


class PersonalAddressinfo(Base, db.Model):
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
    person = relationship('PersonalPersonalinfo', back_populates="address")

    def __repr__(self):
        return "{addressType:'%s',door:'%s', street:'%s', city=%s', state='%s', country='%s'}" %(self.address_type, \
                                        self.door, self.street, self.city,\
                                        self.state, self.country)


    def __str__(self):
        return ("id:",self.id,",address_type:",self.address_type)



class PersonalBankdebitdetail(Base, db.Model):
    __tablename__ = 'personal_bankdebitdetails'

    id = Column(Integer, primary_key=True, server_default=text("nextval('personal_bankdebitdetails_id_seq'::regclass)"))
    debit_dt = Column(Date, nullable=False)
    debit_type = Column(String(2), nullable=False)
    debit_desc = Column(String(2000), nullable=False)
    amount = Column(Integer, nullable=False)
    remarks = Column(String(2000), nullable=False)
    bankmembership_id = Column(ForeignKey('personal_bankmembership.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    bankmembership = relationship('PersonalBankmembership')

class PersonalBankinfo(Base, db.Model):
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
    bank_info = relationship("PersonalBankmembership", back_populates="bank")

class PersonalBankmembership(Base, db.Model):
    __tablename__ = 'personal_bankmembership'
    __table_args__ = (
        UniqueConstraint('person_id', 'bank_id', 'acct_type', 'acctnbr'),
    )

    
    id = Column(Integer, primary_key=True, server_default=text("nextval('personal_bankmembership_id_seq'::regclass)"))
    acct_type = Column(String(2), nullable=False)
    bank_id = Column(ForeignKey('personal_bankinfo.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    person_id = Column(ForeignKey('personal_personalinfo.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    acctnbr = Column(String(15), nullable=False)

    bank = relationship('PersonalBankinfo',back_populates="bank_info" )
    person = relationship('PersonalPersonalinfo', back_populates="bank_membership")

class PersonalPersonalinfo(Base, db.Model):
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
    address = relationship("PersonalAddressinfo", back_populates="person")
    bank_membership = relationship("PersonalBankmembership", back_populates="person")
    phoneinfo= relationship("PersonalPhoneinfo",back_populates="person")

    def __repr__(self):
        return "{firstName:'%s',middleName:'%s',  lastName:'%s', emailid='%s', gender='%s', age='%d'}" %(self.first_name, \
                                        self.middle_name,  self.last_name, self.emailid,\
                                        self.gender, self.age)

class PersonalPhoneinfo(Base, db.Model):
    __tablename__ = 'personal_phoneinfo'
    __table_args__ = (
        UniqueConstraint('person_id', 'phone_type', 'phone_nbr'),
    )

    
    id = Column(Integer, primary_key=True, server_default=text("nextval('personal_phoneinfo_id_seq'::regclass)"))
    phone_type = Column(String(1), nullable=False)
    person_id = Column(ForeignKey('personal_personalinfo.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    phone_nbr = Column(String(15), nullable=False)
    person = relationship('PersonalPersonalinfo', back_populates="phoneinfo")

class AddressInfoSchema(ma.ModelSchema):
    id = fields.Int(dump_only=True)
    address_type = fields.Str()
    door = fields.Str()
    street = fields.Str()
    city = fields.Str()
    state = fields.Str()
    country = fields.Str()
    person_id = fields.Int()
    pin = fields.Int(Integer, nullable=False)
    person = fields.Nested('PersonalInfoSchema', many=True)

    class Meta:
        model = PersonalAddressinfo

class BankMembershipSchema(ma.ModelSchema):
    id = fields.Int(dump_only=True)
    acct_type = fields.Str()
    bank_id = fields.Str()
    person_id = fields.Int()
    acctnbr = fields.Int()

    bank = fields.Nested('BankInfoSchema', many=True)
    person = fields.Nested('PersonalInfoSchema', many=True)

    class Meta:
        model = PersonalBankmembership

class BankInfoSchema(ma.ModelSchema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    branch = fields.Str()
    address = fields.Str()
    phone_nbr = fields.Int()
    bnk_abbr_name = fields.Str()
    brn_abbr_name = fields.Str()
    bank_info = fields.Nested('BankMembershipSchema', many=True, exclude=("bank"))

    class Meta:
        model = PersonalBankinfo

class PhoneInfoSchema(ma.ModelSchema):
    id = fields.Int()
    phone_type = fields.Str()
    person_id = fields.Int()
    phone_nbr = fields.Int()
    person = fields.Nested('PersonalInfoSchema', many=True)

    class Meta:
        model = PersonalPhoneinfo

class PersonalInfoSchema(ma.ModelSchema):
    id = fields.Int(dump_only=True)
    gender = fields.Str()
    age = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()
    middle_name = fields.Str()
    emailid = fields.Str()
    address = fields.Nested(AddressInfoSchema, many=True, exclude=("person"))
    bank_membership = fields.Nested(BankMembershipSchema, many=True, exclude=("person"))
   # phoneinfo= fields.Nested(PhoneInfoSchema, many=True, exclude=("person"))

    class Meta:
        model = PersonalPersonalinfo

class PollsChoice(Base):
    __tablename__ = 'polls_choice'

    id = Column(Integer, primary_key=True, server_default=text("nextval('polls_choice_id_seq'::regclass)"))
    choice_text = Column(String(200), nullable=False)
    votes = Column(Integer, nullable=False)
    question_id = Column(ForeignKey('polls_question.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    question = relationship('PollsQuestion')

class PollsChoicedtl(Base):
    __tablename__ = 'polls_choicedtl'

    id = Column(Integer, primary_key=True, server_default=text("nextval('polls_choicedtl_id_seq'::regclass)"))
    choice_text = Column(String(200), nullable=False)
    pub_date = Column(DateTime(True), nullable=False)


class PollsQuestion(Base):
    __tablename__ = 'polls_question'

    id = Column(Integer, primary_key=True, server_default=text("nextval('polls_question_id_seq'::regclass)"))
    question_text = Column(String(200), nullable=False)
    pub_date = Column(DateTime(True), nullable=False)


class PollsQuestionChoiceLnk(Base):
    __tablename__ = 'polls_question_choice_lnk'

    id = Column(Integer, primary_key=True, server_default=text("nextval('polls_question_choice_lnk_id_seq'::regclass)"))
    choice_id = Column(ForeignKey('polls_choicedtl.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    question_id = Column(ForeignKey('polls_questiondtl.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    choice = relationship('PollsChoicedtl')
    question = relationship('PollsQuestiondtl')


class PollsQuestionChoiceResult(Base):
    __tablename__ = 'polls_question_choice_results'

    id = Column(Integer, primary_key=True, server_default=text("nextval('polls_question_choice_results_id_seq'::regclass)"))
    choice_id = Column(ForeignKey('polls_choicedtl.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    question_id = Column(ForeignKey('polls_questiondtl.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    choice = relationship('PollsChoicedtl')
    question = relationship('PollsQuestiondtl')


class PollsQuestiondtl(Base):
    __tablename__ = 'polls_questiondtl'

    id = Column(Integer, primary_key=True, server_default=text("nextval('polls_questiondtl_id_seq'::regclass)"))
    question_text = Column(String(200), nullable=False)
    pub_date = Column(DateTime(True), nullable=False)
    chosen_response = Column(String(1), nullable=False)


class PollsQuestiondtlChoice(Base):
    __tablename__ = 'polls_questiondtl_choices'
    __table_args__ = (
        UniqueConstraint('questiondtl_id', 'choicedtl_id'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('polls_questiondtl_choices_id_seq'::regclass)"))
    questiondtl_id = Column(ForeignKey('polls_questiondtl.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    choicedtl_id = Column(ForeignKey('polls_choicedtl.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    choicedtl = relationship('PollsChoicedtl')
    questiondtl = relationship('PollsQuestiondtl')
