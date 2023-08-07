from sqlalchemy.orm import Session


class CRUDManager:
    def __init__(self, model) -> None:
        self.model = model

    async def create(self, db: Session, data: dict):
        obj = self.model(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    async def get_all(self, *filters, db: Session):
        return db.query(self.model).filter(*filters).all()

    async def get_by_id(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.id==id)
