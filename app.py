from flask import Flask, request
from flask_restx import Api, Resource, fields
from spam_detector.predict import predict_spam

app = Flask(__name__)
api = Api(app, version='1.0', title='Spam Detector API',
          description='An API to detect whether a message is spam or not')

ns = api.namespace('spam', description='Spam detection operations')

# Define the expected input schema for Swagger docs
spam_model = api.model('Message', {
    'message': fields.String(required=True, description='The message to analyze')
})

@ns.route('/detect-spam')
class SpamDetector(Resource):
    @ns.expect(spam_model)
    def post(self):
        '''Detect if a message is spam'''
        data = request.get_json()
        message = data.get("message", "")
        prediction = predict_spam(message)
        return {"spam": prediction}

if __name__ == '__main__':
    app.run(debug=True)
