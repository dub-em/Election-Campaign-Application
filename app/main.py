from fastapi import FastAPI
from .routers import general_trends, citizen_sentiment, complaint_areas, politicians_reputation
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"] #"*" allows every single domain to be able to access our API.
                #If we have an exclusive list of domains we want to have access to our API, then we put them in our list.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#uvicorn app.main:app --reload

app.include_router(general_trends.router)
app.include_router(citizen_sentiment.router)
app.include_router(complaint_areas.router)
app.include_router(politicians_reputation.router)