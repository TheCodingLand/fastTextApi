This is a very simple python api implementation for fastText https://github.com/facebookresearch/fastText.git

It will grow in features and will get a frontend for loading models, predicting, training and testing

Instructions for now : 

- chose a place to store the volume (replace /my/data/folder/ below)
- chose a model name for your model
- you can have several versions (integer value only for now)
- quantized or not
- only supervised for now

Put your models into /my/data/folder/models/<modelname>/<modelversion>/model.ftz or model.bin

then do : 
  git clone https://github.com/TheCodingLand/fastTextApi
  cd fastTextApi
  docker build .
  docker run -p 5000:5000 -v /my/data/folder:/data <containerid>


open a browser and go to <dockerhost>:5000

First, load your model, you can try the default one with language classification that I configured for testing :
"{
  "name": "language",
  "version": 0,
  "supervised": true,
  "quantized": true
}"


then use the predict post method :


{
  "name": "language",
  "version": 0,
  "text": "my tailor is rich",
  "nbofresults": 2
}



This is the minimal working version. please give me some time before opening issues as I'm working on this actively. cheers.
