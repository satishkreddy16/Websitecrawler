from pydantic import BaseModel


class model(BaseModel):
    """
    Represents the data structure of a model.
    """

    modelname: str
    price: str
    instalment: str
    regdate: str
    coeremaining: float
    mileage: int
    owner: str
  
