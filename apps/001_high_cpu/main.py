from fastapi import FastAPI
import os

app = FastAPI()



@app.get("/")
async def health_check():
    return {
        "status": "healthy",
        "service": "high_cpu",
        "version": "1.0.0"
    }

@app.get("/burn")
async def burn():
    try:
        os.system("yes > /dev/null & yes > /dev/null & yes > /dev/null &")
        return {"status": "success", "message": "Burn Baby Burn!"}
    except:
        return {"status": "error", "message": "Something went wrong"}

@app.get("/relax")
async def relax():
    try:
        os.system("killall yes")
        return {"status": "success", "message": "Things are better now..."}
    except:
        return {"status": "error", "message": "Something went wrong"}
