# py4web glossary

{{- /*
# TODO: Unfinished
* #action
* #mvc
* requires
* required
* [templates directory](#templates-directory)
* #template
* view
* create-model
* create-view
* create-controller
*/ -}}


## action

## DAL
DAL stands for Database Abstraction Layer (DAL). A DAL lets you manipulate databses, queries, and tables using Python instead of, say SQL. A DAL differents from an [ORM](#orm) in that it doesn't use an extensive object model. Practically that means it's lightweight, faster, and requires less overhead to both to write and to execute.

By default py4web uses a package called [PyDal](https://github.com/web2py/pydal) for its DAL, though you aren't required to use PyDal.

## ORM
An Object Relational Mapper. An ORM lets you manipulate databases, queries, and tables using Python instead of, say, SQL. An ORM is object-oriented abstraction over database access, and is familiar to uses of legacy languages such as Java. ORMs tend to include many class libraries over and above the normal SQL access. That makes them somewhat harder to learn, and slower to execute, than DALs like [PyDAL](#pydal). [SQLAlchemy](https://www.sqlalchemy.org/) is a popular Python ORM.

## notnull
`notnull` is a [PyDal](#pydal) field [validator](#validator) that ensures a record can't be inserted into the database with the specified field empty.

## PyDAL
The database abstraction later, or [DAL](#dal), that py4web uses by default.
PyDAL is a portable, ridiculously comprehensive, yet lightweight means of using databases from SQLite to MongoDB to PostgreSQL and many more. SQLite is included with web2py so you can publish a database-backed web app with zero configuration at all. PyDAL is used in other frameworks such as [web2py](https://web2py.com) and has been refined for about 15 years at the time of writing. 

PyDAL lets you describe not just the database tables, but also constraints in both data entry and data storage. Here's an example of PyDAL in action:

```python
db.define_table('task',
    Field('title',length=80,notnull=True),
    Field('description','text'),
    Field('priority','integer',default=2,requires=IS_IN_SET([1,2,3]))
```

This example:
* Creates the database table named `task` (no manual `CREATE TABLE` statement needed)
* Adds the database field (also known as a column) `title`, with a maximum 80 characters. [notnull](#notnull) specifieds that this field cannot be left empty.
* Adds the field `description` with the freeform `text` type, which means the text entered can be of essentially unlimited length
* Adds the `priority` field with an integer data type. Its [requires](#requires) parameter enforces at a form, not database, level that only integral values 1 through 3 (expressed as a Python [set object](https://docs.python.org/3/library/stdtypes.html#set)) are allowed.

You can use other DALs with py4web. PyDAL stands alone and is simply a Python package that happens to be bundled with py4web.

## requires

## required

## template

A py4web **template** is actually the view portion of the [model/view/controller](#mvc) paradigm. The py4web [templates directory](#templates-directory)


## validator

```python
db.define_table('task',
    Field('title',length=80,notnull=True),
    Field('priority','integer',default=2,requires=IS_IN_SET([1,2,3])),
```

## view

The term "view" has

