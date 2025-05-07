# YouTube Sentiment & Topic Explorer

This project uses Natural Language Processing (NLP) to analyze and visualize YouTube comments based on sentiment and topic trends. The goal is to explore how comments relate to sentiments (positive, neutral, negative) and uncover dominant topics using LDA (Latent Dirichlet Allocation) modeling.

## Features

1. **Sentiment Distribution**: A histogram visualizing the distribution of positive, neutral, and negative sentiments in the dataset.
2. **Sample Comments**: A feature that allows users to view sample comments for each sentiment type (positive, neutral, negative).
3. **Topic Modeling**: Interactive visualization of dominant topics in the comments using LDA and pyLDAvis.

## How to Use

1. **Install Dependencies**:
   First, install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

2. **Prepare Data**:
   Ensure your `comments_with_sentiment.csv` file is structured correctly, with at least the following columns:

   * `sentiment_label`: sentiment classification (positive, neutral, negative).
   * `comment`: the actual comment text.

3. **Run the App**:
   Start the app by running:

   ```bash
   streamlit run app.py
   ```

   This will open the app in your browser, where you can:

   * View the overall sentiment distribution.
   * Select a sentiment to explore sample comments.
   * Interact with the topic modeling visualization.

## LDA Topic Modeling

This project uses LDA for topic modeling, a method for uncovering abstract topics in a collection of text. The model and its data (corpus, dictionary) have been pre-trained and are loaded in the app. The topics are visualized using **pyLDAvis**, allowing users to explore topic clusters interactively.

## Files

* `app.py`: The main Streamlit app that loads the data, generates visualizations, and displays the interactive interface.
* `comments_with_sentiment.csv`: Dataset containing YouTube comments with sentiment labels.
* `models/lda_model.pkl`: Pre-trained LDA model.
* `models/dictionary.pkl`: Dictionary used by the LDA model.
* `models/corpus.pkl`: Corpus used by the LDA model.
* `requirements.txt`: File listing all the required Python libraries.

## Conclusion

This project provides an interactive way to explore YouTube comments, understand sentiment trends, and uncover underlying topics using NLP techniques. The visualizations and interactive components make it a great tool for anyone looking to analyze YouTube content more deeply.

---
