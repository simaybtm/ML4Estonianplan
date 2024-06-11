import _1_create_synthetic_data
import _2_synthetic_model
import _3_test_model

def main():
    # Create synthetic data
    synthetic_data = _1_create_synthetic_data.main()
    
    # Train the model
    model = _2_synthetic_model.main(synthetic_data)
    
    # Test the model
    _3_test_model.main(model)
    
    print("     ")
    print("All done!")

if __name__ == '__main__':
    main()
    