def exponential_MA(price_vector, alpha = 0.5):
    ema_new = price_vector[0]
    ema = [ema_new]
    for i in range(1, len(price_vector)):
        ema_new = alpha * price_vector[i] + (1 - alpha) * ema_new
        ema.append(ema_new)
    return ema
