import streamlit as st
import pickle
import numpy as np

# Load the model from the file
with open('titanic_model.pkl', 'rb') as file:
    model = pickle.load(file)
    # Define the Streamlit app
def main():
    st.title("Titanic Survival Prediction")
    
    st.write("Please enter the following details to predict if the passenger would have survived:")
    
    # Input fields for user data
    Pclass = st.radio("Choose a Class : ",['Upper','Middle','Lower'])
    Sex = st.radio("Choose a Gender : ",['Male','Female'])
    SibSp = st.number_input("No. of Siblings abord the ship : ",0 ,10)
    Parch = st.number_input("No. of Parents and Children abord the ship : ",0 ,10)
    Embarked = st.selectbox("Port to Embark from : ",['Southampton','Cherbourg','Queenstown'])
    AgeGroup = st.selectbox("Select AgeGroup : ",['Unknown','Baby','Child','Teenager','Young Adult','Adult','Senior'])
    FareBand = st.selectbox("Ticket Quota : ",['Basic $','Standard $$','Premium $$$','Royal $$$$'])
    
    # Mapping inputs to correct numerical values
    pclass_mapping = {'Upper': 1, 'Middle': 2, 'Lower': 3}
    sex_mapping = {'Male': 0, 'Female': 1}
    embarked_mapping = {'Southampton': 0, 'Cherbourg': 1, 'Queenstown': 2}
    agegroup_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Young Adult': 4, 'Adult': 5, 'Senior': 6}
    fareband_mapping = {'Basic $': 0, 'Standard $$': 1, 'Premium $$$': 2, 'Royal $$$$': 3}
    

    pclass_num = pclass_mapping[Pclass]
    sex_num = sex_mapping[Sex]
    sibsp_num = SibSp
    parch_num = Parch
    embarked_num = embarked_mapping[Embarked]
    agegroup_num = agegroup_mapping[AgeGroup]
    fareband_num = fareband_mapping[FareBand]
    
    # Combine all the mapped values into a single input array for prediction
    input_data = np.array([pclass_num, sex_num, sibsp_num, parch_num, embarked_num, agegroup_num, fareband_num]).reshape(1, -1)
    
    if st.button("Predict"):
        prediction = model.predict(input_data)[0]
        
        if prediction == 1:
            st.success("The passenger would have survived.")
        else:
            st.error("The passenger would not have survived.")
    

if __name__ == '__main__':
    main()

