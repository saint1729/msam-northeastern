data <- read.table(file="lowbwt.txt", header = TRUE)
plot(data$apgar5, data$sbp, xlab = "apgar", ylab = "systolic blood pressure")

#part b
#part b
summary(lm(formula = data$sbp ~ data$gestage+ data$apgar5,data=data))

#part d
fit<-lm(sbp~gestage+apgar5, data=data)
predict(fit,  newdata=data.frame(gestage = 31, apgar5 = 7), interval='confidence')

#part e
summary(lm(formula = sbp ~ gestage + apgar5, data = data))

#part g
plot(fit, which=1)
