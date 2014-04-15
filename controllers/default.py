# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()
def twitter():
    session.counter=(session.counter or 0) + 1
    return dict(counter=session.counter)
def settings():
    return dict()
def first():
    form = SQLFORM.factory(Field('visitor_name',label='what is your name?',requires=IS_NOT_EMPTY()))
    if form.process().accepted:
        session.visitor_name = form.vars.visitor_name
        redirect(URL('second'))
    return dict(form=form)
def second():
    if not request.function=='first' and not session.visitor_name:
        redirect(URL('first'))
    return dict()
def error():
    return dict()

