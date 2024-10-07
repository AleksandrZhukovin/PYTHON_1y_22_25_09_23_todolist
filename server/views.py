from .config import *

from fastapi import Request
from fastapi.responses import HTMLResponse


__all__ = (
    'index',
)


@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
