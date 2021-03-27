contr1 <- c(1, 1, 1, -3)
require(psych)
require(data.table)


data <- read.csv("temp.csv")

k <- 4

contr1.est<-sum(contr1*data[,'mean'])
MSE<-summary(PF.fit)[[1]][2,'Mean Sq'] #extract MSE
contr1.se<- sqrt(sum(contr1^2/stat.fev2[,'n'])*MSE)
contr1.t<- contr1.est/contr1.se
k<-length(levels(PF.data$center)) #number of groups
contr1.p<-2*pt(-abs(contr1.t),df=sum(stat.fev2[,'n'])-k)

c(contr1.est, contr1.se, contr1.t, contr1.p)
