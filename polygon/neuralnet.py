import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
#let's import 4 algorithms we would like to test				
#neural networks			
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
#random forests		
from sklearn.ensemble import RandomForestClassifier
dataset = pd.read_csv('malware-dataset.csv')
state = np.random.randint(100)

X = dataset.drop('clean',axis =1)

y = dataset['clean']

X = np.asarray(X)

y = np.asarray(y)

X = X[:,1:]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size =0.1,random_state=0)
#let's start with random forests
#we initiate the classifier
clf1 = RandomForestClassifier()
#training
clf1.fit(X_train,y_train)
#prediction labels for X_test
y_pred=clf1.predict(X_test)
#metrics evaluation
					


"""
					

tn = True Negative a correct prediction clean predicted as clean
					

fp = False Positive a false alarm clean predicted as malicious
					

tp = True Positive a correct prediction (malicious)
					

fn = False Negative a malicious label predicted as clean
					

"""
					

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

print "TN = ",tn

print "TP = ",tp

print "FP = ",fp

print "FN = ",fn
