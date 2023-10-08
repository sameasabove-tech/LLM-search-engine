# look up models that do encoding to a document to vector, src level, encoder.py, have an enocder class 

# import os
import numpy as np 
from sentence_transformers import SentenceTransformer
from uuid import uuid1
from dataclasses import dataclass


@dataclass
class TextEmbedding:
    """
    _summary_
    
    """
    document: list[str] 
    id = uuid1() 
    model_name: str 
    text_embedding = None


    def encode_document(self): 
        model = SentenceTransformer(self.model_name)
        self.text_embedding = model.encode(self.document)
        # return self.text_embedding