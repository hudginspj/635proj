import pickle
import csvToExamples

# # take user input to take the amount of data
# number_of_data = int(input('Enter the number of data : '))
# data = []

# # take input of the data
# for i in range(number_of_data):
#     raw = input('Enter data '+str(i)+' : ')
#     data.append(raw)

# # open a file, where you ant to store the data
# file = open('learning/important', 'wb')

# # dump information to that file
# pickle.dump(data, file)

# # close the file
# file.close()


# open a file, where you stored the pickled data
file = open('learning/save.p', 'rb')
# dump information to that file
importances = pickle.load(file)
# close the file
file.close()

features = csvToExamples.feature_list('./features/pred-fa_feat_ProtrWeb.csv')
features = csvToExamples.feature_list('./training_data/all_features.csv')

print(importances)

selected = []
for i in range(len(importances)):
    # print(importances[i])
    # condition = importances[i] > 0.0005 and len(features[i]) == 3
    # condition = importances[i] > 0.0005
    condition = importances[i] > 0.0009 and not features[i].startswith("[G1") and not features[i].startswith(" [G1") and not features[i].startswith("[G2")
    if condition:
        print(features[i], importances[i])
        selected.append(features[i])

print("|".join(selected))
print("Selected count: ", len(selected))

