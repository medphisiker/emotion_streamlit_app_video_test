import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from streamlit_image_select import image_select
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import ImageSequenceClip
import numpy as np


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

        progress_text = "Преобразование видео"
        progress_bar = st.progress(0, text=progress_text)

        fps = clip.fps
        total_frames = int(fps * clip.duration)
        frames_in_percent = int(total_frames / 100)
        st.write(f"Всего кадров в видео, - {total_frames}")

        cnt = 0
        clip_frames = []
        for i, frame in enumerate(clip.iter_frames()):
            image = Image.fromarray(frame.astype("uint8"), "RGB")
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype("Roboto-Regular.ttf", 36)
            draw.text((10, 10), f"Кадр {i}/{total_frames}", font=font, fill=(0, 255, 0))
            frame = np.array(image)
            clip_frames.append(frame)
            cnt += 1
            if cnt // frames_in_percent == 1:
                progress_bar.progress(i, text=f"Обработка {i}%")
                cnt = cnt % frames_in_percent

        joined_video = "video.mp4"
        clip = ImageSequenceClip(clip_frames, fps)
        clip.write_videofile(joined_video)

        st.title("Склеенное из кадров видео")
        st.video(joined_video)
