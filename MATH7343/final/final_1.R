data <- read.table(file="hospital.txt", header = TRUE)

plot(data$expadm, data$los, xlab = "average expense per admission into a community hospital",
     ylab = "average length of stay",
     main = "scatter plot of expadm vs los")

plot(data$expadm, data$salary, xlab = "average expense per admission into a community hospital",
     ylab = "average salary per employee in 1982",
     main = "scatter plot of expadm vs salary")



line <- lm(data$expadm ~ data$los)
summary(line)




predict(line, data.frame(los = 6), interval = "confidence")


plot(line, which = 1)
plot(line, which = 2)

line2 <- lm(expadm ~ los + salary, data = data)
summary(line2)

line3 <- lm(expadm ~ los, data = data)
anova(line2, line3)