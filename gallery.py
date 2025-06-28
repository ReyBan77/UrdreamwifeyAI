
class Gallery:
    def __init__(self):
        self.images = []

    def save(self, prompt, image_url):
        self.images.append({ "prompt": prompt, "image": image_url })

    def get_images(self):
        return self.images
