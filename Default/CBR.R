CaseBasedReasoningfunction <- function(FOREST,ImportanceFile)
{
library(CaseBasedReasoning)
library(randomForest)
library(e1071)
df1 <- read.csv(file=ImportanceFile, header=TRUE, sep=",")
features = df1$Features
Importance = df1$VarImp

library(tidyverse)
library(survival)
library(CaseBasedReasoning)
features <- factor(features)
Importance <- factor(Importance)

coxBeta <- CoxBetaModel$new(features,Importance)
coxBeta.fit()

CBR_Matrix = coxBeta.get_similar_cases()

write.csv(CBR_Matrix,'P.csv')
 
}