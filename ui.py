import streamlit as st

from youtube_analyzer import build_youtube_agent

st.set_page_config(page_title="YouTube Video Analyzer", layout= "centered")

st.title("🎥AI YouTube Video Analyzer")


# cache - fast access, temp stoage => most freq accesssed

@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

# Input Box
video_url = st.text_input("Enter YouTube Video Link:") #str
button = st.button("Analyze Video") # True/ False

if video_url and button:
    with st.spinner("Analyzing video..."):
        response = agent.run(
            f"Analyze this video: {video_url}",
        )
    st.markdown("Analysis Report of Video")
    st.markdown(response.content)