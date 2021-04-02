x <- 4
n <- 45
z <- 1.645
p <- x / n
CI_90 <- p + c(-1, 1) * z * sqrt(p * (1 - p) / n)
binom.test(x, n, 0.22, conf.level = 0.95, alternative = "two.sided")
