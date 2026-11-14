
import streamlit as st
from business import load_business, save_business

st.title("Business Owner Dashboard")

business = load_business()


st.subheader("Business Information")

with st.form("business_form"):
    name = st.text_input(
        "Business Name",
        value=business["name"]
    )

    location = st.text_input(
        "Location",
        value=business["location"]
    )

    submitted = st.form_submit_button("Save Business Info")

    if submitted:
        business["name"] = name
        business["location"] = location

        save_business(business)

        st.success("Business information updated!")


st.subheader("Service Prices")

with st.form("prices_form"):

    haircut = st.number_input(
        "Haircut ($)",
        min_value=0,
        value=business["services"]["haircut"]
    )

    beard = st.number_input(
        "Beard Trim ($)",
        min_value=0,
        value=business["services"]["beard_trim"]
    )

    combo = st.number_input(
        "Haircut + Beard ($)",
        min_value=0,
        value=business["services"]["haircut_and_beard"]
    )

    submitted = st.form_submit_button("Save Changes")

    if submitted:
        business["services"]["haircut"] = haircut
        business["services"]["beard_trim"] = beard
        business["services"]["haircut_and_beard"] = combo

        save_business(business)

        st.success("Prices updated successfully!")



st.subheader("Opening Hours")

with st.form("hours_form"):

    weekday_hours = st.text_input(
        "Monday - Saturday",
        value=business["hours"]["monday_saturday"]
    )

    sunday_hours = st.text_input(
        "Sunday",
        value=business["hours"]["sunday"]
    )

    submitted = st.form_submit_button("Save Hours")

    if submitted:
        business["hours"]["monday_saturday"] = weekday_hours
        business["hours"]["sunday"] = sunday_hours

        save_business(business)

        st.success("Opening hours updated!")
