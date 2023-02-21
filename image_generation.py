import os
import openai


OUTPUT_FILENAME = 'results.txt'
REQUEST = "6 pixelated game assets of a standing character. First asset must be facing front, the second facing back and the third facing side. The other 3 assets are the same but the character must be walking."
NUM_OF_IMAGES = 4


def generate_images() -> list[str]:
    """This function calls OpenAI API, specifically the 
    DALL-E 2 algorithm for drawing the requested text in
    the REQUEST global constant. The amount of images drawn
    is specified on the global constant NUM_OF_IMAGES.

    Returns
    -------
    list[str]
        A list of urls, each contains an image draw as requested.
    """
    response = openai.Image.create(
        prompt=REQUEST,
        n=NUM_OF_IMAGES,
        size="256x256"
    )
    images_urls = [img['url'] for img in response['data']]
    return images_urls


def save_urls(images_urls: list[str]):
    """Saves the urls inside an output file, which name is 
    specified on the global constant OUTPUT_FILENAME.

    Parameters
    ----------
    images_urls : list[str]
        Result images URLs in a list.
    """
    with open(OUTPUT_FILENAME, 'w') as f:
        f.writelines(line + '\n' for line in images_urls)


if __name__ == '__main__':
    openai.api_key = os.getenv("OPENAI_API_KEY")
    urls = generate_images()
    save_urls(urls)
