# py4web tutorial: create a todo list web app in 75 lines of code

## Create the database model

py4web uses a database access abstraction layer (DAL) package called [PyDal](glossary.html#pydal). It's a portable, ridiculously comprehensive, yet lightweight means of using databases from SQLite to MongoDB to PostgreSQL and many more. SQLite is included with web2py so you can publish a database-backed web app with zero configuration at all.

### Add the following lines to `models.py`:

```python
from datetime import datetime

db.define_table('task',
    Field('title',unique=True,notnull=True),
    Field('description','text'),
    Field('priority','integer',default=3,requires=IS_IN_SET([1,2,3,4,5]),zero=True),
    Field('created_on', 'datetime', default=datetime.now),
    Field('created_by','reference auth_user',default=Auth.get_user))

db.commit()
```


