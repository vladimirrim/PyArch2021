from ariadne import graphql_sync, ObjectType, load_schema_from_path, make_executable_schema, \
    snake_case_fallback_resolvers
from flask import request, jsonify

from api import app
from api.book.mutations import create_book_resolver, update_book_resolver, delete_book_resolver, \
    create_book_by_isbn_resolver, create_book_by_title_resolver
from api.book.queries import listBooks_resolver, getBook_resolver

query = ObjectType("Query")
mutation = ObjectType("Mutation")

query.set_field("listBooks", listBooks_resolver)
query.set_field("getBook", getBook_resolver)

mutation.set_field("createBook", create_book_resolver)
mutation.set_field("createBookByTitle", create_book_by_title_resolver)
mutation.set_field("createBookByISBN", create_book_by_isbn_resolver)
mutation.set_field("updateBook", update_book_resolver)
mutation.set_field("deleteBook", delete_book_resolver)

type_defs = load_schema_from_path("../api/book/schemas/book_schema.graphql")
schema = make_executable_schema(type_defs, query, mutation, snake_case_fallback_resolvers)


@app.route("/books", methods=["POST"])
def books_server():
    data = request.get_json()

    success, result = graphql_sync(schema,
                                   data,
                                   context_value=request,
                                   debug=app.debug)

    status_code = 200 if success else 400
    return jsonify(result), status_code
