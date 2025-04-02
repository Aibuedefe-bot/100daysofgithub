import opendatasets as od
import os

kaggle_link = input('Kaggle Dataset: ')

# Ask the user where to download the dataset
download_dir = input("Enter the directory to save the dataset (leave blank for current directory): ")

# Set default directory if none is provided
if not download_dir:
    download_dir = os.getcwd()  # Use current directory

# Ensure the directory exists
os.makedirs(download_dir, exist_ok=True)

# Download the dataset to the specified directory
od.download(kaggle_link, data_dir=download_dir)

print(f"Dataset downloaded to: {download_dir}")

os.listdir()
