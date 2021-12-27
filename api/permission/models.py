from api import db
from api.permission.types import UserPermissionType, BookPermissionType


class UserPermission(db.Model):
    __bind_key__ = 'user_permissions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    library_id = db.Column(db.Integer)
    permission_type = db.Column(db.Enum(UserPermissionType))

    def to_dict(self):
        return {"id": self.id,
                "user_id": self.user_id,
                "library_id": self.library_id,
                "permission_type": self.permission_type}


class BookPermission(db.Model):
    __bind_key__ = 'book_permissions'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer)
    permission_type = db.Column(db.Enum(BookPermissionType))

    def to_dict(self):
        return {"id": self.id,
                "book_id": self.book_id,
                "permission_type": self.permission_type}
