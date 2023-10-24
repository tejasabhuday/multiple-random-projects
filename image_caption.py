from huggingface_hub import notebook_login
notebook_login()


from datasets import load_dataset
ds= load_dataset("lamdalabs/pokemon-blip-captions")
ds
print("HI")