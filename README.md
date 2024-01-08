# Machine-Learning-powered-Phishing-URL-Detection
A Machine Learning based approach for Phishing URL Detection
Phishing attacks have become prevalent in recent times.Cybersecurity domain has been ever evolving to tackle the increasing fraudulent websites,emails,links etc.Data privacy and security is an important aspect of safeguarding personal information
Machine Learning approach is a cutting edge technology that can be utilised to detect phishing URL
Several Machine Learning algorithms have been tested and validated and finally the algorithm with the highest accuracy have been selected for deployment
Gradient Booster algorithm have been found to have the highest accuracy 97.4%
A website has been created for the purpose of detecting phishing URLs.
HTML,CSS has been used as the front end
Flask framework of Python has been used to deploy the model
Spyder and Visual Studio Code are the chosen environments
Dataset have been obtained from Kaggle and comprises of more than 11,000 instances and 31 features.



#Project Pathway
Train the Gradient Booster Model using the chosen dataset
The dataset is balanced and does not contain any null values
Use train_test_split to split the data
The data has been divided based on the features- 30 independent features and 1 dependent feature(i.e Class)
The final model after training has been saved as a pickle file(model.pkl)
A python file has been created to test the input url from the user to fetch the feature values for evaluation (feature.py)


