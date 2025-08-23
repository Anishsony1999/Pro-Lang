# pip install pyarrow pandas
from typing import Iterator
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def read_csv_in_chunks(path: str, chunksize: int = 100_000) -> Iterator[pd.DataFrame]:
    for chunk in pd.read_csv(path, chunksize=chunksize):
        yield chunk

def to_parquet_stream(csv_path: str, parquet_path: str, chunksize=100_000):
    writer = None
    for i, df in enumerate(read_csv_in_chunks(csv_path, chunksize)):
        table = pa.Table.from_pandas(df, preserve_index=False)
        if writer is None:
            writer = pq.ParquetWriter(parquet_path, table.schema, compression="snappy")
        writer.write_table(table)
        print(f"Wrote chunk {i+1}")
    if writer is not None:
        writer.close()

if __name__ == "__main__":
    to_parquet_stream("large.csv", "out.parquet", chunksize=200_000)



import os, time, uuid
from contextlib import contextmanager

@contextmanager
def file_lock(lock_path: str, timeout: int = 30):
    token = str(uuid.uuid4())
    start = time.time()
    while True:
        try:
            fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, token.encode())
            os.close(fd)
            break
        except FileExistsError:
            if time.time() - start > timeout:
                raise TimeoutError("Lock timeout")
            time.sleep(0.1)
    try:
        yield
    finally:
        if os.path.exists(lock_path):
            os.remove(lock_path)

# Usage:
# with file_lock("/tmp/my.lock"):
#     critical_section()



# 2) Concurrency: Threading vs Multiprocessing vs AsyncIO

# pip install requests
import concurrent.futures, requests

def fetch(url: str) -> int:
    return requests.get(url, timeout=10).status_code

urls = ["https://example.com"] * 50
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as ex:
    for code in ex.map(fetch, urls):
        pass  # handle result



# CPU-bound (parse/transform heavy) — use multiprocessing

from concurrent.futures import ProcessPoolExecutor
def heavy(n: int) -> int:
    s = 0
    for i in range(10_000_000):
        s += (i * n) % 97
    return s

with ProcessPoolExecutor() as ex:
    results = list(ex.map(heavy, range(8)))


# pip install aiohttp
import asyncio, aiohttp

async def fetch(session, url):
    async with session.get(url) as r:
        return r.status

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, u) for u in urls]
        return await asyncio.gather(*tasks)

# asyncio.run(main(urls))


# 3) Data Validation with Pydantic

# pip install pydantic==1.*  (or pydantic>=2 and update syntax)
from pydantic import BaseModel, validator
from typing import Optional

class Event(BaseModel):
    user_id: str
    ts: int
    country: Optional[str]
    amount: float

    @validator("amount")
    def non_negative(cls, v):
        if v < 0:
            raise ValueError("amount must be >= 0")
        return v

# Validate incoming JSON records before writing
payload = {"user_id":"u1","ts":1690000000,"amount":12.5}
evt = Event(**payload)



# pip install confluent-kafka or aiokafka
from confluent_kafka import Producer, Consumer

# Producer
p = Producer({"bootstrap.servers":"localhost:9092"})
p.produce("events", key="u1", value='{"user_id":"u1","amount":12.5}')
p.flush()

# Consumer
c = Consumer({"bootstrap.servers":"localhost:9092","group.id":"demo","auto.offset.reset":"earliest"})
c.subscribe(["events"])
msg = c.poll(5.0)
if msg:
    print(msg.key(), msg.value())
c.close()


# args = dbutils.widgets.get("args") # string
# args = json.loads(args) # dict


# dbutils.widgets.text("args",'{ " param1" : " val1 " , "param2" : "val2" }')

import json

# args = dbutils.widgets.get("args")

# args = json.loads(args)

# print(args["param1"])


# email_args = json.dumps({"table" :table_name,
#                          "ingstion_date": ingestion_date,
#                          "type" : "Transformation"}) 


# x = {

# }

# if isinstance(x,(list,dict)):
# 	return json.dumps(x) # string

# str(x)

col_remove = []
a =[]
col= []


x = [col for _ in a if x not in col_remove]
