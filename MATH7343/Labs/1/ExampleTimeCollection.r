##### Example 3: the Response time data, import from the formatted data.
# Import data set. This is just one variable, but has three extra columns of zeros 
TimeData <- read.table(file="ExampleTimeCollection.txt", header=TRUE)
# Only take the first column
MyTime <- TimeData[,1]

# We can also make this vector into a data frame as above (here only one column)
time.data<-data.frame(MyTime)
# We now add new variables to this data frame
time.data$obs.order<-seq(length(time.data$MyTime))
# Scatterplot of response time versus observation order
plot(MyTime~obs.order, data=time.data)
