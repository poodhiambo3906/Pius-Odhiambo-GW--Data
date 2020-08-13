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

  

                                     
