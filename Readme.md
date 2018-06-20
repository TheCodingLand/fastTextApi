This is a very simple python api implementation for fastText https://github.com/facebookresearch/fastText.git

It will grow in features and will get a frontend for loading models, predicting, training and testing

Instructions for now : 

  git clone https://github.com/TheCodingLand/fastTextApi
  cd fastTextApi
  docker build . -t fasttext
  docker run -p 5000:5000 -v fasttext:/data fasttext


open a browser and go to <dockerhost>:5000

I included an example model, named language, with verson 0, supervised, quantized :

load the model :
"{
  "name": "language",
  "version": 0,
  "supervised": true,
  "quantized": true
}"

try the predict post method :

{
  "name": "language",
  "version": 0,
  "text": "my tailor is rich",
  "nbofresults": 2
}

returns :
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


This is the minimal working version. please give me some time before opening issues as I'm working on this actively. cheers.

you can add your models, i'll provide better ways for this later, but for now:

then you can put model files into 

/var/lib/docker/volumes/fasttext/_data/models/<modelname>/<modelversion>/model.ftz or model.bin

and query them like :
{
  "name": "modelname",
  "version": version,
  "text": "my text to test",
  "nbofresults": x number of results I want
}
