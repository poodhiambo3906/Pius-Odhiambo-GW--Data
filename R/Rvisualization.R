library(tidyverse)

ufo <- read_csv("C:/Users/poodh/Desktop/gwu-arl-data-pt-03-2020-u-c/01-Class-Activities/Mon-Wed-Class/18-R/2/Activities/01-Stu_UFO/Unsolved/ufo.csv")
tail(ufo)


nrow(ufo)


length(unique(ufo$country))


summary(ufo)
summary(ufo$`duration (seconds)`)

arrange(summarise(duration= mean(`duration (seconds)`), group_by(ufo, state)), desc(duration))


ufo %>% 
    group_by(state) %>%
    summarise(duration= mean(`duration (seconds)`)) %>% 
    arrange(desc(duration))



# calculate the maximum duration in hours for every state
ufo %>% 
  group_by(state) %>%
  summarise(duration= max(`duration (seconds)`)) %>% 
  arrange(desc(duration))
view(ufo)

library(datasets)  
head(iris)
unique(iris$Species)                                     
length(unique(iris$Species))



iris %>% 
  group_by(Species) %>%
  summarise(NumberSpecies=length(Species))
  #arrange(desc(duration))

  #View(iris)

summary(iris)
plot(iris)

plot(iris$Species)
plot(iris$Sepal.Length)
plot(iris$Petal.Length, iris$Petal.Width)
plot(iris$Species,iris$Petal.Width)
plot(iris$Species,iris$Petal.Width)
plot(iris$Species,iris$Sepal.Length)

plot(iris$Species,iris$Sepal.Length,xlab="Iris Species", ylab="Iris Sepal Length",main= "MR. PIUS WHISKER PLOT")

hist()
View(irs)
hist(iris$Sepal.Length)
hist(iris$Sepal.Width)
hist(iris$Petal.Length)
hist(iris$Petal.Width)
#hist(iris$Species)

par(mfrow = c(3,1))

hist(iris$Petal.Width, iris$Species == "Setosa", 
     xlim = c(0, 3),
     breaks = 12,
     main = "Petal Width for Sentosa",
     col="red")


hist(iris$Petal.Length, iris$Species == "Versicolor", 
     xlim = c(0, 3),
     breaks = 12,
     main = "Petal Width for Versicolor",
     col="blue")


hist(iris$Sepal.Width, iris$Species == "Virginica", 
     xlim = c(0, 3),
     breaks = 12,
     main = "Petal Width for Virginica",
     col="green")


head(iris)
