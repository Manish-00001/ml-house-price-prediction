
from datetime import datetime
import streamlit as st
from prediction_helper import predict


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="HomeValue AI",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: #f5f7fb;
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 17px;
    color: #6b7280;
    margin-bottom: 30px;
}

.section-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 20px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.06);
}

.section-title {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 18px;
}

.prediction-box {
    background: white;
    padding: 35px;
    border-radius: 22px;
    text-align: center;
    margin-top: 25px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.08);
}

.prediction-label {
    font-size: 18px;
    color: #6b7280;
}

.prediction-price {
    font-size: 46px;
    font-weight: 800;
    margin-top: 8px;
}

.prediction-note {
    color: #6b7280;
    font-size: 14px;
    margin-top: 10px;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 52px;
    font-size: 18px;
    font-weight: 700;
}

[data-testid="stSidebar"] {
    background: #111827;
}

[data-testid="stSidebar"] * {
    color: white;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("# HomeValue AI")

    st.markdown("""
    ### AI Property Valuation

    Enter your property's details and the machine-learning
    model will estimate its market value.

    ---
    """)

    st.markdown("### Model")

    st.info(
        "XGBoost Regressor\n\n"
        "Trained on historical house-price data."
    )

    st.markdown("---")

    st.caption("House Price Prediction System")
    st.caption("Machine Learning Project")


# =========================================================
# MAIN HEADER
# =========================================================

st.markdown(
    '<div class="main-title">HomeValue AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Estimate your property value using Machine Learning'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# PROPERTY DETAILS
# =========================================================

st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">Property Details</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


with col1:
    number_of_bedrooms = st.number_input(
        "Number of Bedrooms",
        min_value=0,
        max_value=20,
        value=3,
        step=1
    )


with col2:
    number_of_bathrooms = st.number_input(
        "Number of Bathrooms",
        min_value=0.0,
        max_value=20.0,
        value=2.0,
        step=0.5
    )


with col3:
    number_of_floors = st.number_input(
        "Number of Floors",
        min_value=1.0,
        max_value=10.0,
        value=1.0,
        step=0.5
    )


col4, col5, col6 = st.columns(3)


with col4:
    living_area = st.number_input(
        "Living Area (sq ft)",
        min_value=100.0,
        max_value=20000.0,
        value=1500.0,
        step=50.0
    )


with col5:
    lot_area = st.number_input(
        "Lot Area (sq ft)",
        min_value=100.0,
        max_value=100000.0,
        value=5000.0,
        step=100.0
    )


with col6:
    condition_of_the_house = st.slider(
        "Condition of the House",
        min_value=1,
        max_value=5,
        value=3
    )


st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# LOCATION DETAILS
# =========================================================

st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">Location and Property Information</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


with col1:
    city = st.selectbox(
        "Select City",
        [
            "Delhi",
            "Noida",
            "Ghaziabad",
            "Gurgaon"
        ]
    )


with col2:
    postal_code = st.number_input(
        "Postal Code",
        min_value=10000,
        max_value=999999,
        value=110017,
        step=1
    )


with col3:
    latitude = st.number_input(
        "Latitude",
        min_value=-90.0,
        max_value=90.0,
        value=28.594950,
        format="%.6f"
    )


col4, col5 = st.columns(2)


with col4:
    longitude = st.number_input(
        "Longitude",
        min_value=-180.0,
        max_value=180.0,
        value=77.252170,
        format="%.6f"
    )


with col5:
    number_of_schools_nearby = st.number_input(
        "Number of Schools Nearby",
        min_value=0,
        max_value=50,
        value=3,
        step=1
    )


st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# PROPERTY AGE
# =========================================================

st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">Property Age</div>',
    unsafe_allow_html=True
)


built_year = st.number_input(
    "Built Year",
    min_value=1900,
    max_value=datetime.now().year,
    value=2005,
    step=1
)


house_age = datetime.now().year - built_year


st.info(
    f"House Age: {house_age} years"
)

st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# PROPERTY SUMMARY
# =========================================================

st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">Property Summary</div>',
    unsafe_allow_html=True
)


s1, s2, s3, s4 = st.columns(4)


with s1:
    st.metric("Bedrooms", number_of_bedrooms)

with s2:
    st.metric("Bathrooms", number_of_bathrooms)

with s3:
    st.metric(
        "Living Area",
        f"{living_area:,.0f} sq ft"
    )

with s4:
    st.metric(
        "Lot Area",
        f"{lot_area:,.0f} sq ft"
    )


st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# PREDICTION BUTTON
# =========================================================

predict_col1, predict_col2, predict_col3 = st.columns([1, 2, 1])


with predict_col2:

    predict_button = st.button(
        "Estimate House Price",
        use_container_width=True
    )


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    input_dict = {

        "number_of_bedrooms": number_of_bedrooms,

        "number_of_bathrooms": number_of_bathrooms,

        "number_of_floors": number_of_floors,

        "living_area": living_area,

        "lot_area": lot_area,

        "condition_of_the_house": condition_of_the_house,

        "city": city,

        "built_year": built_year,

        "postal_code": postal_code,

        "latitude": latitude,

        "longitude": longitude,

        "number_of_schools_nearby": number_of_schools_nearby,

        "house_age": house_age
    }


    try:

        prediction = predict(input_dict)

        prediction = float(prediction)


        st.markdown(
            f"""
            <div class="prediction-box">

                <div class="prediction-label">
                    Estimated Property Value
                </div>

                <div class="prediction-price">
                    ₹{prediction:,.0f}
                </div>

                <div class="prediction-note">
                    Estimated using the trained XGBoost model
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    except Exception as e:

        st.error(
            f"Prediction error: {str(e)}"
        )

