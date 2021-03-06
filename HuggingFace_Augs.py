# download the model outside of the sampling function
def get_model():
  import transformers
  model = transformers.AutoModelForCausalLM.from_pretrained("distilgpt2")
  

def GPT2_sampler(model):
  from transformers import pipeline
  pipe = pipeline("text-generation", model=model)
  return pipe
  
