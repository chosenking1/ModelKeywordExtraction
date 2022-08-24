import pickle
import uvicorn
from fastapi import FastAPI

from data_training import KeywordExtraction

app = FastAPI()
pickle_in = open("generate.pkl", "rb")
keyword_extraction = pickle.load(pickle_in)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post('/generate')
def predict_price(data: KeywordExtraction):
    data = data.dict()
    title = data['title']
    abstract = data['abstract']
    paper_text = data['paper_text']

    prediction = keyword_extraction({'title': [title], 'abstract': [abstract], 'paper_text': [paper_text]})
    return {
        'prediction': round(prediction[0], 0)

    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.2', port=8000)
