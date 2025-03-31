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

# Possession Data
labels = ["Spain", "England"]
sizes = [64.67, 35.33]
colors = ["#d7191c", "#2c7bb6"]  # Spain (Red), England (Blue)

# Create a styled pie chart
fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct="%1.2f%%", colors=colors, startangle=90,
    wedgeprops={"edgecolor": "black", "linewidth": 1.5}, textprops={"fontsize": 12}
)

# Improve contrast of percentage labels
for autotext in autotexts:
    autotext.set_color("white")
    autotext.set_fontweight("bold")

ax.axis("equal")  # Ensures the pie chart is circular

# Display in Streamlit
st.header("Possession")
st.pyplot(fig)

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


# Defensive Stats & Focus Team Analysis
st.header("Defensive Stats & Focus Team Analysis")

# Dropdown to select the focus team (ensure it's before using focus_team)
focus_team = st.selectbox("Choose Focus Team", ["Spain", "England"])

# Define stats for both teams
team_stats = {
    "Spain": {
        "Completed Passes (Opposition)": 228,
        "Defensive Actions (Team)": 23,
        "PPDA": 9.91,
        "Pressures": 161,
        "Counterpressures": 51,
        "Ball Recoveries in Opposition Half": 16,
        "Focus Team Pressure Count": 161,
        "Focus Team PAdj Pressures": 261.64
    },
    "England": {
        "Completed Passes (Opposition)": 377,
        "Defensive Actions (Team)": 22,
        "PPDA": 17.14,
        "Pressures": 166,
        "Counterpressures": 43,
        "Ball Recoveries in Opposition Half": 21,
        "Focus Team Pressure Count": 166,
        "Focus Team PAdj Pressures": 62.23
    }
}

# Display stats for the selected team
st.subheader(f"{focus_team}")

# Show team stats dynamically
for stat, value in team_stats[focus_team].items():
    st.write(f"**{stat}:** {value}")
    
# Add Image (xG Race Chart)
xg_image_path = "/Users/andreasbancheri/Documents/Tottenham/xg_racechart.png"
st.image(xg_image_path, caption="xG Race Chart", use_container_width=True)

# Add Image (Spain PPDA Analysis)
spain_ppda_image_path = "/Users/andreasbancheri/Documents/Tottenham/Spain_PPDA_Analysis.png"
st.image(spain_ppda_image_path, caption="Spain PPDA Analysis", use_container_width=True)

# Add Image (England PPDA Analysis)
england_ppda_image_path = "/Users/andreasbancheri/Documents/Tottenham/England_PPDA_Analysis.png"
st.image(england_ppda_image_path, caption="England PPDA Analysis", use_container_width=True)

# Add Image (England Pass Network Intervals)
england_pass_network_image_path = "/Users/andreasbancheri/Documents/Tottenham/England_PassNetwork_Intervals.png"
st.image(england_pass_network_image_path, caption="England Pass Network Intervals", use_container_width=True)

# Add Image (Spain Pass Network Intervals)
spain_pass_network_image_path = "/Users/andreasbancheri/Documents/Tottenham/Spain_PassNetwork_Intervals.png"
st.image(spain_pass_network_image_path, caption="Spain Pass Network Intervals", use_container_width=True)

# Add Image (Field Tilt)
field_tilt_image_path = "/Users/andreasbancheri/Documents/Tottenham/fieldtilt.png"
st.image(field_tilt_image_path, caption="Field Tilt", use_container_width=True)

# Footer with additional details or metadata
st.markdown("---")
st.markdown("Analysis done by Andreas Bancheri.")

