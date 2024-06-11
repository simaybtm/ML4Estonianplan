import joblib
import pandas as pd

def main(model):
    # Load the trained model using synthetic data
    model = joblib.load('synthetic_model.pkl')
    
    # Load the FME output CSV
    fme_data = pd.read_csv('input.csv')
    
    # Combine 'discipline' and 'element_type' into a single feature
    fme_data['combined'] = fme_data['discipline'] + ' ' + fme_data['element_type'].fillna('')
    
    # Extract the combined data
    new_data = fme_data['combined']
    
    # Make predictions using the model trained on synthetic data
    predictions = model.predict(new_data)
    
    # Print predictions with numbers
    print ("     ")
    print('Input:                Predicted Category:')
    for i, (item, prediction) in enumerate(zip(new_data, predictions)):
        print(f'{str(i+1).ljust(5)}. {item.ljust(20)} -> {prediction}')

    
    print("Test finished.")
    
if __name__ == '__main__':
    model = joblib.load('synthetic_model.pkl')
    main(model)