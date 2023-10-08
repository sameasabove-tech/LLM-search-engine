# look up models that summarize documents, have a summmarizer class

# import os
# import numpy as np 
from transformers import pipeline
from uuid import uuid1
from dataclasses import dataclass

@dataclass
class Summary:
    """Data class that will hold a document and a summary of the document.

    Attributes:
        document (list[str]): List of text data inputted into the class. 
        id (str): Variable unique string of characters initialized when the class is called.
        model_name (str): LLM of our choice used create the summary. 
        summary_list (None): List of summaries place holder.
    """
    document: str
    id = uuid1() 
    model_name: str 
    summary_list = None


    def summarize_document(self):
        """_summary_
        """
        summarizer_pipeline = pipeline(
          task = "summarization",
          model= self.model_name,
        )
        summary_pipeline_outputs = summarizer_pipeline(self.document, truncation=True, batch_size=1)
        self.summary_list = [summary['summary_text'] for summary in summary_pipeline_outputs]