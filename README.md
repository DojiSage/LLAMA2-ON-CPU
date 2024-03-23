# LLAMA2-ON-CPU
Steps 1:
clone the repository

Steps 2:
Create a virtual environment

conda create -n cpullama python=3.8 -y

conda activate cpullama

Step 3:
Run template.py to create folder structure and files

pip install -r requirements.txt

Download the quantize model from the link provided in model folder & keep the model in the model directory:
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
