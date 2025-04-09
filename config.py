# config.py

BASE_URL = "https://www.sgcarmart.com/used-cars/listing?pr1=20001&pr2=35000&cts[]=18&eng=4&own_c=%3C&own=2&fr=2017&to=2017&mil1=80001&mil2=90000"
CSS_SELECTOR = "[class^='styles_listing_box__eDRd3']"
REQUIRED_KEYS = [
    "model name",
    "price",
    "instalment",
    "reg date",
    "coe remaining",
    "mileage",
    "owner",
]
