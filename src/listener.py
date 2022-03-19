import fastapi
from kafka import KafkaConsumer, KafkaProducer
from typing import List,Dict,AnyStr
import json

import numpy as np
import uvicorn
import pydantic

app = fastapi.FastAPI()
producer = KafkaProducer(bootstrap_servers='localhost:29092',
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))

class JobRequest(pydantic.BaseModel):
    jobType: AnyStr
    jobParams: Dict

class JobResponse(pydantic.BaseModel):
    res: AnyStr


@app.post('/AddJob', response_model=JobResponse)
def addJob2List(req: JobRequest):

    try:
        producer.send('MMR',req.jobParams)
        status='job added secsussfly'
    except:
        print("An exception occurred")
        status = "An exception occurred"
        #data_o = json.dumps({'plot_list':[]})

    return JobResponse(res=status)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)