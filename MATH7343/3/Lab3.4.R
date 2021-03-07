nobs <- 4000
X <- rnorm(nobs)
Y <- rf(nobs, 4, 9)

print(mean(X^2 / Y))

