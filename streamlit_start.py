import streamlit as st
from PIL import Image
from streamlit_image_select import image_select
from moviepy.video.io.VideoFileClip import VideoFileClip


def load_image(path2image):
    image = Image.open(path2image)
    image.load()
    return image


# инициализация модели
# модель должна загружаться из MLFLow он под VPN.
# в качестве альтернативы модель грузиться из Google Drive
# но в Streamlit Cloud это не работает
# поэтому для него ложим модель в репозиторий и считываем ее напрямую
video_file = open("01-01-01-01-01-01-01.mp4", "rb").read()

if __name__ == "__main__":
    # Верстка
    st.title("Видео")
    st.video(video_file)

    split_video_btn = st.button("Разбить видео на кадры")

    if split_video_btn:
        clip = VideoFileClip("01-01-01-01-01-01-01.mp4")
        for i, frame in enumerate(clip.iter_frames()):
            # Do something with the frame
            st.write(i, frame.shape)
