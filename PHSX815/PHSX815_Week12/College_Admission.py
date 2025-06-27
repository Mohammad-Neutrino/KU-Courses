
####################################
#   Original Code by:              #
#   Hakan Ahmad Fatahillah         #
#                                  #
#   Modified by:                   #
#   Mohammad Ful Hossain Seikh     #
#   @University of Kansas          #
#   April 28, 2021                 #
#                                  #
####################################




import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn.linear_model import LinearRegression 
from sklearn.ensemble import RandomForestRegressor 
from sklearn.model_selection import GridSearchCV,train_test_split 
from sklearn.metrics import mean_absolute_error



admissions = pd.read_csv('/home/mohammad/University of Kansas/Computational_Physics/HomeWork12/Admission_Predict_Ver1.1.csv')
admissions = admissions.drop('Serial No.', axis = 1)


print (admissions.head(), "\n\n")


print (admissions.describe(), "\n\n")

print (
    "This table has 7 features to predict the chance of one's admission:\n"
    "GRE Score\n"
    "TOEFL Score\n"
    "University Rating\n"
    "SOP (Statement of Purpose)\n"
    "LOR (Letter of Recommendation)\n"
    "CGPA (Undergraduate GPA)\n"
    "Research (Whether someone has a research experience in the past)\n"
    "The GRE Score, TOEFL Score, CGPA, LOR, and SOP are numeric, while Univeristy Rating and Research are categorical.\n\n"
)



sns.set_context(rc = {"axes.labelsize":4})
sns.set_context(rc = {"xtick.labelsize":4})
sns.set_context(rc = {"ytick.labelsize":4})
sns.set_context(font_scale = 0.5)
sns.pairplot(admissions[admissions.columns], palette= 'BuPu' , diag_kind = "hist", kind = 'hist', height = 0.8)
plt.savefig('Correlogram.pdf')
plt.show()


corr = admissions.corr()
b = sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values, cmap="YlGnBu", annot = True)
_, labels = plt.xticks()
b.set_xticklabels(labels, size = 3.5)
_, labels = plt.yticks()
b.set_yticklabels(labels, size = 3.5)
plt.savefig('Correlation_Heatmap.pdf')
plt.show()



nFeatures = len(admissions.columns)
nCols = 3
nRows = int(np.ceil(nFeatures/nCols))
cols = admissions.columns
fig, axs = plt.subplots(nRows, nCols, figsize = (12,22))
col = 0
for i in range(nRows):
    for j in range(nCols):
        if col >= nFeatures:
           break
        h = axs[i,j].hist(admissions[cols[col]], bins = 20, color = 'b', density = True)
        h = axs[i,j].set_title(cols[col], fontsize = 'x-small')
        h = axs[i,j].tick_params(axis='both', which='major', labelsize= 5)
        h = axs[i,j].tick_params(axis='both', which='minor', labelsize= 5)
        h = axs[i,j].set_xlabel('Range Interval', fontsize = 4)
        h = axs[i,j].set_ylabel('Probability', fontsize = 4)
        h = axs[2,2].set_axis_off()
        col += 1
plt.subplots_adjust(top = 0.9, bottom = 0.1, hspace = 0.8, wspace = 0.3)
plt.grid(color = 'b', alpha = 0.5, linestyle = 'dotted', linewidth = 0.7)
plt.savefig('Input_Features.pdf')
plt.show()


X = admissions.drop('Chance of Admit ',axis = 1)
y = admissions['Chance of Admit ']
X_train,X_val,y_train,y_val = train_test_split(X,y,test_size = .25,random_state = 123)
lin_model = LinearRegression()
lin_model.fit(X_train,y_train)

print ('Mean absolute error for linear model: %0.4f' %mean_absolute_error(y_val,lin_model.predict(X_val)))
rf_model = RandomForestRegressor(n_estimators = 100,random_state = 42)
rf_model.fit(X_train,y_train)
print ('Mean absolute error for linear model after fit: %0.4f' %mean_absolute_error(y_val,rf_model.predict(X_val)))



feature_importance = pd.DataFrame(sorted(zip(rf_model.feature_importances_, X.columns)), columns=['Value','Feature'])
plt.figure(figsize=(10, 6))
sns.barplot(x="Value", y="Feature", data=feature_importance.sort_values(by="Value", ascending=False))
plt.title('Random Forest Feature Importance')
plt.tight_layout()
plt.savefig('Random_Forest.pdf')
plt.show()

