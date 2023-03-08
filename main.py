import uvicorn

import InputReader
import requests
from fastapi import FastAPI

file = InputReader.InputReader()
data = file.readInputFile()

app = FastAPI()
bacon_endpoint = "https://baconipsum.com/api/"
bacon_request = {'type': 'all-meat'}


@app.get("/class/{class_name}")
async def read_class(class_name):
    return data[class_name]


@app.get("/attribute/{attr_name}")
async def read_attribute(attr_name):
    class_list = []
    ret_list = []
    for class_key, attr_value in data.items():
        for attr_key, dt_value in attr_value.items():
            if attr_key == attr_name:
                datatype = dt_value
                class_list.append(class_key)
    ret_list.append(datatype)
    ret_list.append(class_list)
    return ret_list


@app.get("/datatype/{datatype}")
async def read_datatype(datatype):
    ret_list = []
    for class_key, attr_value in data.items():
        for attr_key, dt_value in attr_value.items():
            if dt_value == datatype:
                ret_list.append(attr_key)
    return ret_list


@app.get("/random")
def random_bacon():
    request = requests.get(url=bacon_endpoint, params=bacon_request)
    response = request.json()
    return response[0:4]


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
