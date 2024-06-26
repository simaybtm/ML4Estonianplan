import subprocess
import os

def run_fme_script():
    # Specify the full path to the FME executable
    fme_path = r'C:\Program Files\FME\fme.exe'
    fme_script_path = 'ml.fmw'
    
    if not os.path.exists(fme_script_path):
        print("FME script not found at:", fme_script_path)
        return
    
    # Run the FME script
    subprocess.run([fme_path, fme_script_path])

def run_synthetic_data_generation():
    run_all_script_path = 'run_all.py'
    
    if not os.path.exists(run_all_script_path):
        print("run_all.py script not found at:", run_all_script_path)
        return
    
    subprocess.run(['python', run_all_script_path])

def main():
    
    print ("- This script will run an FME script to generate input data, and then run a synthetic data generation script.")
    print ("- The FME  generated input data will be used against the trained model to predict the category of the Estonian layer.")
    print ("     ")
           
    # Run the FME script
    run_fme_script()
    print("--FME script run completed.")
    print ("     ")
    # Check if input.csv is created
    if not os.path.exists('input.csv'):
        print("Input.csv not found. Exiting...")
        return
    
    # Run the synthetic data generation script
    print("Running synthetic data generation script and then testing the input data against the trained model...")
    run_synthetic_data_generation()
    print("--Testing against the trained model completed.")
    print ("     ")
    print("All done!")

if __name__ == "__main__":
    main()
