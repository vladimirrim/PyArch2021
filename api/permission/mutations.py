from ariadne import convert_kwargs_to_snake_case
from flask_login import login_required, current_user

from api import db, permission_manager
from api.permission.models import BookPermission, UserPermission


@convert_kwargs_to_snake_case
@login_required
def create_book_permission_resolver(obj, info, book_id, permission_type, library_id):
    if not permission_manager.check_admin_permissions(current_user.id, library_id):
        return {"success": False, "errors": ["403"]}
    permission = BookPermission(book_id=book_id, permission_type=permission_type)
    db.session.add(permission)
    db.session.commit()
    payload = {"success": True, "book": permission.to_dict()}
    return payload


@convert_kwargs_to_snake_case
@login_required
def create_user_permission_resolver(obj, info, user_id, permission_type, library_id):
    if not permission_manager.check_admin_permissions(current_user.id, library_id):
        return {"success": False, "errors": ["403"]}
    permission = UserPermission(user_id=user_id, library_id=library_id, permission_type=permission_type)
    db.session.add(permission)
    db.session.commit()
    payload = {"success": True, "book": permission.to_dict()}
    return payload


@convert_kwargs_to_snake_case
@login_required
def update_book_permission_resolver(obj, info, id, permission_type, library_id):
    if not permission_manager.check_admin_permissions(current_user.id, library_id):
        return {"success": False, "errors": ["403"]}
    try:
        permission = BookPermission.query.get(id)
        if permission:
            permission.permission_type = permission_type
        db.session.add(permission)
        db.session.commit()
        payload = {"success": True, "post": permission.to_dict()}
    except AttributeError:
        payload = {"success": False, "errors": [f"item matching id {id} not found"]}
    return payload


@convert_kwargs_to_snake_case
@login_required
def update_user_permission_resolver(obj, info, id, permission_type, library_id):
    if not permission_manager.check_admin_permissions(current_user.id, library_id):
        return {"success": False, "errors": ["403"]}
    try:
        permission = BookPermission.query.get(id)
        if permission:
            permission.permission_type = permission_type
        db.session.add(permission)
        db.session.commit()
        payload = {"success": True, "post": permission.to_dict()}
    except AttributeError:
        payload = {"success": False, "errors": [f"item matching id {id} not found"]}
    return payload


@convert_kwargs_to_snake_case
@login_required
def delete_book_permission_resolver(obj, info, id, library_id):
    if not permission_manager.check_admin_permissions(current_user.id, library_id):
        return {"success": False, "errors": ["403"]}
    try:
        permission = BookPermission.query.get(id)
        db.session.delete(permission)
        db.session.commit()
        payload = {"success": True, "post": permission.to_dict()}

    except AttributeError:
        payload = {"success": False, "errors": ["Not found"]}

    return payload


@convert_kwargs_to_snake_case
@login_required
def delete_user_permission_resolver(obj, info, id, library_id):
    if not permission_manager.check_admin_permissions(current_user.id, library_id):
        return {"success": False, "errors": ["403"]}
    try:
        permission = BookPermission.query.get(id)
        db.session.delete(permission)
        db.session.commit()
        payload = {"success": True, "post": permission.to_dict()}

    except AttributeError:
        payload = {"success": False, "errors": ["Not found"]}

    return payload
