from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
tokenizer.padding_side = "left" 
tokenizer.pad_token = tokenizer.eos_token # to avoid an error
model = GPT2LMHeadModel.from_pretrained('gpt2')

device = 'cuda' if torch.cuda.is_available() else 'cpu'

texts = ["this is a first prompt", "this is a second prompt"]
encoding = tokenizer(texts, return_tensors='pt').to(device)
with torch.no_grad():
    generated_ids = model.generate(**encoding)
generated_texts = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)


from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
tokenizer.padding_side = "left" 
tokenizer.pad_token = tokenizer.eos_token # to avoid an error
model = GPT2LMHeadModel.from_pretrained('gpt2')

device = 'cuda' if torch.cuda.is_available() else 'cpu'

texts = ["this is a first prompt", "this is a second prompt"]
encoding = tokenizer(texts, padding=True, return_tensors='pt').to(device)
with torch.no_grad():
    generated_ids = model.generate(**encoding)
generated_texts = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
