import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from scipy.sparse import hstack

# Load the dataset
df = pd.read_csv('doc.csv')

# Drop irrelevant columns for modeling
df.drop(['product_id', 'invoice_date'], axis=1, inplace=True)

# Concatenate textual columns
textual_cols = ['first_name', 'last_name', 'email', 'address', 'city', 'job']
df['text_features'] = df[textual_cols].apply(lambda x: ' '.join(x), axis=1)

# Initialize CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the text data
X_text = vectorizer.fit_transform(df['text_features'])

# Combine text features with other features
X_other = df.drop(textual_cols + ['text_features', 'amount'], axis=1)
X_combined = hstack([X_other.values, X_text])

# Split data into features (X) and target variable (y)
y = df['amount']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_combined, y, test_size=0.2, random_state=42)

# Initialize and train the RandomForestRegressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
rf_regressor.fit(X_train, y_train)

# Make predictions
y_pred = rf_regressor.predict(X_test)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
