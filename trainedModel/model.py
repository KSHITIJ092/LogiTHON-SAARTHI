import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the dataset
df = pd.read_csv('doc.csv')

# Drop irrelevant columns for modeling
df.drop(['product_id', 'invoice_date'], axis=1, inplace=True)

# Concatenate textual columns
textual_cols = ['first_name', 'last_name', 'email', 'address', 'city', 'job']
df['text_features'] = df[textual_cols].apply(lambda x: ' '.join(x), axis=1)
print(df.head())

# Initialize CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the text data
X_text = vectorizer.fit_transform(df['text_features'])

# Convert to DataFrame and concatenate with original DataFrame
df_text_features = pd.DataFrame(X_text.toarray(), columns=vectorizer.get_feature_names_out())
df = pd.concat([df, df_text_features], axis=1)
print(df.head())

# Drop original textual columns
df.drop(textual_cols + ['text_features'], axis=1, inplace=True)

# Split data into features (X) and target variable (y)
X = df.drop('amount', axis=1)
y = df['amount']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("i am bot")
# Initialize and train the RandomForestRegressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
rf_regressor.fit(X_train, y_train)
print("i am not a bot")

# Make predictions
y_pred = rf_regressor.predict(X_test)
print(y_pred)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
