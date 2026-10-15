from sklearn.linear_model import LinearRegression

# Step 1: Prepare the data
hours = [[1], [2], [3], [4], [5]]
marks = [20, 30, 40, 50, 60]

# Step 2: Create the machine learning model
model = LinearRegression()

# Step 3: Train the model
model.fit(hours, marks)

# Step 4: Predict marks for 6 hours of study
predicted_marks = model.predict([[6]])

# Step 5: Display the result
print("Hours studied:", 6)
print("Predicted marks:", predicted_marks[0])