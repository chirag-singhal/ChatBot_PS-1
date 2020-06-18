"""
input: string of question
We have a corpus with various sentences. Then, for a given query sentence,
we want to find the most similar sentence in this corpus.
The object has to be instantiated only once when the server is starting
The respond function then outputs for various queries the most similar sentence in the corpus.
The getData function retreives all training questions from the database
"""
from sentence_transformers import SentenceTransformer
import scipy.spatial
import string

class nlp_module:

    def __init__(self):
        # Find the closest sentence of the corpus for each query sentence based on cosine similarity
        self.closest_n = 5 #No. of closest sentences from the corpus desired
        self.remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)  #Removes the punctuation
        self.embedder = SentenceTransformer('bert-base-nli-mean-tokens')

        # Corpus with training sentences

        self.questions = self.getData()  #change this for input
        self.corpus = self.questions.lower().translate(self.remove_punct_dict).splitlines() #Removes punctuation from the corpus
        self.questions=self.questions.splitlines() #Splits the corpus into different lines
        self.corpus_embeddings = self.embedder.encode(self.corpus) #Generates feature vectors for the corpus

    #import data
    #Change to integrate with database
    def getData(self) : #function to get the predefined data
        f = open("./myqs.txt", "r")
        data = f.read()
        return data

    def respond(self,query):
        query.lower().translate(self.remove_punct_dict) #removes punctuations from the input
        query_embedding=self.embedder.encode([query])[0] #generates a feature vector for the inputted question
        distances = scipy.spatial.distance.cdist([query_embedding], self.corpus_embeddings, "cosine")[0] #Calculates the cosine similarity between the vectors
        results = zip(range(len(distances)), distances)
        results = sorted(results, key=lambda x: x[1]) #sorts the distances

        #print("\n\n======================\n\n")
        #print("Query:", query)
        #print("\nTop 5 most similar sentences in corpus:")

        #for idx, distance in results[0:self.closest_n]:
            #print(self.corpus[idx].strip(), "(Score: %.4f)" % (1-distance))
        return self.questions[results[0][0]];
