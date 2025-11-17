from fastapi import FastAPI, Request
from waf.pipelines import run_pipeline

app = FastAPI()

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def waf_entrypoint(request: Request, path: str):
    return run_pipeline(request)