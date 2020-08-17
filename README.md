# Titanic: Machine Learning from Disaster
![Titanic](webapp/static/img/titanicimg.jpg)

### Goal 

RMS Titanic was a British passenger liner operated by the White Star Line that sank in the North Atlantic Ocean in the early morning hours of 15 April 1912, after striking an iceberg during her maiden voyage from Southampton to New York City. Of the estimated 2,224 passengers and crew aboard, more than 1,500 died. While there was some element of luck involved in surviving, it seems some groups of people were more likely to survive than others. By analyzing features, such as class, gender, age, number of children, number of parents, fare, and more, in the Titanic passenger dataset, we trained eight different machine learning models and selected the one with the highest accuracy score to build an application that can predict whether a given passenger would have survived this disaster or not.

### Data

The dataset consisted of 1,309 observations and 14 variables not including the engineered features.
Below is a detailed description of the dataset:

![Overview](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/Overview.PNG)

### Process

* The extracted dataset had some missing values (see dataset information below), which were replaced by calculated average values in the ‘age’ and ‘fare’ columns and using backfill method in the ‘embarked’ column. Some columns were dropped, as they did not hold any relevant information for the passenger survival prediction analysis.

![Missing Values](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/Dataset.PNG)

* The calculation shows that only 38% of the passengers survived. Not the best odds. The reason for this massive loss of life is that the Titanic was only carrying 20 lifeboats, which was not nearly enough for the 1,317 passengers and 885 crew members aboard.

![Survival of Passengers](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/survived-perished.PNG)

* The below chart demonstrates distribution of passengers by age. 40% of the passengers were between 20 and 30 years old.

![Age Demographics of Passengers](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/age-survival.PNG)

* While the Titanic was sinking, the officers famously prioritized who was allowed in a lifeboat with the strict maritime tradition of evacuating women and children first. The below visualization demonstrates results of this policy. Across all passenger classes, women were much more likely to survive than men.

![Visualizing Gender Survival](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/gender-survival.PNG)

* The following plot highlights how passenger class affected passengers’ chance of survival, especially if the passenger was a first-class member.

![Passenger Class Survival](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/PassengerClassAndSurvival.png)

* For the feature engineering, each passenger name has been broke down into additional meaningful variables, which can feed predictions. Passenger title is contained within the passenger name variable categorize passengers through the titles in the name and drew relation with survival.

![Feature Engineering Title](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/TitleSurvived.png)

* Siblings, spouses, parents, and children were combined together to show the total number of relatives each passenger had on the board of Titanic. A new column, 'relative', has been created to add an additional feature, which demonstrated if a passenger was traveling alone or with a family.

![Feature Engineering Family Size](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/FamilySizeAndSurvival.jpg)

* The following visualization shows that the fare would be somewhere greater than £7 and less than £10, this adds another filter to calculate the mean. Post applying all three filters, the calculated mean of a fare was £8.03 ponds. Which replaced the NaN value in Mr. Storey's fare!

![Imputing Missing Value in Fare Column](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/FamilySizeAndSurvival.jpg)

* The median fare for a first-class passenger departing from Charbourg (‘C’) port coincides nicely with the £80 paid by other embarkment-deficient passengers. As a result, all NaN values in the ‘embarked’ column have been replaced by ‘C’.

![Imputing Missing Value in Embarkment Column](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/MissingEmbarkment.png)

* Feature election:

![important features](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/master/webapp/static/img/BestFeatures.png)

* Data distribution:

![Data](https://github.com/SurabhiSood/titanic-survival-machine-learning/blob/Preethi_branch/static/img/densityplot.png)


### Prediction Models

1. KNN - 86%
2. Logistic Regression - 84%
3. RandomForestClassifier - 77%
