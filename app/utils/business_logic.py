from sqlalchemy.orm import Session
from .. import models

def calculate_book_rating(db: Session, book_id: int) -> float:
    reviews = db.query(models.Review).filter(models.Review.book_id == book_id).all()
    if not reviews:
        return 0.0
    return sum(review.rating for review in reviews) / len(reviews)
