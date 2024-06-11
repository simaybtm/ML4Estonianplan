import _1_create_synthetic_data
import _2_synthetic_model

def main():
    # Create synthetic data
    synthetic_data = _1_create_synthetic_data.main()
    
    # Train the model
    model = _2_synthetic_model.main()
    
    print("     ")
    print("All done! Use the output.csv created to get the Estonian discipline name predictions.")

if __name__ == '__main__':
    main()
    