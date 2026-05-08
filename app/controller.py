from fastapi import FastAPI, UploadFile, File
from typing import List, Dict, Any
import uvicorn

app = FastAPI()

@app.get("/searchJob")
def searchJob(skill: str, location: str) -> List[Dict[str, Any]]:
    return [ 
        {
            "job list based on skill and location."
            "title": f"{skill} Engineer",
            "company": "Tech Corp",
            "location": location,
            "source_badge": "LinkedIn"
        }
    ]

@app.post("/uploadResume")
def uploadResume(file: UploadFile = File(...)):
     return {"message": "Resume uploaded and processed", "filename": file.filename}

@app.post("/analyzeResume")
def analyzeResume(file: UploadFile = File(...)):
     return {"message": "Resume analyzed", "filename": file.filename, "skills": ["Python", "FastAPI", "Machine Learning"]}

@app.get("/health")
def health_check():
    return {"status": "Health is Alright!"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8396)