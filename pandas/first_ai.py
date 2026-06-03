import joblib
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
print("1. Loading and cleaning data...")
df=pd.read_csv('anime.csv')

df=df[df['episodes']!= 'Unknown']
df=df.dropna(subset=['rating','episodes','members'])
print("2. Setting up Inputs(features) and Output(target)")
X=df[['episodes','members']]
y=df[['rating']]
print("3. Training the AI model")
model = DecisionTreeRegressor()
model.fit(X,y)
print("4. Making predictions")
fake_data = [[24, 50000]]
predicted_rating = model.predict(fake_data)
print(f"5. Predicted rating for the fake data: {predicted_rating[0]:.2f}/10")
print("5. Saving the Model...")
joblib.dump(model, 'anime_rating_brain.pkl')
print("Model saved successfully as anime_rating_brain.pkl!")