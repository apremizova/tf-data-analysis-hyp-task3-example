import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest

chat_id = 370558433 # Ваш chat ID, не меняйте название переменной

def solution(x) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    stat, pval = ztest(x,value = 300,alternative= 'smaller')
    ans = True if pval < 0.04 else False
    return ans # Ваш ответ, True или False
