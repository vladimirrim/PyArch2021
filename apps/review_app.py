from ariadne import graphql_sync, ObjectType, load_schema_from_path, make_executable_schema, \
    snake_case_fallback_resolvers
from flask import request, jsonify

from api import app
from api.review.mutations import create_review_resolver, update_review_resolver, delete_review_resolver
from api.review.queries import listReviews_resolver, getReview_resolver

query = ObjectType("Query")
mutation = ObjectType("Mutation")

query.set_field("listReviews", listReviews_resolver)
query.set_field("getReview", getReview_resolver)

mutation.set_field("createReview", create_review_resolver)
mutation.set_field("updateReview", update_review_resolver)
mutation.set_field("deleteReview", delete_review_resolver)

type_defs = load_schema_from_path("../api/review/schemas/review_schema.graphql")
schema = make_executable_schema(type_defs, query, mutation, snake_case_fallback_resolvers)


@app.route("/reviews", methods=["POST"])
def reviews_server():
    data = request.get_json()

    success, result = graphql_sync(schema,
                                   data,
                                   context_value=request,
                                   debug=app.debug)

    status_code = 200 if success else 400
    return jsonify(result), status_code
