library(magrittr)
library(dplyr)

lowbwt <- read.csv(file = './lowbwt.txt')

lowbwt %>%
  group_by(sex) %>%
  summarise(mu = mean(sbp), sigma = sd(sbp))

males_sbp <- subset(lowbwt, sex == 1)$sbp
females_sbp <- subset(lowbwt, sex == 0)$sbp

t.test(males_sbp)
t.test(females_sbp)
