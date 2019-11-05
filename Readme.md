# This is a very simple python api implementation for fastText https://github.com/facebookresearch/fastText.git

It is intended as an small proof of concept of a flask API exposing trained models through a prediction api.



## Instructions :

  git clone https://github.com/TheCodingLand/fastTextApi

  cd fastTextApi

  docker build . -t fasttext

  docker run -p 5000:5000 -v fasttext:/data fasttext


open a browser and go to yourdockerhost:5000

I included an example model, named language, with version 0, supervised, quantized :

load the model :
```json
{
  "name": "language",
  "version": 0,
  "supervised": true,
  "quantized": true
}
```

try the predict post method :
```json
{
  "name": "language",
  "version": 0,
  "text": "my tailor is rich",
  "nbofresults": 2
}
```
returns :
```json
{
  "status": "success",
  "results": [
    {
      "category": "en",
      "confidence": 0.9863510129824254
    },
    {
      "category": "fr",
      "confidence": 0.005755515951242966
    }
  ]
}
```

you can add your models files into 

/var/lib/docker/volumes/fasttext/_data/models/{modelname}/{modelversion}/model.ftz or model.bin

and query them like :
```json
{
  "name": "modelname",
  "version": version,
  "text": "my text to test",
  "nbofresults": x number of results I want
}
```

This is the minimal working version. 
