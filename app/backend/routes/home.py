from fastapi import Request, APIRouter, responses
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory=("app/frontend/templates"))

home_router = APIRouter(prefix="/home", tags=["Home"])
auth_router = APIRouter(prefix="/auth", tags=["Auth"])

@auth_router.get("/")
async def init_auth(request: Request):
    return templates.TemplateResponse(request=request, name="auth.html")


@home_router.get("/")
async def init_home(request: Request):
    return templates.TemplateResponse(request=request, name="home.html")

@auth_router.post("/get_credencials")
async def get_credencials(request: Request):
    data: list = await request.json()
    name: str = data["name"]
    if name == "nadson":
        return responses.RedirectResponse("/home/")
    else:
        return {"STATUS" : "PERMISSION DENIED"}

    