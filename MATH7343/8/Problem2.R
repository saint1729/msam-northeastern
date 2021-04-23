
data <- read.table(file="Problem2.txt", header = TRUE)

#part a
plot(data$Cholesterol, data$Triglyceride, xlab = "Cholesterol", ylab = "Triglyceride")


#part c
(cor(data$Cholesterol, data$Triglyceride, method = "pearson"))

#part d
(cor.test(data$Cholesterol, data$Triglyceride, result = "pearson"))


#part e 
(cor(data$Cholesterol, data$Triglyceride, method = "spearman"))
(cor.test(data$Cholesterol, data$Patient, method = "spearman"))



#part g
cor.test(data$Cholesterol, data$Patient, method = "spearman")

#part h
perm.cor.test<-function(x,y, n.perm=100000, cor.method="spearman")
  {
n<-length(x)
T.obs<- cor(x,y, method=cor.method)
T.perm = rep(NA, n.perm)
for(i in 1:n.perm) 
  {y.perm = sample(y, n, replace=F) 
T.perm[i] = cor(x, y.perm, method=cor.method)}
mean(abs(T.perm)>=abs(T.obs))
}
perm.cor.test(data$Cholesterol, data$Triglyceride, cor.method = "pearson")
perm.cor.test(data$Cholesterol, data$Triglyceride, cor.method = "spearman")
              
