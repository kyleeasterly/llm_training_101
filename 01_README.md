Large Language Model Training 101
=================================
Welcome to Large Language Model Training 101! This repository teaches you everything you need to know to train a model yourself.


# Theory

## Neural Networks
- Neurons
- Weights & biases
- Forward pass
  - Input is encoded
  - Neurons activate, or don't
  - Decode output
- Training
  - Suppose you ask the model a question and you don't like the answer. How would you change the weights of the network so that it answers how you'd like?
  - You could measure the difference between the answer the model gives naturally and the answer you'd like...
  - Then sort out how much you need to tweak all of the weights to get closer to the desired answer.
  - That's backpropagation and training in a nutshell.

# Setting up your Python virtual environment
We should always use a virtual environment (venv) when working with Python. This keeps dependencies managed on a per-project basis instead of installing dependencies directly onto our machine. With AI libraries in particular, you can run into conflicting requirements if you install everything to your machine side-by-side.

To create your virtual environment: `python -m venv llm101`
Activate your virtual environment on Windows: `.\llm101\Scripts\activate.bat`
Activate your virtual environment on Linux: `/llm101/activate`

# 02_requirements.txt
This is a Python requirements.txt file, which is used to specify a list of modules for pip to install. Our requirements.txt file contains the following modules:

`accelerate`

`bitsandbytes` allows us to load models with 4-bit quantization. This is where the 16-bit values of the model's weights are quantized down to 4 bits, trading some precision for a lower memory footprint. This has a mild performance degradation on the model but is usually worth the tradeoff if it means you can load a model with more parameters.

`datasets` is required to train using a json file.

`huggingface_hub`

`peft` allows us to perform *parameter-efficient fine-tuning* or PEFT. This technique is also known as *low-rank adaptation* or LoRA. These techniques are when you only change a subset of a model's parameters during training, instead of changing the weights of the entire model. This results in a small "adapter" model file that may be attached to a base model in a modular fashion.

`scipy`

`sentencepiece`

`transformers` is a library from HuggingFace that allows you to run inference with transformers-based language models.

`wandb` allows us to login to Weights & Biases from the command line, which will then allow us to send telemetry to W&B during training. Visualizing what's happening during training is an important tool, particularly when you are first learning how to train and if you are troubleshooting any issues.

Make sure you are in your virtual environment - you should see (llm101) before your command line input. Then run `pip install `

# 03_inference.py
Inference is the act of using the model to generate a response for a given prompt. If training is a compiler, inference is runtime. Let's start by using the `03_inference.py` script to prompt the base OpenLlama model.

In your venv console: `python 03_inference.py`

# 04_train.py


# 05_data.json
This is the data that you are using to fine-tune the OpenLlama model.