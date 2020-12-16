# Title: Robustness Evaluation of Housing, Health, & Happiness using Machine Learning Techniques

The website containing the Datastory for this project can be found [here](https://danieljsmarda.github.io/hhhml/).

# Abstract
From a high level, we determined that the paper thoroughly analyses the data provided and rigorously shows using linear regressors that the implementation of the Piso Firme program had a statistically significant impact on the dependent variables shown. We aim to extend this analysis in two distinct ways. First, we use _classifiers_ and the associated feature importances to further confirm or reject the conclusions found by the original authors' regression analyses. Second, we aim to build regressors that predicts the features collected in the 2005 survey that most generalizeable to other areas of public policy. Importantly, we aim to build these regressors _using only features from the 2000 census_. The ability to successfully derive the survey features from the census data would indicate that executing the 2005 survey was not necessary, and that time and funding allotted to similar future public policy surveys could be saved. 


# Research questions
- **[Task A]** Do Machine Learning-based classification approaches find similar positive treatment effects as the regression analyses of the paper? In other words, do we reach the same conclusions as the researchers if we try to classify households as `treatment` or `control` based on the dependent variables?
- **[Task B]** Is it possible to predict the most important variables from the 2005 survey using only data from the 2000 census?


# Proposed datasets
`households.dta` dataset from the paper. It contains information about the households included in the study. We aim to build classifiers and regressors for the dependent variables found in Tables 4 and 6, which do not require any further data.

# Methods

## Data collection
We already have the necessary datasets, as we are only using the datasets from the original paper.

## Data analysis
- __Task A__:
        1. Build Machine Learning classifiers (Logistic Regression, XGBoost, Random Forest) to classify whether a household belongs to the treatment or control group.
        2. Perform feature importance analysis to see the relative contribution of the different features to the classification. We will first build a model with only the control variables, and expect a low classification accuracy. Then, we will build a model with the same control features, plus a single "Outcome" feature (e.g., "Share of rooms with cement floors"), and evaluate the feature importance of this "Outcome" feature.
    We expect the features corresponding to outcome variables such as 'Share of rooms with cement floors' to have a large importance, and control variables such as demographics to have negligible importances.
        3. Compare the importances with the regression analyses from the paper.
We expect our feature importances to be relatively proportional to the effects found in the regression analysis of the paper.

- __Task B__: 
    Build regressors using OLS, Random Forest Regressor, Lasso Regression, Ridge Regression, and Multi-Layer Perceptron algorithms. For features, use only features from 2000 Census data. For outcomes, use the outcomes in Table 6. Among the features found in the `households.dta` file, the features in Table 6 are the features most generalizeable to other areas of public policy, and also the features which are the least likely to be collected in a standard census. Finally, compare the predictions based on the Mean Squared Error (MSE).

## Visualizations
1. The first visualization will show the treatment and control households on a geographical map. This will give a sense of the proximity between the treatment and control groups. (This is not directly related to our research questions, but will be useful for the data story). 

2. Feature importances in task A: the importance of each feature will be represented alongside the importance from the paper. The different variations of feature importance analyses will either be shown separately on different plots, or we will select a single one.

3. Prediction performances on task B: Barplots comparing the MSEs

# Proposed timeline and organization within the team

## General
- Jonathan: Task A
- Max: Task B
- Daniel: Group organization, data story organization.

## Week 1
- Jonathan: Perform all analyses and plots for task A
- Max: Perform all analyses and plots for task B
- Daniel: Set up Jekyll website, connect it to github repo, structure data story

## Week 2
- All group members: Meet over zoom and review the conclusions of our two tasks.
- Jonathan: Revise/Update analyses/plots for task A
- Max: Revise/Update analyses/plots task B
- Daniel: Add conclusions found from week 1 to data story.

## Week 3
- Daniel: Add conclusions from week 2 into data story, finish writing the data story
- Jonathan: Write analysis for task A in data story
- Max: Write analysis for task B in data story
- Whole group: Make the short presentation video

# Questions for TAs
We would appreciate feedback on the scope of our paper. We currently are planning to run 4 algorithms for task A and 5 algorithms for task B. Is it better to focus on just 2-3 algorithms instead? If yes, how should we pick which 2-3 algorithms to use for each section?
