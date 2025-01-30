from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from bordeux.models import author_cad

bordeux = FastAPI()

bordeux.add_middleware(
    CORSMiddleware,
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
    allow_origins=['*']
)

posts = {}
authors = {}


# @bordeux.get('/')
# def read_root():
#     pass


@bordeux.get('/posts')
def read_posts():
    return posts


@bordeux.get('/posts/{post_id}')
def find_post(post_id):
    return posts[post_id]


@bordeux.post('/posts/new/', status_code=HTTPStatus.CREATED)
def make_post(post_id, priority, author_id, content):
    if post_id in posts:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail='aready exists')

    else:
        posts[post_id] = {
            'priority': priority,
            'author_id': author_id,
            'content': content
        }
        return f'{post_id} created'


@bordeux.get('/authors')
def read_authors():
    return authors

@bordeux.get('/authors/{author_id}')
def find_author(author_id):
    return authors[author_id]


@bordeux.post('/authors/new/', status_code=HTTPStatus.CREATED, response_model=author_cad)
def write_author(nick_name, author_name):
    if author_name in authors:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail='aready exists')

    else:
        authors[nick_name] = author_name
        return f'{author_name} created'
