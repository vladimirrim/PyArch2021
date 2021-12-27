BOOK_REQUEST = """mutation CreateBook { createBook(
title: "New Blog Post",
author: "k l"
description:"Some Description",
library_id: 1) {
book {
  id
  library_id
  title
  author
  description
  created_at
}
success
errors}}"""


BOOK_MODIFY1 = """mutation UpdateBook { updateBook(
id: """
BOOK_MODIFY2 = """
title: "2",
author: "k l"
description:"1") {
book {
  id
  title
  author
  description
  created_at
}
success
errors}}"""

BOOK_DELETE1 = """mutation DeleteBook { deleteBook(
id: " """
BOOK_DELETE2 = """"
) {
book {
  id
  title
  author
  description
  created_at
}
success
errors}}"""