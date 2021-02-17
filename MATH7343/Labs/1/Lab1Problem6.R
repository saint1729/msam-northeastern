salary.data <- read.table(file="salary.txt", header=TRUE)
salary.data

# a) Histogram of the salaries using R default setting
hist(salary.data$SALARY)

# b) Histogram with break points (at least 15 intervals)
hist(salary.data$SALARY,
     breaks=95+(0:14)*12,
     main = "Histogram Plot - Salaries",
     xlab = "Salaries",
     ylab = "Frequency",
     border = FALSE,
     labels = TRUE,
     xlim = c(min(salary.data$SALARY), max(salary.data$SALARY)),
     ylim = c(0, 8),
     col = rainbow(12))

# c) Boxplot of the salaries
boxplot(salary.data$SALARY,
        main = "Box Plot - Salaries",
        xlab = "All genders",
        ylab = "Salaries",
        labels = TRUE,
        boxwex = 0.3,
        outline = TRUE,
        las = 1,
        notch = FALSE,
        staplewex = 1,
        col = "purple")

# d) Boxplots of the salaries in two gender groups
boxplot(SALARY~GENDER, data=salary.data,
        main = "Box Plot - Salaries grouped by Gender",
        xlab = "Gender",
        ylab = "Salaries",
        labels = TRUE,
        boxwex = 0.3,
        outline = TRUE,
        outpch = 16,
        outcol = "seagreen3",
        las = 1,
        notch = FALSE,
        staplewex = 1,
        col = "tomato")

library(psych)

# e) summary statistics of salaries as one group and summary statistics within each gender
describe(salary.data$SALARY)
describeBy(salary.data$SALARY, salary.data$GENDER)

