import streamlit as st

def calculate_bmi(height, weight):
    # Convert height from cm to meters
    height = height / 100
    # Calculate BMI
    bmi = weight / (height * height)
    return bmi

def main():
    st.title("BMI Calculator")

    with st.form("bmi_form"):
        st.header("Enter your details")

        age = st.slider("Age", min_value=1, max_value=100, step=1, value=25)
        height = st.slider("Height (cm)", min_value=100.0, max_value=250.0, step=1.0, value=170.0)
        weight = st.slider("Weight (kg)", min_value=20.0, max_value=300.0, step=0.1, value=70.0)

        submit_button = st.form_submit_button("Calculate BMI")

        if submit_button:
            bmi = calculate_bmi(height, weight)

            st.header("Your BMI Results")
            st.write(f"Age: {age}")
            st.write(f"Height: {height} cm")
            st.write(f"Weight: {weight} kg")
            st.write(f"BMI: {bmi:.2f}")

            st.warning("Note: BMI is a general indicator, and it may not accurately reflect an individual's health.")

if __name__ == "__main__":
    main()
