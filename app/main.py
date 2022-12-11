import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from io import BytesIO
import barcode
from barcode.writer import ImageWriter
import re

def sum_of_digits(digit :int) -> int:
    return 0 if digit == 0 else int(digit % 10) + sum_of_digits(int(digit / 10))
def check_digit(code :str) -> int:
    weights = [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1]
    total_sum = sum(list(map(lambda x,y: sum_of_digits(int(x) * y), code, weights))) % 10
    return total_sum if total_sum == 0 else 10 - total_sum

app = FastAPI()

@app.get("/{code}")
async def gen_barcode(code: str):
    pattern = re.compile("^[0-9]{15}$")
    if not pattern.match(code):
        raise HTTPException(status_code=418, detail="The barcode code format incorrect")
    headers = {
        'Content-Dispostion': 'inline; filename="pps.png"'
    }
    rv = BytesIO()
    options = {
        'font_size': 6,
        'text_distance': 3
    }
    code128 = barcode.get_barcode_class('code128')
    code128(code + str(check_digit(code)), writer=ImageWriter()).write(rv, options = options)
    rv.seek(0)
    return StreamingResponse(rv, headers=headers,media_type="image/png")

