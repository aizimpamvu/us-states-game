import pandas

data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()
print(data_dict)