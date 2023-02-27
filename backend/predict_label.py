def predict_label(url):
    from nltk.stem import WordNetLemmatizer
    from nltk.tokenize import RegexpTokenizer
    import pandas as pd
    import numpy as np
    import pickle
    
    # Load the saved model
    with open('cv_model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    with open('vectorizer.pkl', 'rb') as v:
        cv = pickle.load(v)
    
    # preprocess
    tok= RegexpTokenizer(r'[A-Za-z0-9]+')
    wnl = WordNetLemmatizer()
    cleaned_url = [wnl.lemmatize(word) for word in tok.tokenize(url)]
    cleaned_url_series = pd.Series([cleaned_url])
    url_features = cv.transform(cleaned_url_series.astype('str'))
    
    # Make the prediction
    prediction = model.predict(url_features)
    return prediction[0]
