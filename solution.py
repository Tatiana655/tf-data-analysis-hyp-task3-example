import pandas as pd
import numpy as np

import statsmodels.stats.weightstats

chat_id = 372005520 # Ваш chat ID, не меняйте название переменной

def solution(x) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.02
    _, pvalue = statsmodels.stats.weightstats.ztest(x, value=500, alternative="larger")
    return pvalue <= alpha
