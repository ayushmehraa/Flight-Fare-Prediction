<div align="center">
    <h1 align="center">
        <img src="https://img.icons8.com/arcade/512/airplane-front-view.png" width="80" />
        <br>Flight Fare Prediction
    </h1>

<h3 align="center">
Predict Flight Fare with data and plan you budget easy.
</h3>
<br>
<h3 align="center">
Technologies used.
</h3>
<br>
<p align="center">
        <img width="48" height="48" src="https://img.icons8.com/fluency/48/python.png" alt="python"/>
        <img width="48" height="48" src="https://img.icons8.com/fluency/48/jupyter.png" alt="jupyter"/>
        <img width="48" height="48" src="https://img.icons8.com/dotty/80/228BE6/visible.png" alt="visible"/>
        <img width="48" height="48" src="https://img.icons8.com/color/48/brain-3.png" alt="brain-3"/>
        <img width="55" height="55" src="https://img.icons8.com/nolan/64/flask.png" alt="flask"/>
        <img width="48" height="48" src="https://img.icons8.com/ios-filled/50/22C3E6/html-filetype.png" alt="html-filetype"/>
        <img width="48" height="48" src="https://img.icons8.com/color/48/git.png" alt="git"/>

</p>
</div>
<br>



## 📖 Table of Contents

- [📖 Table of Contents](#-table-of-contents)
- [📂 Dataset](#-dataset)
- [📜 *Overview*](#-dataset-overview)
- [📍 Overview](#-overview)
- [⚙️ Features](#️-features)
- [🛠 Project Structure](#-project-structure)
- [🚀 Getting Started](#-getting-started)
- [🤖 Web App](#-web-app)
    - [🌲 Flask Web App for Flight Fare Prediction](#-Flask-web-app-for-flight-fare-prediction)
        - [📜 Overview](-overview)
        - [      Development Steps](-development-steps)
    - [🌲 Streamlit Web App for Flight Fare Prediction](#-streamlit-web-app-for-flight-fare-prediction)
        - [📜 Overview](-overview)
        - [Development Steps](-development-steps)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 📍 Overview

This project focuses on predicting flight fares to help travelers make informed decisions when booking flights. Flight fares can be highly variable due to factors like airline, time of booking, route, and more. This predictive model utilizes machine learning techniques to forecast flight prices, enabling users to plan their travel budgets more effectively.

---

## 📂 Dataset

The Flight Fare Prediction dataset from Kaggle is a comprehensive collection of flight-related data designed for predicting the fares of flights. This dataset is widely used by data scientists and machine learning enthusiasts to develop and fine-tune predictive models that accurately estimate the cost of air travel. Let's take a closer look at this dataset:

#### 📜 Dataset Overview

Source: Kaggle (https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh)

Description: The dataset contains a diverse range of features associated with flights, including departure and arrival cities, airlines, departure and arrival times, duration, stops, and more. It's designed to simulate real-world flight data to help researchers and data practitioners build effective models for predicting flight fares.

Features: The dataset includes a variety of features, such as:

- Airline: The airline company operating the flight.
- Date of Journey: The date when the flight journey is scheduled.
- Source: The departure city.
- Destination: The arrival city.
- Route: The route taken by the flight.
- Duration: The duration of the flight in hours and minutes.
- Total Stops: The number of stops during the journey.
- Additional Information: Supplementary information about the flight.
- Target Variable: The primary target variable is the "Price" column, which represents the flight fare in Indian Rupees (INR).

---
## ⚙️ Features

- Data Collection: The project starts by gathering historical flight data, including details such as departure and arrival locations, airline, departure time, and more.
- Data Preprocessing: Raw data is preprocessed, including handling missing values, converting categorical variables, and normalizing numerical features.
- Feature Engineering: Relevant features are identified, and new features might be created to enhance the predictive power of the model.
- Model Selection: Different machine learning algorithms are explored, such as regression models, ensemble methods, and deep learning, to find the best-performing model for the task.
- Model Training: The selected model is trained on a portion of the dataset, and hyperparameters are tuned to optimize performance.
- Evaluation: The model's performance is evaluated using metrics like mean absolute error, root mean squared error, and others to quantify its accuracy.
- Prediction: Users can input flight details, and the trained model will predict the fare for the given flight.
- Web Interface: The prediction functionality is integrated into a user-friendly web interface where users can interact with the model.

---

## 🛠 Project Structure

- data: Contains the dataset used for training and testing the model.
- notebooks: Jupyter notebooks demonstrating data preprocessing, feature engineering, model training, and evaluation.
- src: Python scripts for data preprocessing, model training, and web interface development.
- web_app: Files for the web interface, including HTML, CSS, and JavaScript components.

---

## 🚀 Getting Started

- Clone the repository: git clone https://github.com/ayushmehraa/Flight-Fare-Prediction.git
- Navigate to the project directory: cd flight-fare-prediction
- Install the required packages: pip install -r requirements.txt
- Run the Jupyter notebooks to explore data preprocessing, model training, and evaluation.
- Set up the web app by following instructions in the web_app directory.

---

## 🤖 Web App

Flask and Streamlit are both popular frameworks for creating web applications in Python. They serve different purposes and have their own strengths. Here's a brief overview of how you could use Flask and Streamlit to create web apps for flight fare prediction:

#### 🌲Flask Web App for Flight Fare Prediction 
###### 👇 Overview
Flask is a micro web framework that allows you to build web applications in Python. It's highly flexible and can be used to create a wide range of web applications, including those with machine learning models for flight fare prediction.
[Flask-app](https://ayushmehraa.pythonanywhere.com)

###### Development Steps
- Create Flask App Structure: Set up a Flask project structure with templates, static files, and the necessary Python files.

- Model Integration: Train your flight fare prediction model using the chosen dataset. Once the model is trained and saved, integrate it into your Flask app.

- Create Routes: Define routes for different pages of your web app, such as a home page, prediction page, and result page.

- Create HTML Templates: Use HTML templates to design the user interface of your web app. The prediction form should allow users to input flight details.

- Form Submission and Prediction: Handle form submissions in your Flask app. Extract user inputs, pass them to the model for prediction, and display the predicted fare on the result page.

- Styling and UI: Enhance the UI using CSS to make your app visually appealing.

- Deployment: Deploy your Flask app on a web server so that users can access it online.

#### 🌲 Streamlit Web App for Flight Fare Prediction

##### 👇 Overview
Streamlit is a Python library designed for creating interactive web applications for data science and machine learning projects. It's particularly suited for creating quick and intuitive data apps without much web development effort.
[Streamlit-app](https://flight-fare-prediction-app.streamlit.app)
###### Development Steps

- Install Streamlit: Install the Streamlit library using pip install streamlit.

- Create Streamlit App: Create a single Python script that contains your entire Streamlit web app.

- User Interface: Use Streamlit's simple syntax to create widgets like sliders, input fields, and buttons for user interaction.

- Model Integration: Integrate your flight fare prediction model into the Streamlit app. You can use Streamlit to display inputs, invoke the model, and show predictions.

- App Layout: Arrange the widgets and outputs in the Streamlit app layout to create a user-friendly interface.

- Styling: Customize the app's appearance using Streamlit's built-in styling options.

- Running the App: Run the Streamlit app using the command streamlit run your_app.py. It will open in a web browser.

- Deployment: Streamlit apps are easily shareable by simply sharing the Python script. You can also deploy the app on platforms like Streamlit Sharing.

#### 🎮 Choosing Between Flask and Streamlit

- Flask: If you need more control over the structure and behavior of your web app, and if you're familiar with web development, Flask provides more flexibility. It's suitable for more complex projects where customization is key.

- Streamlit: If you're primarily focused on data presentation and want to quickly create interactive visualizations, Streamlit is a great choice. It's ideal for data scientists who want to create interactive data apps without delving into web development intricacies.

- Ultimately, the choice between Flask and Streamlit depends on your project's complexity, your familiarity with web development, and your specific goals for the flight fare prediction web app.

---

## 🤝 Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please submit an issue or a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---
