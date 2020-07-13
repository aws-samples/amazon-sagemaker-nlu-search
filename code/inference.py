import argparse
import logging
import sagemaker_containers
import requests

import os
import json
import io
import time
import torch
from sentence_transformers import models, losses, SentenceTransformer

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# set the constants for the content types
CONTENT_TYPE = 'text/plain'

def model_fn(model_dir):
    logger.info('model_fn')
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logger.info(model_dir)
    model = SentenceTransformer(model_dir + '/transformer/')
    logger.info(model)
    return model.to(device)

# Deserialize the Invoke request body into an object we can perform prediction on
def input_fn(serialized_input_data, content_type=CONTENT_TYPE):
    logger.info('Deserializing the input data.')
    if content_type == CONTENT_TYPE:
        data = [serialized_input_data.decode('utf-8')]
        return data
    raise Exception('Requested unsupported ContentType in content_type: {}'.format(content_type))

# Perform prediction on the deserialized object, with the loaded model
def predict_fn(input_object, model):
    logger.info("Calling model")
    start_time = time.time()
    sentence_embeddings = model.encode(input_object)
    print("--- Inference time: %s seconds ---" % (time.time() - start_time))
    response = sentence_embeddings[0].tolist()
    return response

# Serialize the prediction result into the desired response content type
def output_fn(prediction, accept):
    logger.info('Serializing the generated output.')
    if accept == 'application/json':
        output = json.dumps(prediction)
        return output
    raise Exception('Requested unsupported ContentType in Accept: {}'.format(content_type))
