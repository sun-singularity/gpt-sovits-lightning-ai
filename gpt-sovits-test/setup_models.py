import os
import zipfile
import nltk

# Define paths
nltk_data_url = "https://github.com/RVC-Boss/GPT-SoVITS/files/14717070/nltk_data.zip"
nltk_data_zip = "/teamspace/studios/this_studio/nltk_data.zip"
nltk_data_dir = "/teamspace/studios/this_studio/nltk_data"

# Function to download the NLTK data zip file
def download_nltk_data():
    os.system(f"wget {nltk_data_url} -O {nltk_data_zip}")

# Function to extract the NLTK data zip file
def extract_nltk_data():
    with zipfile.ZipFile(nltk_data_zip, 'r') as zip_ref:
        zip_ref.extractall(nltk_data_dir)

# Function to set the NLTK data path
def set_nltk_data_path():
    nltk.data.path.append(nltk_data_dir)

def install_nltk_data():
    download_nltk_data()
    extract_nltk_data()
    set_nltk_data_path()

if __name__ == "__main__":
    install_nltk_data()
    print("NLTK data path set to:", nltk.data.path)
