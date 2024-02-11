import argparse
from peft import PeftModel
import torch
import torch.nn.functional as F
from transformers import LlamaTokenizer, LlamaForCausalLM

parser = argparse.ArgumentParser()
parser.add_argument('--model_path', type=str, default='openlm-research/open_llama_7b')
parser.add_argument('--load_in_4bit', type=bool, default=True)
parser.add_argument('--use_lora', type=bool, default=False)
parser.add_argument('--lora_path', type=str, default='./loras/open_llama_7b_demo')
args = parser.parse_args()

tokenizer = LlamaTokenizer.from_pretrained(args.model_path)
model = LlamaForCausalLM.from_pretrained(args.model_path, torch_dtype=torch.float16, device_map='auto', load_in_4bit=args.load_in_4bit)

if args.use_lora:
    print(f"Using LoRA {args.lora_path}.")
    model = PeftModel.from_pretrained(model, args.lora_path)

print("Ready.")

while True:
    prompt = input()
    inputs = tokenizer([prompt], return_tensors="pt")
    inputs = inputs.to('cuda')
    outputs = model.generate(**inputs, max_new_tokens=256, return_dict_in_generate=True, output_scores=True)

    for token_id in outputs.sequences[0][inputs.input_ids.shape[1]:]: # slice from end of input to end of output
        print(f"{token_id}")