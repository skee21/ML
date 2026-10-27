#Boosting and Bagging
print("Bagging and Boosting")
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report
from sklearn.ensemble import BaggingClassifier,AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
#load iris dataset
iris=load_iris()
X=iris.data
y=iris.target
#Split Dataset
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
#Bagging Classifer
bagging=BaggingClassifier(estimator=DecisionTreeClassifier(),n_estimators=50,random_state=42)
bagging.fit(X_train,y_train)
y_pred_bag=bagging.predict(X_test)
#Boosting Classifier
boosting=AdaBoostClassifier(estimator=DecisionTreeClassifier(max_depth=1),n_estimators=50,learning_rate=1,random_state=42)
boosting.fit(X_train,y_train)
y_pred_boost=boosting.predict(X_test)

print("Bagging Performance:")
print("Accuracy:",accuracy_score(y_test,y_pred_bag))
print(classification_report(y_test,y_pred_bag,target_names=iris.target_names))
print("Boosting Performance:")
print("Accuracy:",accuracy_score(y_test,y_pred_boost))
print(classification_report(y_test,y_pred_boost,target_names=iris.target_names))