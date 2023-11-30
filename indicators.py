import numpy as np

def exponential_MA(price_vector, alpha = 0.5):
    ema_new = price_vector[0]
    ema = [ema_new]
    for i in price_vector[1:]:
        ema_new = alpha * i + (1 - alpha) * ema_new
        ema.append(ema_new)
    return ema
