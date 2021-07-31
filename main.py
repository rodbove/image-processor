import cli.app
import cv2
from src.lib import utils

@cli.app.CommandLineApp
def imgp(app):
    handle_command(app.params)

imgp.add_param("-p", "--path", help="Path to image file", type=str, required=True)
imgp.add_param("-f", "--flip", help="Orientation to flip image", type=str)
imgp.add_param("-d", "--downscale", help="Multiplier to downscale image (2, 3, 4 times...)", type=int)
imgp.add_param("-t", "--target", help="Target destination for modified file. Directory defaults do current if just the file name is provided", type=str, required=True)

def handle_command(params):
    image = cv2.imread(params.path)

    if params.flip:
        image = utils.flip_image(params.flip, image)

    if params.downscale:
        image = utils.scale_image_down(params.downscale, image)

    cv2.imwrite(params.target, image)

if __name__ == "__main__":
    imgp.run()
