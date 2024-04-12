"""
https://github.com/pytube/pytube
"""

import pytube
from os import mkdir

DEFAULT_FOLDER = 'downloads'
DEFAULT_PATH = r'./' + DEFAULT_FOLDER

def run():
    video_url = input("Video URL: ")
    youtube = pytube.YouTube(video_url)
    video = youtube.streams.filter(res="480p").first()
    
    print("downloading...")
    video.download(get_folder(None))
    print("Done :)")


def get_folder(folder_by_user):
    create_directory(DEFAULT_FOLDER)
    return DEFAULT_PATH


def create_directory(directory):
    """
    Create a new folder in the class location

    Attributes:
        directory -- folder name
    """
    try:
        mkdir(directory)
    except OSError as os_error:
        pass
    else:
        print("Directory has been created: %s " % directory)


if __name__ == "__main__":
    run()