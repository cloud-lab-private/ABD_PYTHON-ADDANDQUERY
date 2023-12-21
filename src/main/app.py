import chromadb

from main.lab import sample
from main.lab import add_file
from main.lab import get_relevant_file
from main.lab import chroma_client
from main.lab import collection

"""
This file will contain some sample code to send the output of the functions in lab.py to the 
console. You may modify this file in any way, it will not affect the test results.
"""
def main():

    print("First, let's see the result of the sample function provided. On the query \n"
          "string 'how is singles different from doubles', ChromaDB should \n"
          "locate the 'tennis' document: ")
    sample_result = sample()
    print(sample_result.get('ids'))
    print("Next, let's verify that your add_file function is capable of adding files. \n"
          "We will add the checkers, football, hockey, basketball, and checkers files \n"
          "and then output all documents in the 'games' collection.")
    #add files
    add_file("../resources/checkers.md", {"type": "board game"}, "checkers")
    add_file("../resources/hockey.md", {"type": "sport"}, "hockey")
    #grab the chroma client and use it to display collection info
    chroma_client = chromadb.Client()
    games_collection = chroma_client.get_collection(name="games")
    print(games_collection.get().get("ids"))
    print("Next, you may input your query string, and ChromaDB should produce the most relevant document. However, note \n"
          "that a similarity search without any semantic understanding can be naive, and may lead to an incorrect result.")
    user_input = input("input your query about baseball, checkers, chess, hockey, tennis here: ")
    query_result = get_relevant_file(user_input)
    print(query_result.get("ids"))

if __name__ == '__main__':
    main()
