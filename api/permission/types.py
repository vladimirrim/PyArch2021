import enum


class UserPermissionType(enum.Enum):
    ADMIN = 1
    FULL_ACCESS = 2
    READ_WRITE = 3
    READ_ONLY = 4


class BookPermissionType(enum.Enum):
    CLOSED = 1
    OPEN_ACCESS = 2
