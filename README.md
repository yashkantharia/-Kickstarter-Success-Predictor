# Kickstarter-Success-Predictor
Predicting probability of success for a Kickstarter based on features such as time period, field of the project, etc. 

The Code for GUI and classification for success is added. Other models can be made using catboost regression very easily by editing the classification code. This regression models can be used to display a report consisting of predicted values for the given input and the difference between the input values and predicted values. There are sav files of the other models included in this repository.

The GUI is made using tkinter and the whole source code for thwe models and the GUI are in python 3. The GUI is a exe file executable on Windows.

IDE used for develeopment: Spyder 3.

The dataset is available on Kaggle: https://www.kaggle.com/yashkantharia/kickstarter-campaigns  


# Note that the weighted random forest code is not part of the GUI.
The Weighted Random Forest code works on the dataset sub-sampled on main category of the Kickstarter. The individuals models are generated and weights are assigned in consecutive runs to provide optimal results. The average of their results provide a marginal increase than the CatBoost model while using the traditional substitutions for categorical features i.e. One hot encoding.
