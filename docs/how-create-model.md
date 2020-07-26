# How to create a model in py4web

Py4web lets you create and modify database tables, and generate queries, in pure Python code using the popular [PyDAL](glossary.md#pydal) package.
The query language feels roughly like SQL but works identically on both supported SQL databases, such as PostgreSQL or the built-in SQLite, 
and supported NoSQL databases, such as MongoDB. PyDAL is compact and does a lot of work under the hood. For example, you don't normally need 
to do a separate migration step. Just change your Python code that defines the table and you're done. (If you need full control, 
no problem. See the PyDAL [Migrations](http://py4web.com/_documentation/static/index.html#table_migrations)
chapter.

Here are complete instructions illustrating what to do when you're told to create a model.
