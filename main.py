from fastapi import FastAPI
import uvicorn

app = FastAPI(title="pillama LLM API Validation")

@app.get("/")
async def read_root():
    return {"message": "I'm awake!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# To run the server, use the command:
# uvicorn main:app --host