import json
from datetime import datetime
from json import dumps, loads, JSONEncoder
from base64 import b64encode, b64decode
import pickle
from sqlalchemy import Boolean, CheckConstraint, Column, Date, DateTime, ForeignKey, Integer, SmallInteger, String, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta

Base = declarative_base()

class personal_personalinfo(Base):
    __tablename__ = 'personal_personalinfo'

    id = Column(Integer, primary_key=True)
    gender = Column(String(2), nullable=False)
    age = Column(Integer, nullable=False)
    first_name = Column(String(500), nullable=False)
    last_name = Column(String(500), nullable=False)
    middle_name = Column(String(500), nullable=False)
    emailid = Column(String(500), nullable=False)

    def __repr__(self):
        return "<firstName:'%s',middleName:'%s',  lastName:'%s', emailid:'%s', gender:'%s', age:'%d'>" %(self.first_name, \
                                        self.middle_name,  self.last_name, self.emailid,\
                                        self.gender, self.age)


class PythonObjectEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            print("having date time")
        elif isinstance(obj, (list, dict, str, int, float, bool, type(None))):
            return super().default(obj)
        return json.JSONEncoder.default(self, obj)
#        return {'_python_object': b64encode(pickle.dumps(obj)).decode('utf-8')}


def as_python_object(dct):
    if '_python_object' in dct:
        return pickle.loads(b64decode(dct['_python_object'].encode('utf-8')))
    return dct
