import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("iris.csv")
# print(dataset.describe())
import matplotlib.pyplot as pd
x=dataset.iloc[:,0:2]
y = x.value_counts()
print(y)

# plt.pie(x)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# y = np.array([35, 25, 25, 15])
# myLabels = ["Apples", "Bananas", "Dates", "Mangos"]
# plt.pie(y,labels=myLabels)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# data = {'C': 20, 'C++': 15, 'Java': 30, 'Python': 35}
# courses = list(data.keys())
# values = list(data.values())
# # fig = plt.figure(figsize=(10,5))
# plt.bar(courses, values, color='blue', width=0.4)
# plt.xlabel("Courses offered")
# plt.ylabel("No. of students enrolled")
# plt.title("Students enrolled in different courses")
# plt.show()

# import pandas as pd
#
# data = pd.read_csv("Data.csv")
# data.sort_values(by=["Country"], inplace=True)
# data.drop_duplicates(subset=["Country","Age","Salary","Purchased"], keep="first", inplace=True)
# print(data)

# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
#
# dataset = pd.read_csv("Data.csv")
# dataset.sort_values(by=["Country", "Age"], inplace=True)
# x = dataset.iloc[:, :-1].values
# y = dataset.iloc[:, 3].values
#
# from sklearn.impute import SimpleImputer
#
# imp_mean = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
# imp_mean = imp_mean.fit(x[:, 0:3])
# x[:, 0:3] = imp_mean.transform(x[:, 0:3])
#
# print(x)
