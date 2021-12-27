from flask_login import current_user, login_required

from api import permission_manager
from api.permission.models import BookPermission


@login_required
def listBookPermissions_resolver(obj, info, book_id):
    try:
        permissions = BookPermission.query.filter_by(book_id=book_id)
        if len(permissions) > 0:
            if not permission_manager.check_read_permission(current_user.id, permissions[0].id,
                                                            permissions[0].library_id):
                return {"success": False, "errors": ["403"]}
        payload = {"success": True, "posts": book_id}
    except Exception as error:
        payload = {"success": False, "errors": [str(error)]}
    return payload
