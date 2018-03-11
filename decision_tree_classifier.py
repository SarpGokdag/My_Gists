#These data sets are randomly generated. They are not scientifically real !
from sklearn import tree
clf = tree.DecisionTreeClassifier()
Gender = ["F","M","F","M","M","F","M","F","M","F","M","F","F","M","M","M","M","F","F","F",
          "M","F","M","F","M","F","F","F","M","F","M","M","F","M","F","M","M","F","M","M"]
Age =    [[24],[31],[20],[74],[52],[30],[81],[19],[76],[82],[49],[39],[54],[27],[80],[69],[58],[23],[58],[49],
          [45],[21],[23],[67],[86],[45],[34],[36],[67],[28],[21],[93],[89],[48],[51],[61],[82],[24],[42],[43]]
clf = clf.fit(Age, Gender) #Training Data Sets
prediction = clf.predict([[21]]) #Predicting 
print(prediction) #Output
