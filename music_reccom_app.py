import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from fuzzywuzzy import process

st.set_page_config(page_title="Spotify Music Recommender", layout="wide")
st.title("🎵 Spotify Music Recommendation System")
st.write("Upload your Spotify dataset and get personalized song recommendations!")

uploaded_file = st.file_uploader("📂 Upload your Spotify playlist (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    features = ['Danceability', 'Energy', 'Key', 'Loudness', 'Mode', 'Speechiness',
                'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo', 'Duration (ms)']
    
    if not set(features).issubset(df.columns):
        st.error("⚠️ Uploaded dataset is missing required features! Please check your CSV file.")
    else:
        df_features = df[features]
        scaler = StandardScaler()
        df_scaled = scaler.fit_transform(df_features)

        model = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='cosine')
        model.fit(df_scaled)

        song_name = st.text_input("🎵 Enter a song name:", "").strip().lower()

        if song_name:
            df['lower_track_name'] = df['Track Name'].astype(str).str.lower()
            match = process.extractOne(song_name, df['lower_track_name'].dropna())

            if match and match[1] >= 60:
                best_match = match[0]
                matching_songs = df[df['lower_track_name'] == best_match]

                unique_artists = matching_songs['Artist Name(s)'].unique()
                artist_name = None

                if len(unique_artists) > 1:
                    artist_name = st.selectbox("🎤 Select an artist (optional):", ["Any"] + list(unique_artists))
                    if artist_name != "Any":
                        matching_songs = matching_songs[matching_songs['Artist Name(s)'] == artist_name]
                else:
                    artist_name = unique_artists[0]

                song_index = matching_songs.index[0]
                song_features = scaler.transform([df_features.loc[song_index]])

                distances, indices = model.kneighbors(song_features, n_neighbors=6)
                recommended_songs = df.iloc[indices[0][1:]]

                st.subheader("🎶 Selected Song Details")
                selected_song = df.iloc[song_index]
                st.markdown(f"## {selected_song['Track Name']}")
                st.write(f"**Artist:** {selected_song['Artist Name(s)']}")
                st.write(f"**Album:** {selected_song['Album Name']}")
                st.write(f"**Duration:** {selected_song['Duration (ms)'] // 60000} min {selected_song['Duration (ms)'] % 60000 // 1000} sec")

                st.subheader("🎧 Recommended Songs")
                for i, (_, row) in enumerate(recommended_songs.iterrows(), 1):
                    st.markdown(f"### {i}. {row['Track Name']}")
                    st.write(f"**Artist:** {row['Artist Name(s)']}")
                    st.write(f"**Album:** {row['Album Name']}")
                    st.write(f"**Duration:** {row['Duration (ms)'] // 60000} min {row['Duration (ms)'] % 60000 // 1000} sec")
            else:
                st.error("❌ No close matches found. Try a different song name.")
