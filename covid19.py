import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from gekko import gekko
#from scipy.optmize import curve_fit as cf

table = pd.read_csv('C:/Users/Rodrigo Reis/Desktop/covid_19/data.csv',usecols=['dia', 'infetados', 'suspeitos'])
np_table = table.to_numpy()

dia = [i[0] for i in np_table]
infetados = [i[1] for i in np_table]
suspeitos = [i[2] for i in np_table]
dia_infetados = [[i[0],i[1]] for i in np_table]

step=0.00001

def func(l, y):
    return abs(y - sum([s[1]/(y**s[0]) for s in l]) / len(l))

def calc_x(l,res):
    return sum([s[1]/(res**s[0]) for s in l]) / len(l)

value = 10
l = [i for i in np.arange(1.0, 3.0, step)]

b = 0
min_value = func(dia_infetados, l[0])

for value in l:
    current = func(dia_infetados, value)
    if current < min_value:
        min_value = current
        b = value

a = dia_infetados[len(dia_infetados)-1][1]/(b**len(dia_infetados))


def exp(a, b, x):
    return a*b**x

x = np.arange(1, 18, 1)
previsao = round(exp(a, b, len(dia_infetados)+1), 0)

plt.scatter(dia, infetados, label='infetados', color='blue', alpha=0.5)
plt.plot(x, exp(a, b, x), label='exponencial', color='orange')
plt.scatter(len(dia_infetados)+1, previsao, color ='red', label='PREVISÃO DIA '+ str(len(dia_infetados)+1) + ': ' + str(previsao) + ' INFETADOS')
plt.xlabel('dias')
plt.ylabel('população')
plt.title('COVID-19 PORTUGAL')
plt.legend()
plt.show()