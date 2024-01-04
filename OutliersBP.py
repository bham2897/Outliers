import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/Users/divya/Desktop/Python projects/stroke_data.csv'
stroke_data = pd.read_csv(file_path)

# Splitting 'Blood Pressure Levels' into 'Systolic BP' and 'Diastolic BP'
stroke_data[['Systolic BP', 'Diastolic BP']] = stroke_data['Blood Pressure Levels'].str.split('/', expand=True).astype(float)

# Splitting 'Cholesterol Levels' into 'HDL' and 'LDL'
stroke_data['HDL'] = stroke_data['Cholesterol Levels'].str.extract(r'HDL: (\d+)').astype(float)
stroke_data['LDL'] = stroke_data['Cholesterol Levels'].str.extract(r'LDL: (\d+)').astype(float)

# Dropping the original composite columns
stroke_data.drop(['Blood Pressure Levels', 'Cholesterol Levels'], axis=1, inplace=True)

# Visualizing the distributions of the new numeric columns
new_numeric_columns = ['Systolic BP', 'Diastolic BP', 'HDL', 'LDL']
plt.figure(figsize=(12, 4))
for i, col in enumerate(new_numeric_columns):
    plt.subplot(1, 4, i + 1)
    sns.boxplot(x=stroke_data[col])
    plt.title(f'Distribution of {col}')
plt.tight_layout()
plt.show()

# Summary statistics of the new numeric columns
new_numeric_summary = stroke_data[new_numeric_columns].describe()
print(new_numeric_summary)
