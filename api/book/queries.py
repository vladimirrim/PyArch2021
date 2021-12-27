from ariadne import convert_kwargs_to_snake_case
from flask_login import current_user, login_required

from api import permission_manager
from api.book.models import Book

@login_required
def listBooks_resolver(obj, info):
    try:
        posts = [post.to_dict() for post in Book.query.all()]
        if len(posts) > 0:
            if not permission_manager.check_read_permission(current_user.id, posts[0].id, posts[0].library_id):
                return {"success": False, "errors": ["403"]}
        payload = {"success": True, "posts": posts}
    except Exception as error:
        payload = {"success": False, "errors": [str(error)]}
    return payload

@login_required
@convert_kwargs_to_snake_case
def getBook_resolver(obj, info, id):
    try:
        post = Book.query.get(id)
        if not permission_manager.check_read_permission(current_user.id, post.id, post.library_id):
            return {"success": False, "errors": ["403"]}
        payload = {"success": True, "post": post.to_dict()}
    except AttributeError:
        payload = {"success": False, "errors": [f"Book with id {id} not found"]}
    return payload


