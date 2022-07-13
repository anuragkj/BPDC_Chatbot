from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("blenderbot-400M-distill")
model = AutoModelForSeq2SeqLM.from_pretrained("blenderbot-400M-distill")
UTTERANCE = "i am bored"
inputs = tokenizer([UTTERANCE], return_tensors="pt")
reply_ids = model.generate(**inputs)
print(tokenizer.batch_decode(reply_ids))