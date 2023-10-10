# look up models that do encoding to a document to vector, src level, encoder.py, have an enocder class 
# https://github.com/UKPLab/sentence-transformers
# import os
import numpy as np 
from sentence_transformers import SentenceTransformer
from uuid import uuid1
from dataclasses import dataclass


@dataclass
class TextEmbedding:
    """Data class that will hold a document and transform it into a text embedding.

    Attributes:
        document (list[str]): List of text data inputted into the class. 
        id (str): Variable unique string of characters initialized when the class is called.
        model_name (str): LLM of our choice used create the text embedding.
        text_embedding (None): Text embedding place holder.
    """
    document: list[str] 
    id = uuid1() 
    model_name: str 
    text_embedding = None


    def encode_document(self): 
        """Document data will be transformed to a text emedding and stored in the test_embedding variable of the dataclass.
        """
        model = SentenceTransformer(self.model_name)
        self.text_embedding = model.encode(self.document)
        # return self.text_embedding