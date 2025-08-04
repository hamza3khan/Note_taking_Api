from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Note(BaseModel):
    title: str
    content: str

class NoteOut(Note):
    id: int

# In-memory database
notes_db = []
note_id_counter = 1

# CREATE
@app.post("/notes", response_model=NoteOut)
def create_note(note: Note):
    global note_id_counter
    new_note = note.dict()
    new_note["id"] = note_id_counter
    note_id_counter += 1
    notes_db.append(new_note)
    return new_note

# READ ALL
@app.get("/notes", response_model=List[NoteOut])
def get_all_notes():
    return notes_db

# READ ONE
@app.get("/notes/{note_id}", response_model=NoteOut)
def get_note(note_id: int):
    for note in notes_db:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")

# UPDATE
@app.put("/notes/{note_id}", response_model=NoteOut)
def update_note(note_id: int, updated_note: Note):
    for note in notes_db:
        if note["id"] == note_id:
            note["title"] = updated_note.title
            note["content"] = updated_note.content
            return note
    raise HTTPException(status_code=404, detail="Note not found")

# DELETE
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for i, note in enumerate(notes_db):
        if note["id"] == note_id:
            notes_db.pop(i)
            return {"message": "Note deleted successfully"}
    raise HTTPException(status_code=404, detail="Note not found")
