import streamlit as st
from PIL import Image
from streamlit_image_select import image_select


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
st.video(video_file)