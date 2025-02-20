import replicate
import os
import requests
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
from datetime import datetime

# 🔹 Load the global .env file
env_path = os.path.expanduser("~/Projects/global/.env")
if not os.path.exists(env_path):
    raise FileNotFoundError(f"❌ .env file not found at: {env_path}")

load_dotenv(env_path)

# 🔹 Retrieve & verify API token
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

if not REPLICATE_API_TOKEN:
    raise ValueError("❌ API token not found! Please check the .env file.")

print("✅ API token successfully loaded.")

# 🔹 Initialize Replicate Client
try:
    replicate_client = replicate.Client(api_token=REPLICATE_API_TOKEN)
except Exception as e:
    raise RuntimeError(f"❌ Error initializing the Replicate client: {e}")

# 🔹 Define prompt for image generation
input_data = {
    "prompt": "A majestic Viking ship on a stormy sea, dramatic lighting, highly detailed",
}

try:
    # 🔹 Run model and generate images
    output_urls = replicate_client.run("black-forest-labs/flux-schnell", input=input_data)

    if not output_urls:
        raise ValueError("❌ No images received from Replicate. Please check the API token or model name.")

    # 🔹 Set save path (folder `Automation/Projects/Masterimages/`)
    save_directory = os.path.expanduser("~/Automation/Projects/Masterimages")
    os.makedirs(save_directory, exist_ok=True)  # Create folder if it does not exist

    # 🔹 Download images using a session
    with requests.Session() as session:
        for index, url in enumerate(output_urls):
            try:
                response = session.get(url, timeout=10)  # Timeout for safety
                response.raise_for_status()  # Check for HTTP errors
                
                # 🔹 Open image with Pillow
                image = Image.open(BytesIO(response.content))

                # 🔹 Resize to 16:9 (1920x1080)
                target_size = (1920, 1080)
                image = image.resize(target_size, Image.LANCZOS)

                # 🔹 Set save path with timestamp (to prevent overwriting)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                image_path = os.path.join(save_directory, f"output_{timestamp}_{index}.jpg")

                # 🔹 Save image as JPG
                image.save(image_path, "JPEG", quality=90)

                print(f"✅ Image saved: {image_path}")
            except requests.exceptions.RequestException as e:
                print(f"❌ Error downloading image {index}: {e}")
            except Exception as e:
                print(f"❌ Error processing image {index}: {e}")

except Exception as e:
    print(f"❌ Error running the Replicate model: {e}")
