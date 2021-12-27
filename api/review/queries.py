from ariadne import convert_kwargs_to_snake_case
from flask_login import current_user, login_required

from api import permission_manager
from api.review.models import Review


@login_required
def listReviews_resolver(obj, info):
    try:
        revs = [rev.to_dict() for rev in Review.query.all()]
        if len(revs) > 0:
            if not permission_manager.check_read_permission(current_user.id, revs[0].id, revs[0].library_id):
                return {"success": False, "errors": ["403"]}
        payload = {"success": True, "posts": revs}
    except Exception as error:
        payload = {"success": False, "errors": [str(error)]}
    return payload


@login_required
@convert_kwargs_to_snake_case
def getReview_resolver(obj, info, id):
    try:
        rev = Review.query.get(id)
        if not permission_manager.check_read_permission(current_user.id, rev.id, rev.library_id):
            return {"success": False, "errors": ["403"]}
        payload = {"success": True, "post": rev.to_dict()}
    except AttributeError:
        payload = {"success": False, "errors": [f"Review with id {id} not found"]}
    return payload


@login_required
@convert_kwargs_to_snake_case
def getBookReviews_resolver(obj, info, book_id):
    try:
        revs = Review.query.filter_by(book_id=book_id)
        if len(revs) > 0:
            if not permission_manager.check_read_permission(current_user.id, revs[0].id, revs[0].library_id):
                return {"success": False, "errors": ["403"]}
        payload = {"success": True, "post": [rev.to_dict() for rev in revs]}
    except AttributeError:
        payload = {"success": False, "errors": [f"Book with id {id} not found"]}
    return payload
