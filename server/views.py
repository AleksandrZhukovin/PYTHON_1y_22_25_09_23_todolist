from .config import *
from .db import get_db, Project, User

from fastapi import Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session


__all__ = (
    'index',
)


def login_required(func):
    def wrap(request: Request, *args, **kwargs):
        if not request.session.get('is_auth', False):
            return RedirectResponse('/login', status_code=303)
        return func(request, *args, **kwargs)
    return wrap


@app.get('/', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    projects = db.query(Project).all()
    return templates.TemplateResponse('index.html', {'projects': projects, 'request': request})


@login_required
@app.post('/add-project')
def add_project(request: Request, name = Form(), db: Session = Depends(get_db)):
    project = Project(name=name, user_id=request.session['user_id'])
    db.add(project)
    db.commit()
    db.refresh(project)
    return {}


@app.get('/login', response_class=HTMLResponse)
def login(request: Request, after_fail: bool = False):
    context = {'request': request}
    if after_fail:
        context['message'] = 'Username or password is incorrect'
    return templates.TemplateResponse('login.html', context)


@app.post('/login')
def login(request: Request, name: str = Form(), password: str = Form(), db: Session = Depends(get_db)):
    user = db.query(User).filter_by(name=name).first()
    if user is None or user.password != password:
        return RedirectResponse('/login?after_fail=True', status_code=303)
    request.session['user_id'] = user.id
    request.session['is_auth'] = True
    return RedirectResponse('/', status_code=303)
