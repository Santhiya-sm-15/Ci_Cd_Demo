from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"messages":"Hello..!"}

@app.get("/health")
def health_check():
    return {"messages":"Health check"}