Python 3.11.0 (v3.11.0:deaf509e8f, Oct 24 2022, 14:43:23) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
... from sklearn.linear_model import LinearRegression
... import pandas as pd
... 
... #Database
... # x = Data, y = Target
... #x = [[1],[3],[5],[7],[9]]
... #y = [2, 6, 10, 14, 18]
... FileDB = 'perkalian.txt'
... Database = pd.read_csv(FileDB, sep=",", header=0)
... print ("---------------------")
... print (Database)
... #x = data, y = target
... x = Database[[u'Feature']] #ciri1, ciri2, dst
... y = Database.Target
... 
... regr = LinearRegression().fit(x,y)
... regr.score(x,y)
... 
... #Data uji
... predict = np.array([[1100]])
... 
... #Menampilakn data prediksi
... print ("Prediksi")
... print ("Input = ", predict)
