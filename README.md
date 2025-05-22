
# Job-Posting-Classification-

This Streamlit app scrapes job listings from [Karkidi.com](https://www.karkidi.com), preprocesses and clusters them using unsupervised learning (KMeans), and recommends jobs to users based on their input skills or interests.

 Features

-  Web scraping from Karkidi.com
-  Text preprocessing (Skills + Summary)
-  TF-IDF vectorization
-  Clustering using KMeans
-  Streamlit-based interactive web app
-  Simple job recommender by user input

 Project Structure
├── app.py                    # Streamlit app UI
├── clustered\_jobs.csv        # Pre-scraped & clustered job data
├── cluster\_model.pkl         # Trained KMeans model
├── vectorizer.pkl            # Trained TF-IDF vectorizer
├── requirements.txt          # Dependencies for the app
├── README.md                 # You're here

 Installation & Run Locally


# Clone the repository
git clone https://github.com/yourusername/job-posting-classifier.git
cd job-posting-classifier

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

 It Works

### 1. Scraping (`scrape_karkidi_jobs`)

* Scrapes job titles, companies, locations, summaries, and skills

### 2. Preprocessing

* Merges summary + skills into a single text feature

### 3. Clustering

* Vectorizes text with `TfidfVectorizer`
* Clusters job posts using `KMeans` into predefined clusters
* Saves model and vectorizer with `joblib`

### 4. Streamlit App

* User enters their interests/skills
* App predicts the most relevant job cluster
* Shows jobs from that cluster

## Requirements

txt
streamlit
pandas
scikit-learn
beautifulsoup4
requests
joblib
