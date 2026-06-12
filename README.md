# ShelfLog

A Django application for tracking your personal media consumption — books, films, and albums.

## Features

- Track **Books** with reading status (want to read / reading / finished), finish date, and author
- Track **Films** with director
- Track **Albums** with artist and label
- All media types share a common base: title, release year, 1–5 star rating, and freeform notes
- Django admin interface for managing all entries

## Tech Stack

- Python 3.13+
- Django 6.x
- Django REST Framework
- SQLite (development)
- Poetry for dependency management

## Getting Started

### Prerequisites

- Python 3.13+
- [Poetry](https://python-poetry.org/)

### Installation

```bash
git clone https://github.com/jnutterdev/shelflog.git
cd shelflog
poetry install
```

### Configuration

Copy `.env` and set your secret key:

```bash
cp .env .env.local
```

Edit `.env` and set `SECRET_KEY` to a unique value.

### Running the development server

```bash
poetry run python manage.py migrate
poetry run python manage.py createsuperuser
poetry run python manage.py runserver
```

The admin interface is available at `http://127.0.0.1:8000/admin/`.

## Data Models

### MediaItem (abstract base)

| Field          | Type        | Notes                    |
|----------------|-------------|--------------------------|
| `title`        | CharField   |                          |
| `release_year` | IntegerField| 1000–9999                |
| `rating`       | IntegerField| 1–5, optional            |
| `notes`        | TextField   | Optional                 |

### Book

Extends `MediaItem` with `author`, `status` (`want` / `reading` / `finished`), and optional `date_finished`.

### Film

Extends `MediaItem` with `director`.

### Album

Extends `MediaItem` with `artist` and optional `label`.
