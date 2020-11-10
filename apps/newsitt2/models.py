from .common import db, Field
from pydal.validators import *

db.define_table('post',  
    Field('title','string'),
    Field('body', 'text'))

db.commit()

