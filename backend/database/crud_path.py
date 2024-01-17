from sqlalchemy.orm import Session

from . import models, schemas


def get_path(db: Session, path_id: int):
    return db.query(models.Path).filter(models.Path.id == path_id).first()


def get_paths(db: Session):
    return db.query(models.Path).all()


def delete_path(db: Session, path_id):
    path = db.query(models.Path).filter(models.Path.id == path_id).first()

    if path:
        db.delete(path)
        db.commit()


def create_path(db: Session, schem_path: schemas.Path):
    try:
        db_path = models.Path(path=schem_path)
        db.add(db_path)
        db.commit()
        db.refresh(db_path)
    except Exception:
        return None