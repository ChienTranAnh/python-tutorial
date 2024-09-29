from fastapi import FastAPI, Request

mpp = FastAPI()

@mpp.get('/')
def read_root(request: Request):
    url = str(request.url)
    header = request.headers

    return {"url": url, "header": header}

@mpp.post('/m')
async def create(request: Request):
    data = await request.json()

    return {"data": data}
