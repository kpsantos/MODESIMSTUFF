##SMS Spam Detection using Supervised Learning
A study conducted by N. Chaurasia et al., [1] tackles the use of supervised learning for detecting SMS spam messages. The researchers have noticed that only few researches have been done to address the problem of smishing in their country India. In the process of finding a solution, the researchers have selected various models to train their dataset with:
•	Support Vector Machine (SVM) – Can be used to utilized for both classification and regression tasks.
•	Naïve Bayes (NB) – Significantly adaptable as you can require different limits of features or factors, which is especially useful for smishing detection. It is also the quickest and the least complex model for the training stage.
•	Decision Tree (DT) – Straightforward for the usage of decision trees that contains inside and outer nodes connected with one another.
o	Information Gain – measure of change in entropy based on the independent variable/
o	Entropy – Helps in constructing an appropriate decision tree for choosing the best splitter.
o	Gini Impurity  - Identical to entropy, however there is a significant gap in calculation of both approaches. So this will only be used to measure Gini impurity of the features after splitting them.
•	Random Forest (RF) – Fabricates a group decision trees. Best used to solve the overfitting issue. 
•	AdaBoost – Meta AI calculation that improves the classifier’s yield. Although this model requires some investment to build the supported model.
•	Logistic Regression – Used to anticipate the likelihood  of a dependent variable. The dependent variable is a Boolean variable.

Using Logistic Regression, results have shown that the model they have created is 77% accurate. Making it the best model for detecting smishing messages. However, it is also mentioned by the researchers that there is more research to be done, as some fields are left unexplored, and the accuracy can be improved, as well as the minimization of numbers that decides features and factors.





##Classifying Swahili Smishing Attacks for Mobile Money Users: A Machine-Learning Approach

Attackers use the smishing method against mobile money users as well, and smishing attacks costs companies and individuals millions of dollars annually. Many models have been introduced however, I.S. Mambina et al., [2] also deals with similar problems with these models [1]. They do not target a localized language such as Swahili. The researchers conducted dataset collection in Tanzania, where mobile network operators were selected based on its mobile money market share. They also used university students as part of the dataset. 
Based on the results, using a hybrid model of Extratree classifier feature selection and Random Forest using TFIDF (Term Frequency Inverse Document Frequency) the accuracy of the model of the vectorization leads to a staggering 99.86%. Where the model returns a low rate of false positive and false negative of 2 and 4. When compared to the dataset of 32259 messages, it means that the dataset is proven to be extremely reliable with a Log-Loss of 0.04.



References

[1] 	N. Chaurasia, P. Bharali and R. Naresh, "SMS Spam Detection using Supervised Learning," Turkish Journal of Computer and Mathematics Education, vol. 12, no. 11, pp. 3454-3461, 10 May 2021. 
[2] 	I. S. Mambina, J. D. Ndibwile and K. F. Michael, "Classifying Swahili Smishing Attacks for Mobile Money Users: A Machine-Learning Approach," IEEE Access, vol. 10, pp. 83061 - 83074, 04 August 2022. 


