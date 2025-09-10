import streamlit as st

st.sidebar.image("logo.png")
st.sidebar.title("Artistas")
st.title("Sound Cartepier")
generos = ["Rock", "R&B", "Hip Hop", "Pop"]

artistas = {
    "Rock": ["Gorillaz", "Deftones", "Korn", "Skillet"],
    "R&B": ["Michael Jackson", "Baco Exu do Blues", "Djavan", "Rita Lee"],
    "Hip Hop": ["Tyler the Creator","Kendrick Lamar","Kanye West","Mf Doom"],
    "Pop": ["SZA", "Doja Cat", "Kali Uchis", "Sabrina Carpenter"]
}
genero_selecionado = st.sidebar.selectbox("Selecione o gênero:", generos)

if genero_selecionado:
    artista_selecionado = st.sidebar.selectbox("Selecione seu artista", artistas[genero_selecionado])

if genero_selecionado and artista_selecionado:
    st.write(f"genero selecionado: {genero_selecionado}")
    st.write(f"artista selecionado: {artista_selecionado}")
    st.image(f"{artista_selecionado}.png", width=800)
    st.markdown("----")

    if genero_selecionado == "Rock" and artistas == "Gorillaz":
        st.video("https://www.youtube.com/watch?v=bbA5p54Rw2M&pp=ygUWZ29yaWxsYXogc3RyYW5nZSB0aW1leg%3D%3D")
    if genero_selecionado == "Rock" and artistas == "Deftones":
        st.video("https://www.youtube.com/watch?v=ifN91YvHj7g&pp=ygUIZGVmdG9uZXPSBwkJsgkBhyohjO8%3D")
    if genero_selecionado == "Rock" and artistas == "Korn":
        st.video("https://www.youtube.com/watch?v=xmOOGeZE-aE&pp=ygUEa29ybg%3D%3D")
    if genero_selecionado == "Rock" and artistas == "Skillet":
        st.video("https://www.youtube.com/watch?v=xmOOGeZE-aE&pp=ygUEa29ybg%3D%3D")

    if genero_selecionado == "R&B" and artistas == "Michael Jackson":
        st.video("https://www.youtube.com/watch?v=4V90AmXnguw&pp=ygUQbWljaGFlbCBqYWNrc29tbg%3D%3D")
    if genero_selecionado == "R&B" and artistas == "Baco Exu do Blues":
        st.video("https://www.youtube.com/watch?v=MGlGMa8WNXM&pp=ygUcYmFjbyBleHUgZG8gYmx1ZXMgMjAgbGlnYWNhbw%3D%3D")
    if genero_selecionado == "R&B" and artistas == "Djavan":
        st.video("https://www.youtube.com/watch?v=P-lxOj0XpEE&pp=ygUGZGphdmFu")
    if genero_selecionado == "R&B" and artistas == "Rita Lee":
        st.video("https://www.youtube.com/watch?v=RytrevkteVs&pp=ygUIcml0YSBsZWU%3D")

    if genero_selecionado == "Hip Hop" and artistas == "Tyler The Creator":
        st.video("https://www.youtube.com/watch?v=544H6xprGsY&pp=ygURdHlsZXIgdGhlIGNyZWF0b3I%3D")
    if genero_selecionado == "Hip Hop" and artistas == "Kendrick Lamar":
        st.video("https://www.youtube.com/watch?v=tXouRklJ8fk&pp=ygUPa2VuZHJpY2sgYWxhbWFy")
    if genero_selecionado == "Hip Hop" and artistas == "Kanye West":
        st.video("https://www.youtube.com/watch?v=G8u3P7Xqlvo&pp=ygUKa2FueWUgd2VzdA%3D%3D")
    if genero_selecionado == "Hip Hop" and artistas == "Mf Doom":
        st.video("https://www.youtube.com/watch?v=yKYgCD3m9AU&pp=ygUHbWYgZG9vbQ%3D%3D")

    if genero_selecionado == "Pop" and artistas == "SZA":
        st.video("https://www.youtube.com/watch?v=eqQO098eddE&pp=ygUDc3ph")
        