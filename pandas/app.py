import streamlit as st
import pandas as pd
import joblib

# 1. Load the frozen brain and the original data
model = joblib.load('anime_rating_brain.pkl')
df = pd.read_csv('anime.csv')

st.title("Anime Success Predictor AI")
st.write("Filter the dataset and adjust parameters to predict ratings.")

# 2. Clean the genre data and get a list of all unique genres
# Anime genres in the CSV are often comma-separated strings (e.g., "Action, Comedy, Sci-Fi")
# We need to extract every unique genre to put in our dropdown
df = df.dropna(subset=['genre']) # Drop rows with missing genres
all_genres = set()
for genres_string in df['genre']:
    genres_list = genres_string.split(', ')
    for genre in genres_list:
        all_genres.add(genre)
sorted_genres = sorted(list(all_genres)) # Sort them alphabetically

# 3. Create the multiselect dropdown for the user
selected_genres = st.multiselect(
    "Filter by Genre (Leave blank to use all data):",
    options=sorted_genres,
    default=[]
)

# 4. Filter the dataset based on the user's selection
if selected_genres:
    # Create the filter mask
    mask = df['genre'].apply(lambda x: any(genre in x for genre in selected_genres))
    filtered_df = df[mask]
    st.write(f"Dataset filtered down to {len(filtered_df)} shows matching these genres.")
else:
    filtered_df = df
    st.write(f"Using full dataset of {len(filtered_df)} shows.")

# --- NEW CODE: SORT AND DISPLAY ---
st.subheader("Leaderboard")
# Clean the data: drop rows where rating is missing so the sort doesn't crash
filtered_df = filtered_df.dropna(subset=['rating'])

# Sort by rating in descending order (highest to lowest)
sorted_df = filtered_df.sort_values(by='rating', ascending=False)

# Display an interactive table showing only the columns that matter
st.dataframe(
    sorted_df[['name', 'rating', 'episodes', 'genre', 'members']], 
    use_container_width=True, # Makes the table stretch across the screen
    hide_index=True # Hides the ugly row numbers
)


# 5. Create interactive sliders for the user
st.markdown("---")
st.subheader("Predict a New Show")
episodes = st.slider("Number of Episodes", min_value=1, max_value=1000, value=24)
members = st.slider("Community Members (Popularity)", min_value=100, max_value=2000000, value=500000)

# 6. Make the prediction
if st.button("Predict Rating"):
    # Pass the slider values into the model
    prediction = model.predict([[episodes, members]])
    st.success(f"Predicted Rating: {prediction[0]:.2f} / 10")