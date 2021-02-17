##### Example 1: the Faculty Salary data 
# Import data set. This is formatted two columns/variables
fsalary.data <- read.table(file="fsalary.txt", header=TRUE)
fsalary.data #display data

# For the categorical variable RANK, do a frequency table
table(fsalary.data$RANK)
# Draw a barchart
barplot(table(fsalary.data$RANK), main='Bar Chart for Rank')

#Draw a histogram for the continuous variable SALARY
hist(fsalary.data$SALARY)
#Define our own breakpoints for histogram: 27.5, 42.5, ..., 97.5
hist(fsalary.data$SALARY, breaks=27.5+(0:14)*5)

#Draw a boxplot
boxplot(fsalary.data$SALARY)
#Boxplot by the rank
boxplot(fsalary.data$SALARY~fsalary.data$RANK)
##A different syntax doing the same task
boxplot(SALARY~RANK, data=fsalary.data)

#Calculate statistics: mean, median, standard deviation
mean(fsalary.data$SALARY)
median(fsalary.data$SALARY)
sd(fsalary.data$SALARY)

#Summary statistics: min, max, 1st/3rd quartile, mean, median.
summary(fsalary.data$SALARY)
#Contrast this with summary of the whole data set (two variables)
summary(fsalary.data)  #For class(nominal) variable 'RANK', it gives the counts.

#More summary statistics, use some package. Here use 'psych' for example.
#The package needs to be installed beforehand. Installation is needed only once 
#  on a computer. But needs to load the library once every R session.
#install.packages("psych")
library(psych)
describe(fsalary.data$SALARY)
#Summary statistics by groups (rank)
describeBy(fsalary.data$SALARY, fsalary.data$RANK)

#Clear workspace
#You do not have to do this. 
#But it is a good habit to clear out all data after finishing.
#(Just to avoid confusion, may inadvertently use same variable name next time.)
rm(list=ls()) 

##### Example 2: the Response time data 
# Import data set. This is just one variable. 
#  We use 'scan' which input unformatted data.
#  This will create a vector variable
MyTime <- scan(file="ResponseTime.txt")
# We can also make this vector into a data frame as above (here only one column)
time.data<-data.frame(MyTime)
# We now add new variables to this data frame
time.data$obs.order<-seq(length(time.data$MyTime))
time.data$obs.phrase<- ifelse(time.data$obs.order<=5, 1, 
                              ifelse(time.data$obs.order<=10, 2, 
                                     ifelse(time.data$obs.order<=15, 3, 4)))
# Scatterplot of response time versus observation order
plot(MyTime~obs.order, data=time.data)
# stratified scatterplot of response time by 4 phrases of observations.
plot(MyTime~obs.phrase, data=time.data)

#Clear workspace
rm(list=ls())

##### Example 3: the trees data
# There are datasets that comes with R. So no need to import them.
#  Use data() to see which datasets are there.
#  We use 'trees' data as an example.

#Summary statistics
summary(trees)
#Scatterplot of Volume versus Height
plot(Volume~Height, data=trees)

# We can inspect the contents of a dataset with str()
str(trees)
# Display the first few observations
head(trees) 


