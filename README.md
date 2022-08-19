
# Crop Recommendation System

This is a web-app which includes a number of functions including a Crop-price prediction system,
a Crop-Recommendation system and a Fertilizer-Recommendation system.

It was designed as a part of the research conducted during my internship at the MSRF. 
The aim was to design a single portal for some of the common resources that might 
be required for the farmers or likewise while choosing a crop to be 
grown for that particular season and location. 


## Documentation
As mentioned above, this contains 3 Machine Learning models:

**A. Crop-price prediction**: 
                        
The model was trained on a large dataset of
which consisted of around 8 lakh instances including features such 
as 'commodity', 'state', 'market', 'min_price', 'max_price', 
'modal_price', and 'date'. Many algorithms were tried on and we 
found RandomForest to be giving the best accuracy of 97%. 
       
The model is contained in the - [Crop_price_prediction.ipynb](https://github.com/Zuess05/Crop-Recommendation-System/blob/main/Crop_Price_prediction.ipynb) file
and dataset is the - [agridata_csv_202110311352.csv](https://github.com/Zuess05/Crop-Recommendation-System/blob/main/agridata_csv_202110311352.csv) file.  
    
**B. Crop Recommendation:**

This was prepared with the [Crop_recommendation.csv](https://github.com/Zuess05/Crop-Recommendation-System/blob/main/Crop_recommendation.csv) dataset and 
a decision tree model was used for the recommendations. We obtained an accuracy of 
around 90%.

Model - [Crop_recommendation.ipynb](https://github.com/Zuess05/Crop-Recommendation-System/blob/main/crop_recomm_msrf.ipynb)

**C. Fertilizer Recommendation:**

This was done on the [Fertilizer_data.csv](https://github.com/Zuess05/Crop-Recommendation-System/blob/main/Fertilizer%20Prediction.csv) and a RandomForest classifier was
used to obtain results. The accuracy turned out to be 95%. Model - [Fertilizer_recom.ipynb](https://github.com/Zuess05/Crop-Recommendation-System/blob/main/Fertilizer_prediction_msrf%20(1).ipynb)


- Finally, the front-end was designed with the streamlit library. 


           



## Run Locally

Clone the project

```bash
  git clone https://github.com/Zuess05/Crop-Recommendation-System.git
```

Go to the project directory

```bash
  cd Crop-Recommendation-System
```

Install dependencies

```bash
  pip install streamlit
```

Start the server

```bash
  streamlit run Crop_price_prediction_app.py
```

