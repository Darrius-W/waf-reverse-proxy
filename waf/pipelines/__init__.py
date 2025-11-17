from .forwarding_layer import forward_to_backend

async def run_pipeline(request):
    return await forward_to_backend(request)