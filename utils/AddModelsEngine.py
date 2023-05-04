import os
import importlib
from configs.database import engine

def addmodels():
    moduleNamesOST = os.listdir("models")
    for moduleName in moduleNamesOST:
        name, ext = os.path.splitext(moduleName)
        if (ext == ".py"):
            module = importlib.import_module("models." + name)
            module.Base.metadata.create_all(bind=engine)