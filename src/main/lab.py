import os

import chromadb

"""
An LLM in a RAG application is intended to acquire some persona
that is built on top of the existing baseline LLM. This means that the LLM will need
to be aware of human-written documents that define important information about your
organization, such as
    - standard operating procedures
    - technical reference documents
    - legal documents
    - marketing materialAn
An LLM needs to be granted the ability to retrieve these documents
when they are relevant to the AI's actions. We may determine the relevancy of documents
using a 'vector search', which may mathematically comparing the pre-generated
'embeddings' of a document against the tokens contained in a prompt.

ChromaDB will be used here as our vector database. Your curricula may reference a
different Vector offering, but Chroma is lightweight and may be used locally.
Below, the Chroma collection for this lab is established. A Collection can be thought of
as a grouping of related documents, and can be treated similarly to a database table.
"""

chroma_client = chromadb.Client()
# prior to running the app, completely reset the collection to prevent conflicts
# with duplicate documents
try:
    chroma_client.delete_collection("games")
except ValueError:
    """games collection doesn't exist, create the collection next"""
finally:
    collection = chroma_client.create_collection(name="games")

"""
Below is a function that adds some documents contained in the resources folder
to a locally-stored vector database, ChromaDB. ChromaDB will automatically generate
the embeddings needed for a document. It will then query the database for the
most relevant document to the query "How is singles different from doubles?", which
should be identified as being related to the Tennis document.
"""


def sample():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    with open("../resources/baseball.md") as baseball_file:
        baseball = baseball_file.read()
    with open("../resources/chess.md") as chess_file:
        chess = chess_file.read()
    with open("../resources/tennis.md") as tennis_file:
        tennis = tennis_file.read()
    collection.add(
        documents=[baseball, chess, tennis],
        metadatas=[{"type": "sport"}, {"type": "board game"}, {"type": "sport"}],
        ids=["baseball", "chess", "tennis"]
    )
    most_relevant_file = collection.query(
        query_texts=["How is singles different from doubles?"],
        n_results=1
    )
    return most_relevant_file


"""
TODO: write a function to add a single file to ChromaDB. The relative path of the file
is provided as a parameter to the function. It doesn't need to return anything.
The full path, starting from the root directory of the workspace, will be provided, eg
relative_path may be "../resources/tennis.md". Metadata will be a dict containing all
required for adding the file and may be used as-is, eg metadatas=[metadata]. 
The id may be used as-is, eg ids = [id].
"""


def add_file(relative_path, metadata, id):
    return "todo"


"""
TODO: write a function to query ChromaDB for the most relevant document for a given
string. The String is provided as a parameter to the function. It should
return the document.
"""


def get_relevant_file(query_string):
    return "todo"
