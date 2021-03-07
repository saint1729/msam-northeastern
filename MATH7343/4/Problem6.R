beds <- read.table(file="bed.txt", header=TRUE)
library(psych)

describe(beds$bed80)
describe(beds$bed86)

t.test(beds$bed80, beds$bed86, var.equal = TRUE)
t.test(beds$bed80, beds$bed86, paired = T)
