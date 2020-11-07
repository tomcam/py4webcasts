# py4web glossary

[//]: # "TODO: Unfinished"
[//]: # "Consider define_table insert, truncate, drop, import_from_csv_file http://www.web2py.com/books/default/chapter/29/06/the-database-abstraction-layer#The-DAL-A-quick-tour"
[//]: # "action (have an expert check my definition)"
[//]: # "controller"
[//]: # "create-model"
[//]: # "create-controller"
[//]: # "create-view"
[//]: # "decorator"
[//]: # "dict()"
[//]: # "fixture (have an expert check my definition)"
[//]: # "flash"
[//]: # "mvc"
[//]: # "IS_IN_SET"
[//]: # "Field"
[//]: # "required"
[//]: # "requires"
[//]: # "#template"
[//]: # "Template object"
[//]: # "[templates directory](#templates-directory)"
[//]: # "uses (have an expert check my definition)"
[//]: # "validator needs finishing"
[//]: # "view"
[//]: # "yatl: add example"


## action

An action is a public function in a [controller](#controller) that processes an HTTP request and
maps it to Python code in the controller. 
In py4web the action returns either a string or a Python dictionary object.
The py4web `@action` [decorator](#decorator) maps HTTP requests to controller functions, often applying
function-level [fixtures](#fixture) to the code that alter its results or add features such as
saving session data.
Often the dictionary object returned by the action is applied to a [Template](#template-object) fixture 
that evaluates the Python embedded in the HTML, interpolates its return values into the HTML,
and converts the result into a string. Often that string is rendered as HTML to be displayed as a web page.

### @action Examples:

* The action named `@action('index')` would process the HTTP request `myapp/index`, 
calling the controller function `index`.
* The action named `@action('view/<id>'` would process HTTP requests like `myapp/view/2022` to
call a controller function named `view` on the record whose ID is 2022
* The action named `@action('edit/<id>',method=['GET','POST'])` would work on an edit form,
so `myapp/edit/2022` would call the controller function named `edit`. It could, for example, display the contents of the record whose ID is 2022 (the `GET` request) in form, and post back any changes to it (the `EDIT` request)

## controller

Controller functions are Python code that handle the program's application logic, also known as its business rules.
py4web controllers use the [action](#action) decorator to convert HTTP requests into
Python functions or parameters. Often controller functions interact with the [model](#model) layer to make database queries
or process forms, then produce dictionaries that get passed to the [view](#view) layer.

Here's an example of a brief but complete controller function. The `@action('new')` decorator routes the path
`myapp/new` (for example) to the Python function named `new()`, which creates a default form that uses the schema 
and [validators](#validator) for the database table `task` to determine the field names, types, and layout.

##### file controllers.py
```python
@action('new')
@action.uses(auth, 'new.html')
def new():
    form=Form(db.task)
    return dict(form=form)
```

See also [MVC](#mvc)

## DAL

DAL stands for Database Abstraction Layer (DAL). From the [PyDAL](https://github.com/web2py/pydal) documentation: A DAL is "an API that maps Python objects into database objects such as queries, tables, and records." A DAL differ from an [ORM](#orm) in that it doesn't use an extensive object model. In practice that means it's lightweight, faster, and requires less overhead to both to write and to execute. It also lets you perform database operations on noSQL and SQL databases using the same Python code.

By default py4web uses [PyDal](#pydal) for its DAL, though you can use any Python ORM or DAL package you like.

## database level

When you define a model in [PyDal]](#pydal), you can pass parameters to the [Field](#field) constructor 
constraining whether record can be inserted into the database. The term used informally in py4web 
for this is that these are applied *database level*.

For example, if your back end is SQL this would be a considered SQL constraint. 
In the example below, a column in the `task` table named `title` is defined as `notnull`. 
While it works on all back ends py4web supports, if it's a SQL database `notnull` would be
translated into a `NOT NULL` SQL constraint. 

```python
db.define_table('task',
    Field('title',length=80,notnull=True),
    Field('description','text'))
```

No matter what the PyDal form validators say, it's impossible in the above example
for a record to be added to the database with an empty `title` field, hence the term *database level*.

This differs from parameters applied at the *[forms level]*(#forms-level), which constrain data entry at runtime.

## decorator

In Python, a decorator is a function that wraps another function. 
By convention Python decorators begin with the `@` character.
In py4web, decorators are most often used for [actions](#action), which give the developer a simplified, intuitive
way to create routes to your application such as `myapp/edit`.

See also [Python Wiki](https://wiki.python.org/moin/PythonDecorators), Real Python [Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)

## define_table

define_table is a [PyDAL](#pydal) function that creates a database table in a portable way, eliminating
the need to do the equivalent of a SQL `CREATE TABLE` statement, or whatever the equivalent [NoSQL](#nosql)
command would be. This allows the same Python code to be used for a wide variety of databases.

### See also

* [PyDAL example](#pydal-example) for a typical use of `define_table` `define_table` 
* PyDAL [source code](https://github.com/web2py/pydal/blob/master/pydal/base.py)
* [readthedocs](https://pydal.readthedocs.io/en/latest/index.html#pydal.base.DAL.define_table)

## Field()

`Field()` is a constructor passed to the [PyDal](#pydal) [define_table()](#define_table) function. 
It represents both a field (aka column) to be added to a database table definition.
Optional parameters also allow validation rules used for entering data in at the forms level, 
and as constraints for records to be accepted into the table at the database level.

## fixture
A py4web fixture is a form of middleware applied at the level of an [action](#action) (controller function).
Most middleware adds overhead to all functions in the package, or requires boilerplate code to be added
to all functions. The advantage to the approach used by py4web is that it's per function, not per package,
and it's also easier to understand what's going on.

The example below shows two fixtures in action. The first maps the `/new` URL to the `new()` function defined
under it. The second adds a login requirement to the `new.html` [template](#template) without any changes required to 
the template code.

##### file controllers.py
```python
@action('new')
@action.uses(auth, 'new.html')
def new():
    form=Form(db.task)
    return dict(form=form)
```

### See also 
* py4web [Fixture documentation](https://py4web.com/_documentation/static/index.html#chapter-04)

## forms level

When you define a model in [PyDal]](#pydal), you can pass parameters called [validators](#validator) to the [Field](#field) constructor 
controlling how data is entered into a form at runtime. T
hese forms-level operations happen independently of, and before, [database level](#database-level) constraints.

In the example below, a column in the `task` table named `priority` uses the validators `default=2`
and `requires=IS_IN_SET([1,2,3])`. The `default` validator gets applied when a data entry form for a new task is rendered, 
causing the number 2 to appear in the field before data entry starts. 

The `requires=IS_IN_SET([1,2,3])` validator ensures that a user can only enter 1, 2, or 3 into the `priority` field.
Because it's enforced at the forms level and not the database level, a database being imported could contain
values other than 1, 2, or 3.

```python
db.define_table('task',
    Field('title',length=80,notnull=True),
    Field('description','text'),
    Field('priority','integer',default=2,requires=IS_IN_SET([1,2,3]))
```

In all cases, forms level validators are attempts at runtime to constrain user entry before it gets 
inserted into the database. That's what makes them different from [database-level](#database-level)
validators.

## IS_IN_SET

`IS_IN_SET` is a py4web [validator](#validator) used to ensure that data entered into a form
is restricted to the values in the Python set object passed to it. In the example below the
`Priority` field limits data entry to integers from 1-3 inclusive.

##### file models.py
```python
db.define_table('task',
    Field('title',length=80,notnull=True),
    Field('description','text'),
    Field('priority','integer',default=2,requires=IS_IN_SET([1,2,3]))
```

## model
In py4web, the model is the database layer of a py4web app, represented as code using [PyDAL](#pydal).
[MVC applications](#mvc) separate database access logic (the model) from display logic (the [view](#view)),
and application flow (the [controller](#controller)). [PyDAL example](#pydal-example) shows typical
PyDAL model code defining a database table.

## length
`length` is a parameter passed to the [Field](#field) constructor restricting the size of a field. [It applies only to](https://py4web.com/_documentation/static/index.html#chapter-05) fields of type `string`, `uploadfield`, and `authorize`.
See the [PyDAL example](#pydal-example) for a typical use of `length`.

<a id="mvc"></a>
## MVC or Model/View/Controller paradigm

The Model/View/Controller or MVC paradigm describes web frameworks like py4web. 
An MVC represents an application's separation of concerns into the database layer (model),
display logic (also known as a [view](#view) or [template](#template)), and application logic ([controller](#controller)). 
That separation is particularly clean and pronounced in py4web, which uses standard Python modules, framework
conventions, and file structure to enforce isolation. 

Py4web's model database layer uses [PyDAL](#pydal) 
by default, but could use another DAL if needed. Its view layer is provided by the [YATL](#yatl)
template language, which allows you to mix pure Python with HTML code to display data, and the
business logic is found in the Python file `controllers.py`, which manages HTTP requests and routing. 

## NoSQL
[PyDAL](#pydal) lets you create, query, and manipulate database tables identically, whether they're
SQL-based, like the built-in support for [SQLite](https://www.sqlite.org/index.html) or non-SQL (aka [NoSQL](https://en.wikipedia.org/wiki/NoSQL))databases supported by PyDAL, such as [MongoDB](https://www.mongodb.com).
For example, the vaguely SQL-like [PyDAL code shown here](#pydal_example) would work on any PyDAL-supported database manager,
SQL-based or not.


## ORM

An Object Relational Mapper. An ORM lets you manipulate databases, queries, and tables using Python instead of, say, SQL. An ORM is object-oriented abstraction over database access, and is familiar to uses of legacy languages such as Java. ORMs tend to include many class libraries over and above the normal SQL access. That makes them somewhat harder to learn, and slower to execute, than DALs like [PyDAL](#pydal). [SQLAlchemy](https://www.sqlalchemy.org/) is a popular Python ORM.

## notnull
`notnull` is a [PyDal](#pydal) field [validator](#validator) ensuring, at the [database level](#database-level), that a record can't be inserted into the database with the specified field empty.

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
* Creates the database table named `task` (no manual `CREATE TABLE`-style statement needed)
* Defines the database field (also known as a column) `title`, with a maximum 80 characters. [notnull](#notnull) specifieds that this field cannot be left empty.
* Defines the field `description` with the freeform `text` type, which means the text entered can be of essentially unlimited length
* Defines the `priority` field with an integer data type. Its [requires](#requires) parameter enforces at a form, not database, level that only integral values 1 through 3 (expressed as a Python [set object](https://docs.python.org/3/library/stdtypes.html#set)) are allowed.

You can use other DALs with py4web. PyDAL stands alone and is simply a Python package that happens to be bundled with py4web.

## required
`required` is a [validator](#validator) passed to the [Field](#field) constructor when defining a table in [PyDAL](#pydal). 
It prevents records from being saved at the database (technicallly, DAL) level unless a value for the field is specified.

## requires
`requires` is a [validator](#validator) passed to the [Field](#field) constructor when defining a table in [PyDAL](#pydal). It controls data entry
at the [form level](https://py4web.com/_documentation/static/index.html#chapter-05#field-constructor), preventing any attempt to save a record interactively until the validator's requirements are met. The record insert (save) is then called at the DAL level, which means a [required](#required) validator may also prevent the record insertion.

## Template object
The `Template` object is a [fixture](#fixture) that takes the specified [template](#template) file, converts
it into a Python [dictionary object](https://realpython.com/python-dicts/).

## template

A py4web **template** is actually the view portion of the [model/view/controller](#mvc) paradigm. It's an HTML file with embedded Python code. Py4web looks for its templates, also known as views, in the [templates directory](#templates-directory).

## templates directory

## validator

Validators are constraints on data entry. They can occur at the form, DAL, or database level.

```python
db.define_table('task',
    Field('title',length=80,notnull=True),
    Field('priority','integer',default=2,requires=IS_IN_SET([1,2,3])),
```

## view
An HTML file with Python code interplolated. The term `view` is used interchangeably with [template](#template)
Unfortunately Django web framework confuses `view` with `template`, so py4web sometimes perpetuates
that usage.

The python code is embedded into HTML using square brackets as delimiter by convention, although
that can be changed on a per-function bases with py4web (shown below). This example ranges through
a set named `query` returned from a [PyDAL](#pydal) `select` call:

```html
    [[for q in query:]]
        <tr><td>[[=q.priority]]</td><td>[[=q.title]]</td></tr>
    [[pass]]
```

### view example

Here's a complete though simplistic example of Python embedded in a view. The controller
generates a query of the `task` table that returns all tasks in reverse priority order.
It returns that query as a Python [dictionary object](https://realpython.com/python-dicts/):

##### file controllers.py

```python
@action('index')
def index():
    query=db(db.task).select(orderby=~db.task.priority)
    return dict(query=query)
```

The `index` [action](#action) shown above is shorthand for this:

```python
@action.uses(Template('index.html', delimiters='[[ ]]')
```

The `Template` [fixture](#fixture) serializes that dictionary into HTML usable by
the `index.html` [template](#template):

##### file index.html

```python
[[extend 'layout.html']]
<div class="vue">
    <h1>Tasks</h1>
    <table class="table is-full-width">
        <tr><th>Priority</th><th>Title</th></tr>
    [[for q in query:]]
        <tr><td>[[=q.priority]]</td><td>[[=q.title]]</td></tr>
    [[pass]]
    </table>
    [[=A('New task', _href=URL('new'))]]    
</div>
```

### See also
* [template](#template)


## uses
The `uses` method of the [@action](#action) decorator specifies a [fixture](#fixture) to apply to an action. 

### uses example

Here's a typical example of `uses`, which adds authentication to the form used by the `new` action.

##### file controllers.py
```python
@action('new')
@action.uses(auth, 'new.html')
def new():
    form=Form(db.task)
    return dict(form=form)
```

### All @action decorators have a uses method

All `@action` decorators have a `uses` method. Since the most common case by far is 
using the Template fixture to convert the dictionary returned by the action into
a form, py4web shortcuts that case. In the example above,

```python
@action.uses(auth, 'new.html')
```

is actually the equivalent of:

```python
@action.uses(Template('new.html', delimiters='[[ ]]')
```

One reason you might want the full version is to change the delimiters. In py4web's predecessor
[web2py](https://web2py.com) the delimiters were curly braces, so form code started like this:

```python
{{extend 'layout.html'}}
```

If you wanted to reuse some old web2py form code you could do it as easily as:

##### file controllers.py
```
@action.uses(Template('new.html', delimiters='{{ }}')
```

### See also
* py4web [Fixtures](https://py4web.com/_documentation/static/index.html#chapter-04) documentation
* [core.py](https://github.com/web2py/py4web/blob/master/py4web/core.py) py4web source code

## YATL
One of the most important functions of py4web is the ability to add pure Python code to an HTML file.
YATL, which stands for Yet Another Template Language, preprocesses the HTML file and 
delimits Python code (using `[[` and `]]` by default but the delimiters can be changed).

### See also
* [YATL template language](https://py4web.com/_documentation/static/index.html#chapter-07)
* [template](#template)
* [MVC](#mvc)

