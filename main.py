import qrcode
import streamlit as st
import os
import sys

#BASE_DIR = os.path.abspath(os.path.join(__file__, '../../'))
#sys.path.append(BASE_DIR)


st.markdown("# QRcode generator app made by Ferhat")
st.markdown("_Give us an url and we will give you a QRcode you can scan to go to your url_")

url=st.text_input("Write here your url ✨")
#url = 'https://tparduino.streamlit.app/'

# Générer le QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Sauvegarder le QR code dans un fichier
img.save("qrcode.png")
#st.image("qrcode.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")



download_button = st.empty()

if os.path.exists("qrcode.png"):
    with open("qrcode.png", 'rb') as op_img:
        download = download_button.download_button('Télécharger le qrcode', data = op_img, file_name='YouQRcode.png')

        if download:
            st.session_state['download'] = True



if os.path.exists("qrcode.png") and st.session_state['download']:
    os.remove("qrcode.png")
    st.session_state['download'] = False
    download_button.empty()
