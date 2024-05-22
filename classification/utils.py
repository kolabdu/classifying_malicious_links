import pickle
import dill
from sklearn.feature_extraction.text import TfidfVectorizer
#from . import vectorizer_rename as vector

def clean_url(url):
    prefixes = ['http://www.', 'https://www.', 'www.']
    for prefix in prefixes:
        if url.startswith(prefix):
            url = url.replace(prefix, '')
            break
    return url

import dill
from sklearn.feature_extraction.text import TfidfVectorizer

# Define the makeTokens function
def makeTokens(f):
    tkns_BySlash = str(f.encode('utf-8')).split('/')    # make tokens after splitting by slash
    total_Tokens = []
    for i in tkns_BySlash:
        tokens = str(i).split('-')    # make tokens after splitting by dash
        tkns_ByDot = []
        for j in range(0, len(tokens)):
            temp_Tokens = str(tokens[j]).split('.')    # make tokens after splitting by dot
            tkns_ByDot = tkns_ByDot + temp_Tokens
        total_Tokens = total_Tokens + tokens + tkns_ByDot
    total_Tokens = list(set(total_Tokens))    # remove redundant tokens
    if 'com' in total_Tokens:
        total_Tokens.remove('com')    # removing .com since it occurs a lot of times and it should not be included in our features
    return total_Tokens

# Initialize TfidfVectorizer with custom tokenizer
#vectorizer = TfidfVectorizer(tokenizer=makeTokens)




def load_model_and_vectorizer():
    with open('logit_model.pkl', 'rb') as file:
        model = pickle.load(file)
    with open('vectorizer_dill.pkl', 'rb') as file:
        vectorizer = dill.load(file)
    return model, vectorizer

def predict_url_category(url, model,vectorizer):
       
    prediction = model.predict(vectorizer.transform(url))
    if prediction == 'good':
        return 'The URL is safe'
    else:
        return "URL APPEARS TO BE MALICIOUS"


# import pickle
# from sklearn.feature_extraction.text import TfidfVectorizer

# print("utils.py is being imported!")

# def clean_url(url):
#     prefixes = ['http://www.', 'https://www.', 'www.']
#     for prefix in prefixes:
#         if url.startswith(prefix):
#             url = url.replace(prefix, '')
#             break
#     return url

# def makeTokens(url):
#     tkns_BySlash = str(url.encode('utf-8')).split('/')  # make tokens after splitting by slash
#     total_Tokens = []
#     for i in tkns_BySlash:
#         tokens = str(i).split('-')  # make tokens after splitting by dash
#         tkns_ByDot = []
#         for j in range(0, len(tokens)):
#             temp_Tokens = str(tokens[j]).split('.')  # make tokens after splitting by dot
#             tkns_ByDot = tkns_ByDot + temp_Tokens
#         total_Tokens = total_Tokens + tokens + tkns_ByDot
#     total_Tokens = list(set(total_Tokens))  # remove redundant tokens
#     if 'com' in total_Tokens:
#         total_Tokens.remove('com')  # removing .com since it occurs a lot of times and it should not be included in our features
#     return total_Tokens

# def load_model_and_vectorizer():
#     with open('logit_model.pkl', 'rb') as file:
#         model = pickle.load(file)
#     with open('vectorizer.pkl', 'rb') as file:
#         vectorizer = pickle.load(file)
#     return model, vectorizer

# def predict_url_category(url, model, vectorizer):
#     cleaned_input = clean_url(url)  # Clean the URL directly
#     makeTokens(cleaned_input)  # Tokenize the cleaned URL
#     new_x = vectorizer.transform([cleaned_input])
#     prediction = model.predict(new_x)
#     return prediction[0]#, total_tokens  # Return both prediction and total_tokens



# import pickle

# def makeTokens(f):
#   """
#   This function tokenizes a URL by splitting it by slashes (/), dashes (-), and dots (.).

#   Args:
#       f (str): The URL to tokenize.

#   Returns:
#       list: A list of unique tokens extracted from the URL.
#   """
#   tkns_BySlash = str(f.encode('utf-8')).split('/')  # Split by slash
#   total_Tokens = []
#   for i in tkns_BySlash:
#     tokens = str(i).split('-')  # Split by dash
#     tkns_ByDot = []
#     for j in range(0, len(tokens)):
#       temp_Tokens = str(tokens[j]).split('.')  # Split by dot
#       tkns_ByDot = tkns_ByDot + temp_Tokens
#     total_Tokens = total_Tokens + tokens + tkns_ByDot
#   total_Tokens = list(set(total_Tokens))  # Remove redundant tokens
#   if 'com' in total_Tokens:
#     total_Tokens.remove('com')  # Remove ".com" as it's common
#   return total_Tokens

# def clean_url(url):
#   """
#   This function removes common prefixes from a URL.

#   Args:
#       url (str): The URL to clean.

#   Returns:
#       str: The cleaned URL without prefixes.
#   """
#   prefixes = ['http://www.', 'https://www.', 'www.']
#   for prefix in prefixes:
#     if url.startswith(prefix):
#       url = url.replace(prefix, '')
#       break
#   return url

# def load_model_and_vectorizer():
#   """
#   This function loads the pre-trained model and vectorizer from pickle files.

#   **Note:** Adjust the file paths based on your project structure.

#   Returns:
#       tuple: A tuple containing the loaded model and vectorizer.
#   """
#   with open('Machine-Learning-In-Julia-JCharisTech-master/logit_model.pkl', 'rb') as file:
#     model = pickle.load(file)
#   with open('Machine-Learning-In-Julia-JCharisTech-master/vectorizer.pkl', 'rb') as file:
#     vectorizer = pickle.load(file)
#   return model, vectorizer

# def predict_url_category(url, model, vectorizer):
#   """
#   This function predicts the category of a URL using the loaded model and vectorizer.

#   Args:
#       url (str): The URL to predict the category for.
#       model (object): The pre-trained model for prediction.
#       vectorizer (object): The vectorizer used to transform the URL into a numerical representation.

#   Returns:
#       str: The predicted category of the URL.
#   """
#   new_x = vectorizer.transform([url])
#   prediction = model.predict(new_x)
#   return prediction[0]

