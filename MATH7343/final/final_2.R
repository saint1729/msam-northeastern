data <- read.table(file="shopping.txt", header = TRUE)
data$difference <- (data$OldAccount - data$NewAccount)
hist(data$difference, xlab = "price difference", ylab = "frequency",
     main = "Histogram of price difference")

wilcox.test(data$OldAccount, data$NewAccount, paired = TRUE, alternative = "greater")

