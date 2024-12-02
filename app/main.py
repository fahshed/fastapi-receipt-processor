from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.api.endpoints import router
from app.models.responses import ErrorResponse

app = FastAPI(
    title="Receipt Processor",
    description="A simple receipt processor",
    version="1.0.0",
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, _):
    if request.url.path == "/receipts/process":
        message = "The receipt is invalid"
    else:
        message = "Unprocessable entity"
    return JSONResponse(
        status_code=400,
        content=ErrorResponse(detail=message).model_dump(),
    )


app.include_router(router)
