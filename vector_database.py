import chromadb

client = chromadb.Client()

collection = client.create_collection(name="policy")

sentences = [
    "What is Artificial Intelligence?",
    "How do you cook spaghetti pasta?",
    "Basics of machine learning and data science",
    "Python is a versatile programming language",
    "Deep learning is a subfield of machine learning",
    "Best practices for cooking Italian food",
    "Guide to AI tools and frameworks",
    "Natural language processing with Transformers",
    "Introduction to neural networks",
    "Steps to make pasta carbonara"
]

for i in range(len(sentences)):
    collection.upsert(
        documents=[sentences[i]],
        ids=[str(i)]
    )

results = collection.query(
    query_texts=["how does NLP work"],
    n_results=2
)

print(results)