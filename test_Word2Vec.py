from gensim.models import Word2Vec

model = Word2Vec.load('Word2Vec_1.model') #load model

#print(model.wv.vocab.keys())
print(model.wv.similar_by_word("เอเลี่ยน"))