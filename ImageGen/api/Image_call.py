from celery import shared_task
import requests

API_URL = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
API_KEY = "sk-JbSs9ZzcPxy9RlW6NSbyNWUskmip4Tmi0UP3C1WKptTsPetS"

@shared_task
def generate_image(prompt):
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "text_prompts": [
            {
                "text": prompt
            }
        ],
        "cfg_scale": 7,
        "height": 1024,
        "width": 1024,
        "samples": 1,
        "steps": 30,
    }

    response = requests.post(API_URL, json=data, headers=headers)
    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    response.raise_for_status()
    image = response.json()["artifacts"][0]["base64"]
    seed = response.json()["artifacts"][0]["seed"]
    return {"prompt": prompt, "image": image, "seed":seed}
