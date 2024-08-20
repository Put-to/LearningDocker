from django.http import JsonResponse
from .Image_call import generate_image
from .models import GeneratedImage
from django.utils import timezone
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def image_generator(request):
    latest_images = GeneratedImage.objects.order_by('-created_at')[:5]

    if request.method == "POST":
        prompt = request.POST.get("prompt")
        task = generate_image.delay(prompt)
        try:
            result = task.get(timeout=30)
            
            image_base64 = result["image"]
            seed = result["seed"]
            created_at = created_at = timezone.now()

            GeneratedImage.objects.create(prompt=prompt, image_base64=image_base64, seed=seed, created_at=created_at)
            return JsonResponse({"image_base64": image_base64})

        except Exception as e:
            logger.error(f"Error generating image: {str(e)}")
            return JsonResponse({"error": str(e)}, status=500)
        
    return render(request, "home.html", {"latest_images": latest_images})

def generate_default_images_view(request):
    latest_images = GeneratedImage.objects.order_by('-created_at')[:5]
    if request.method == "POST":
        default_prompts = [
            "A red flying dog",
            "A piano ninja",
            "A footballer kid"
        ]
        images = []

        tasks = [generate_image.delay(prompt) for prompt in default_prompts]
        try:
            for task in tasks:
                result = task.get(timeout=30)
                image_base64 = result["image"]
                images.append({"image_base64": image_base64})
            return JsonResponse({"images": images})
        except Exception as e:
            logger.error(f"Error generating image: {str(e)}")
            return JsonResponse({"error": str(e)}, status=500)
        
    return render(request, "home.html", {"latest_images": latest_images})
