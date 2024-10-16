from .config import *
from .db import get_db, Project

from fastapi import Request, Depends, Form
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session


__all__ = (
    'index',
)


@app.get('/', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    projects = db.query(Project).all()
    return templates.TemplateResponse('index.html', {'projects': projects, 'request': request})


@app.post('/add-project')
def add_project(name = Form(), db: Session = Depends(get_db)):
    project = Project(name=name, user_id=1)
    db.add(project)
    db.commit()
    db.refresh(project)
    return {}
