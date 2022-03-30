# NLP Midterm Assignment

Assignment for the course in Natural Language Processing 20587  

In this assignment, you can find my project entailing the application of various NLP frameworks and models. The notebook `main.ipynb` contains the entirety of the project.It is split up into Dataset Preprocessing, Analysis, and Visualization.

## Dataset

The dataset used for this assignment consists of all the articles from **The Guardian**, a British daily newspaper, from 1914 up to the 23rd of March 2023, that contain the words "war", "warfare" or "conflict" in the *politics* section of the editorial.  
The articles were obtained freely through their open API https://open-platform.theguardian.com/, the scripts to request, download and clean the files are included in the folder under `/dataset_guardian`.  
The final, cleaned dataset consists of 21233 articles (after dropping duplicates), with 3 columns: headline, body (the article itself, where we're going to focus our analysis on) and date of first publication.

For our research, we are going to look into the major wars that the UK has been a part of in the time-frame considered. https://en.wikipedia.org/wiki/List_of_wars_involving_the_United_Kingdom#United_Kingdom_of_Great_Britain_and_Northern_Ireland_(1922%E2%80%93present)  

We are going to tag our datasets according to the timeframe given by the above wikipedia page, and adding a query filter to the body article to contain some keyword to identify press coverage around such war. This method is far from perfect, but it is good enough for our analysis.

The wars we will consider are:
- `The Troubles` (1968 - 1998), a long civil conflict between Great Britain and various Irish paramilitary and independentist groups;
- `Afghanistan War` (2001 - 2021), against the Taliban-ruled Islamic Emirate
- `Iraq War` (2003 - 2009), 
- `Lybian Civil War` (2011)
- `Operation Shader` (2014 -), the ongoing intervention of UK as part of the conflict in Iraq and Syria against Islamic State that succeeded al-Qaeda.
- `Ukraine War` (2022 -), the ongoing conflict following the Russian invasion of Ukrainian borders.

## Analysis and Models Used

- Word Embedding (Word2Vec)
- Document Embedding (Doc2Vec)
- Dimensionality Reduction for visualization (t-SNE)
- Continuous Representations (TF-IDF)
- Topic Modeling (LDA)
- Language Models (N-gram models)