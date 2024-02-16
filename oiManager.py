from openai import OpenAI
import os


class OiManager:
    def __init__(self):

        self.openai = OpenAI(api_key=self.getKey())
        self.document = self.getDocument()

    def getKey(self):

        # with open('secret.txt', 'r') as file:
        #     secret = file.read().replace('\n', '')
        # return secret

        return os.environ['OPENAI_API_KEY']

    
    def getDocument(self):
        #read the document as a text from data.txt

        with open("data.txt","r") as doc:
            document = doc.read()

        return document

    def createHistory(self):
        history = [
            {"role":"system","content":"you are to answer questions related the document provided by user. Use turkish language"},
            {"role":"user","content":self.document}


        ]
        return history
    
    def runModel(self,userInput):
        history  = self.createHistory()
        history.append({"role":"user","content":userInput})

        modelResponse = self.openai.chat.completions.create(
            messages=history,
            model="gpt-4-turbo-preview",
            max_tokens=500
        )
        
        return modelResponse.choices[0].message.content
