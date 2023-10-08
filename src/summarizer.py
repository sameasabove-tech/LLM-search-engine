# look up models that summarize documents, have a summmarizer class

# import os
import numpy as np 
# from sentence_transformers import SentenceTransformer
from uuid import uuid1
from dataclasses import dataclass


@dataclass
class Summarizer:
    """
    _summary_
    
    """
    # document: list[str] 
    # id = uuid1() 
    # model_name: str 
    # text_embedding = None

    # def encode_document(self): 
    #     model = SentenceTransformer(self.model_name)
    #     text_embedding = model.encode(self.document)
    #     # return self.text_embedding