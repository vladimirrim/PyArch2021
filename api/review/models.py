from api import db, create_app


class Review(db.Model):
    __bind_key__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    review = db.Column(db.String)
    created_at = db.Column(db.Date)

    def to_dict(self):
        return {"id": self.id,
                "book_id": self.book_id,
                "rating": self.rating,
                "review": self.review,
                "created_at": str(self.created_at.strftime('%d-%m-%Y'))}