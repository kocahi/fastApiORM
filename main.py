from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from configs.database import engine
import utils.AddControllers 
from utils.AddEntitiesEngine import addmodels

app = FastAPI(docs_url="/")



addmodels()

app.include_router(utils.AddControllers.populate_router)



