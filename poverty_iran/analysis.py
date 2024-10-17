import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Create the DataFrame from the provided data
data = {
    'year': [1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399],
    'low_income': [0.462008574, 0.37265892, 0.378932924, 0.385212221, 0.375212447, 0.383526628, 0.324694938, 0.318764932, 0.306730275, 0.310985272, 0.286736021, 0.252317643, 0.250462697, 0.22622403, 0.206049838, 0.214364019, 0.236922385, 0.247276741, 0.24948627, 0.255770859, 0.24780597, 0.302922476, 0.341775789, 0.368393338],
    'middle_income': [0.456506109, 0.504972858, 0.510738803, 0.498190794, 0.501900686, 0.489336801, 0.543929371, 0.533400369, 0.539150437, 0.516406841, 0.534371503, 0.564545468, 0.558091526, 0.58011008, 0.612324221, 0.616044697, 0.615695406, 0.60515582, 0.59665641, 0.590197175, 0.579678758, 0.548800919, 0.538266625, 0.519619258],
    'high_income': [0.081485318, 0.122368222, 0.110328273, 0.116596985, 0.122886866, 0.127136571, 0.131375692, 0.147834699, 0.154119288, 0.172607887, 0.178892476, 0.183136889, 0.191445777, 0.19366589, 0.181625941, 0.169591284, 0.147382209, 0.147567439, 0.15385732, 0.154031965, 0.172515272, 0.148276605, 0.119957586, 0.111987404]
}

df = pd.DataFrame(data)

# Function to fit linear model and predict
def fit_linear_segment(years, values):
    model = LinearRegression()
    X = np.array(years).reshape(-1, 1)
    y = np.array(values)
    model.fit(X, y)
    return model.predict(X)

# Splitting data for each income group based on the requested segments
# Segment 1: 1376 to 1390
years_1 = df['year'][df['year'] <= 1390]
low_income_1 = df['low_income'][df['year'] <= 1390]
middle_income_1 = df['middle_income'][df['year'] <= 1390]
high_income_1 = df['high_income'][df['year'] <= 1390]

# Segment 2: 1390 to 1395
years_2 = df['year'][(df['year'] > 1390) & (df['year'] <= 1395)]
low_income_2 = df['low_income'][(df['year'] > 1390) & (df['year'] <= 1395)]
middle_income_2 = df['middle_income'][(df['year'] > 1390) & (df['year'] <= 1395)]
high_income_2 = df['high_income'][(df['year'] > 1390) & (df['year'] <= 1395)]

# Segment 3: 1395 to the end
years_3 = df['year'][df['year'] > 1395]
low_income_3 = df['low_income'][df['year'] > 1395]
middle_income_3 = df['middle_income'][df['year'] > 1395]
high_income_3 = df['high_income'][df['year'] > 1395]

# Fit linear models and predict
low_income_pred_1 = fit_linear_segment(years_1, low_income_1)
low_income_pred_2 = fit_linear_segment(years_2, low_income_2)
low_income_pred_3 = fit_linear_segment(years_3, low_income_3)

middle_income_pred_1 = fit_linear_segment(years_1, middle_income_1)
middle_income_pred_2 = fit_linear_segment(years_2, middle_income_2)
middle_income_pred_3 = fit_linear_segment(years_3, middle_income_3)

high_income_pred_1 = fit_linear_segment(years_1, high_income_1)
high_income_pred_2 = fit_linear_segment(years_2, high_income_2)
high_income_pred_3 = fit_linear_segment(years_3, high_income_3)

# Plot the original data and fitted linear segments again with more accurate vertical lines
plt.figure(figsize=(12, 8))

# Low income
plt.scatter(df['year'], df['low_income'], label='Low Income Data', color='blue')
plt.plot(years_1, low_income_pred_1, label='Low Income Linear Fit (1376-1390)', linestyle='--', color='blue')
plt.plot(years_2, low_income_pred_2, label='Low Income Linear Fit (1390-1395)', linestyle='--', color='lightblue')
plt.plot(years_3, low_income_pred_3, label='Low Income Linear Fit (1395-End)', linestyle='--', color='darkblue')

# Middle income
plt.scatter(df['year'], df['middle_income'], label='Middle Income Data', color='green')
plt.plot(years_1, middle_income_pred_1, label='Middle Income Linear Fit (1376-1390)', linestyle='--', color='green')
plt.plot(years_2, middle_income_pred_2, label='Middle Income Linear Fit (1390-1395)', linestyle='--', color='lightgreen')
plt.plot(years_3, middle_income_pred_3, label='Middle Income Linear Fit (1395-End)', linestyle='--', color='darkgreen')

# High income
plt.scatter(df['year'], df['high_income'], label='High Income Data', color='red')
plt.plot(years_1, high_income_pred_1, label='High Income Linear Fit (1376-1390)', linestyle='--', color='red')
plt.plot(years_2, high_income_pred_2, label='High Income Linear Fit (1390-1395)', linestyle='--', color='lightcoral')
plt.plot(years_3, high_income_pred_3, label='High Income Linear Fit (1395-End)', linestyle='--', color='darkred')

# Adding more accurate vertical lines for sanctions, adjusted for one year earlier
plt.axvline(x=1389 + 8/12, color='gray', linestyle=':', label='Sanctions (Dey 1390)')
plt.axvline(x=1396 + 2/12, color='black', linestyle=':', label='Sanctions (Ordibehesht 1397)')

plt.text(1389 + 8/12, 0.6, 'Dey 1390 Sanctions', rotation=90, verticalalignment='bottom', horizontalalignment='right', color='gray')
plt.text(1396 + 2/12, 0.6, 'Ordibehesht 1397 Sanctions', rotation=90, verticalalignment='bottom', horizontalalignment='right', color='black')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Income Group Proportion')
plt.title('Income Group Trends with Linear Fits and Sanction Annotations')

# Move the legend outside
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()

# Create a DataFrame with the original data and the linear fits
df_fits = pd.DataFrame({
    'year': df['year'],
    'low_income': df['low_income'],
    'middle_income': df['middle_income'],
    'high_income': df['high_income'],
    'low_income_fit': np.concatenate([low_income_pred_1, low_income_pred_2, low_income_pred_3]),
    'middle_income_fit': np.concatenate([middle_income_pred_1, middle_income_pred_2, middle_income_pred_3]),
    'high_income_fit': np.concatenate &#8203;:contentReference[oaicite:0]{index=0}&#8203;
