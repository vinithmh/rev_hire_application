from fastapi import FastAPI

from . import database
from . import models
from .routers import jobseeker, employer, jobposting, jobapplication, jobseeker_login

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(jobseeker.router)
app.include_router(employer.router)
app.include_router(jobposting.router)
app.include_router(jobapplication.router)
app.include_router(jobseeker_login.router)















    