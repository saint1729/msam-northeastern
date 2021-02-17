MyTime <- scan(file = "CollectedResponseTimes.txt")
time.data <- data.frame(MyTime)
time.data$obs.order <- seq(length(time.data$MyTime))
time.data$obs.phrase <- ifelse(time.data$obs.order <= 10,
                               1,
                               ifelse(time.data$obs.order <= 20,
                                      2, 3))
# scatter plot of ResponseTime vs Observation Order
plot(MyTime ~ obs.order, data = time.data)
# Stratified scatter plot of 3 stages
plot(MyTime ~ obs.phrase, data = time.data)

summary(MyTime)
summary(MyTime[1:10])
summary(MyTime[11:20])
summary(MyTime[21:30])
