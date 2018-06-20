import json
import os
import re
from pyfasttext import FastText
import logging
import glob, os
#need to move this to a worker instance, for now we simulate

logger = logging.getLogger(__name__)

UNSUPDATADIR = "/data/datafiles/unsupervised/"
SUPDATADIR = "/data/datafiles/supervised/"
MODELDIR =  "/data/models/"


class fastTextApp(object):
    configs= []
    loadedmodels = []
    datafiles = []

    def findDataFiles(self):
        for f in glob.glob(f"{SUPDATADIR}*"):
            d = datafile(f,f.split('/')[-1], supervised=True)
            self.datafiles.append(d)
        for f in glob.glob(f"{UNSUPDATADIR}*"):
            d = datafile(f, f.split('/')[-1], supervised=True)
            self.datafiles.append(d)

    def loadConfig(self,config):    
        c = config(config)
        c.load()
        self.configs.append(c)

    def loadConfigs(self,configs):
        
        for conf in configs:
            self.loadConfig(conf)

    def loadModel(self,name, version, supervised, quantized):
        
        m = model(name,version,supervised,quantized)
        result = m.load()
        if result == "success":
            self.loadedmodels.append(m)

        return result
        
        
    #loadallmodels ???
            


class datafile(object):
    name=""
    supervised=False
    filename=""
    
    def __init__(self, filename, name, supervised):
        self.name= name
        self.supervised = supervised
        self.filename = self.filename
    
        
        

class config(object):
    bias = 0
    ngrams = 3
    learningRate = .2
    epoch = 200
    method = ""  #(skipgram of cbow fur unsupervised)
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if type(value) != type(getattr(self, key)):
                logger.error(f'error in type for key :{key} with type {type(getattr(self, key) )}')
            else:                    
                setattr(self, key, value)
        



class model(object):
    name =""
    version = 0
    supervised = True
    ft = None
    loaded = False
    quantized = False
    config = None
    filepath =""

    def __init__(self, name, version, supervised, quantized):
        self.name = name
        self.version = version
        self.supervised = supervised
        self.quantized = quantized
        
        if quantized==True:
            self.filepath = f"{MODELDIR}{self.name}/{self.version!s}/model.ftz"
        else:
            self.filepath = f"{MODELDIR}{self.name}/{self.version!s}/model.bin"
    def quantize(self):
            logger.error("TODO")
    def load(self):
        try:
            self.ft = FastText(self.filepath)
        except:
            return "Failed to Load FT file"
        logger.info(f"loaded file {self.filepath}")
        self.loaded = True
        return "success"


    def train(self, trainingfile):
        
    
        """Starts model building"""
        
        logger.info(f'Training started with : learningRate:{self.config.learningRate!s}, epoch:{self.config.epoch!s}, ngrams :{self.config.ngrams!s}')
        model = FastText()
        if self.supervised:
            model.supervised(input=trainingfile, output=self.filepath, epoch=self.config.epochs, lr=self.config.learningRate, wordNgrams=self.config.ngrams, verbose=2, minCount=1)
        elif self.config.method == "cbow":
            model.cbow(input=trainingfile, output='model', epoch=self.config.epoch, lr=self.config.learningRate)
        else:
            model.skipgram(input=trainingfile, output='model', epoch=self.config.epoch, lr=self.config.learningRate)
        
        

    def predict(self, text, nbpredictions=1):
        if self.loaded==False:
            return ['error',"please load model first"]
        
        logger.info(f"making prediction for {text}")
        predictions = self.ft.predict_proba_single(text, k=nbpredictions)
        logger.info(predictions)
        results = []
        for prediction in predictions:
            if len(prediction) ==2:
                
                result = { "category" : prediction[0], "confidence" : prediction[1] }
                results.append(result)
                logger.info(f"{prediction[0]} {prediction[1]!s}")
        
        return results

                
        
        




