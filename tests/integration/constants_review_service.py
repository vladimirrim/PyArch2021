REVIEW_REQUEST = """mutation CreateReview {
  createReview(
    book_id: 2,
    rating: 2
    review:"Some Description") {
    review {
      id
      book_id
      rating
      review
      created_at
    }
    success
    errors
  }
}"""


REVIEW_MODIFY1 = """mutation UpdateReview { updateReview(
id: """
REVIEW_MODIFY2 = """
book_id: 2,
rating: 3
review:"Some Description") {
review {
      id
      book_id
      rating
      review
      created_at
    }
success
errors}}"""

REVIEW_DELETE1 = """mutation DeleteReview { deleteReview(
id: " """
REVIEW_DELETE2 = """"
) {
review {
      id
      book_id
      rating
      review
      created_at
    }
success
errors}}"""