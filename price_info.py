from pydantic import BaseModel

class PriceInfo(BaseModel):
    open: float
    volume: float
    low: float
    high: float