#  Note-Taking App - FastAPI CRUD Project

This is a simple **Note-Taking API** built using **FastAPI**. The project supports full **CRUD** (Create, Read, Update, Delete) operations on notes. It uses an in-memory list to store notes (no database required for this basic version).

##  Features

- Create a new note  
- Get all notes  
- Get a specific note by ID  
- Update a note by ID  
- Delete a note by ID  

---

##  Technologies Used

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn (for running the server)

---

## Project Structure
note_api/
├── main.py # Main FastAPI app
├── README.md # Project documentation


Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate 

Install Dependencies
pip install fastapi uvicorn

 Run the Server
uvicorn main:app --reload


 Open API Docs
Open your browser and go to:
http://127.0.0.1:8000/docs
This will open Swagger UI where you can test all endpoints easily.

 Author
Hamza Khan
Backend Developer | Python & FastAPI Enthusiast
GitHub • LinkedIn

