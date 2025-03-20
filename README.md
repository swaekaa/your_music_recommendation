# 🎵 Spotify Music Recommendation System  

This is a **Streamlit web application** that suggests similar songs based on a selected track. It uses **K-Nearest Neighbors (KNN) with cosine similarity** to find the most relevant recommendations.  

---

## 🌟 Recommended: Export Your Spotify Playlist  
To get the best recommendations, export your Spotify playlist using **[Exportify](https://exportify.net/)**:  
1️⃣ **Go to** [Exportify](https://exportify.net/)  
2️⃣ **Log into** your Spotify account  
3️⃣ **Export** your desired playlist as a **CSV file**  
4️⃣ **Upload** the CSV file into this app to get recommendations  

---

## 🚀 Features  
✅ Upload your **Spotify dataset (CSV)**  
✅ Get **5 song recommendations** based on a selected track  
✅ Uses **KNN (cosine similarity)** for accurate results  
✅ Simple and interactive **web interface** with Streamlit  

---

## 📂 Dataset Format  
Your uploaded **CSV file** should contain the following columns:  

| Column Name       | Description |
|------------------|-------------|
| `Track Name` | Song title |
| `Danceability` | Measure of how suitable a track is for dancing (0 to 1) |
| `Energy` | Intensity and activity level of a song (0 to 1) |
| `Key` | The overall musical key of the track (Integer) |
| `Loudness` | Overall loudness in decibels (dB) |
| `Mode` | Major (1) or Minor (0) scale of the song |
| `Speechiness` | Presence of spoken words in a track (0 to 1) |
| `Acousticness` | Probability of a track being acoustic (0 to 1) |
| `Instrumentalness` | Probability of a track having no vocals (0 to 1) |
| `Liveness` | Probability of a track being a live recording (0 to 1) |
| `Valence` | Positivity of a track (0 to 1) |
| `Tempo` | Estimated beats per minute (BPM) |
| `Duration (ms)` | Length of the song in milliseconds |

Ensure the column names **match exactly** for the model to work correctly.

---

## 🛠 Installation  
### 1️⃣ Clone this repository:  
```sh
git clone https://github.com/swaekaa/your_music_reccomendation.git
cd your_music_reccomendation
