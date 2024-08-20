"""from django.test import TestCase, Client
from django.urls import reverse
from api.Image_call import generate_image
from api.models import GeneratedImage
import json
from django.conf import settings
import redis

class RedisConnectionTest(TestCase):
    def test_redis_connection(self):

        try:
            # Create a Redis client using the Redis URL from settings
            client = redis.Redis.from_url(settings.CELERY_BROKER_URL)
            # Ping the Redis server to check connectivity
            response = client.ping()
            self.assertTrue(response, "Redis server is not responding to PING")
        except redis.ConnectionError as e:
            self.fail(f"Redis connection failed: {e}")
            
    def test_celery_backend_connection(self):
        try:
            # Create a Redis client using the Redis URL for the result backend
            client = redis.Redis.from_url(settings.CELERY_RESULT_BACKEND)
            # Ping the Redis server to check connectivity
            response = client.ping()
            self.assertTrue(response, "Redis backend server is not responding to PING")
        except redis.ConnectionError as e:
            self.fail(f"Redis backend connection failed: {e}")


class GenerateImageTaskTestCase(TestCase):
    def test_generate_image_task(self):
        prompt = "A red flying dog"
        result = generate_image(prompt)
        self.assertIn("image", result)
        self.assertTrue(len(result["image"]) > 0)  # Ensure image_base64 data is returned

# Test for the image_generator view
class ImageGeneratorViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_image_generator_post(self):
        prompt = "A piano ninja"
        response = self.client.post(reverse('image_generator'), {"prompt": prompt})
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertIn("image_base64", response_data)

        # Verify the image is stored in the database
        image_record = GeneratedImage.objects.get(prompt=prompt)
        self.assertIsNotNone(image_record)
        self.assertEqual(image_record.prompt, prompt)
        self.assertTrue(len(image_record.image_base64) > 0)

# Test for the generate_default_images_view view
class GenerateDefaultImagesViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_generate_default_images(self):
        response = self.client.post(reverse('generate_default_images'))
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)

        self.assertIn("images", response_data)
        self.assertEqual(len(response_data["images"]), 3)

        for image in response_data["images"]:
            self.assertIn("image_base64", image)
            self.assertTrue(len(image["image_base64"]) > 0)

# Test for the GeneratedImage model
class GeneratedImageModelTestCase(TestCase):
    def test_generated_image_creation(self):
        prompt = "A footballer kid"
        image_base64 = "base64image"
        seed = "12345"
        generated_image = GeneratedImage.objects.create(
            prompt=prompt,
            image_base64=image_base64,
            seed=seed
        )
        
        self.assertEqual(generated_image.prompt, prompt)
        self.assertEqual(generated_image.image_base64, image_base64)
        self.assertEqual(generated_image.seed, seed)
        self.assertIsNotNone(generated_image.created_at)
"""