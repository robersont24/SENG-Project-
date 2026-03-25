# CalPal – REST API (FastAPI)

## Project Overview
CalPal is a RESTful calorie tracking API that allows users to log and retrieve meals with calorie information. This project demonstrates a working MVP with API endpoints, database integration, and containerized deployment.

---

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite (for MVP)
- Docker
- GitHub Actions (CI)

---

## Running the Application (Local)

### Install dependencies
pip install -r requirements.txt

### Run FastAPI server
uvicorn app.main:app --reload

### Open Swagger UI
http://127.0.0.1:8000/docs

---

## Running with Docker

### Build Docker image
docker build -t calpal .

### Run container
docker run -p 8080:8080 calpal

### Open Swagger UI
http://localhost:8080/docs

---

## API Endpoints

### Health Check
GET /

---

### Create Meal
POST /meals

Example request:
{
  "name": "Chicken",
  "calories": 300
}

---

### Get Meals
GET /meals

Example response:
[
  {
    "id": 1,
    "name": "Chicken",
    "calories": 300
  }
]

---

## MVP Functionality

This project currently supports:
- Creating meals (POST)
- Retrieving meals (GET)
- Database persistence using SQLite
- End-to-end flow: request → API → database → response

---

## CI Pipeline

A basic GitHub Actions workflow is included to verify:
- Dependencies install correctly
- Project builds successfully

---

## Limitations

- SQLite used instead of Cloud SQL
- No authentication implemented yet
- Limited to basic endpoints (no update/delete yet)
- No frontend interface

---

## Future Improvements

- Deploy to Google Cloud Run
- Replace SQLite with Cloud SQL
- Add authentication (JWT)
- Implement full CRUD operations
- Add frontend dashboard

---

## Demo

The system demonstrates:
- POST request to create a meal
- GET request to retrieve stored meals
- Full working data flow through the API
