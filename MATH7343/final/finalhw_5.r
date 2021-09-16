#import data set 
data <- read.table(file="programmer.txt", header = TRUE)
lr.fit<-glm(formula = success ~ Experience, family = binomial(link = "logit"),data = data)
summary(lr.fit)

#part b
exp(0.1665*12 + c(-1,1)*1.96*0.0659*12)

