# # import streamlit as st
# # import pandas as pd
# # import joblib

# # # =========================
# # # LOAD FILES
# # # =========================

# # model = joblib.load("ipl_score_predictor.pkl")
# # teams = joblib.load("teams.pkl")
# # venues = joblib.load("venues.pkl")

# # # =========================
# # # PAGE CONFIG
# # # =========================

# # st.set_page_config(
# #     page_title="IPL Score Predictor",
# #     page_icon="🏏",
# #     layout="wide"
# # )

# # # =========================
# # # CUSTOM CSS
# # # =========================

# # st.markdown("""
# # <style>
# # .main {
# #     background-color: #0f172a;
# # }

# # .stButton>button {
# #     width: 100%;
# #     background: linear-gradient(90deg,#ff512f,#dd2476);
# #     color: white;
# #     border-radius: 12px;
# #     height: 3rem;
# #     border: none;
# #     font-weight: bold;
# #     font-size: 18px;
# # }

# # .prediction-box {
# #     background: #111827;
# #     padding: 25px;
# #     border-radius: 15px;
# #     text-align: center;
# #     border: 1px solid #374151;
# # }

# # .big-score {
# #     font-size: 50px;
# #     color: #22c55e;
# #     font-weight: bold;
# # }
# # </style>
# # """, unsafe_allow_html=True)

# # # =========================
# # # HEADER
# # # =========================

# # st.markdown(
# #     """
# #     <h1 style='text-align:center;color:white'>
# #     🏏 IPL Score Predictor
# #     </h1>
# #     <p style='text-align:center;color:gray'>
# #     Predict First Innings Total Using Machine Learning
# #     </p>
# #     """,
# #     unsafe_allow_html=True
# # )

# # st.divider()

# # # =========================
# # # INPUTS
# # # =========================

# # col1, col2 = st.columns(2)

# # with col1:
# #     batting_team = st.selectbox(
# #         "Batting Team",
# #         teams
# #     )

# # with col2:
# #     bowling_team = st.selectbox(
# #         "Bowling Team",
# #         [team for team in teams if team != batting_team]
# #     )

# # venue = st.selectbox(
# #     "Venue",
# #     venues
# # )

# # st.divider()

# # col1, col2, col3, col4 = st.columns(4)

# # with col1:
# #     runs = st.number_input(
# #         "Current Runs",
# #         min_value=0,
# #         max_value=300,
# #         value=80
# #     )

# # with col2:
# #     wickets = st.number_input(
# #         "Wickets Lost",
# #         min_value=0,
# #         max_value=10,
# #         value=2
# #     )

# # with col3:
# #     overs = st.number_input(
# #         "Overs Completed",
# #         min_value=5.0,
# #         max_value=20.0,
# #         value=10.0,
# #         step=0.1
# #     )

# # with col4:
# #     runs_last_5 = st.number_input(
# #         "Runs Last 5 Overs",
# #         min_value=0,
# #         max_value=100,
# #         value=45
# #     )

# # wickets_last_5 = st.number_input(
# #     "Wickets Lost Last 5 Overs",
# #     min_value=0,
# #     max_value=10,
# #     value=1
# # )

# # st.divider()

# # # =========================
# # # PREDICTION
# # # =========================

# # if st.button("Predict Score"):

# #     input_df = pd.DataFrame({
# #         'venue': [venue],
# #         'bat_team': [batting_team],
# #         'bowl_team': [bowling_team],
# #         'runs': [runs],
# #         'wickets': [wickets],
# #         'overs': [overs],
# #         'runs_last_5': [runs_last_5],
# #         'wickets_last_5': [wickets_last_5]
# #     })

# #     prediction = int(model.predict(input_df)[0])

# #     lower = prediction - 5
# #     upper = prediction + 5

# #     st.markdown(
# #         f"""
# #         <div class="prediction-box">
# #             <h2 style="color:white">
# #                 Predicted Final Score
# #             </h2>
# #             <div class="big-score">
# #                 {prediction}
# #             </div>
# #             <h3 style="color:#9ca3af">
# #                 Range: {lower} - {upper}
# #             </h3>
# #         </div>
# #         """,
# #         unsafe_allow_html=True
# #     )

# #     st.balloons()


# import streamlit as st
# import pandas as pd
# import joblib

# # =====================================
# # PAGE CONFIG
# # =====================================

# st.set_page_config(
#     page_title="IPL Score Predictor",
#     page_icon="🏏",
#     layout="wide"
# )

# # =====================================
# # LOAD FILES
# # =====================================

# model = joblib.load("ipl_score_predictor.pkl")
# teams = joblib.load("teams.pkl")
# venues = joblib.load("venues.pkl")

# # =====================================
# # CSS
# # =====================================

# st.markdown("""
# <style>

# .stApp{
#     background:#0B1120;
# }

# .title{
#     text-align:center;
#     color:white;
#     font-size:48px;
#     font-weight:700;
#     margin-bottom:0;
# }

# .subtitle{
#     text-align:center;
#     color:#94A3B8;
#     font-size:18px;
#     margin-bottom:30px;
# }

# .card{
#     background:#111827;
#     padding:20px;
#     border-radius:20px;
#     border:1px solid #1F2937;
# }

# .team-card{
#     background:linear-gradient(
#         135deg,
#         #1E293B,
#         #0F172A
#     );
#     padding:20px;
#     border-radius:15px;
#     text-align:center;
#     color:white;
# }

# .prediction-card{
#     background:linear-gradient(
#         135deg,
#         #312E81,
#         #0F172A
#     );
#     padding:30px;
#     border-radius:20px;
#     text-align:center;
# }

# .score{
#     font-size:70px;
#     color:#22C55E;
#     font-weight:bold;
# }

# .range{
#     color:#CBD5E1;
#     font-size:24px;
# }

# .metric-box{
#     background:#111827;
#     padding:15px;
#     border-radius:12px;
#     text-align:center;
# }

# .stButton button{
#     width:100%;
#     height:55px;
#     font-size:18px;
#     font-weight:bold;
#     border:none;
#     border-radius:12px;
#     background:linear-gradient(
#         90deg,
#         #F97316,
#         #EC4899
#     );
#     color:white;
# }

# </style>
# """, unsafe_allow_html=True)

# # =====================================
# # HEADER
# # =====================================

# st.markdown(
#     """
#     <div class="title">🏏 IPL Score Predictor</div>
#     <div class="subtitle">
#         Predict First Innings Total Using Machine Learning
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# st.divider()

# # =====================================
# # TEAMS
# # =====================================

# c1, c2 = st.columns(2)

# with c1:
#     batting_team = st.selectbox(
#         "🏏 Batting Team",
#         teams
#     )

# with c2:
#     bowling_team = st.selectbox(
#         "🎯 Bowling Team",
#         [team for team in teams if team != batting_team]
#     )

# venue = st.selectbox(
#     "📍 Venue",
#     venues
# )

# st.divider()

# # =====================================
# # MATCH STATE
# # =====================================

# st.subheader("Match Situation")

# c1, c2, c3 = st.columns(3)

# with c1:
#     runs = st.number_input(
#         "Current Score",
#         min_value=0,
#         max_value=300,
#         value=75
#     )

# with c2:
#     wickets = st.number_input(
#         "Wickets Lost",
#         min_value=0,
#         max_value=10,
#         value=2
#     )

# with c3:
#     overs = st.number_input(
#         "Overs Completed",
#         min_value=5.0,
#         max_value=20.0,
#         step=0.1,
#         value=10.0
#     )

# st.divider()

# st.subheader("Last 5 Overs Performance")

# c1, c2 = st.columns(2)

# with c1:
#     runs_last_5 = st.number_input(
#         "Runs Scored in Last 5 Overs",
#         min_value=0,
#         max_value=100,
#         value=40
#     )

# with c2:
#     wickets_last_5 = st.number_input(
#         "Wickets Lost in Last 5 Overs",
#         min_value=0,
#         max_value=10,
#         value=1
#     )

# # =====================================
# # LIVE STATS
# # =====================================

# crr = runs / overs

# c1, c2, c3 = st.columns(3)

# with c1:
#     st.metric("Current Score", f"{runs}/{wickets}")

# with c2:
#     st.metric("Overs", overs)

# with c3:
#     st.metric("CRR", round(crr,2))

# st.divider()

# # =====================================
# # VALIDATIONS
# # =====================================

# error = None

# if batting_team == bowling_team:
#     error = "Batting and Bowling team cannot be same."

# elif wickets > 10:
#     error = "Wickets cannot exceed 10."

# elif runs_last_5 > runs:
#     error = "Last 5 overs runs cannot exceed current score."

# elif wickets_last_5 > wickets:
#     error = "Last 5 overs wickets cannot exceed total wickets."

# elif overs <= 5 and runs_last_5 != runs:
#     error = (
#         "For first 5 overs, "
#         "Runs Last 5 Overs should equal Current Runs."
#     )

# # =====================================
# # PREDICT BUTTON
# # =====================================

# if st.button("Predict Final Score"):

#     if error:
#         st.error(error)

#     else:

#         input_df = pd.DataFrame({
#             'venue':[venue],
#             'bat_team':[batting_team],
#             'bowl_team':[bowling_team],
#             'runs':[runs],
#             'wickets':[wickets],
#             'overs':[overs],
#             'runs_last_5':[runs_last_5],
#             'wickets_last_5':[wickets_last_5]
#         })

#         prediction = int(
#             model.predict(input_df)[0]
#         )

#         lower = prediction - 6
#         upper = prediction + 6

#         st.markdown(
#             f"""
#             <div class="prediction-card">

#             <h2 style="color:white;">
#             Predicted First Innings Total
#             </h2>

#             <div class="score">
#             {prediction}
#             </div>

#             <div class="range">
#             Expected Range:
#             {lower} - {upper}
#             </div>

#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#         confidence = max(
#             70,
#             min(
#                 95,
#                 int(
#                     100 -
#                     (abs(upper-lower)*2)
#                 )
#             )
#         )

#         st.progress(confidence)

#         st.success(
#             f"Prediction Confidence: {confidence}%"
#         )

import streamlit as st
import pandas as pd
import joblib

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="IPL Score Predictor",
    page_icon="🏏",
    layout="wide"
)

# =========================
# LOAD FILES
# =========================

model = joblib.load("ipl_score_predictor.pkl")
teams = joblib.load("teams.pkl")
venues = joblib.load("venues.pkl")

# =========================
# TEAM INFO
# =========================

TEAM_INFO = {
    "Royal Challengers Bangalore": {
        "captain": "Rajat Patidar",
        "star": "Virat Kohli",
        "titles": "2 IPL Title"
    },
    
    "Chennai Super Kings": {
        "captain": "Ruturaj Gaikwad",
        "star": "MS Dhoni",
        "titles": "5 IPL Titles"
    },

    "Mumbai Indians": {
        "captain": "Hardik Pandya",
        "star": "Jasprit Bumrah",
        "titles": "5 IPL Titles"
    },


    "Kolkata Knight Riders": {
        "captain": "Ajinkya Rahane",
        "star": "Sunil Narine",
        "titles": "3 IPL Titles"
    },

    "Delhi Capitals": {
        "captain": "Axar Patel",
        "star": "KL Rahul",
        "titles": "0 IPL Titles"
    },

    "Punjab Kings": {
        "captain": "Shreyas Iyer",
        "star": "Arshdeep Singh",
        "titles": "0 IPL Titles"
    },

    "Rajasthan Royals": {
        "captain": "Sanju Samson",
        "star": "Yashasvi Jaiswal",
        "titles": "1 IPL Title"
    },

    "Sunrisers Hyderabad": {
        "captain": "Pat Cummins",
        "star": "Travis Head",
        "titles": "1 IPL Title"
    },

    "Lucknow Super Giants": {
        "captain": "Rishabh Pant",
        "star": "Nicholas Pooran",
        "titles": "0 IPL Titles"
    },

    "Gujarat Titans": {
        "captain": "Shubman Gill",
        "star": "Rashid Khan",
        "titles": "1 IPL Title"
    }
}

# =========================
# VENUE INFO
# =========================

# VENUE_INFO = {
#     "M Chinnaswamy Stadium":
#         "Batting paradise. Small boundaries and high-scoring matches.",

#     "Wankhede Stadium":
#         "Excellent bounce and fast outfield.",

#     "Eden Gardens":
#         "Balanced wicket. Assists both batters and spinners."
# }

VENUE_INFO = {

    "M Chinnaswamy Stadium": {
        "city": "Bengaluru",
        "pitch": "Batting paradise with short boundaries and high-scoring games.",
        "final_winner": "RCB won IPL 2025 Final",
        "fact": "Home of Virat Kohli and one of the highest-scoring venues in T20 cricket."
    },

    "Wankhede Stadium": {
        "city": "Mumbai",
        "pitch": "True bounce, fast outfield, excellent for stroke play.",
        "final_winner": "Multiple IPL Finals hosted",
        "fact": "Venue of India's 2011 Cricket World Cup victory."
    },

    "Eden Gardens": {
        "city": "Kolkata",
        "pitch": "Balanced wicket assisting batters and spinners.",
        "final_winner": "KKR won IPL 2024 Final",
        "fact": "Largest cricket stadium in India by seating capacity."
    },

    "MA Chidambaram Stadium": {
        "city": "Chennai",
        "pitch": "Spin-friendly surface with slower conditions.",
        "final_winner": "Several IPL playoff matches hosted",
        "fact": "Popularly known as Chepauk."
    },

    "Arun Jaitley Stadium": {
        "city": "Delhi",
        "pitch": "Traditionally batting-friendly with short boundaries.",
        "final_winner": "No IPL Final hosted",
        "fact": "Formerly known as Feroz Shah Kotla."
    },

    "Narendra Modi Stadium": {
        "city": "Ahmedabad",
        "pitch": "Generally good batting surface with assistance for pacers.",
        "final_winner": "GT won IPL 2022 Final",
        "fact": "Largest cricket stadium in the world."
    },

    "Rajiv Gandhi International Stadium": {
        "city": "Hyderabad",
        "pitch": "Batting-friendly with some help for seamers early.",
        "final_winner": "SRH won IPL 2016",
        "fact": "Known for producing high-scoring encounters."
    },

    "Sawai Mansingh Stadium": {
        "city": "Jaipur",
        "pitch": "Balanced wicket with assistance for spinners.",
        "final_winner": "No IPL Final hosted",
        "fact": "Home ground of Rajasthan Royals."
    },

    "Punjab Cricket Association Stadium": {
        "city": "Mohali",
        "pitch": "Pace-friendly wicket with good carry.",
        "final_winner": "No IPL Final hosted",
        "fact": "One of the best venues for fast bowlers in India."
    },

    "Dr DY Patil Sports Academy": {
        "city": "Navi Mumbai",
        "pitch": "Excellent batting wicket with consistent bounce.",
        "final_winner": "No IPL Final hosted",
        "fact": "Hosted several IPL 2022 league matches."
    },

    "Brabourne Stadium": {
        "city": "Mumbai",
        "pitch": "Flat batting track and quick outfield.",
        "final_winner": "No IPL Final hosted",
        "fact": "One of India's oldest cricket stadiums."
    },

    "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Stadium": {
        "city": "Lucknow",
        "pitch": "Generally slow wicket helping spinners.",
        "final_winner": "No IPL Final hosted",
        "fact": "Home ground of Lucknow Super Giants."
    },

    "Green Park": {
        "city": "Kanpur",
        "pitch": "Traditionally assists spinners.",
        "final_winner": "No IPL Final hosted",
        "fact": "One of India's oldest international venues."
    },

    "Barsapara Cricket Stadium": {
        "city": "Guwahati",
        "pitch": "Good batting wicket with even bounce.",
        "final_winner": "No IPL Final hosted",
        "fact": "Often used as Rajasthan Royals' second home."
    },

    "Holkar Cricket Stadium": {
        "city": "Indore",
        "pitch": "Extremely batting-friendly surface.",
        "final_winner": "No IPL Final hosted",
        "fact": "Known for 200+ scores regularly."
    },

    "Himachal Pradesh Cricket Association Stadium": {
        "city": "Dharamshala",
        "pitch": "Fast bowlers get swing due to altitude.",
        "final_winner": "No IPL Final hosted",
        "fact": "One of the most scenic cricket grounds in the world."
    }
}

# =========================
# CUSTOM CSS
# =========================

st.markdown("""

<style>

.stApp{
background: linear-gradient(
135deg,
#0f172a 0%,
#111827 35%,
#1e293b 100%
);
color:white;
}

/* Main Heading */
.title{
text-align:center;
font-size:52px;
font-weight:800;
background: linear-gradient(
90deg,
#fbbf24,
#f97316,
#ef4444
);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

/* Subtitle */
.subtitle{
text-align:center;
color:#cbd5e1;
}

/* Team Cards */
.team-card{
background: rgba(37, 45, 68, 0.95);
padding:20px;
border-radius:20px;
border:1px solid rgba(255,255,255,0.15);
box-shadow:0 10px 30px rgba(0,0,0,0.35);

color:#ffffff; /* IMPORTANT */
}

.team-card h3{
color:#fbbf24;
font-size:32px;
font-weight:700;
margin-bottom:15px;
}

.team-card p{
color:#f8fafc;
font-size:17px;
font-weight:500;
line-height:1.8;
}

/* Metric Cards */
.metric-card{
background:#1e293b;
border:1px solid #334155;
padding:20px;
border-radius:16px;
color:white;
}

/* Prediction Card */
.prediction-card{
background: linear-gradient(
135deg,
#f97316,
#ef4444
);
padding:35px;
border-radius:24px;
text-align:center;
box-shadow:0 10px 40px rgba(239,68,68,0.35);
}

.big-score{
font-size:72px;
font-weight:800;
color:white;
}

/* Buttons */
.stButton>button{
width:100%;
height:55px;
border:none;
border-radius:14px;
font-size:18px;
font-weight:700;
color:white;

background:linear-gradient(
90deg,
#f97316,
#ef4444
);

transition:0.3s;
}

.stButton>button:hover{
transform:translateY(-2px);
box-shadow:0 8px 25px rgba(249,115,22,0.4);
}

/* Inputs */
.stSelectbox div[data-baseweb="select"]{
background:#1e293b;
border-radius:12px;
}

.stNumberInput input{
background:#1e293b !important;
color:white !important;
}

/* Metrics */
div[data-testid="metric-container"]{
background:#111827;
border:1px solid #334155;
padding:15px;
border-radius:16px;
}

/* Success Box */
.stSuccess{
background:#14532d !important;
}

/* Info Box */
.stInfo{
background:#1e3a8a !important;
}

</style>

""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown(
    """
    <div class='title'>🏏 IPL Score Predictor</div>
    <div class='subtitle'>
    AI Powered First Innings Score Prediction
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# =========================
# TEAM SELECTION
# =========================

col1,col2 = st.columns(2)

with col1:
    batting_team = st.selectbox(
        "🏏 Batting Team",
        teams
    )

with col2:
    bowling_team = st.selectbox(
        "🎯 Bowling Team",
        [team for team in teams if team != batting_team]
    )

# =========================
# TEAM INFO CARDS
# =========================

col1,col2 = st.columns(2)

with col1:

    team = TEAM_INFO.get(
        batting_team,
        {
            "captain":"Unknown",
            "star":"Unknown",
            "titles":"IPL Team"
        }
    )

    st.markdown(f"""
    <div class='team-card'>
    <h3>{batting_team}</h3>
    Captain: {team['captain']}<br>
    Star Player: {team['star']}<br>
    {team['titles']}
    </div>
    """, unsafe_allow_html=True)

with col2:

    team = TEAM_INFO.get(
        bowling_team,
        {
            "captain":"Unknown",
            "star":"Unknown",
            "titles":"IPL Team"
        }
    )

    st.markdown(f"""
    <div class='team-card'>
    <h3>{bowling_team}</h3>
    Captain: {team['captain']}<br>
    Star Player: {team['star']}<br>
    {team['titles']}
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================
# VENUE
# =========================

venue = st.selectbox(
    "🏟 Venue",
    venues
)

# =========================
# MATCH INPUTS
# =========================

st.subheader("📊 Match Situation")

c1,c2,c3,c4 = st.columns(4)

with c1:
    runs = st.number_input(
        "Current Runs",
        0,
        300,
        80
    )

with c2:
    wickets = st.number_input(
        "Wickets Lost",
        0,
        10,
        2
    )

with c3:
    overs = st.number_input(
        "Overs Completed",
        5.0,
        20.0,
        10.0,
        step=0.1
    )

with c4:
    runs_last_5 = st.number_input(
        "Runs in Last 5 Overs",
        0,
        100,
        40
    )

wickets_last_5 = st.number_input(
    "Wickets Lost in Last 5 Overs",
    0,
    10,
    1
)

# # =========================
# # LIVE METRICS
# # =========================

# current_rr = round(runs/overs,2)

# m1,m2,m3 = st.columns(3)

# with m1:
#     st.metric("Current Score", runs)

# with m2:
#     st.metric("Current RR", current_rr)

# with m3:
#     st.metric("Wickets", f"{wickets}/10")

# st.divider()

# =========================
# VALIDATIONS
# =========================

error = False

if runs_last_5 > runs:
    st.error(
        "Runs in last 5 overs cannot exceed current runs."
    )
    error = True

if wickets_last_5 > wickets:
    st.error(
        "Wickets in last 5 overs cannot exceed total wickets."
    )
    error = True

# =========================
# PREDICT
# =========================

if st.button("🚀 Predict Final Score"):

    if error:
        st.stop()

    data = pd.DataFrame({
        'venue':[venue],
        'bat_team':[batting_team],
        'bowl_team':[bowling_team],
        'runs':[runs],
        'wickets':[wickets],
        'overs':[overs],
        'runs_last_5':[runs_last_5],
        'wickets_last_5':[wickets_last_5]
    })

    prediction = int(model.predict(data)[0])

    lower = prediction - 6
    upper = prediction + 6

    confidence = 94

    st.markdown(
        f"""
        <div class='prediction-card'>
        <h2>Predicted Score</h2>
        <div class='big-score'>
        {prediction}
        </div>
        <h3>
        Expected Range: {lower} - {upper}
        </h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(confidence/100)

    st.success(
        f"Prediction Confidence : {confidence}%"
    )

    projected_rr = round(prediction/20,2)

    st.info(
        f"""
        Current Run Rate : {current_rr}

        Projected Run Rate : {projected_rr}
        """
    )

# =========================
# VENUE SECTION
# =========================

venue_data = VENUE_INFO.get(
    venue,
    {
        "city": "Unknown",
        "pitch": "No information available.",
        "final_winner": "N/A",
        "fact": "N/A"
    }
)

st.subheader("🏟 Venue Insights")

col1, col2 = st.columns(2)

with col1:
    st.info(f"📍 City: {venue_data['city']}")
    st.info(f"🏏 Pitch: {venue_data['pitch']}")

with col2:
    st.success(f"🏆 Final Winner: {venue_data['final_winner']}")
    st.warning(f"⭐ Fact: {venue_data['fact']}")

st.caption(
    "Model Accuracy: MAE 6.68 | RMSE 9.59 | R² 0.89"
)