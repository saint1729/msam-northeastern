data.bulimic <- read.table(file="daily_calories_bulimic.txt", header = TRUE)
data.healthy <- read.table(file="daily_calories_healthy.txt", header = TRUE)
data.bulimic
data.healthy
wilcox.test(data.bulimic$bulimic, data.healthy$healthy, alternative="two.sided")
