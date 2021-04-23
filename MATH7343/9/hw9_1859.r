data <- read.table(file="lowbwt.txt", header = TRUE)
plot(data$gestage, data$sbp, xlab = "gestational age", ylab = "systolic blood pressure")
lm(formula = data$sbp ~ data$gestage)
summary(lm(formula = data$sbp ~ data$gestage))
fit <- lm(sbp~gestage, data=data)
predict(fit, newdata=data.frame(gestage=31),interval='confidence')
predict(fit, newdata=data.frame(gestage=31),interval='prediction')
plot(fit, which=1)
