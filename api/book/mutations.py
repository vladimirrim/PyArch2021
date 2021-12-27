from datetime import date

from ariadne import convert_kwargs_to_snake_case
from flask_login import login_required, current_user

from api import db, google_books_api_manager, permission_manager
from api.book.models import Book


@convert_kwargs_to_snake_case
@login_required
def create_book_resolver(obj, info, title, author, description, library_id):
    author = parse_author(author)
    if author is None:
        return {"success": False, "errors": ["Invalid author format"]}
    return __create_book(author, title, description, library_id)


@convert_kwargs_to_snake_case
@login_required
def create_book_by_isbn_resolver(obj, info, isbn, library_id):
    book_info = google_books_api_manager.get_book_info_by_isbn(isbn)
    if book_info is None:
        return {"success": False, "errors": ["Could not find book by isbn"]}
    author = ' '.join(book_info["authors"])
    title = book_info["title"]
    return __create_book(author, title, '', library_id)


@convert_kwargs_to_snake_case
@login_required
def create_book_by_title_resolver(obj, info, title, library_id):
    book_info = google_books_api_manager.get_book_info_by_title(title)
    if book_info is None:
        return {"success": False, "errors": ["Could not find book by title"]}
    author = ' '.join(book_info["authors"])
    title = book_info["title"]
    return __create_book(author, title, '', library_id)


def __create_book(author, title, description, library_id):
    today = date.today()
    if current_user.is_authenticated:
        permission_manager.add_admin_permissions(current_user.id, library_id)
    book = Book(library_id=library_id, title=title, author=author, description=description, created_at=today)
    db.session.add(book)
    db.session.commit()
    payload = {"success": True, "book": book.to_dict()}
    return payload


def parse_author(author):
    tokens = author.split()
    if len(tokens) != 2 or len(tokens[0]) == 0 or len(tokens[1]) == 0:
        return None
    return tokens[0].capitalize() + ' ' + tokens[1].capitalize()


@convert_kwargs_to_snake_case
@login_required
def update_book_resolver(obj, info, id, title, author, description):
    author = parse_author(author)
    if author is None:
        return {"success": False, "errors": ["Invalid author format"]}
    try:
        book = Book.query.get(id)
        if current_user.is_authenticated and not permission_manager.check_update_permission(current_user.id, book.library_id):
            return {"success": False, "errors": ["403"]}
        if book:
            book.title = title
            book.author = author
            book.description = description
        db.session.add(book)
        db.session.commit()
        payload = {"success": True, "post": book.to_dict()}
    except AttributeError:
        payload = {"success": False, "errors": [f"item matching id {id} not found"]}
    return payload


@convert_kwargs_to_snake_case
@login_required
def delete_book_resolver(obj, info, id):
    try:
        book = Book.query.get(id)
        if current_user.is_authenticated and not permission_manager.check_update_permission(current_user.id, book.library_id):
            return {"success": False, "errors": ["403"]}
        db.session.delete(book)
        db.session.commit()
        payload = {"success": True, "post": book.to_dict()}

    except AttributeError:
        payload = {"success": False, "errors": ["Not found"]}

    return payload
