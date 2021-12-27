from ariadne import graphql_sync, ObjectType, load_schema_from_path, make_executable_schema, \
    snake_case_fallback_resolvers
from flask import request, jsonify

from api import app
from api.permission.mutations import create_user_permission_resolver, update_user_permission_resolver, \
    create_book_permission_resolver, delete_user_permission_resolver, update_book_permission_resolver, \
    delete_book_permission_resolver
from api.permission.queries import listBookPermissions_resolver

query = ObjectType("Query")
mutation = ObjectType("Mutation")

query.set_field("listBookPermissions", listBookPermissions_resolver)

mutation.set_field("createUserPermission", create_user_permission_resolver)
mutation.set_field("updateUserPermission", update_user_permission_resolver)
mutation.set_field("deleteUserPermission", delete_user_permission_resolver)

mutation.set_field("createBookPermission", create_book_permission_resolver)
mutation.set_field("updateBookPermission", update_book_permission_resolver)
mutation.set_field("deleteBookPermission", delete_book_permission_resolver)

type_defs = load_schema_from_path("api/permission/schemas/permissions_schema.graphql")
schema = make_executable_schema(type_defs, query, mutation, snake_case_fallback_resolvers)


@app.route("/permissions", methods=["POST"])
def books_server():
    data = request.get_json()

    success, result = graphql_sync(schema,
                                   data,
                                   context_value=request,
                                   debug=app.debug)

    status_code = 200 if success else 400
    return jsonify(result), status_code
