from .forwarding_layer import forward_to_backend

# WAF processing pipeline that routes each requests through a series
# of asynchronous inspection layers before forwarding it to the backend
async def run_pipeline(request):
    return await forward_to_backend(request)