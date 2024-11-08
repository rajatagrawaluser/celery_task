# Asynchronous Task Processing with FastAPI, Celery, and Docker

This project demonstrates how to handle background tasks asynchronously using **FastAPI**, **Celery**, and **Docker**. Users can send tasks to be processed in the background and monitor the task status.

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your machine.
- Postman (optional, for API testing)

### Setup

Clone this repository and navigate to the project directory.

### Start the Services

Use Docker Compose to build and run the containers for FastAPI, Celery (with Redis as the message broker), and Flower (to monitor Celery tasks).

```bash
$ docker-compose up -d --build
```

- The FastAPI application will be available at [http://localhost:8004](http://localhost:8004).
- The Celery monitoring tool Flower will be available at [http://localhost:5556](http://localhost:5556).

### Usage

#### Trigger a New Task

**Using `curl`**

To trigger a new task, make a POST request to the `/task` endpoint. This will create a new task and return the `task_id`.

Example request using `curl`:

```bash
$ curl -X POST http://localhost:8004/task -H "Content-Type: application/json" --data '{"total_steps": 0}'
```

The response will include a `task_id` that you can use to monitor the status.

**Using Postman**

1. Open Postman and create a new `POST` request.
2. Enter the URL: `http://localhost:8004/task`.
3. Go to the "Body" tab, select "raw" and set the format to `JSON`.
4. Enter the request body, e.g., `{"total_steps": 0}`.
5. Click "Send."

Postman will display the response, including the `task_id`, which you can use for monitoring.

#### Check Task Status

**Using `curl`**

To monitor the progress of a specific task, make a GET request to the `/task/{task_id}` endpoint, replacing `{task_id}` with the ID returned in the previous step.

Example request using `curl`:

```bash
$ curl http://localhost:8004/task/<TASK_ID>
```

This will return the current status of the task, including whether it is pending, in progress, or completed.

**Using Postman**

1. Open Postman and create a new `GET` request.
2. Enter the URL: `http://localhost:8004/task/<TASK_ID>`, replacing `<TASK_ID>` with the actual task ID.
3. Click "Send."

Postman will display the response with the task's current status.

### Monitoring with Flower

Flower provides a real-time monitoring interface for Celery tasks. You can view the status of all tasks at [http://localhost:5556](http://localhost:5556).

### Additional Information

For more details on setting up asynchronous task processing, see [Celery documentation](https://docs.celeryproject.org/) and [FastAPI documentation](https://fastapi.tiangolo.com/).

---
This setup provides a scalable way to handle asynchronous processing with FastAPI and Celery, making it suitable for background tasks, data processing, and other long-running operations.