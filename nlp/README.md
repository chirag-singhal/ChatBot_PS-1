# nlp_chatbot

To install dependencies, execute the following command
```
pip install -r requirements.txt
```

Now you need to use the nlp module once to get the 400Mb BERT model downloaded

Open python interactive console and execute following lines in that interactive session:
```
from nlp_module import nlp_module
nlp = nlp_module()
```

Now you can start the django server. There's no further need of configuring/setting-up NLP engine.
