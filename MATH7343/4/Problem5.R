library(psych)

heart.data <- read.table(file="heart.txt", header=TRUE, na.strings=".")

describeBy(heart.data$pdi, heart.data$trtment)
describeBy(heart.data$pdi, heart.data$trtment)

describe(heart.data$pdi)
describe(heart.data$mdi)

x <- heart.data$pdi[!is.na(heart.data$pdi)]
y <- heart.data$mdi[!is.na(heart.data$mdi)]

t.test(x, alternative = "two.sided", mu = 100)
t.test(y, alternative = "two.sided", mu = 100)
