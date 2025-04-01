from functools import lru_cache

import torch
from smolagents import tool
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline


@tool
def speech_to_text(file_path: str) -> str:
    """
    Converts an audio file to its transcribed text using a pre-trained pipeline.

    Args:
        file_path: The path to the audio file to be transcribed. This should be a local file path.

    Returns:
        The transcribed text from the audio file.
    """
    pipe = get_pipeline()
    result = pipe(file_path)
    return result["text"]


@lru_cache
def get_pipeline():
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    model_id = "openai/whisper-large-v3-turbo"

    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True
    )
    model.to(device)

    processor = AutoProcessor.from_pretrained(model_id)

    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        chunk_length_s=30,
        torch_dtype=torch_dtype,
        device=device,
    )
    return pipe
