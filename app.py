import streamlit as st
import pandas as pd
import plotly.express as px
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis
import pickle
import gensim
from gensim import corpora

# --- Load the data ---
df = pd.read_csv("data/comments_with_sentiment.csv")

# --- Title and Introduction ---
st.title("📊 YouTube Sentiment & Topic Explorer")
st.markdown("Explore sentiment trends and dominant topics in YouTube comments using NLP.")

# --- Sentiment Distribution ---
st.header("💬 Sentiment Distribution")
fig = px.histogram(
    df,
    x="sentiment_label",
    color="sentiment_label",
    title="Overall Sentiment"
)
st.plotly_chart(fig)

# --- Show Comments by Sentiment ---
st.header("🔍 View Sample Comments")
sentiment_choice = st.selectbox(
    "Select Sentiment",
    ["positive", "neutral", "negative"]
)

filtered_comments = df[df["sentiment_label"] == sentiment_choice]["comment"]

if len(filtered_comments) == 0:
    st.write("No comments found for this sentiment.")
else:
    sample_size = min(5, len(filtered_comments))
    sample_comments = filtered_comments.sample(sample_size)
    for i, comment in enumerate(sample_comments, start=1):
        st.write(f"**{i}.** {comment}")

# --- Topic Modeling Visualization ---
st.header("🧠 Topic Modeling (LDA)")
st.markdown("Explore topic clusters below:")

# Load pre-trained LDA model and data
with open("models/lda_model.pkl", "rb") as f:
    lda_model = pickle.load(f)
with open("models/dictionary.pkl", "rb") as f:
    dictionary = pickle.load(f)
with open("models/corpus.pkl", "rb") as f:
    corpus = pickle.load(f)

# Generate and display pyLDAvis
vis = gensimvis.prepare(lda_model, corpus, dictionary)
html_string = pyLDAvis.prepared_data_to_html(vis)
st.components.v1.html(html_string, height=800, scrolling=True)
