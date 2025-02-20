# replicate-image-generator.

# Replicate Image Generator

## Overview
This script uses the Replicate API to generate images based on a given text prompt. It downloads the generated images, resizes them to 1920x1080, and saves them locally.

## Requirements
- Python 3.8+
- `pip install replicate requests pillow python-dotenv`
- A Replicate API token (stored in a `.env` file)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/replicate-image-generator.git
   cd replicate-image-generator
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your Replicate API token:
   ```sh
   REPLICATE_API_TOKEN=your_api_token_here
   ```

## Usage
Run the script with:
```sh
python generate_images.py
```

### Customizing the Prompt
Edit the `input_data` dictionary in `generate_images.py` to change the image generation prompt:
```python
input_data = {
    "prompt": "A majestic Viking ship on a stormy sea, dramatic lighting, highly detailed",
}
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

