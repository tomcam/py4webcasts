# TODO:
* Find out if the default style sheet has been settled on

# Stages

## newsitt1
* controllers.py: Can I get away with the default imports? Maybe just need to add Form?
* models.py Can I get away with the default imports?

##### templates/index.html
[[extend 'layout.html']]
<table>
[[for q in query:]]
    <tr><td>[[=q.title]]</td></tr>
[[pass]]
</table>
[[=A('New post', _href=URL('new'))]]

##### templates/new.html
[[extend 'layout.html']]
<h1>New Post</h1>
[[=form]]
[[=A('Home', _href=URL('index'))]]

##### models.py
from .common import db, Field
from pydal.validators import *

db.define_table('post',  
    Field('title','string'),
    Field('body', 'text'))
db.commit()


##### controllers.py
from py4web import action, request, abort, redirect, URL
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated
from py4web.utils.form import Form

@unauthenticated()
@action("index")
@action.uses('index.html')
def index():
    query=db(db.post).select()
    return dict(query=query)

@action("new",method=['GET','POST'])    
#@action("new")    
@action.uses('new.html')
def new():
    form=Form(db.post)
    return dict(form=form)
