unicef.data <- read.table(file="unicef.txt", na.strings = ".", header=TRUE)
unicef.data

# (a) Histogram and boxplot of low birth weight
hist(unicef.data$lowbwt,
     breaks=4+(0:14)*4,
     main = "Histogram Plot - Low birth weights",
     xlab = "Low birth weight",
     ylab = "Frequency",
     border = FALSE,
     labels = TRUE,
     xlim = c(0, 60),
     ylim = c(0, 40),
     col = rainbow(7))

boxplot(unicef.data$lowbwt,
        main = "Box Plot - Low birth weights",
        xlab = "All nations",
        ylab = "Low birth weights",
        labels = TRUE,
        boxwex = 0.3,
        outline = TRUE,
        outpch = 16,
        outcol = "seagreen3",
        las = 1,
        notch = FALSE,
        staplewex = 1,
        col = "tomato")

