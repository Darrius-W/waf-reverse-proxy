from fastapi import FastAPI, Request
from waf.pipelines import run_pipeline

app = FastAPI()

# Catch-all route that intercepts all incoming requests and passes them through the
# WAF processing pipeline for inspection before forwarding them to backend services
@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def waf_entrypoint(request: Request, path: str):
    return await run_pipeline(request)