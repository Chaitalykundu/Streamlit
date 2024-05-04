import streamlit as st

# st.title("BMI Calculator")
st.title("Welcome to BMI Calculator")


weight = st.number_input("Enter your weight (in kgs)")
height_option = st.radio("Select your height format:",('cms','meters','feet'))


if(height_option == 'cms'):
    height = st.number_input("Height in cms:")
    try:
        bmi = weight / ((height/100)**2)
    except:
        # st.text("Enter some value of height")       
        pass

elif(height_option == 'meters'):
    height = st.number_input("Height in meters:")
    try:
        bmi = weight / (height ** 2)
    except:
        # st.text("Enter some value of height")
        pass

elif(height_option == 'feet'):
    height = st.number_input("Height in feet:")
    try:
        bmi = weight / ((height/3.28)**2)  # 1 meter = 3.28 feet
    except:
        # st.text("Enter some value of height")
        pass



# BMI calculate button
if(st.button('Calculate BMI')):
    if(weight <= 10 and height <= 100):
        st.text("Please enter valid height and weight")
    elif(weight <= 10 ):
        st.text("Please enter valid weight")
    elif(height <= 100):
        st.text("Please enter valid height")
    else:
        st.text("Your BMI index is {}".format(bmi))
        if(bmi < 16):
            st.error("You are Extremely Underweight")
        elif(bmi >= 16 and bmi < 18.5):
            st.warning("You are Underweight")
        elif(bmi >= 18.5 and bmi < 25):
            st.success("Healthy")
        elif(bmi >= 25 and bmi < 30):
            st.warning("Overweight")
        elif(bmi >= 30):
            st.error("Extremely Overweight")