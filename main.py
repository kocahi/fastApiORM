from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from configs.database import engine
import utils.AddControllers 
from utils.AddModelsEngine import addmodels

app = FastAPI()



addmodels()

app.include_router(utils.AddControllers.populate_router)

