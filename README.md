# Setup databases

```
python3 setup.py
```

# Run application

```
python3 app.py
```

# Docker Deployment

```
sudo docker build -t pydev .
sudo docker run -dp 8888:8888 pydev
```

# Tests

```
python3 -m pytest
```

# GraphQL

```
mutation CreateReview {
  createReview(
    book_id: 2,
    rating: 2
    review:"Some Description",
    library_id: 1) {
    review {
      id
      book_id
      rating
      review
      created_at
      library_id
    }
    success
    errors
  }
}
```
