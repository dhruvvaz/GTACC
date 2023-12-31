import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the data
df = pd.read_csv('/users/andrewvaz/Documents/simulated_student_data.csv')

# Define a function to convert grades to GPA points
def grade_to_gpa(grade):
    # Implement the conversion logic based on your school's grading system
    if grade >= 90:
        return 4.0
    elif grade >= 80:
        return 3.0
    elif grade >= 70:
        return 2.0
    elif grade >= 60:
        return 1.0
    else:
        return 0.0

# Convert grades to GPA points
df['GPA'] = df['Grade'].apply(grade_to_gpa)

# Group the data by 'Student ID' and 'Academic Year' and calculate the average GPA
gpa_trends = df.groupby(['Student ID', 'Academic Year']).agg({'GPA': 'mean'}).reset_index()

# Print the average GPA per student per academic year
print(gpa_trends)
# Assuming 'Academic Year' is in the format '2020-2021', '2021-2022', etc.
academic_years = sorted(df['Academic Year'].unique())

# Pivoting the DataFrame to have one row per student and columns for each academic year's GPA
pivot_df = gpa_trends.pivot(index='Student ID', columns='Academic Year', values='GPA')

# Rename the columns to keep only the start year for simplicity, e.g., '2020' for '2020-2021'
pivot_df.columns = [year.split('-')[0] for year in academic_years]

# Create a feature for GPA change between years
for i in range(1, len(academic_years)):
    year = academic_years[i].split('-')[0]
    prev_year = academic_years[i-1].split('-')[0]
    pivot_df[f'GPA_Change_{year}'] = pivot_df[year] - pivot_df[prev_year]

# Prepare the features (X) and target (y)
# The last year will be used as the target, and the previous years as features
X = pivot_df.drop(columns=[academic_years[-1].split('-')[0]])
y = pivot_df[academic_years[-1].split('-')[0]]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
model.fit(X_train, y_train)

# Predict the GPA for the test set
y_pred = model.predict(X_test)

# Calculate the performance
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5

# Output the performance
print(f'RMSE: {rmse}')

# Predict the future GPA and flag students for counseling based on your criteria
# You would use the model.predict() method on the data you want to predict
