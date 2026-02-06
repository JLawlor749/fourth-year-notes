library(tidyverse)
library(gapminder)

ggplot(gapminder,
       aes(x=lifeExp,
           y=gdpPercap,
           color=continent,
           size = 3)) + geom_point()


