attach(airquality)
airquality[is.na(airquality)] = 0


pairwise.t.test(Ozone, Month, p.adjust.method = "bonf")
pairwise.t.test(Ozone, Month, p.adjust.method = "fdr")

airquality$Month<-as.factor(airquality$Month)
p<-aov(Ozone~Month,data=airquality)
TukeyHSD(p,conf.level = 0.95)
