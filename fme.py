import openai
import json

# Set OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

def categorize_layer(layer_name):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"What category does the following layer name belong to in a detailed plan: {layer_name}?",
        max_tokens=50
    )
    category = response.choices[0].text.strip()
    return category

def getValue(features, attr):
    # Extract attribute value from the first feature
    return features[0].getAttribute(attr)

def pyfunc(feature, context):
    layer_name = feature.getAttribute('layer_name')
    
    # Categorize the layer
    category = categorize_layer(layer_name)
    
    # Set the category back to the feature
    feature.setAttribute('category', category)
    
    return feature
