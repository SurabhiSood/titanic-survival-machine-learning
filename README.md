### Goal 
RMS Titanic was a British passenger liner operated by the White Star Line that sank in the North Atlantic Ocean in the early morning hours of 15 April 1912, after striking an iceberg during her maiden voyage from Southampton to New York City.Of the estimated 2,224 passengers and crew aboard, more than 1,500 died. By examining factors such as class, sex, and age, in our dataset we will experiment with different machine learning algorithms and build a program that can predict whether a given passenger would have survived this disaster. To get sense of the variables, their class type, and the first few observations of each. We know we’re working with 1309 observations of 14 variables. To make things a bit more explicit since a couple of the variable names aren’t 100% illuminating, here’s what we’ve got to deal with:

![Overview](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/Overview.PNG)

### Process -

* We start with Data Visualization post importing the data set via pandas.The chart gives us a sense the variables, and informs us of the missing observations in each column.We see that Age, Cabin, Fare and Embarked columns have missing values which we will impute in the course of Data pre-processing.

![Missing Values](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/Dataset.PNG)

* The calculation shows that only 38% of the passengers survived.Not the best odds. The reason for this massive loss of life is that the Titanic was only carrying 20 lifeboats, which was not nearly enough for the 1,317 passengers and 885 crew members aboard.

![Survival of Passengers](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/survived-perished.PNG)

* The chart displays the number of passengers travelling aboard Titanic categorized based on the age group. 40% of the passengers were in age group of 20-30.

![Age Demographics of Passengers](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/age-survival.PNG)

* While the Titanic was sinking, the officers famously prioritized who was allowed in a lifeboat with the strict maritime tradition of evacuating women and children first. Our statistical results clearly reflect the first part of this policy as, across all classes, women were much more likely to survive than the men. 

![Visualizing Gender Survival](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/gender-survival.PNG)

* Here we see clearly, that Pclass is contributing to a persons chance of survival, especially if this person is in class 1. We will create another pclass plot below.

![Passenger Class Survival](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/PassengerClassAndSurvival.png)

* We broke passenger Name down into additional meaningful variables which can feed predictions. Passenger title is contained within the passenger name variable categorize passengers through the titles in the name and drew relation with survival

![Feature Engineering Title](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/TitleSurvived.png)

* SibSp and Parch would make more sense as a combined feature, that shows the total number of relatives, a person has on the Titanic. We created a 'relative' column and also added a feature that shows if someone is not alone. !

[Feature Engineering Family Size](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/FamilySizeAndSurvival.jpg)

* The visualization shows that the fare would be somewhere greater than 7 and less than 10, this adds another filter to calculate mean. post appling all three filters we get the mean of $ 8.03. Which will be replaced by nan value in Mr.Storey's fare! 
![Imputing Missing Value in Fare Column](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/FamilySizeAndSurvival.jpg)

* The median fare for a first class passenger departing from Charbourg (‘C’) coincides nicely with the $80 paid by our embarkment-deficient passengers. I think we can safely replace the NA values with ‘C’.

![Imputing Missing Value in Embarkment Column](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/MissingEmbarkment.png)

* Feature Selection

![important features](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/BestFeatures.png)

* Data Distribution

![Data](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/Preethi_branch/static/img/densityplot.png)


### Prediction Models-

1. KNN-
2. Logistic Regression - 84%
3. RandomForestClassifier - 77%


                    

