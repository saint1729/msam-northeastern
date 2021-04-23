library(tidyverse)
library(tidyr)
library(readr)
library(dplyr)

baseball_data <- read.csv("./CrimeImpactOnSports/output/baseball_data.csv")
baseball_groups <- baseball_data %>% select(2, 3) %>% group_by(Won)

#shorten df names
bsbl <- baseball_data 

hist(bsbl$Crimes) #check normal distribution of crimes

id <- rownames(bsbl)
bsbl <- cbind(id=id, bsbl)


bsbl1 <- bsbl %>%
  mutate(group = paste0('group_', Won))%>%
  spread(group, Crimes)

bsbl_group0 <- bsbl1 %>%
  select(group_0) %>%
  filter(group_0 !='NA')

bsbl_group1 <-bsbl1 %>%
  select(group_1) %>%
  filter(group_1 !='NA')

hist(bsbl_group0$group_0)
hist(bsbl_group1$group_1)

res <- wilcox.test(bsbl_group0$group_0, bsbl_group1$group_1)
res

t.test(bsbl_group0$group_0, bsbl_group1$group_1, alternative = "two.sided", var.equal = FALSE)

