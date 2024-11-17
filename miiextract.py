# Credits to Arian for the model thing

import os
import requests
from PIL import Image
from io import BytesIO

folder_name = input("Enter the Mii studio data. Not the short code in the URL thing: ")
answer = folder_name

url_types = {
    "FullBody": f"https://studio.mii.nintendo.com/miis/image.png?type=all_body&instanceCount=16&width=512&data={answer}",
    "Portrait": f"https://studio.mii.nintendo.com/miis/image.png?type=face&instanceCount=16&width=512&data={answer}",
    "Head": f"https://studio.mii.nintendo.com/miis/image.png?type=face_only&instanceCount=16&width=512&data={answer}",
}

expression_types = {
    # Portrait face render1!1!
    "Blink_Portrait": f"https://studio.mii.nintendo.com/miis/image.png?type=face&instanceCount=16&expression=blink&width=512&data={answer}",
    "Surprise_Portrait": f"https://studio.mii.nintendo.com/miis/image.png?type=face&instanceCount=16&expression=surprise&width=512&data={answer}",
    "Anger_Portrait": f"https://studio.mii.nintendo.com/miis/image.png?type=face&instanceCount=16&expression=anger&width=512&data={answer}",
    "Sorrow_Portrait": f"https://studio.mii.nintendo.com/miis/image.png?type=face&instanceCount=16&expression=sorrow&width=512&data={answer}",
    "Smile_Portrait": f"https://studio.mii.nintendo.com/miis/image.png?type=face&instanceCount=16&expression=smile&width=512&data={answer}",
    "Frustrated_Portrait": f"https://studio.mii.nintendo.com/miis/image.png?type=face&instanceCount=16&expression=frustrated&width=512&data={answer}",
    "WinkLeft_Portrait": f"https://studio.mii.nintendo.com/miis/image.png?type=face&instanceCount=16&expression=wink_left&width=512&data={answer}",
    "WinkRight_Portrait": f"https://studio.mii.nintendo.com/miis/image.png?type=face&instanceCount=16&expression=wink_right&width=512&data={answer}",
    "WinkLeftSmile_Portrait": f"https://studio.mii.nintendo.com/miis/image.png?type=face&instanceCount=16&expression=like_wink_left&width=512&data={answer}",
    "WinkRightSmile_Portrait": f"https://studio.mii.nintendo.com/miis/image.png?type=face&instanceCount=16&expression=like_wink_right&width=512&data={answer}",
    "Normal_Open_Portrait": f"https://studio.mii.nintendo.com/miis/image.png?type=face&instanceCount=16&expression=normal_open_mouth&width=512&data={answer}",
    "Blink_Open_Portrait": f"https://studio.mii.nintendo.com/miis/image.png?type=face&instanceCount=16&expression=blink_open_mouth&width=512&data={answer}",
    "Surprise_Open_Portrait": f"https://studio.mii.nintendo.com/miis/image.png?type=face&instanceCount=16&expression=surprise_open_mouth&width=512&data={answer}",
    "Anger_Open_Portrait": f"https://studio.mii.nintendo.com/miis/image.png?type=face&instanceCount=16&expression=anger_open_mouth&width=512&data={answer}",
    "Sorrow_Open_Portrait": f"https://studio.mii.nintendo.com/miis/image.png?type=face&instanceCount=16&expression=sorrow_open_mouth&width=512&data={answer}",
    "Smile_Open_Portrait": f"https://studio.mii.nintendo.com/miis/image.png?type=face&instanceCount=16&expression=smile_open_mouth&width=512&data={answer}",
    "WinkLeft_Open_Portrait": f"https://studio.mii.nintendo.com/miis/image.png?type=face&instanceCount=16&expression=wink_left_open_mouth&width=512&data={answer}",
    "WinkRight_Open_Portrait": f"https://studio.mii.nintendo.com/miis/image.png?type=face&instanceCount=16&expression=wink_right_open_mouth&width=512&data={answer}",
    # Head face render1!1!
    "Blink_Head": f"https://studio.mii.nintendo.com/miis/image.png?type=face_only&instanceCount=16&expression=blink&width=512&data={answer}",
    "Surprise_Head": f"https://studio.mii.nintendo.com/miis/image.png?type=face_only&instanceCount=16&expression=surprise&width=512&data={answer}",
    "Anger_Head": f"https://studio.mii.nintendo.com/miis/image.png?type=face_only&instanceCount=16&expression=anger&width=512&data={answer}",
    "Sorrow_Head": f"https://studio.mii.nintendo.com/miis/image.png?type=face_only&instanceCount=16&expression=sorrow&width=512&data={answer}",
    "Smile_Head": f"https://studio.mii.nintendo.com/miis/image.png?type=face_only&instanceCount=16&expression=smile&width=512&data={answer}",
    "Frustrated_Head": f"https://studio.mii.nintendo.com/miis/image.png?type=face_only&instanceCount=16&expression=frustrated&width=512&data={answer}",
    "WinkLeft_Head": f"https://studio.mii.nintendo.com/miis/image.png?type=face_only&instanceCount=16&expression=wink_left&width=512&data={answer}",
    "WinkRight_Head": f"https://studio.mii.nintendo.com/miis/image.png?type=face_only&instanceCount=16&expression=wink_right&width=512&data={answer}",
    "WinkLeftSmile_Head": f"https://studio.mii.nintendo.com/miis/image.png?type=face_only&instanceCount=16&expression=like_wink_left&width=512&data={answer}",
    "WinkRightSmile_Head": f"https://studio.mii.nintendo.com/miis/image.png?type=face_only&instanceCount=16&expression=like_wink_right&width=512&data={answer}",
    "Normal_Open_Head": f"https://studio.mii.nintendo.com/miis/image.png?type=face_only&instanceCount=16&expression=normal_open_mouth&width=512&data={answer}",
    "Blink_Open_Head": f"https://studio.mii.nintendo.com/miis/image.png?type=face_only&instanceCount=16&expression=blink_open_mouth&width=512&data={answer}",
    "Surprise_Open_Head": f"https://studio.mii.nintendo.com/miis/image.png?type=face_only&instanceCount=16&expression=surprise_open_mouth&width=512&data={answer}",
    "Anger_Open_Head": f"https://studio.mii.nintendo.com/miis/image.png?type=face_only&instanceCount=16&expression=anger_open_mouth&width=512&data={answer}",
    "Sorrow_Open_Head": f"https://studio.mii.nintendo.com/miis/image.png?type=face_only&instanceCount=16&expression=sorrow_open_mouth&width=512&data={answer}",
    "Smile_Open_Head": f"https://studio.mii.nintendo.com/miis/image.png?type=face_only&instanceCount=16&expression=smile_open_mouth&width=512&data={answer}",
    "WinkLeft_Open_Head": f"https://studio.mii.nintendo.com/miis/image.png?type=face_only&instanceCount=16&expression=wink_left_open_mouth&width=512&data={answer}",
    "WinkRight_Open_Head": f"https://studio.mii.nintendo.com/miis/image.png?type=face_only&instanceCount=16&expression=wink_right_open_mouth&width=512&data={answer}",
    # Full body face render1!1!
    "Blink_FullBody": f"https://studio.mii.nintendo.com/miis/image.png?type=all_body&instanceCount=16&expression=blink&width=512&data={answer}",
    "Surprise_FullBody": f"https://studio.mii.nintendo.com/miis/image.png?type=all_body&instanceCount=16&expression=surprise&width=512&data={answer}",
    "Anger_FullBody": f"https://studio.mii.nintendo.com/miis/image.png?type=all_body&instanceCount=16&expression=anger&width=512&data={answer}",
    "Sorrow_FullBody": f"https://studio.mii.nintendo.com/miis/image.png?type=all_body&instanceCount=16&expression=sorrow&width=512&data={answer}",
    "Smile_FullBody": f"https://studio.mii.nintendo.com/miis/image.png?type=all_body&instanceCount=16&expression=smile&width=512&data={answer}",
    "Frustrated_FullBody": f"https://studio.mii.nintendo.com/miis/image.png?type=all_body&instanceCount=16&expression=frustrated&width=512&data={answer}",
    "WinkLeft_FullBody": f"https://studio.mii.nintendo.com/miis/image.png?type=all_body&instanceCount=16&expression=wink_left&width=512&data={answer}",
    "WinkRight_FullBody": f"https://studio.mii.nintendo.com/miis/image.png?type=all_body&instanceCount=16&expression=wink_right&width=512&data={answer}",
    "WinkLeftSmile_FullBody": f"https://studio.mii.nintendo.com/miis/image.png?type=all_body&instanceCount=16&expression=like_wink_left&width=512&data={answer}",
    "WinkRightSmile_FullBody": f"https://studio.mii.nintendo.com/miis/image.png?type=all_body&instanceCount=16&expression=like_wink_right&width=512&data={answer}",
    "Normal_Open_FullBody": f"https://studio.mii.nintendo.com/miis/image.png?type=all_body&instanceCount=16&expression=normal_open_mouth&width=512&data={answer}",
    "Blink_Open_FullBody": f"https://studio.mii.nintendo.com/miis/image.png?type=all_body&instanceCount=16&expression=blink_open_mouth&width=512&data={answer}",
    "Surprise_Open_FullBody": f"https://studio.mii.nintendo.com/miis/image.png?type=all_body&instanceCount=16&expression=surprise_open_mouth&width=512&data={answer}",
    "Anger_Open_FullBody": f"https://studio.mii.nintendo.com/miis/image.png?type=all_body&instanceCount=16&expression=anger_open_mouth&width=512&data={answer}",
    "Sorrow_Open_FullBody": f"https://studio.mii.nintendo.com/miis/image.png?type=all_body&instanceCount=16&expression=sorrow_open_mouth&width=512&data={answer}",
    "Smile_Open_FullBody": f"https://studio.mii.nintendo.com/miis/image.png?type=all_body&instanceCount=16&expression=smile_open_mouth&width=512&data={answer}",
    "WinkLeft_Open_FullBody": f"https://studio.mii.nintendo.com/miis/image.png?type=all_body&instanceCount=16&expression=wink_left_open_mouth&width=512&data={answer}",
    "WinkRight_Open_FullBody": f"https://studio.mii.nintendo.com/miis/image.png?type=all_body&instanceCount=16&expression=wink_right_open_mouth&width=512&data={answer}",
}
print(f"Started processing Mii studio data...")
print(f"This will take some time unless you have a super duper processing pc...")
# This for da mii model downloading Arian don't kill me pls
model_url = f"https://mii-unsecure.ariankordi.net/miis/image.glb?erri=sgf0x-rpj&data={answer}"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

expression_folder = os.path.join(folder_name, "expressions")
if not os.path.exists(expression_folder):
    os.makedirs(expression_folder)


for image_type, url in url_types.items():
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        width, height = image.size
        crop_width = width // 16

        for i in range(16):
            left = i * crop_width
            right = left + crop_width
            cropped_image = image.crop((left, 0, right, height))
            cropped_image_path = os.path.join(folder_name, f"{image_type}_MiiImage{i+1}.png")
            cropped_image.save(cropped_image_path)
print(f"--- Mii turnarounds downloaded..")
print(f"Now this next step is gonna be extremely long...")
for expression, url in expression_types.items():
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        width, height = image.size
        crop_width = width // 16

        for i in range(16):
            left = i * crop_width
            right = left + crop_width
            cropped_image = image.crop((left, 0, right, height))
            cropped_image_path = os.path.join(expression_folder, f"{expression}_MiiImage{i+1}.png")
            cropped_image.save(cropped_image_path)
print(f"--- Mii Expressions with Turnarounds downloaded..")
model_response = requests.get(model_url)
if model_response.status_code == 200:
    model_path = os.path.join(folder_name, "MiiModel.glb")
    with open(model_path, "wb") as model_file:
        model_file.write(model_response.content)
    print(f"--- Mii Head Model downloaded.. ( credit Arian, and if you don't want me using this DM me on discord.)")
    print(f"finished downloading Mii data from Mii Studio!")
else:
    print("Failed to download data (Model).")
