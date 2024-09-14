import os
import subprocess
import nltk

# Define the base paths
base_path = "/teamspace/studios/this_studio/gpt-sovits-test/GPT-SoVITS"

def install_dependencies():
    # Install ipykernel and nltk
    os.system("pip install ipykernel nltk")

def download_nltk_resources():
    # Download the required NLTK resources
    nltk_data_path = "/teamspace/studios/this_studio/nltk_data"
    nltk.download('averaged_perceptron_tagger', download_dir=nltk_data_path)
    nltk.download('cmudict', download_dir=nltk_data_path)

def modify_config_file():
    # Modify config.py to replace the 10th line from 'False' to 'True'
    config_file_path = os.path.join(base_path, "config.py")
    with open(config_file_path, 'r') as file:
        lines = file.readlines()

    # Assuming the change is on the 10th line
    if len(lines) >= 10:
        lines[9] = lines[9].replace('False', 'True')

    with open(config_file_path, 'w') as file:
        file.writelines(lines)

def launch_webui():
    # Change directory to the GPT-SoVITS base path
    os.chdir(base_path)

    # Launch the WebUI by running the webui.py script
    subprocess.run(["python", "webui.py"])

if __name__ == "__main__":
    install_dependencies()
    download_nltk_resources()
    modify_config_file()
    launch_webui()
