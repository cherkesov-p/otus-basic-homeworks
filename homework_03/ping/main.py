import uvicorn
from fastapi import FastAPI
from fastapi import status
from starlette.responses import RedirectResponse

from views.ping import router as ping_router

app = FastAPI()
app.include_router(ping_router)


@app.get("/", status_code=status.HTTP_301_MOVED_PERMANENTLY)
def main():
    return RedirectResponse(url='/ping/')


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        reload=True,
    )
