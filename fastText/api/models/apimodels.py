
from flask_restplus import fields
from fastText.api.restplus import api


predict = api.model( 'predict:', {
    'name' : fields.String(description='name of the model'),
    'version': fields.Integer(description='model version optional : 0 by default'),
    'text': fields.String(description='text to feed the prediction algorithm'),
    'nbofresults': fields.Integer(description='Number of labels to return'),
})

loadmodel = api.model('loadmodel:', {
    'name': fields.String(description='name of the model'),
    'version': fields.Integer(description="model version optional : 0 by default'"),
    'supervised': fields.Boolean(),
    'quantized': fields.Boolean(),

}
    )

model = api.model('model:', {
    'model': fields.String(description='name of the model to laod'),
    
})



training = api.model('training:', {
    'config': fields.String(description='name of the configuration model'),
    
})
