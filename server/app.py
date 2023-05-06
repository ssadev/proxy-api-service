from fastapi import FastAPI
# from pydantic import BaseModel
# from .models.endpoint import Endpoint
# from .schema.endpoint import endpoints_serializer, endpoint_serializer
# from .database import collection_ep
# from bson.objectid import ObjectId
import subprocess
import json
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


# @app.post("/ep", response_description="Endpoint creation")
# async def create_ep(ep: Endpoint):
#     _id = collection_ep.insert_one(dict(ep))
#     endpoint = endpoints_serializer(
#         collection_ep.find_one({"_id": _id.inserted_id}))
#     return {"message": "Create a ep", "data": endpoint}


# @app.get("/ep/{epId}", response_description="Endpoint read")
# async def get_ep(epId: str, run):
#     if run != False:
#         print("Run the game")
#     endpoint = collection_ep.find_one({"_id": ObjectId(epId)})
#     print("endpoint", endpoint)
#     if endpoint == None:
#         return {"message": "ep not found"}
#     data = endpoint_serializer(endpoint)
#     print("ep", data)
#     return data


@app.post("/curl", response_description="Curl")
async def run_curl(cmd: str):
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if error:
        print(f"Error running curl command: {error}")
    else:
        print(f"Output: {output.decode()}")
    resp = output.decode()
    return json.loads(resp)
