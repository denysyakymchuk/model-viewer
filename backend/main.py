import shutil

from fastapi import FastAPI, Request, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from users.db import create_db_and_tables, User
from users.schemas import UserRead, UserCreate, UserUpdate
from users.users import fastapi_users, auth_backend, current_active_user
from database import models
from database.database import engine, SessionLocal
from loguru import logger

models.Base.metadata.create_all(bind=engine)

# logs
logger.add("logs/logs.csv",
           format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
           level="INFO",
           rotation="200 MB",
           compression="zip")

app = FastAPI(docs_url="/api/docs", openapi_url='/api/openapi.json')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/storage", StaticFiles(directory="storage"), name="storage")


app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/api/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/api/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/api/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/api/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/api/users",
    tags=["users"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    logger.info(f'{request.url, request.headers}')
    return response


@app.get("/api/")
def read_root():
    logger.info(f'Hello world')
    return {"Hello": "World"}


@app.post("/api/upload-model")
async def upload_file(request: Request, file: UploadFile = File(...),  db: Session = Depends(get_db), user: User = Depends(current_active_user)):
    if not file.filename.endswith('.glb'):
        logger.warning("No valid format")
        raise HTTPException(status_code=422, detail="No valid file format")

    file_location = f"storage/{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    from database.crud_path import create_path

    url = f"{str(request.url)[:-len(request.url.path)]}/{file_location}"

    create_path(db=db, schem_path=url)
    logger.info(f"Create new model with path {url}")
    return {"path": url}


@app.get("/api/models")
async def get_models(db: Session = Depends(get_db)):
    from database.crud_path import get_paths
    logger.info("Get models")
    return {"models": get_paths(db)}


@app.get('/api/delete-model')
async def delete_model(path_id: int, db: Session = Depends(get_db), user: User = Depends(current_active_user)):
    from database.crud_path import delete_path, get_paths
    delete_path(db, path_id)
    logger.info(f"Delete model with id {path_id}")
    return get_paths(db)


@app.get('/api/model')
async def delete_model(path_id: int, db: Session = Depends(get_db)):
    from database.crud_path import get_path
    logger.info(f"Get model with id {path_id}")
    return get_path(db, path_id)


@app.get("/api/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()

