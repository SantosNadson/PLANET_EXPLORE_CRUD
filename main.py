import uvicorn
from fastapi import FastAPI, APIRouter, responses
from app.backend.routes import home
from fastapi.staticfiles import StaticFiles

router = APIRouter()
router.include_router(home.home_router)
router.include_router(home.auth_router)


app = FastAPI()
app.include_router(router)
app.mount("/static", StaticFiles(directory="app/frontend/static"), name="static")

@app.get("/")
async def redirect():
    return responses.RedirectResponse(url="/home/")




if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1", port=8000, reload=True)