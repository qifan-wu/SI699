def save_model():
    import pandas as pd
    import numpy as np
    import seaborn as sb
    import matplotlib.pyplot as plt
    from nltk.tokenize import RegexpTokenizer
    import nltk
    #nltk.download('wordnet')
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.feature_extraction.text import CountVectorizer  
    from sklearn.model_selection import train_test_split
    from sklearn import metrics
    from sklearn.metrics import confusion_matrix,mean_squared_error,precision_score,recall_score,f1_score
    from sklearn.metrics import classification_report , roc_curve, f1_score, accuracy_score, recall_score , roc_auc_score,make_scorer

    import pickle
    
    df= pd.read_csv("phishing_site_urls.csv")

    df.drop(df[df.URL.duplicated() == True].index, axis = 0, inplace = True)
    df.reset_index(drop=True)
    sw=list(set(stopwords.words("english")))
    df['clean_url']=df.URL.astype(str)
    tok= RegexpTokenizer(r'[A-Za-z0-9]+')
    df.clean_url=df.clean_url.map(lambda x: tok.tokenize(x))

    nltk.download('omw-1.4')
    wnl = WordNetLemmatizer()
    df['lem_url'] = df['clean_url'].map(lambda x: [wnl.lemmatize(word) for word in x])
    
    df_train, df_test = train_test_split(df, random_state=42,test_size=0.2,shuffle=True)
    cv = CountVectorizer() 

    y_train = df_train.Label
    y_test = df_test.Label
    y_train=np.where(y_train=='bad',1,0)
    y_test=np.where(y_test=='bad',1,0)

    x_train = cv.fit_transform(df_train.lem_url.astype('str'))
    x_test = cv.transform(df_test.lem_url.astype('str'))

    # save vectorizer
    with open('vectorizer.pkl', 'wb') as f:
        pickle.dump(cv, f)
        
    # train model
    from sklearn.svm import LinearSVC
    trained_clf_svc = LinearSVC().fit(x_train, y_train)
    get_accuracy('LinearSVC',trained_clf_svc,x_train, y_train, x_test, y_test)
    
    # save model
    with open('cv_model.pkl', 'wb') as f:
        pickle.dump(trained_clf_svc, f)
        

def get_accuracy(name, trained_model, x_train, y_train, x_test, y_test):
    tree_predict = trained_model.predict(x_test)
    print("Testing accuracy   :",metrics.accuracy_score(y_test, tree_predict)*100 , "%")
    print("MSE [TEST]          :",mean_squared_error(y_test, tree_predict))


    tree_predict1 = trained_model.predict(x_train)
    print("Training accuracy  :",metrics.accuracy_score(y_train, tree_predict1)*100 ,"%")
    print("MSE [TRAIN]         :",mean_squared_error(y_train, tree_predict1))

    print("precision : ",precision_score(y_test, tree_predict,average='micro'))
    print("recall    : ",recall_score(y_test, tree_predict,average='micro'))
    print("f1_score  : ",f1_score(y_test, tree_predict,average='micro'))


    cf1 = confusion_matrix(y_test,tree_predict)
    sb.heatmap(cf1,annot=True,fmt = '.0f')
    plt.xlabel('prediction')
    plt.ylabel('Actual')
    plt.title(name+ ' Confusion Matrix')
    plt.show()

    print(classification_report(y_train,  trained_model.predict(x_train)))
    print(classification_report(y_test,  trained_model.predict(x_test)))
    
        
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
