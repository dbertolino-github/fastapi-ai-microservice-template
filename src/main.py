import logging.config
from fastapi import FastAPI, Response
from pydantic import BaseModel
import os
from huggingface import HugginfacePipeline

# setup loggers
folder_path = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1])
logging.config.fileConfig(os.path.join(folder_path, 'logging.conf'), disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)  # the __name__ resolve to "main" since we are at the root of the project.

app = FastAPI()
ai_pipeline = HugginfacePipeline()

class QueryingData(BaseModel):
    text: str

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/predict", status_code=200)
async def post_query_classifier(data: QueryingData, response: Response):
    return ai_pipeline.analyze(data.text)
