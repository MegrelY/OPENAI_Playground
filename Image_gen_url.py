from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="An ethereal floating island in the sky, with cascading waterfalls that flow into a misty abyss below, lush green forests dotted with vibrant, bioluminescent plants, and ancient, intricate ruins of a lost civilization nestled within. The sky around is painted in surreal shades of twilight with stars beginning to twinkle, and mythical creatures with soft, glowing wings hover around the ruins, adding a magical ambiance. The scene is peaceful yet brimming with mystery, as beams of golden sunlight break through the clouds, casting a warm glow over the entire landscape.",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print("Image URL:", image_url)
