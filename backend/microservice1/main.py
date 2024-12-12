from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from models import get_engine, Item

app = FastAPI()

# Configurer la session
engine = get_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.get("/items")
def get_items():
    session = SessionLocal()
    items = session.query(Item).all()
    session.close()
    return [{"id": item.id, "name": item.name} for item in items]
