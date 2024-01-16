import shutil

from fastapi import FastAPI, Request, UploadFile, File, Depends
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from database import models
from database.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)


app = FastAPI(docs_url="/api/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/storage", StaticFiles(directory="storage"), name="storage")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/")
def read_root():
    return {"Hello": "World"}


@app.post("/api/upload/")
async def upload_file(request: Request, file: UploadFile = File(...),  db: Session = Depends(get_db)):
    file_location = f"storage/{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    from database.crud_path import create_path

    url = f"{str(request.url)[:-len(request.url.path)]}/{file_location}"

    create_path(db=db, schem_path=url)

    return {"path": url}


@app.get("/api/models")
async def get_models(db: Session = Depends(get_db)):
    from database.crud_path import get_paths

    return {"models": get_paths(db)}