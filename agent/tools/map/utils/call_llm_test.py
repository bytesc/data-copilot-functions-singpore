
from utils.get_config import config_data

def call_llm(question, llm):
    response = llm.chat.completions.create(
        model=config_data["model_name"],
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": question},
        ],
        stream=False
    )

    return response.choices[0].message
