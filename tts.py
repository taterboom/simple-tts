# Following pip packages need to be installed:
# !pip install git+https://github.com/huggingface/transformers sentencepiece datasets

import io
from tqdm import tqdm
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf
import numpy as np

processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

speaker_embeddings = {
    "BDL": "spkemb/cmu_us_bdl_arctic-wav-arctic_a0009.npy",
    "CLB": "spkemb/cmu_us_clb_arctic-wav-arctic_a0144.npy",
    "KSP": "spkemb/cmu_us_ksp_arctic-wav-arctic_b0087.npy",
    "RMS": "spkemb/cmu_us_rms_arctic-wav-arctic_b0353.npy",
    "SLT": "spkemb/cmu_us_slt_arctic-wav-arctic_a0508.npy",
}


def get_speaker_embedding(speaker: str):
    speaker_embedding = np.load(speaker_embeddings[speaker])
    speaker_embedding = torch.tensor(speaker_embedding).unsqueeze(0)
    return speaker_embedding

# # load xvector containing speaker's voice characteristics from a dataset
# embeddings_dataset = load_dataset(
#     "Matthijs/cmu-arctic-xvectors", split="validation")
# speaker_embeddings = torch.tensor(
#     embeddings_dataset[7306]["xvector"]).unsqueeze(0)


# inputs = processor(
#     text="This assumes that your program takes at least a tenth of second to run.", return_tensors="pt")

# # use tdqm to run all the speakr_embeddings
# for speaker in tqdm(speaker_embeddings):
#     speech = model.generate_speech(
#         inputs["input_ids"], get_speaker_embedding(speaker), vocoder=vocoder)
#     sf.write(f"speech_{speaker}.mp3", speech.numpy(), samplerate=16000)

def tts(text, speaker):
    inputs = processor(text=text, return_tensors="pt")
    speech = model.generate_speech(
        inputs["input_ids"], get_speaker_embedding(speaker), vocoder=vocoder)
    filename = f"speech_{speaker}.mp3"
    memory_file = io.BytesIO()
    memory_file.name = filename
    sf.write(memory_file, speech.numpy(), samplerate=16000)
    return memory_file
