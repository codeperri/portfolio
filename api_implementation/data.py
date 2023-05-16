from dataclasses import dataclass


@dataclass
class Product:
    code: str
    name: str
    category: str
    price: float
    quantity: int
    percentage_discount: float
