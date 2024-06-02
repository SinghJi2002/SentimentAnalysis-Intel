import pickle
import re
import nltk
import streamlit as st
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')
from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words('english'))


model=pickle.load(open('D:/SentimentAnalysis-Intel/Saved_Models/model_xgb.pkl', 'rb'))
countVectoriser=pickle.load(open('D:/SentimentAnalysis-Intel/Saved_Models/countVectorizer.pkl', 'rb'))
scaler=pickle.load(open('D:/SentimentAnalysis-Intel/Saved_Models/scaler.pkl', 'rb'))

def prediction(text):
    stemmer = PorterStemmer()
    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower().split()
    review = [stemmer.stem(word) for word in review if not word in STOPWORDS]
    review = ' '.join(review)
    review = countVectoriser.transform([review]).toarray()
    review = scaler.transform(review)
    prediction = model.predict(review)
    return(prediction)
def main():
    st.title('Sentiment Analysis Application')
    review=st.text_area("Enter Your Review")
    pred=''
    if(st.button('Sentiment Analysis')):
        pred=prediction(review)
        pred=pred[0]
        if(pred==2):
            pred='Positive Review'
        elif(pred==1):
            pred='Neutral Review'
        else:
            pred='Negetive Review'
    st.success(pred)
if __name__ == '__main__':
    main()

    
    
     
    
    