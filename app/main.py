from fastapi import FastAPI
from fastapi.responses import JSONResponse

from celery import Celery
from pydantic import BaseModel, Field

celery = Celery('simple_worker',
            broker="redis://localhost:6379",
            backend="redis://localhost:6379")


class RequestModel(BaseModel):
    total_steps: int = Field(title="Number of steps")

app = FastAPI(
    title="Celery Task",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    openapi_url="/documentation",
)

@app.post("/tasks", status_code=201, tags=["Task"])
def run_task(request:RequestModel):
    kwargs={"total_steps": request.total_steps}
    task = celery.send_task('worker.create_task', kwargs=kwargs)
    return JSONResponse({"task_id": task.id})


@app.get("/tasks/{task_id}",tags=["Task"])
def get_status(task_id):
    task_result = celery.AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return result