# Task1 Using PyCharm not Spyder !!!!!
# 1. & 2.
# import pandas as pd
#
# dataset = pd.read_csv("Wuzzuf_Jobs.csv")
# x = dataset.iloc[0:10, 0:2]
# print(x)  # display some from dataset
# print(dataset.info) # display structure
# print(dataset.describe())  # Summary of the data
# ----------------------------------------------------------#
# 3.
# import pandas as pd
# import numpy as np
#
# dataset = pd.read_csv("Wuzzuf_Jobs.csv")
# dataset.sort_values(by=["Title", "Company", "Location", "Type", "Level", "YearsExp", "Country", "Skills"], inplace=True)
# dataset.drop_duplicates(subset=["Title", "Company", "Location", "Type", "Level", "YearsExp", "Country", "Skills"], keep="first", inplace=True)
# x = dataset.iloc[:, :].values
#
# from sklearn.impute import SimpleImputer
#
# imp_mean = SimpleImputer(missing_values=None, strategy='most_frequent')
# imp_mean = imp_mean.fit(x[:, :])
# x[:, :] = imp_mean.transform(x[:, :])
# print(x)
# ----------------------------------------------------------#
# 4. & 5.
# import matplotlib.pyplot as plt
# import pandas as pd
#
# dataset = pd.read_csv("Wuzzuf_Jobs.csv")
# import matplotlib.pyplot as pd
#
# x = dataset.iloc[:, 1:2]
# y = x.value_counts()
# print(y)
# plt.pie(y)
# plt.show()
# ----------------------------------------------------------#
# # 6. & 7.
# import matplotlib.pyplot as plt
# import pandas as pd
#
# dataset = pd.read_csv("Wuzzuf_Jobs.csv")
# import matplotlib.pyplot as pd
#
# x = dataset.iloc[500:550, 0:1]
# y = x.value_counts()
# print(y)
# fig = plt.figure(figsize=(5,2))
# y.plot.bar(color='maroon',width=0.1,fontsize=10)
# plt.xlabel("Jobs")
# plt.ylabel("No. of workers")
# plt.title("Most Jobs")
# plt.show()
# ----------------------------------------------------------#
# # 8. & 9.
# import matplotlib.pyplot as plt
# import pandas as pd
#
# dataset = pd.read_csv("Wuzzuf_Jobs.csv")
# import matplotlib.pyplot as pd
#
# x = dataset.iloc[0:50, 2:3]
# y = x.value_counts()
# print(y)
# y.plot.bar(color='pink', width=0.4, fontsize=8)
# plt.xlabel("Areas")
# plt.ylabel("No. of people")
# plt.title("Most Areas")
# plt.show()
# ----------------------------------------------------------#
# # 10.
# import pandas as pd
#
# dataset = pd.read_csv("Wuzzuf_Jobs.csv")
#
# x = dataset.iloc[:, len(dataset.columns) - 1:len(dataset.columns)]
# y=x.value_counts()
# print(y)
