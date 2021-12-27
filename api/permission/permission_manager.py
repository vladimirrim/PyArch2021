from api import db
from api.permission.models import UserPermission, BookPermission
from api.permission.types import UserPermissionType, BookPermissionType


class PermissionManager:

    def add_admin_permissions(self, user_id, library_id):
        permission = UserPermission(user_id=user_id, library_id=library_id, permission_type=UserPermissionType.ADMIN)
        db.session.add(permission)
        db.session.commit()

    def check_admin_permissions(self, user_id, library_id):
        user_permission = self.get_user_permission(user_id, library_id)
        return user_permission == UserPermissionType.ADMIN

    def check_read_permission(self, user_id, book_id, library_id):
        book_permission = self.get_book_permission(book_id)
        user_permission = self.get_user_permission(user_id, library_id)

        if user_permission == UserPermissionType.ADMIN:
            return True

        if book_permission != BookPermissionType.OPEN_ACCESS:
            return False

    def check_write_permission(self, user_id, library_id):
        user_permission = self.get_user_permission(user_id, library_id)

        if user_permission != UserPermissionType.READ_ONLY:
            return True

    def check_update_permission(self, user_id, library_id):
        user_permission = self.get_user_permission(user_id, library_id)

        if user_permission == UserPermissionType.ADMIN or user_permission == UserPermissionType.FULL_ACCESS:
            return True

    def check_delete_permission(self, user_id, library_id):
        user_permission = self.get_user_permission(user_id, library_id)

        if user_permission == UserPermissionType.ADMIN:
            return True

    def get_user_permission(self, user_id, library_id):
        permissions = UserPermission.query.filter_by(user_id=user_id, library_id=library_id)
        if len(permissions) > 0:
            return permissions[0].permission_type
        else:
            return UserPermissionType.READ_ONLY

    def get_book_permission(self, book_id):
        permissions = BookPermission.query.filter_by(book_id=book_id)
        if len(permissions) > 0:
            return permissions[0].permission_type
        else:
            return BookPermissionType.OPEN_ACCESS
