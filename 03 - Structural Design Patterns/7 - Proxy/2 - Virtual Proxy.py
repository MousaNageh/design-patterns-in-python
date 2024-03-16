'''
Virtual Proxy Example: Imagine a heavy image loading process. 
Instead of loading the image as soon as the program starts,
a virtual proxy image loader could represent the real image. 
The actual image loading from disk would only happen when it's actually necessary to display the image,
thus saving resources initially.
'''
class Image:
    def __init__(self, filename):
        self._filename = filename
        print(f"Loading image from {self._filename}")
        # Simulate the time-consuming loading process
        # time.sleep(2)

    def display(self):
        print(f"Displaying {self._filename}")

class VirtualProxyImage:
    def __init__(self, filename):
        self._filename = filename
        self._image = None

    def display(self):
        if self._image is None:
            self._image = Image(self._filename)
        self._image.display()

# Usage
image = VirtualProxyImage("test_image.png")
# do anthor logic
# Image is not loaded until this point
image.display()