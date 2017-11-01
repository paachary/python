from flask_table import Table, Col, LinkCol

class PersonTable(Table):
    first_name = Col('First Name')
    middle_name = Col('Middle Name')
    last_name = Col('Last Name')
    emailid = Col('Email ID')
    age = Col('Age')
    id1 = LinkCol('Delete', 'main', url_kwargs=dict(id='id'))
    id = LinkCol('Edit', 'main', url_kwargs=dict(id='id'))
