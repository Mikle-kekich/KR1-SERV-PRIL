from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from models import User, Feedback  
app = FastAPI()


feedback_storage = []


user = User(name="Михаил Тимофеев", id=1)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", encoding="utf-8") as f:
        html_content = f.read()
    return html_content

@app.get("/users")
async def get_user():
    return user


@app.post("/feedback")
async def create_feedback(feedback: Feedback):
    
    feedback_storage.append(feedback)
    
    
    return {"message": f"Feedback received. Thank you, {feedback.name}."}


@app.get("/feedback")
async def get_all_feedback():
    return feedback_storage