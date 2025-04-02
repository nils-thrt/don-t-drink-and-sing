
import streamlit  as st
from consts import BASE_DIR


css = open(f"{BASE_DIR}/app/css/all-page.css").readlines()
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)



st.header("Don't drink and sing 🍹🎤", divider=True)






col_left, col_mid, col_right = st.columns(3)


with col_mid:
    st.image(f"{BASE_DIR}/images/spotify-icon-name/img-small.png")







st.button("Login with Spotify")







def display_in_middle(components : list):
    
    if (len(components) < 1):
        return
    
    columns = st.columns(len(components) + 2    )



    counter = 1
    for component in components:
        component(columns[counter])
        counter += 1
    


display_in_middle([
    lambda col : col.button("Hello")
])







st.html("<span>hello</span>")
