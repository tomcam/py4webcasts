# py4web glossary

[//]: # "TODO: Unfinished"
[//]: # "action"
[//]: # "create-model"
[//]: # "create-controller"
[//]: # "create-view"
[//]: # "mvc"
[//]: # "Field"
[//]: # "required"
[//]: # "requires"
[//]: # "#template"
[//]: # "[templates directory](#templates-directory)"
[//]: # "validator"
[//]: # "view"


## action

## DAL
DAL stands for Database Abstraction Layer (DAL). From the [PyDAL](https://github.com/web2py/pydal) documentation: A DAL is "an API that maps Python objects into database objects such as queries, tables, and records." A DAL differ from an [ORM](#orm) in that it doesn't use an extensive object model. In practice that means it's lightweight, faster, and requires less overhead to both to write and to execute. It also lets you perform database operations on noSQL and SQL databases using the same Python code.

By default py4web uses [PyDal](#pydal) for its DAL, though you can use any Python ORM or DAL package you like.

## define_table

define_table is a [PyDAL](#pydal) function that creates a database table in a portable way, eliminating
the need to do the equivalent of a SQL `CREATE TABLE` statement, or whatever the equivalent [NoSQL](#nosql)
command would be. See See the [PyDAL example](#pydal-example) for a typical use of `define_table`.

See also: define_table [source code](https://github.com/web2py/pydal/blob/master/pydal/base.py), [readthedocs](https://pydal.readthedocs.io/en/latest/index.html#pydal.base.DAL.define_table)

## Field()

`Field()` is a constructor passed to the [PyDal](#pydal) `define_table()` function. It represents both a field (aka column)
to be added to a database table definition, but also validation rules used for entering data in at the forms level, 
or as constraints for records to be accepted into the table at the database level.

## length

`length` is a parameter passed to the [Field](#field) constructor restricting the size of a field. [It applies only to](https://py4web.com/_documentation/static/index.html#chapter-05) fields of type `string`, `uploadfield`, and `authorize`.
See the [PyDAL example](#pydal-example) for a typical use of `length`.

## NoSQL

[PyDAL](#pydal) lets you create, query, and manipulate database tables identically, whether they're
SQL-based, like the built-in support for [SQLite](https://www.sqlite.org/index.html) or non-SQL (aka [NoSQL](https://en.wikipedia.org/wiki/NoSQL))databases supported by PyDAL, such as [MongoDB](https://www.mongodb.com). 


## ORM

An Object Relational Mapper. An ORM lets you manipulate databases, queries, and tables using Python instead of, say, SQL. An ORM is object-oriented abstraction over database access, and is familiar to uses of legacy languages such as Java. ORMs tend to include many class libraries over and above the normal SQL access. That makes them somewhat harder to learn, and slower to execute, than DALs like [PyDAL](#pydal). [SQLAlchemy](https://www.sqlalchemy.org/) is a popular Python ORM.

## notnull
`notnull` is a [PyDal](#pydal) field [validator](#validator) that ensures a record can't be inserted into the database with the specified field empty.

## PyDAL
The database abstraction later, or [DAL](#dal), that py4web uses by default.
[PyDAL](https://github.com/web2py/pydal) is a portable, ridiculously comprehensive, yet lightweight means of using databases from SQLite to MongoDB to PostgreSQL and many more. Its
light abstraction layer allows SQL-like operations over all database types for which PyDAL has drivers. 
SQLite is included with web2py so you can publish a database-backed web app with zero configuration at all. 
PyDAL is used in other frameworks such as [web2py](https://web2py.com) and has been refined for about 15 years at the time of writing. 

### PyDAL Example

PyDAL lets you describe not just the database tables, but also constraints in both data entry and data storage. Here's an example of PyDAL in action:

##### file models.py

```python
db.define_table('task',
    Field('title',length=80,notnull=True),
    Field('description','text'),
    Field('priority','integer',default=2,requires=IS_IN_SET([1,2,3]))
```

This simple, but complete, executable example:
* Creates the database table named `task` (no manual `CREATE TABLE` statement needed)
* Defines the database field (also known as a column) `title`, with a maximum 80 characters. [notnull](#notnull) specifieds that this field cannot be left empty.
* Defines the field `description` with the freeform `text` type, which means the text entered can be of essentially unlimited length
* Defines the `priority` field with an integer data type. Its [requires](#requires) parameter enforces at a form, not database, level that only integral values 1 through 3 (expressed as a Python [set object](https://docs.python.org/3/library/stdtypes.html#set)) are allowed.

You can use other DALs with py4web. PyDAL stands alone and is simply a Python package that happens to be bundled with py4web.

## required

`required` is a [validator](#validator) passed to the [Field](#field) constructor when defining a table. 
It prevents inserts at that DAL level unless a value for the field is specified.

## requires

`requires` is a [validator](#validator) passed to the [Field](#field) constructor when defining a table in [PyDAL](#pydal). It controls data entry
at the [form level](https://py4web.com/_documentation/static/index.html#chapter-05#field-constructor).

## template

A py4web **template** is actually the view portion of the [model/view/controller](#mvc) paradigm. The py4web [templates directory](#templates-directory)

## validator

Validators are constraints on data entry. They can occur at the form, DAL, or database level.

```python
db.define_table('task',
    Field('title',length=80,notnull=True),
    Field('priority','integer',default=2,requires=IS_IN_SET([1,2,3])),
```

## view

The term "view" has

