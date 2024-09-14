import os

# Clone the GPT-SoVITS repository
def clone_repository():
    os.system("git clone https://github.com/sun-singularity/GPT-SoVITS")

# Install necessary packages using conda
def install_conda_packages():
    os.system("conda install -y -q -c pytorch -c nvidia cudatoolkit")
    os.system("conda install -y -q -c conda-forge gcc gxx ffmpeg cmake -c pytorch -c nvidia")

# Install Python dependencies
def install_python_dependencies():
    os.chdir("/teamspace/studios/this_studio/gpt-sovits-test/GPT-SoVITS")
    os.system("pip install -r requirements.txt")

if __name__ == "__main__":
    clone_repository()
    install_conda_packages()
    install_python_dependencies()
