import datetime
from base64 import b64decode
import webbrowser
import openai
from openai.error import InvalidRequestError

# Config
API_KEY = "Your seacret key"
SIZES = ['1024x1024', '512x512', '256x256']

openai.api_key = API_KEY # api key bind


def generate_image(prompt, num_image=1, size="512x512", output_format="url"):
    try:
        images = []
        res = openai.Image.create(
            prompt=prompt,
            n=num_image,
            size=size,
            response_format=output_format
        )
        if output_format == 'url':
            for i in res['data']:
                images.append(i.url)
        elif output_format == 'b64_json':
            for i in res['data']:
                images.append(i.b64_json)
        return {'created':datetime.datetime.fromtimestamp(res['created']), 'images':images}
    except InvalidRequestError as e:
        print(e)


def main():
    # Url 
    res = generate_image('Sun and moon in love', num_image=3)
    for i in res['images']:
        webbrowser.open(i)
    # Base64
    res = generate_image('Sun and moon fighting', num_image=3, output_format='b64_json')
    prefix = 'demo'
    for indx, image in enumerate(res['images']):
        with open(f'{prefix}_{indx}.jpg', 'wb') as f:
            f.write(b64decode(image))


if __name__ == "__main__":
    main()