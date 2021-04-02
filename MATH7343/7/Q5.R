library("MKinfer")
s1 <- rbinom(100000, 50, 0.16)
x1 <- round(mean(s1), 0)
CI_wald <- binomCI(x1, 50, 0.16, conf.level = 0.90, method = "wald")
CI_wald
CI_wilson <- binomCI(x1, 50, 0.16, conf.level = 0.90, method = "wilson")
CI_wilson
