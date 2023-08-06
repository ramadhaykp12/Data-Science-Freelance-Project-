import streamlit as st
import pickle


# Function to make predictions using the pickled model
def predict_price(hama, curah_hujan, pupuk, hasil_panen):
    # Load the pickled model
    with open('Trialmodel.pkl', 'rb') as file:
        model = pickle.load(file)

    # Prepare the input data as a list of lists
    input_data = [[hama, curah_hujan, pupuk, hasil_panen]]

    # Make predictions using the loaded model
    prediction = model.predict(input_data)

    return prediction[0]  # Extract the first element from the prediction array

# Streamlit app
def main(): 
    st.title('Prediksi Harga Beras di Kabupaten Pati')

    # Create input fields for user
    st.header('Masukkan data dibawah:')
    hama = st.number_input('Hama', min_value=0, max_value=1000, value=0)
    curah_hujan = st.number_input('Curah Hujan', min_value=0.0, max_value=500.0, value=0.0, step=0.1)
    pupuk = st.number_input('Pupuk', min_value=0, max_value=1000, value=0)
    hasil_panen = st.number_input('Hasil Panen', min_value=0, max_value=1000, value=0)

    # Make predictions
    prediction = predict_price(hama, curah_hujan, pupuk, hasil_panen)

    # Display the prediction
    st.subheader('Prediction:')
    st.write(prediction)
    

if __name__ == '__main__':
    main()
