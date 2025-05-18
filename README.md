# 🎬 AI-Powered Movie Recommendation System

An intelligent, user-friendly movie recommendation system that helps users discover movies they are likely to enjoy using **Content-Based Filtering** and **Collaborative Filtering** techniques. Built using machine learning, the system leverages real-world movie datasets and provides an interactive UI for enhanced user experience.

---

## 📌 Features

- 🔍 Search and select a movie title.
- 🎯 Get a list of similar or recommended movies.
- 🖼️ View movie posters, genres, and descriptions.
- 🤖 Uses ML techniques like TF-IDF, cosine similarity, and matrix factorization.
- 💻 Clean and responsive user interface using Streamlit.
- 🛠️ Handles invalid inputs and missing data gracefully.

---

## 📊 Recommendation Techniques

### 🔹 Content-Based Filtering
Uses metadata such as:
- Genres
- Keywords
- Overviews

Applies:
- **TF-IDF Vectorization** to process text data.
- **Cosine Similarity** to compare movie vectors and return similar titles.

### 🔹 Collaborative Filtering *(Optional / Advanced)*
Uses:
- **MovieLens dataset** with user ratings.
- **Matrix Factorization** (e.g., SVD) to predict unseen movie ratings.

---

## 🗂️ Dataset & APIs Used

- [MovieLens Dataset](https://grouplens.org/datasets/movielens/)
- [TMDB API](https://www.themoviedb.org/documentation/api) for movie posters and details

---

## 💻 Technologies Used

| Category         | Tools/Technologies                        |
|------------------|-------------------------------------------|
| Language         | Python                                    |
| ML Libraries     | Scikit-learn, Pandas, NumPy               |
| NLP Tools        | NLTK, SciPy, TF-IDF Vectorizer            |
| Web Framework    | Streamlit / Flask                         |
| External APIs    | TMDB API                                  |
| Deployment       | Streamlit Cloud / Render.com              |
| Version Control  | Git, GitHub                               |

---

## 🚀 Getting Started

### 1. Clone the Repository
🖼️ Screenshot 
![hackathon ss](https://github.com/user-attachments/assets/c3820d2d-7e5a-4ac9-87b8-aaa69ae973de)
![hackathon ss cmd](https://github.com/user-attachments/assets/ef8f028a-032d-446f-bc05-611daacb47a8)

# bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
📦 Deployment
You can deploy this app on:

Streamlit Cloud

Render.com

Just link your GitHub repo and follow platform-specific instructions.

🧠 How It Works
User inputs a movie title.

The system converts movie descriptions into TF-IDF vectors.

Cosine similarity is calculated between the selected movie and others.

Top N similar movies are fetched and displayed with metadata and posters.

📈 Future Enhancements
Hybrid recommendation engine (content + collaborative).

Mood or emotion-based filtering.

User login/profile system to save history and preferences.

Mobile version using Flutter or React Native.

Voice assistant or chatbot integration.

🤝 Contributing
Contributions are welcome! Feel free to fork this repo and submit pull requests.

Fork the repo

Create your branch (git checkout -b feature-xyz)

Commit your changes (git commit -am 'Add new feature')

Push to the branch (git push origin feature-xyz)

Open a Pull Request

📄 License
This project is licensed under the MIT License.

🙋‍♂️ Acknowledgments
MovieLens

TMDb API

Streamlit
