from fastapi import FastAPI, HTTPException

bordeux = FastAPI()

@bordeux.get('/')
def read_root():
    return {'1':'ola'}