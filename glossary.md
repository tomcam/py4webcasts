# py4web glossary

## DAL
DAL stands for Database Abstraction Layer (DAL). A DAL lets you manipulate databses, queries, and tables using Python instead of, say SQL. A DAL differents from an [ORM](#orm) in that it doesn't use an extensive object model. Practically that means it's lightweight, faster, and requires less overhead to both to write and to execute.

By default py4web uses a package called [PyDal](https://github.com/web2py/pydal) for its DAL, though you aren't required to use PyDal.

## ORM
An Object Relational Mapper. An ORM lets you manipulate databases, queries, and tables using Python instead of, say, SQL. An ORM is object-oriented abstraction over database access, and is familiar to uses of legacy languages such as Java. ORMs tend to include many class libraries over and above the normal SQL access. That makes them somewhat harder to learn, and slower to execute, than DALs such as [PyDal](#pydal). [SQLAlchemy](https://www.sqlalchemy.org/) is a popular Python ORM.

## notnull
`notnull` is a [PyDal](#pydal) field [validator](#validator) that ensures a record can't be inserted into the database with the specified field empty.


## PyDal
The database abstraction later, or [DAL](#dal), that py4web uses by default.
PyDal is a portable, ridiculously comprehensive, yet lightweight means of using databases from SQLite to MongoDB to PostgreSQL and many more. SQLite is included with web2py so you can publish a database-backed web app with zero configuration at all. PyDal is used in other frameworks such as [web2py](https://web2py.com) and has been refined for about 15 years at the time of writing. 

PyDal lets you describe not just the database tables, but also constraints in both data entry and data storage. Here's an example of PyDal in action:

```python
db.define_table('task',
    Field('title',length=80,notnull=True),
    Field('description','text'),
    Field('priority','integer',default=2,requires=IS_IN_SET([1,2,3])),
    Field('created_on', 'datetime', default=datetime.now),
    Field('created_by','reference auth_user',default=Auth.get_user))
```

Most of it's self-explanatory, but notice that you can use [notnull](#notnull) to require that a field cannot be left empty.


You can use other DALs with py4web. PyDal stands alone and is simply a Python package that happens to be bundled with py4web.

## validator

```python
db.define_table('task',
    Field('title',length=80,notnull=True),
    Field('priority','integer',default=2,requires=IS_IN_SET([1,2,3])),
```


