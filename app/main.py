from fastapi import FastAPI
from app.database import engine
from app import models
from app.schemas import MealCreate
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "CalPal API is running"}

@app.post("/meals")
def create_meal(meal: MealCreate, db: Session = Depends(get_db)):
    db_meal = models.Meal(
        name=meal.name,
        calories=meal.calories
    )
    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)
    return db_meal

@app.get("/meals")
def get_meals(db: Session = Depends(get_db)):
    return db.query(models.Meal).all()
