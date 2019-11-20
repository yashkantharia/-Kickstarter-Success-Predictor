#Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Preprocessed_dataset.csv', encoding= 'latin-1')
dataset.dropna(inplace=True)



# Filtering data
a = []
b = []
list1 = dataset['main_category'].unique().tolist()
i=0
for i in range(0,15):
    print(i)
    maincat = list1[i]
    ds1 = dataset[(dataset.main_category == maincat)]
    #Splitting the dataset into dependable variable and independent vector
    cols = [2,4,7,8,9,10,11,12,13]
    X = ds1.iloc[:, cols].values
    Y = ds1.iloc[:, 14].values
    #Y1 = ds4.iloc[:,].values
    
    # Encoding the Independent Variables
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    labelencoder_X = LabelEncoder()
    # 1: Encoding the 'currency' variable
    X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
    # 3: Encoding the 'sub_category' variable
    X[:, 1] = labelencoder_X.fit_transform(X[:, 1])
    # 4: Encoding the 'city' variable
    X[:, 4] = labelencoder_X.fit_transform(X[:, 4])
    # 5: Encoding the 'state' variable
    X[:, 5] = labelencoder_X.fit_transform(X[:, 5])
    # 6: Encoding the 'country' variable
    X[:, 6] = labelencoder_X.fit_transform(X[:, 6])
    
    onehotencoder = OneHotEncoder(categorical_features = [0])
    X = onehotencoder.fit_transform(X).toarray()
    # Encoding the Dependent Variable
    labelencoder_Y = LabelEncoder()
    Y = labelencoder_Y.fit_transform(Y)
    
    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, random_state = 1)
    #Y_train1,Y_test1 =  train_test_split( Y, test_size = 0.1, random_state = 1)
    
    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.transform(X_test)
    
    #RF
    w = 150
    from sklearn.ensemble import RandomForestClassifier
    classifier = RandomForestClassifier(class_weight={0: 1, 1: w}, n_estimators = 150, criterion = 'gini', random_state = 0,n_jobs = -1)
    classifier.fit(X_train, Y_train)
    
    Y_pred = classifier.predict(X_test)
    from sklearn.metrics import accuracy_score
    a.append(list1[i])
    b.append(accuracy_score(Y_test,Y_pred))
    print(len(X),a[i])
    from sklearn.metrics import classification_report
    target_names = ['successful','failed']
    print(classification_report(Y_test,Y_pred,target_names = target_names))
    
results = [a,b]
avg = sum(b)/len(b)

print(avg*100)
