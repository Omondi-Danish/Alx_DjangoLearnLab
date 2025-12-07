# Advanced Query Capabilities for Book API

## Features
- **Filtering**: Filter books by title, author, or publication_year.
  - Example: `/api/books/?author=1&publication_year=1960`
- **Searching**: Search books by title or author name.
  - Example: `/api/books/?search=fall`
- **Ordering**: Order books by title or publication_year.
  - Example: `/api/books/?ordering=title`
  - Example: `/api/books/?ordering=-publication_year`

## Setup
- Install `django-filter`: `pip install django-filter`
- Add to `REST_FRAMEWORK['DEFAULT_FILTER_BACKENDS']` in `settings.py`.

## Testing
Use Postman or curl:
```bash
curl "http://127.0.0.1:8000/api/books/?search=fall&ordering=-publication_year"
