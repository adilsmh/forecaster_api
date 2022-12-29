from fastapi import FastAPI
import numpy as np
import pandas as pd
from datetime import date, timedelta

app = FastAPI()

@app.get("/forecast/{n_weeks}")
def forecast_number_of_products(n_weeks: int):
    data = []
    for i in range(n_weeks):
        # Generate a dummy forecast with a random value
        forecasted_number_of_products = np.random.randint(100)
        forecasting_date =(date.today() + timedelta(weeks=i))
        data.append({"date": forecasting_date, "forecasted_number_of_products": forecasted_number_of_products})

    return data
