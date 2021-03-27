data <- read.table(file="bed2.txt", header=TRUE)
boxplot(data$bed~data$year,
        main="Bloxplot of 1980 & 1986",
        xlab="year",
        ylab="beds per 1000")

data2 <- read.table("bed.txt", header=TRUE );
x <- data2$bed80
y <- data2$bed86
wilcox.test (x, y, paired=TRUE, alternative="two.sided")


wilcox.test (x, y, paired=FALSE, alternative="two.sided")

t.test(data2$bed80, data2$bed86, paired=T)
