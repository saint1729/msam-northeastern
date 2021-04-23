data <- read.table(file="stenosis.txt", header = TRUE)

lr.fit <- glm(data$disease~data$smoke, data = data, family = binomial(link = "logit"))
summary(lr.fit)

exp(0.3863)

exp(0.3863 + c(-1, 1) * 1.96 * 0.2762)

lr.fit2 <- glm(data$disease ~ data$smoke + data$sex, data = data, family = binomial(link = "logit"))
summary(lr.fit2)

exp(0.1946)

exp(0.1946 + c(-1, 1) * 1.96 * 0.2903)

