Hierarchical Clustering of Job Postings
This project scrapes job listings from Karkidi.com, extracts skill-related information, and clusters the jobs using Hierarchical Clustering. It helps to group similar job roles based on the required skills.

 Overview
 Scrapes job postings by keyword and location.
 Cleans and processes skill text.
 Converts skills into feature vectors using TF-IDF.
 Clusters jobs using Agglomerative Clustering.
 Saves clustered data, model, and vectorizer for reuse.

📁 Files
File/Folder	Description
hierarchical_clustering_scrape_the_job_postings_.py	Main Python script
clustered_jobs.csv	Output CSV with job listings and clusters
model/karkidi_model.pkl	Saved clustering model
model/karkidi_vectorizer.pkl	Saved TF-IDF vectorizer

Installation
Make sure you have Python 3.6+ installed, then run:

bash
Copy
Edit
pip install requests beautifulsoup4 pandas scikit-learn joblib

How to Run
bash
Copy
Edit
python hierarchical_clustering_scrape_the_job_postings_.py
You can customize scraping by editing the parameters in:

python
Copy
Edit
df_jobs = scrape_karkidi_jobs(keyword="data science", pages=2)

Functions
scrape_karkidi_jobs(keyword, pages)
Scrapes job posts with specified keyword and number of pages.

preprocess_skills(df)
Cleans skill strings and prepares them for vectorization.

cluster_jobs(df, n_clusters)
Clusters job postings based on required skills.

save_all(df, model, vectorizer)
Saves output CSV and model files to the model/ directory.

Output
A clustered_jobs.csv file with a new column Cluster.
Plots or analysis can be added using the Cluster column.



