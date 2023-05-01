from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification
import torch
import json

class HugginfacePipeline:

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("nickprock/bert-italian-finetuned-ner")
        self.model = AutoModelForTokenClassification.from_pretrained("nickprock/bert-italian-finetuned-ner")
        self.nlp = pipeline("ner",  model=self.model, tokenizer=self.tokenizer)

    def analyze(self, text):
        return json.dumps(str(self.nlp(text)))