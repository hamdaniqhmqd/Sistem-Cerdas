# import torch
# from espnet2.bin.tts_inference import TextToSpeech

# model_id = "espnet/kan-bayashi_ljspeech"
# tts = TextToSpeech.from_pretrained(model_id)
# text = "Selamat datang di program NLP menggunakan ESPnet!"
# audio = tts(text)
# output_file = "output.wav"
# torch.save(audio, output_file)