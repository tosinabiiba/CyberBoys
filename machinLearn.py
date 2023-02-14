import numpy as np
from sklearn import svm

# Training data
X = np.array([[50], [60], [70], [80], [90], [100]])
y = np.array(['cold', 'cold', 'warm', 'warm', 'hot', 'hot'])

# Create and train the classifier
clf = svm.SVC()
clf.fit(X, y)

# Test the classifier
test_data = [[75]]
prediction = clf.predict(test_data)
print(prediction)
