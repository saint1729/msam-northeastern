library("psych")
#import data set 
data <- read.table(file = "cyto.txt", header = TRUE)
summary(data)

#part a 
describeBy(data$censor,data$group)

#part b
a.fit<-survfit(Surv(time, censor) ~ group,data=data)
summary(a.fit)


#part c
ggsurvplot(a.fit, data = data)
plot(a.fit, col=1:2, xscale=1, lwd=2, mark.time=TRUE,
       xlab="time", ylab="Survival Probability")


