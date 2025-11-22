import httpx
from fastapi import Response

# Take incoming request, forward it to the backend by mirroring the
# original request, then return the backend response to the user
async def forward_to_backend(request):
    backend_url = "http://localhost:8001" + request.url.path

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=backend_url,
            content=await request.body(),
            headers=request.headers
        )

    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=response.headers,
    )