import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(page_title="Spain vs England Stats Dashboard", layout="wide")

# Header of the Dashboard
st.title("Football Stats Dashboard: Spain vs England")
st.markdown("An analysis of key performance statistics for Spain and England.")

# Sidebar for control options (if any)
st.sidebar.header("Statistics Overview")

# Possession stats
st.header("Possession")
col1, col2 = st.columns(2)
with col1:
    st.metric("Spain Possession", "64.67%")
with col2:
    st.metric("England Possession", "35.33%")

# Passes & Progressions
st.header("Passes & Progressions")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Spain")
    st.write("Passes into the Box: 107")
    st.write("Passes into the Final Third: 159")
    st.write("Deep Progressions: 67")
with col2:
    st.subheader("England")
    st.write("Passes into the Box: 43")
    st.write("Passes into the Final Third: 78")
    st.write("Deep Progressions: 49")

# xG and Shot Stats
st.header("xG and Shot Statistics")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Spain")
    st.write("Total xG: 1.79")
    st.write("Open Play xG: 1.42")
    st.write("Set Piece xG (From Corner or Free Kick): 0.37")
    st.write("xG per Shot: 0.11")
    st.write("Total Shots: 16")
    st.write("Open Play Shots: 10")
    st.write("Set Piece Shots (From Corner): 6")
    st.write("Average Shot Distance: 16.84 meters")
with col2:
    st.subheader("England")
    st.write("Total xG: 0.73")
    st.write("Open Play xG: 0.16")
    st.write("Set Piece xG (From Corner or Free Kick): 0.57")
    st.write("xG per Shot: 0.08")
    st.write("Total Shots: 9")
    st.write("Open Play Shots: 3")
    st.write("Set Piece Shots (From Corner): 6")
    st.write("Average Shot Distance: 16.87 meters")

# Defensive Stats
st.header("Defensive Stats")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Spain")
    st.write("Completed Passes (Opposition): 228")
    st.write("Defensive Actions (Team): 23")
    st.write("PPDA: 9.91")
    st.write("Pressures: 161")
    st.write("Counterpressures: 51")
    st.write("Ball Recoveries in Opposition Half: 16")
with col2:
    st.subheader("England")
    st.write("Completed Passes (Opposition): 377")
    st.write("Defensive Actions (Team): 22")
    st.write("PPDA: 17.14")
    st.write("Pressures: 166")
    st.write("Counterpressures: 43")
    st.write("Ball Recoveries in Opposition Half: 21")

# Focus Team Analysis
st.header("Focus Team Analysis")
focus_team = st.selectbox("Choose Focus Team", ["Spain", "England"])
if focus_team == "Spain":
    st.write(f"Focus Team: Spain")
    st.write(f"Focus Team Pressure Count: 161")
    st.write(f"Focus Team PAdj Pressures: 261.64")
elif focus_team == "England":
    st.write(f"Focus Team: England")
    st.write(f"Focus Team Pressure Count: 166")
    st.write(f"Focus Team PAdj Pressures: 62.23")

# Optionally, you can add more graphs here for any other data

# Footer with additional details or metadata
st.markdown("---")
st.markdown("Data provided by your football analytics source. Analysis done using Python libraries.")
