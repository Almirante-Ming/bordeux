from fastapi import FastAPI, HTTPException

bordeux = FastAPI()

tasks={}
authors={}

@bordeux.get('/')
def read_root():
    return 'http://127.0.0.1:8000/docs'

@bordeux.get('/tasks')
def read_tasks():
    return tasks

@bordeux.get('/tasks/{task_id}')
def read_tasks(task_id):
    return tasks[task_id]

@bordeux.post('/tasks/new/{task_id}:{priority}')
def write_task(task_id, priority):
    
    if task_id in tasks:
        raise HTTPException(status_code=401, detail='tarefa ja existente')
    
    else:
        tasks[task_id]=priority
        return f'tarefa {task_id} adicionada com sucesso'
    
    
@bordeux.get('/author')
def read_authors():
    return authors

@bordeux.post('/authors/new/{author_name}:{nick_name}')
def write_author(nick_name,author_name):

    if author_name in authors:
        raise HTTPException(status_code=401, detail='autor ja existente')
    
    else:
        authors[nick_name]=author_name
        return f'autor {author_name} criado com sucesso'

        