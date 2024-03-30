from fastapi import FastAPI


app = FastAPI()

@app.get('/model/list')
def list_model():
    return {'models': []}