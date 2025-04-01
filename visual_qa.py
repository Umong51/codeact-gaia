import base64
import os

import litellm
from dotenv import load_dotenv
from smolagents import tool

load_dotenv()


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


@tool
def visual_qa(image_path: str, question: str) -> str:
    """
    A tool that can answer questions about attached images.
    Args:
        image_path: The path to the image on which to answer the question. This should be a local path to downloaded image.
        question: The question to answer.
    Returns:
        Answer to the question.
    """
    base64_image = encode_image(image_path)

    response = litellm.completion(
        model="azure/" + os.getenv("MODEL_NAME"),
        api_base=os.getenv("AZURE_BASE"),
        api_version=os.getenv("AZURE_API_VERSION"),
        api_key=os.getenv("AZURE_API_KEY"),
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": question,
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ],
    )

    return response.choices[0].message.content
