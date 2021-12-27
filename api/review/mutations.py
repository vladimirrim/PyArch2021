from datetime import date

from ariadne import convert_kwargs_to_snake_case
from flask_login import login_required, current_user

from api import db, permission_manager
from api.review.models import Review


@convert_kwargs_to_snake_case
@login_required
def create_review_resolver(obj, info, book_id, rating, review, library_id):
    today = date.today()
    if not permission_manager.check_write_permission(current_user.id, library_id):
        return {"success": False, "errors": ["403"]}
    rev = Review(book_id=book_id, rating=rating, review=review, created_at=today)
    db.session.add(rev)
    db.session.commit()
    payload = {"success": True, "review": rev.to_dict()}
    return payload


def validate_rating(rating):
    try:
        rating = int(rating)
        if rating > 5 or rating < 1:
            return None
        return rating
    except Exception:
        return None

@convert_kwargs_to_snake_case
@login_required
def update_review_resolver(obj, info, id, book_id, rating, review):
    rating = validate_rating(rating)
    if rating is None:
        return {"success": False, "errors": ["Invalid rating format"]}
    try:
        rev = Review.query.get(id)
        if not permission_manager.check_update_permission(current_user.id, rev.library_id):
            return {"success": False, "errors": ["403"]}
        if rev:
            rev.book_id = book_id
            rev.review = review
            rev.rating = rating
        db.session.add(rev)
        db.session.commit()
        payload = {"success": True, "post": rev.to_dict()}
    except AttributeError:
        payload = {"success": False, "errors": [f"item matching id {id} not found"]}
    return payload


@convert_kwargs_to_snake_case
@login_required
def delete_review_resolver(obj, info, id):
    try:
        review = Review.query.get(id)
        if not permission_manager.check_update_permission(current_user.id, review.library_id):
            return {"success": False, "errors": ["403"]}
        db.session.delete(review)
        db.session.commit()
        payload = {"success": True, "post": review.to_dict()}
    except AttributeError:
        payload = {"success": False, "errors": ["Not found"]}
    return payload
