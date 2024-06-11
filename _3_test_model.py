import joblib
import pandas as pd

def main(model):
    # Load the trained model using synthetic data
    model = joblib.load('synthetic_model.pkl')
    
    # Load the FME output CSV and split it into three attributes
    fme_data = pd.read_csv('input.csv', delimiter=',', names=['discipline', 'ifc_unique_id', 'element_type'])
    
    # Combine 'discipline' and 'element_type' into a single feature
    fme_data['combined'] = fme_data['discipline'] + ' ' + fme_data['element_type'].fillna('')
    
    # Extract the combined data
    new_data = fme_data['combined']
    
    # Make predictions using the model trained on synthetic data
    predictions = model.predict(new_data)
    
    # Print predictions with numbers
    print("\nInput:                Predicted Category:")
    for i, (item, prediction) in enumerate(zip(new_data, predictions), start=1):
        # Skip the first row (header)
        if i == 1:
            continue
        print(f'{str(i-1).ljust(5)}. {item.ljust(20)} -> {prediction}')

    print("\nTest finished.")
    
    # Save the predictions to a CSV
    fme_data['predicted_discipline'] = predictions
    # Add the 'ifc_unique_id' column from the input.csv
    fme_data['ifc_unique_id'] = fme_data['ifc_unique_id']

    # Add second column ifc_unique_id to the output.csv
    fme_data = fme_data[['ifc_unique_id', 'predicted_discipline']]  

    fme_data.to_csv('output.csv', index=False)
    print("Predictions saved to output.csv.")
    

if __name__ == '__main__':
    model = joblib.load('synthetic_model.pkl')
    main(model)
