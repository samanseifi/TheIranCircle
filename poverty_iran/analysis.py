# Provide the complete code and generate the final CSV

# Complete code:

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

# Define the segments
# Segment 1: 1376 to 1389
years_1 = df['year'][df['year'] <= 1389]
low_income_1 = df['low_income'][df['year'] <= 1389]
middle_income_1 = df['middle_income'][df['year'] <= 1389]
high_income_1 = df['high_income'][df['year'] <= 1389]

# Segment 2: 1389 to 1395
years_2 = df['year'][(df['year'] > 1389) & (df['year'] <= 1395)]
low_income_2 = df['low_income'][(df['year'] > 1389) & (df['year'] <= 1395)]
middle_income_2 = df['middle_income'][(df['year'] > 1389) & (df['year'] <= 1395)]
high_income_2 = df['high_income'][(df['year'] > 1389) & (df['year'] <= 1395)]

# Segment 3: 1395 onwards
years_3 = df['year'][df['year'] > 1395]
low_income_3 = df['low_income'][df['year'] > 1395]
middle_income_3 = df['middle_income'][df['year'] > 1395]
high_income_3 = df['high_income'][df['year'] > 1395]

# Fit the three segments
low_income_pred_1 = fit_linear_segment(years_1, low_income_1)
low_income_pred_2 = fit_linear_segment(years_2, low_income_2)
low_income_pred_3 = fit_linear_segment(years_3, low_income_3)

middle_income_pred_1 = fit_linear_segment(years_1, middle_income_1)
middle_income_pred_2 = fit_linear_segment(years_2, middle_income_2)
middle_income_pred_3 = fit_linear_segment(years_3, middle_income_3)

high_income_pred_1 = fit_linear_segment(years_1, high_income_1)
high_income_pred_2 = fit_linear_segment(years_2, high_income_2)
high_income_pred_3 = fit_linear_segment(years_3, high_income_3)

# Combine all predictions and segments
low_income_fit_combined_all = np.concatenate([low_income_pred_1, low_income_pred_2, low_income_pred_3])
middle_income_fit_combined_all = np.concatenate([middle_income_pred_1, middle_income_pred_2, middle_income_pred_3])
high_income_fit_combined_all = np.concatenate([high_income_pred_1, high_income_pred_2, high_income_pred_3])

# Now create the DataFrame with the fitted years
years_fitted_all = np.concatenate([years_1, years_2, years_3])

# Creating the final DataFrame with the added segment
df_fits_full = pd.DataFrame({
    'year': years_fitted_all,
    'low_income': np.concatenate([low_income_1, low_income_2, low_income_3]),
    'middle_income': np.concatenate([middle_income_1, middle_income_2, middle_income_3]),
    'high_income': np.concatenate([high_income_1, high_income_2, high_income_3]),
    'low_income_fit': low_income_fit_combined_all,
    'middle_income_fit': middle_income_fit_combined_all,
    'high_income_fit': high_income_fit_combined_all
})

# Save the DataFrame as a CSV file
csv_path_full_final = '/mnt/data/income_group_fits_three_segments_final.csv'
df_fits_full.to_csv(csv_path_full_final, index=False)

csv_path_full_fina