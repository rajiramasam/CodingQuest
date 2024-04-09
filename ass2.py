import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('data.pkl','rb'))
def predict(Size,Weight,Sweetness,Crunchiness,Juiciness,Ripeness,Acidity):
    input=np.array([[Size,Weight,Sweetness,Crunchiness,Juiciness,Ripeness,Acidity]]).astype(np.float64)
    prediction=model.predict_proba(input)
    pred='{0:.{1}f}'.format(prediction[0][0],2)
    return float(pred)
def main():
    st.title("Prediction")
    html_temp="""
    <div style="background-color:#e2062c ;padding:10px">
    <h2 style="color:white;text-align:center;">Apple Quality Prediction </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Size=st.text_input("Size")
    Weight=st.text_input("Weight")
    Sweetness=st.text_input("Sweetness")
    Crunchiness=st.text_input("Crunchiness")
    Juiciness=st.text_input("Juiciness")
    Ripeness=st.text_input("Ripeness")
    Acidity=st.text_input("Acidity")
    safe_html="""
    <div style="background-color:##32cd32;padding:10px">
    <h2 style="color:white;text-align:center;">Your apple is good</h2>
    </div>
    """
    danger_html="""
    <div style="background-color:#DC3545;padding:10px">
    <h2 style="color:black;text-align:center;">Your apple is bad</h2>
    </div>
    """
    if st.button("Predict"):
        output=predict(Size,Weight,Sweetness,Crunchiness,Juiciness,Ripeness,Acidity)
        if output>0.5:
            st.markdown(safe_html,unsafe_allow_html=True)
        else:
            st.markdown(danger_html,unsafe_allow_html=True)
if __name__=='__main__':
    main()