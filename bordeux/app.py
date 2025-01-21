from fastapi import FastAPI, HTTPException

bordeux = FastAPI()

posts = {}
authors = {}


@bordeux.get('/')
def read_root():
    return 'http://127.0.0.1:8000/docs'


@bordeux.get('/posts')
def read_posts():
    return posts


@bordeux.get('/posts/{post_id}')
def read_posts(post_id):
    return posts[post_id]


@bordeux.post('/posts/new/')
def write_post(post_id, priority):
    if post_id in posts:
        raise HTTPException(status_code=401, detail='tarefa ja existente')

    else:
        posts[post_id] = priority
        return f'tarefa {post_id} adicionada com sucesso'


@bordeux.get('/author/{author_id}')
def read_authors():
    return authors


@bordeux.post('/authors/new/')
def write_author(nick_name, author_name):
    if author_name in authors:
        raise HTTPException(status_code=401, detail='autor ja existente')

    else:
        authors[nick_name] = author_name
        return f'autor {author_name} criado com sucesso'
