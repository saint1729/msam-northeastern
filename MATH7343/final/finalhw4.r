data <- data.frame(Nematodes = factor(c(0, 0, 0, 0,
                                             1000, 1000, 1000, 1000,
                                             5000, 5000, 5000, 5000,
                                             10000, 10000, 10000, 10000)),
                  SeedlingGrowth = c(10.8, 9.1, 13.5, 9.2,
                                     11.1, 11.1, 8.2, 11.3,
                                     5.4, 4.6, 7.4, 5.0,
                                     5.8, 5.3, 3.2, 7.5))
summary(data)
#part a
aov.fit <- aov(SeedlingGrowth~Nematodes, data=data)
summary(aov.fit)

#part b
TukeyHSD(aov.fit)
par(mar=c(2, 7, 2, 2))
plot(TukeyHSD(aov.fit, conf.level=0.99), las=2) 

#part c
TukeyHSD(aov.fit)
