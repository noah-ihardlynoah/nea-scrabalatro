from openai import OpenAI
from rich import print
import dotenv
import base64

dotenv.load_dotenv()
client = OpenAI()

def getFileName(jokerName):
    fileName = f"{jokerName.replace(" ", "-").lower()}.png"
    return fileName

allJokers = open("powerupsraw.txt", "r")
count = 1
joker = allJokers.readline().strip()
while joker:
    fileName = getFileName(joker)
    print(f"""[bold]
==============
[/bold][bold yellow]Joker No. {count}: {joker}
(image will be saved as {fileName})[/bold yellow]
--""",)
    descInput = input("Img desc: ")
    chatgptMessage = f"""
Below is a brief description of the illustration that should appear on a square, Scrabble-like tile as part of a Balatro-Scrabble crossover game. 
The input will be in the following format: [Joker Name] [Description]
Please output nothing but the file as a PNG. The art style should be similar to the Balatro joker icons, but square. Do not keep the Joker imagery, as these will be called power-ups. Keep the vibrant colours and pixelated nature. It should be a 256x256 image with no metadata (minimum file size pls).

{}
"""
    chatgptResponse = client.images.generate(model="gpt-image-2.5-flare",prompt=chatgptMessage)
    image_base64 = chatgptResponse.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)
    with open(f"powerupimgs/{fileName}", "wb") as f:
        f.write(image_bytes)
    joker = allJokers.readline().strip()
    
    count += 1