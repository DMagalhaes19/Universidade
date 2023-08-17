### INSTALL AND UPLOAD PACKAGES (COMMENT IF NECESSARY) ###
install.packages("caret")
install.packages("dplyr")
install.packages("ellipse")
install.packages("kernlab")
install.packages("randomForest")
install.packages("timeDate")
install.packages("ggthemes")
install.packages("naniar")
install.packages("tidyverse")
install.packages("lubridate")
install.packages("hrbrthemes")
install.packages("ggplot2")
install.packages("fmsb")
install.packages("data.table")
library("data.table")
library("caret")
library("dplyr")
library("ellipse")
library("ggplot2")
library("lattice")
library("kernlab")
library("randomForest")
library("timeDate")
library("ggthemes")
library("naniar")
library("tidyverse")
library("lubridate")
library("hrbrthemes")
library("ggplot2")
library("fmsb")

#### UPLOAD AND CREATE DATASET OBJECTS ###
read.csv("./COFFEE_RATINGS_DATASET.csv", header = TRUE, sep = ",") -> dataset # READ THE IRIS DATASET FROM A CSV FILE
class(dataset) # CHECK THE CLASS OF THE DATASET OBJECT
attach(dataset) # ATTACH THE DATASET OBJECT TO THE WORKSPACE

################### DATA SUMMARY ###################
head(dataset) # PRINT THE FIRST 10 LINES OF DATA (AS EXAMPLE)
dim(dataset) # GET DATASET DIMENSIONS (SPACE, ROWS, COLUMNS)
sapply(dataset, class) # SAPPLY() USED TO MAP FUNCTION TO EACH ATTRIBUTE; CLASS FUNCTION RETURNS DATA CLASS TYPE FOR A GIVEN ATTRIBUTE
levels(dataset$cupper_points) # LISTS ALL UNIQUE CLASS LEVELS WITHIN THE cupper_points ATTRIBUTE OF DATASET
percentage <- prop.table(table(dataset$cupper_points)) * 100 # CREATE THE PERCENTAGE VARIABLE AND CALCULATE EACH INDIVIDUAL LEVEL
cbind(freq = table(dataset$cupper_points), percentage = percentage) # LISTS FREQUENCY AND PERCENTAGE OF EACH INDIVIDUAL CLASS LEVEL WITHIN cupper_points ATTRIBUTE
glimpse(dataset) # PRINTS A CONCISE SUMMARY OF THE DATASET
vis_miss(dataset) # VISUALISE MISSING DATA

### STATISTICAL SUMMARY ###
summary(dataset) # CALCULATE THE STATISTICAL SUMMARY OF THE DATASET
(
  country_table <- dataset %>% # CREATE A NEW DATAFRAME WITH THE COUNTRY OF ORIGIN ATTRIBUTE
    count(country_of_origin = factor(country_of_origin)) %>% # COUNT THE NUMBER OF OCCURENCES OF EACH COUNTRY OF ORIGIN
    mutate(pct = prop.table(n)) %>% # CALCULATE THE PERCENTAGE OF EACH COUNTRY OF ORIGIN
    arrange(-pct) %>% # ARRANGE THE COUNTRIES OF ORIGIN IN DESCENDING ORDER
    tibble() # CREATE A TIBBLE OBJECT
)

ggplot(
  country_table %>% filter(country_of_origin != "NA"), # FILTER OUT THE NA VALUES
  mapping = aes( # MAPPING THE DATA TO THE PLOT
    x = reorder(country_of_origin, n), # REORDER THE COUNTRIES OF ORIGIN BY THE NUMBER OF OCCURENCES
    y = pct, # SET THE Y AXIS TO THE PERCENTAGE
    group = 1, # SET THE GROUP TO 1
    label = scales::percent(pct) # SET THE LABEL TO THE PERCENTAGE
  ) # END OF MAPPING
) + # ADD THE FOLLOWING TO THE PLOT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  geom_bar(stat = "identity", # SET THE GEOM TO BAR
           fill = "#634832") + # SET THE FILL COLOUR
  geom_text(position = position_dodge(width = 0.9), # SET THE POSITION OF THE TEXT
            hjust = -0.05, # SET THE HORIZONTAL JUSTIFICATION
            size = 2.5) + # SET THE SIZE OF THE TEXT
  labs(x = "Country of Origin", # SET THE X AXIS LABEL
       y = "Proportion of Dataset") + # SET THE Y AXIS LABEL
  theme(axis.text.x = element_text( # SET THE X AXIS TEXT
    angle = 90, # SET THE ANGLE OF THE TEXT
    vjust = 0.5, # SET THE VERTICAL JUSTIFICATION
    hjust = 1 # SET THE HORIZONTAL JUSTIFICATION
  )) + # END OF THEME
  ggtitle("Country of Origin Listed in Coffee Ratings Dataset ") + # SET THE TITLE OF THE PLOT
  scale_y_continuous(labels = scales::percent) + # SET THE Y AXIS LABEL TO PERCENTAGE
  coord_flip() # FLIP THE COORDINATES

species_table <- dataset %>% # CREATE A NEW DATAFRAME WITH THE SPECIES ATTRIBUTE
  count(species = factor(species)) %>% # COUNT THE NUMBER OF OCCURENCES OF EACH SPECIES
  mutate(pct = prop.table(n)) %>% # CALCULATE THE PERCENTAGE OF EACH SPECIES
  tibble() # CREATE A TIBBLE OBJECT
ggplot(species_table, mapping = aes(x = species, y = pct, group = 1, label = scales::percent(pct))) + # MAPPING THE DATA TO THE PLOT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  geom_bar(stat = "identity", # SET THE GEOM TO BAR
           fill = c("#634832", "#3b2f2f")) + # SET THE FILL COLOUR
  geom_text(position = position_dodge(width = 0.9), # SET THE POSITION OF THE TEXT
            vjust = -0.5, # SET THE VERTICAL JUSTIFICATION
            size = 4) + # SET THE SIZE OF THE TEXT
  scale_y_continuous(labels = scales::percent) + # SET THE Y AXIS LABEL TO PERCENTAGE
  ggtitle("Arabica vs Robusta Proportion in Dataset ") # SET THE TITLE OF THE PLOT

(
  arabica_countries<-dataset %>%
    filter(species =="Arabica") %>%
    count(species=factor(species),
          country=country_of_origin) %>%
    mutate(pct = prop.table(n)) %>%
    arrange(-n) %>%
    tibble()
)

ggplot(arabica_countries %>% filter(country!="NA"),
       mapping=aes(x=reorder(country,n),y=pct,group=1,label=scales::percent(pct))) +
  theme_fivethirtyeight()+
  geom_bar(stat="identity",
           fill="#634832")+
  geom_text(position = position_dodge(width = 0.9),
            # move to center of bars
            hjust = -0.05,
            #Have Text just above bars
            size = 2.5) +
  ggtitle("Arabica Coffee Countries (for our dataset) ") +
  scale_y_continuous(labels = scales::percent) +
  coord_flip()

(
  robusta_countries<-dataset %>%
    filter(species =="Robusta") %>%
    count(species = factor(species),
          country=country_of_origin) %>%
    mutate(pct = prop.table(n)) %>%
    arrange(-n) %>%
    tibble()
)

ggplot(robusta_countries %>% filter(country!="NA"),
       mapping=aes(x=reorder(country,n),y=pct,group=1,label=scales::percent(pct))) +
  theme_fivethirtyeight()+
  geom_bar(stat="identity",
           fill="#3b2f2f")+
  geom_text(position = position_dodge(width = 0.9),
            # move to center of bars
            hjust = -0.05,
            #Have Text just above bars
            size = 2.5) +
  ggtitle("Robusta Coffee Countries (for our dataset) ") +
  scale_y_continuous(labels = scales::percent) +
  coord_flip()

dataset %>% # CREATE A NEW DATAFRAME WITH THE COUNTRY OF ORIGIN ATTRIBUTE
  filter(country_of_origin %in% c("India", "Uganda", "Ecuador", "United States", "Vietnam")) %>% # FILTER OUT THE COUNTRIES WE WANT TO LOOK AT
  count(country_of_origin, cupper_points) %>% # COUNT THE NUMBER OF OCCURENCES OF EACH COUNTRY OF ORIGIN
  group_by(country_of_origin) %>% # GROUP THE DATA BY COUNTRY OF ORIGIN

  ggplot(dataset %>% filter(country_of_origin %in% c("India", "Uganda", "Ecuador", "United States", "Vietnam")), # FILTER OUT THE COUNTRIES WE WANT TO LOOK AT
         mapping = aes(x = country_of_origin, fill = cupper_points)) + # MAPPING THE DATA TO THE PLOT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  geom_bar(position = "fill") + # SET THE GEOM TO BAR
  scale_fill_manual(values = c("#BE9B7B", "#3b2f2f")) + # SET THE FILL COLOUR
  theme(legend.title = element_blank()) + # REMOVE THE LEGEND TITLE
  ggtitle("Arabica/Robusta Ratio from countries with Robusta data ") # SET THE TITLE OF THE PLOT

dataset$new_dates <- dataset$grading_date %>% mdy() # CONVERT THE GRADING DATE TO A DATE OBJECT
dataset$score_year <- dataset$new_dates %>% year() # EXTRACT THE YEAR FROM THE GRADING DATE

(
  top_annual_score <- dataset %>% # CREATE A NEW DATAFRAME WITH THE TOP ANNUAL SCORE
    group_by(cupper_points, # GROUP THE DATA BY CUPPER POINTS
             score_year, # GROUP THE DATA BY SCORE YEAR
             country_of_origin) %>% # GROUP THE DATA BY COUNTRY OF ORIGIN
    summarise(max_points = max(total_cup_points)) %>% # SUMMARISE THE DATA BY THE MAXIMUM TOTAL CUP POINTS
    filter(max_points == max(max_points)) %>% # FILTER OUT THE MAXIMUM TOTAL CUP POINTS
    arrange(-max_points) # ARRANGE THE MAXIMUM TOTAL CUP POINTS IN DESCENDING ORDER
)

ggplot(top_annual_score, # FILTER OUT THE NA VALUES
       mapping = aes(x = score_year, # MAPPING THE DATA TO THE PLOT
                     y = max_points, # MAPPING THE DATA TO THE PLOT
                     label = paste0(score_year, "\n", country_of_origin, "\n", max_points), # SET THE LABEL TO THE YEAR, COUNTRY OF ORIGIN AND MAXIMUM TOTAL CUP POINTS
                     color = country_of_origin)) + # SET THE COLOUR TO COUNTRY OF ORIGIN
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  geom_text(position = position_dodge(width = 0.9), # SET THE POSITION OF THE TEXT
            hjust = -0.2, # SET THE HORIZONTAL JUSTIFICATION
            size = 3.5) + # SET THE SIZE OF THE TEXT
  geom_point(size = 5, # SET THE SIZE OF THE POINTS
             alpha = 0.8) + # SET THE ALPHA OF THE POINTS
  theme(legend.position = "none") + # REMOVE THE LEGEND
  facet_wrap(~cupper_points) + # FACET THE PLOT BY CUPPER POINTS
  ggtitle(" Top Scoring Coffees by Year - Faceted on cupper_points ") # SET THE TITLE OF THE PLOT

(arabica_robusta_average_score <- # CREATE A NEW DATAFRAME WITH THE AVG TOTAL CUP POINTS
  dataset %>% # CREATE A NEW DATAFRAME WITH THE COUNTRY OF ORIGIN ATTRIBUTE
    group_by(cupper_points) %>% # GROUP THE DATA BY CUPPER POINTS
    summarise(average_score = mean(total_cup_points), # SUMMARISE THE DATA BY THE AVERAGE TOTAL CUP POINTS
              lower_ci = mean(total_cup_points) - 1.96 * sqrt(var(total_cup_points) / length(total_cup_points)), # SUMMARISE THE DATA BY THE LOWER CONFIDENCE INTERVAL
              upper_ci = mean(total_cup_points) + 1.96 * sqrt(var(total_cup_points) / length(total_cup_points))) # SUMMARISE THE DATA BY THE UPPER CONFIDENCE INTERVAL
)

ggplot(dataset, mapping = aes(x = score_year, y = total_cup_points, group = score_year)) + # MAPPING THE DATA TO THE PLOT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  geom_boxplot(color = "#3b2f2f") + # SET THE COLOUR OF THE BOX PLOT
  coord_flip() + # FLIP THE COORDINATES
  facet_wrap(~cupper_points) + # FACET THE PLOT BY CUPPER POINTS
  geom_hline(data = arabica_robusta_average_score, # PLOT THE AVERAGE SCORE
             mapping = aes(yintercept = average_score), # MAPPING THE DATA TO THE PLOT
             size = 0.5) + # SET THE SIZE OF THE LINE
  geom_hline(data = arabica_robusta_average_score, # PLOT THE LOWER CONFIDENCE INTERVAL
             mapping = aes(yintercept = lower_ci), # MAPPING THE DATA TO THE PLOT
             linetype = "dashed", # SET THE LINE TYPE TO DASHED
             size = 0.5) + # SET THE SIZE OF THE LINE
  geom_hline(data = arabica_robusta_average_score, # PLOT THE UPPER CONFIDENCE INTERVAL
             mapping = aes(yintercept = upper_ci), # MAPPING THE DATA TO THE PLOT
             linetype = "dashed", # SET THE LINE TYPE TO DASHED
             size = 0.5) + # SET THE SIZE OF THE LINE
  ggtitle("Boxplots of Arabica and Robusta Beans from 2010-2018 \n
           with confidence intervals plotted") # SET THE TITLE OF THE PLOT

(
  arabica_aroma <- dataset %>% # CREATE A NEW DATAFRAME WITH THE AROMA ATTRIBUTE
    filter(species == "Arabica") %>% # FILTER OUT THE ARABICA BEANS
    count(species = factor(species), # COUNT THE NUMBER OF ARABICA BEANS
          Aroma = aroma, rating = total_cup_points) %>% # COUNT THE NUMBER OF ARABICA BEANS
    mutate(pct = prop.table(n)) %>% # CALCULATE THE PROPORTION OF ARABICA BEANS
    arrange(-n) %>% # ARRANGE THE NUMBER OF ARABICA BEANS IN DESCENDING ORDER
    tibble() # CONVERT THE DATAFRAME TO A TIBBLE
)

ggplot(arabica_aroma, aes(x = Aroma, y = rating)) + # MAPPING THE DATA TO THE PLOT
  geom_point() + # PLOT THE POINTS
  geom_smooth(method = lm, color = "red", fill = "#69b3a2", se = TRUE) + # PLOT THE LINE OF BEST FIT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  ggtitle("Arabic Coffee Aroma") # SET THE TITLE OF THE PLOT

(
  arabica_flavor <- dataset %>% # CREATE A NEW DATAFRAME WITH THE FLAVOR ATTRIBUTE
    filter(species == "Arabica") %>% # FILTER OUT THE ARABICA BEANS
    count(species = factor(species), # COUNT THE NUMBER OF ARABICA BEANS
          Flavor = flavor, Rating = total_cup_points) %>% # COUNT THE NUMBER OF ARABICA BEANS
    mutate(pct = prop.table(n)) %>% # CALCULATE THE PROPORTION OF ARABICA BEANS
    arrange(-n) %>% # ARRANGE THE NUMBER OF ARABICA BEANS IN DESCENDING ORDER
    tibble() # CONVERT THE DATAFRAME TO A TIBBLE
)

ggplot(arabica_flavor, aes(x = Flavor, y = Rating)) + # MAPPING THE DATA TO THE PLOT
  geom_point() + # PLOT THE POINTS
  geom_smooth(method = lm, color = "red", fill = "#69b3a2", se = TRUE) + # PLOT THE LINE OF BEST FIT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  ggtitle("Arabic coffee Flavor") # SET THE TITLE OF THE PLOT

(
  arabica_aftertaste <- dataset %>% # CREATE A NEW DATAFRAME WITH THE AFTER TASTE ATTRIBUTE
    filter(species == "Arabica") %>% # FILTER OUT THE ARABICA BEANS
    count(species = factor(species), # COUNT THE NUMBER OF ARABICA BEANS
          Aftertaste = aftertaste, Rating = total_cup_points) %>% # COUNT THE NUMBER OF ARABICA BEANS
    mutate(pct = prop.table(n)) %>% # CALCULATE THE PROPORTION OF ARABICA BEANS
    arrange(-n) %>% # ARRANGE THE NUMBER OF ARABICA BEANS IN DESCENDING ORDER
    tibble() # CONVERT THE DATAFRAME TO A TIBBLE
)

ggplot(arabica_aftertaste, aes(x = Aftertaste, y = Rating)) + # MAPPING THE DATA TO THE PLOT
  geom_point() + # PLOT THE POINTS
  geom_smooth(method = lm, color = "red", fill = "#69b3a2", se = TRUE) + # PLOT THE LINE OF BEST FIT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  ggtitle("Arabic coffee Aftertaste") # SET THE TITLE OF THE PLOT

(
  arabica_acidity <- dataset %>% # CREATE A NEW DATAFRAME WITH THE ACIDITY ATTRIBUTE
    filter(species == "Arabica") %>% # FILTER OUT THE ARABICA BEANS
    count(species = factor(species), # COUNT THE NUMBER OF ARABICA BEANS
          Acidity = acidity, Rating = total_cup_points) %>% # COUNT THE NUMBER OF ARABICA BEANS
    mutate(pct = prop.table(n)) %>% # CALCULATE THE PROPORTION OF ARABICA BEANS
    arrange(-n) %>% # ARRANGE THE NUMBER OF ARABICA BEANS IN DESCENDING ORDER
    tibble() # CONVERT THE DATAFRAME TO A TIBBLE
)

ggplot(arabica_acidity, aes(x = Acidity, y = Rating)) + # MAPPING THE DATA TO THE PLOT
  geom_point() + # PLOT THE POINTS
  geom_smooth(method = lm, color = "red", fill = "#69b3a2", se = TRUE) + # PLOT THE LINE OF BEST FIT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  ggtitle("Arabic coffee Acidity") # SET THE TITLE OF THE PLOT

(
  arabica_body <- dataset %>% # CREATE A NEW DATAFRAME WITH THE BODY ATTRIBUTE
    filter(species == "Arabica") %>% # FILTER OUT THE ARABICA BEANS
    count(species = factor(species), # COUNT THE NUMBER OF ARABICA BEANS
          Body = body, Rating = total_cup_points) %>% # COUNT THE NUMBER OF ARABICA BEANS
    mutate(pct = prop.table(n)) %>% # CALCULATE THE PROPORTION OF ARABICA BEANS
    arrange(-n) %>% # ARRANGE THE NUMBER OF ARABICA BEANS IN DESCENDING ORDER
    tibble() # CONVERT THE DATAFRAME TO A TIBBLE
)

ggplot(arabica_body, aes(x = Body, y = Rating)) + # MAPPING THE DATA TO THE PLOT
  geom_point() + # PLOT THE POINTS
  geom_smooth(method = lm, color = "red", fill = "#69b3a2", se = TRUE) + # PLOT THE LINE OF BEST FIT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  ggtitle("Arabic coffee Body") # SET THE TITLE OF THE PLOT

(
  arabica_balance <- dataset %>% # CREATE A NEW DATAFRAME WITH THE BALANCE ATTRIBUTE
    filter(species == "Arabica") %>% # FILTER OUT THE ARABICA BEANS
    count(species = factor(species), # COUNT THE NUMBER OF ARABICA BEANS
          Balance = balance, Rating = total_cup_points) %>% # COUNT THE NUMBER OF ARABICA BEANS
    mutate(pct = prop.table(n)) %>% # CALCULATE THE PROPORTION OF ARABICA BEANS
    arrange(-n) %>% # ARRANGE THE NUMBER OF ARABICA BEANS IN DESCENDING ORDER
    tibble() # CONVERT THE DATAFRAME TO A TIBBLE
)

ggplot(arabica_balance, aes(x = Balance, y = Rating)) + # MAPPING THE DATA TO THE PLOT
  geom_point() + # PLOT THE POINTS
  geom_smooth(method = lm, color = "red", fill = "#69b3a2", se = TRUE) + # PLOT THE LINE OF BEST FIT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  ggtitle("Arabic coffee Balance") # SET THE TITLE OF THE PLOT

(
  arabica_uniformity <- dataset %>% # CREATE A NEW DATAFRAME WITH THE UNIFORMITY ATTRIBUTE
    filter(species == "Arabica") %>% # FILTER OUT THE ARABICA BEANS
    count(species = factor(species), # COUNT THE NUMBER OF ARABICA BEANS
          Uniformity = uniformity, Rating = total_cup_points) %>% # COUNT THE NUMBER OF ARABICA BEANS
    mutate(pct = prop.table(n)) %>% # CALCULATE THE PROPORTION OF ARABICA BEANS
    arrange(-n) %>% # ARRANGE THE NUMBER OF ARABICA BEANS IN DESCENDING ORDER
    tibble() # CONVERT THE DATAFRAME TO A TIBBLE
)

ggplot(arabica_uniformity, aes(x = Uniformity, y = Rating)) + # MAPPING THE DATA TO THE PLOT
  geom_point() + # PLOT THE POINTS
  geom_smooth(method = lm, color = "red", fill = "#69b3a2", se = TRUE) + # PLOT THE LINE OF BEST FIT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  ggtitle("Arabic coffee Uniformity") # SET THE TITLE OF THE PLOT

(
  arabica_clean_cup <- dataset %>% # CREATE A NEW DATAFRAME WITH THE CLEAN CUP ATTRIBUTE
    filter(species == "Arabica") %>% # FILTER OUT THE ARABICA BEANS
    count(species = factor(species), # COUNT THE NUMBER OF ARABICA BEANS
          Clean_cup = clean_cup, Rating = total_cup_points) %>% # COUNT THE NUMBER OF ARABICA BEANS
    mutate(pct = prop.table(n)) %>% # CALCULATE THE PROPORTION OF ARABICA BEANS
    arrange(-n) %>% # ARRANGE THE NUMBER OF ARABICA BEANS IN DESCENDING ORDER
    tibble() # CONVERT THE DATAFRAME TO A TIBBLE
)

ggplot(arabica_clean_cup, aes(x = Clean_cup, y = Rating)) + # MAPPING THE DATA TO THE PLOT
  geom_point() + # PLOT THE POINTS
  geom_smooth(method = lm, color = "red", fill = "#69b3a2", se = TRUE) + # PLOT THE LINE OF BEST FIT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  ggtitle("Arabic coffee Clean Cup") # SET THE TITLE OF THE PLOT

(
  arabica_sweetness <- dataset %>% # CREATE A NEW DATAFRAME WITH THE SWEETNESS ATTRIBUTE
    filter(species == "Arabica") %>% # FILTER OUT THE ARABICA BEANS
    count(species = factor(species), # COUNT THE NUMBER OF ARABICA BEANS
          Sweetness = sweetness, Rating = total_cup_points) %>% # COUNT THE NUMBER OF ARABICA BEANS
    mutate(pct = prop.table(n)) %>% # CALCULATE THE PROPORTION OF ARABICA BEANS
    arrange(-n) %>% # ARRANGE THE NUMBER OF ARABICA BEANS IN DESCENDING ORDER
    tibble() # CONVERT THE DATAFRAME TO A TIBBLE
)

ggplot(arabica_sweetness, aes(x = Sweetness, y = Rating)) + # MAPPING THE DATA TO THE PLOT
  geom_point() + # PLOT THE POINTS
  geom_smooth(method = lm, color = "red", fill = "#69b3a2", se = TRUE) + # PLOT THE LINE OF BEST FIT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  ggtitle("Arabic coffee Sweetness") # SET THE TITLE OF THE PLOT

(
  robusta_aroma <- dataset %>% # CREATE A NEW DATAFRAME WITH THE AROMA ATTRIBUTE
    filter(species == "Robusta") %>% # FILTER OUT THE ROBUSTA BEANS
    count(species = factor(species), # COUNT THE NUMBER OF ROBUSTA BEANS
          Aroma = aroma, rating = total_cup_points) %>% # COUNT THE NUMBER OF ROBUSTA BEANS
    mutate(pct = prop.table(n)) %>% # CALCULATE THE PROPORTION OF ROBUSTA BEANS
    arrange(-n) %>% # ARRANGE THE NUMBER OF ROBUSTA BEANS IN DESCENDING ORDER
    tibble() # CONVERT THE DATAFRAME TO A TIBBLE
)

ggplot(robusta_aroma, aes(x = Aroma, y = rating)) + # MAPPING THE DATA TO THE PLOT
  geom_point() + # PLOT THE POINTS
  geom_smooth(method = lm, color = "red", fill = "#69b3a2", se = TRUE) + # PLOT THE LINE OF BEST FIT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  ggtitle("Robusta coffee Aroma") # SET THE TITLE OF THE PLOT

(
  robusta_flavor <- dataset %>% # CREATE A NEW DATAFRAME WITH THE FLAVOR ATTRIBUTE
    filter(species == "Robusta") %>% # FILTER OUT THE ROBUSTA BEANS
    count(species = factor(species), # COUNT THE NUMBER OF ROBUSTA BEANS
          Flavor = flavor, Rating = total_cup_points) %>% # COUNT THE NUMBER OF ROBUSTA BEANS
    mutate(pct = prop.table(n)) %>% # CALCULATE THE PROPORTION OF ROBUSTA BEANS
    arrange(-n) %>% # ARRANGE THE NUMBER OF ROBUSTA BEANS IN DESCENDING ORDER
    tibble() # CONVERT THE DATAFRAME TO A TIBBLE
)

ggplot(robusta_flavor, aes(x = Flavor, y = Rating)) + # MAPPING THE DATA TO THE PLOT
  geom_point() + # PLOT THE POINTS
  geom_smooth(method = lm, color = "red", fill = "#69b3a2", se = TRUE) + # PLOT THE LINE OF BEST FIT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  ggtitle("Robusta coffee Flavor") # SET THE TITLE OF THE PLOT

(
  robusta_aftertaste <- dataset %>% # CREATE A NEW DATAFRAME WITH THE AFTERTASTE ATTRIBUTE
    filter(species == "Robusta") %>% # FILTER OUT THE ROBUSTA BEANS
    count(species = factor(species), # COUNT THE NUMBER OF ROBUSTA BEANS
          Aftertaste = aftertaste, Rating = total_cup_points) %>% # COUNT THE NUMBER OF ROBUSTA BEANS
    mutate(pct = prop.table(n)) %>% # CALCULATE THE PROPORTION OF ROBUSTA BEANS
    arrange(-n) %>% # ARRANGE THE NUMBER OF ROBUSTA BEANS IN DESCENDING ORDER
    tibble() # CONVERT THE DATAFRAME TO A TIBBLE
)

ggplot(robusta_aftertaste, aes(x = Aftertaste, y = Rating)) + # MAPPING THE DATA TO THE PLOT
  geom_point() + # PLOT THE POINTS
  geom_smooth(method = lm, color = "red", fill = "#69b3a2", se = TRUE) + # PLOT THE LINE OF BEST FIT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  ggtitle("Robusta coffee Aftertaste") # SET THE TITLE OF THE PLOT

(
  robusta_acidity <- dataset %>% # CREATE A NEW DATAFRAME WITH THE ACIDITY ATTRIBUTE
    filter(species == "Robusta") %>% # FILTER OUT THE ROBUSTA BEANS
    count(species = factor(species), # COUNT THE NUMBER OF ROBUSTA BEANS
          Acidity = acidity, Rating = total_cup_points) %>% # COUNT THE NUMBER OF ROBUSTA BEANS
    mutate(pct = prop.table(n)) %>% # CALCULATE THE PROPORTION OF ROBUSTA BEANS
    arrange(-n) %>% # ARRANGE THE NUMBER OF ROBUSTA BEANS IN DESCENDING ORDER
    tibble() # CONVERT THE DATAFRAME TO A TIBBLE
)

ggplot(robusta_acidity, aes(x = Acidity, y = Rating)) + # MAPPING THE DATA TO THE PLOT
  geom_point() + # PLOT THE POINTS
  geom_smooth(method = lm, color = "red", fill = "#69b3a2", se = TRUE) + # PLOT THE LINE OF BEST FIT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  ggtitle("Robusta coffee Acidity") # SET THE TITLE OF THE PLOT

(
  robusta_body <- dataset %>% # CREATE A NEW DATAFRAME WITH THE BODY ATTRIBUTE
    filter(species == "Robusta") %>% # FILTER OUT THE ROBUSTA BEANS
    count(species = factor(species), # COUNT THE NUMBER OF ROBUSTA BEANS
          Body = body, Rating = total_cup_points) %>% # COUNT THE NUMBER OF ROBUSTA BEANS
    mutate(pct = prop.table(n)) %>% # CALCULATE THE PROPORTION OF ROBUSTA BEANS
    arrange(-n) %>% # ARRANGE THE NUMBER OF ROBUSTA BEANS IN DESCENDING ORDER
    tibble() # CONVERT THE DATAFRAME TO A TIBBLE
)

ggplot(robusta_body, aes(x = Body, y = Rating)) + # MAPPING THE DATA TO THE PLOT
  geom_point() + # PLOT THE POINTS
  geom_smooth(method = lm, color = "red", fill = "#69b3a2", se = TRUE) + # PLOT THE LINE OF BEST FIT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  ggtitle("Robusta coffee Body") # SET THE TITLE OF THE PLOT

(
  robusta_balance <- dataset %>% # CREATE A NEW DATAFRAME WITH THE BALANCE ATTRIBUTE
    filter(species == "Robusta") %>% # FILTER OUT THE ROBUSTA BEANS
    count(species = factor(species), # COUNT THE NUMBER OF ROBUSTA BEANS
          Balance = balance, Rating = total_cup_points) %>% # COUNT THE NUMBER OF ROBUSTA BEANS
    mutate(pct = prop.table(n)) %>% # CALCULATE THE PROPORTION OF ROBUSTA BEANS
    arrange(-n) %>% # ARRANGE THE NUMBER OF ROBUSTA BEANS IN DESCENDING ORDER
    tibble() # CONVERT THE DATAFRAME TO A TIBBLE
)

ggplot(robusta_balance, aes(x = Balance, y = Rating)) + # MAPPING THE DATA TO THE PLOT
  geom_point() + # PLOT THE POINTS
  geom_smooth(method = lm, color = "red", fill = "#69b3a2", se = TRUE) + # PLOT THE LINE OF BEST FIT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  ggtitle("Robusta coffee Balance") # SET THE TITLE OF THE PLOT

(
  robusta_uniformity <- dataset %>% # CREATE A NEW DATAFRAME WITH THE UNIFORMITY ATTRIBUTE
    filter(species == "Robusta") %>% # FILTER OUT THE ROBUSTA BEANS
    count(species = factor(species), # COUNT THE NUMBER OF ROBUSTA BEANS
          Uniformity = uniformity, Rating = total_cup_points) %>% # COUNT THE NUMBER OF ROBUSTA BEANS
    mutate(pct = prop.table(n)) %>% # CALCULATE THE PROPORTION OF ROBUSTA BEANS
    arrange(-n) %>% # ARRANGE THE NUMBER OF ROBUSTA BEANS IN DESCENDING ORDER
    tibble() # CONVERT THE DATAFRAME TO A TIBBLE
)

ggplot(robusta_uniformity, aes(x = Uniformity, y = Rating)) + # MAPPING THE DATA TO THE PLOT
  geom_point() + # PLOT THE POINTS
  geom_smooth(method = lm, color = "red", fill = "#69b3a2", se = TRUE) + # PLOT THE LINE OF BEST FIT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  ggtitle("Robusta coffee Uniformity") # SET THE TITLE OF THE PLOT

(
  robusta_clean_cup <- dataset %>% # CREATE A NEW DATAFRAME WITH THE CLEAN CUP ATTRIBUTE
    filter(species == "Robusta") %>% # FILTER OUT THE ROBUSTA BEANS
    count(species = factor(species), # COUNT THE NUMBER OF ROBUSTA BEANS
          Clean_cup = clean_cup, Rating = total_cup_points) %>% # COUNT THE NUMBER OF ROBUSTA BEANS
    mutate(pct = prop.table(n)) %>% # CALCULATE THE PROPORTION OF ROBUSTA BEANS
    arrange(-n) %>% # ARRANGE THE NUMBER OF ROBUSTA BEANS IN DESCENDING ORDER
    tibble() # CONVERT THE DATAFRAME TO A TIBBLE
)

ggplot(robusta_clean_cup, aes(x = Clean_cup, y = Rating)) + # MAPPING THE DATA TO THE PLOT
  geom_point() + # PLOT THE POINTS
  geom_smooth(method = lm, color = "red", fill = "#69b3a2", se = TRUE) + # PLOT THE LINE OF BEST FIT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  ggtitle("Robusta coffee Clean Cup") # SET THE TITLE OF THE PLOT

(
  robusta_sweetness <- dataset %>% # CREATE A NEW DATAFRAME WITH THE SWEETNESS ATTRIBUTE
    filter(species == "Robusta") %>% # FILTER OUT THE ROBUSTA BEANS
    count(species = factor(species), # COUNT THE NUMBER OF ROBUSTA BEANS
          Sweetness = sweetness, Rating = total_cup_points) %>% # COUNT THE NUMBER OF ROBUSTA BEANS
    mutate(pct = prop.table(n)) %>% # CALCULATE THE PROPORTION OF ROBUSTA BEANS
    arrange(-n) %>% # ARRANGE THE NUMBER OF ROBUSTA BEANS IN DESCENDING ORDER
    tibble() # CONVERT THE DATAFRAME TO A TIBBLE
)

ggplot(robusta_sweetness, aes(x = Sweetness, y = Rating)) + # MAPPING THE DATA TO THE PLOT
  geom_point() + # PLOT THE POINTS
  geom_smooth(method = lm, color = "red", fill = "#69b3a2", se = TRUE) + # PLOT THE LINE OF BEST FIT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  ggtitle("Robusta coffee Sweetness") # SET THE TITLE OF THE PLOT

df <- arabica_aroma # CREATE A NEW DATAFRAME WITH THE AROMA ATTRIBUTE
mean_of_aroma <- mean(df$Aroma) # CALCULATE THE MEAN OF THE AROMA ATTRIBUTE
mean_of_aroma # PRINT THE MEAN OF THE AROMA ATTRIBUTE

df <- arabica_flavor # CREATE A NEW DATAFRAME WITH THE FLAVOR ATTRIBUTE
mean_of_flavor <- mean(df$Flavor) # CALCULATE THE MEAN OF THE FLAVOR ATTRIBUTE
mean_of_flavor # PRINT THE MEAN OF THE FLAVOR ATTRIBUTE

df <- arabica_aftertaste # CREATE A NEW DATAFRAME WITH THE AFTERTASTE ATTRIBUTE
mean_of_aftertaste <- mean(df$Aftertaste) # CALCULATE THE MEAN OF THE AFTERTASTE ATTRIBUTE
mean_of_aftertaste # PRINT THE MEAN OF THE AFTERTASTE ATTRIBUTE

df <- arabica_acidity # CREATE A NEW DATAFRAME WITH THE ACIDITY ATTRIBUTE
mean_of_acidity <- mean(df$Acidity) # CALCULATE THE MEAN OF THE ACIDITY ATTRIBUTE
mean_of_acidity # PRINT THE MEAN OF THE ACIDITY ATTRIBUTE

df <- arabica_body # CREATE A NEW DATAFRAME WITH THE BODY ATTRIBUTE
mean_of_body <- mean(df$Body) # CALCULATE THE MEAN OF THE BODY ATTRIBUTE
mean_of_body # PRINT THE MEAN OF THE BODY ATTRIBUTE

df <- arabica_balance # CREATE A NEW DATAFRAME WITH THE BALANCE ATTRIBUTE
mean_of_balance <- mean(df$Balance) # CALCULATE THE MEAN OF THE BALANCE ATTRIBUTE
mean_of_balance # PRINT THE MEAN OF THE BALANCE ATTRIBUTE

df <- arabica_uniformity # CREATE A NEW DATAFRAME WITH THE UNIFORMITY ATTRIBUTE
mean_of_uniformity <- mean(df$Uniformity) # CALCULATE THE MEAN OF THE UNIFORMITY ATTRIBUTE
mean_of_uniformity # PRINT THE MEAN OF THE UNIFORMITY ATTRIBUTE

df <- arabica_clean_cup # CREATE A NEW DATAFRAME WITH THE CLEAN CUP ATTRIBUTE
mean_of_clean_cup <- mean(df$Clean_cup) # CALCULATE THE MEAN OF THE CLEAN CUP ATTRIBUTE
mean_of_clean_cup # PRINT THE MEAN OF THE CLEAN CUP ATTRIBUTE

df <- arabica_sweetness # CREATE A NEW DATAFRAME WITH THE SWEETNESS ATTRIBUTE
mean_of_sweetness <- mean(df$Sweetness) # CALCULATE THE MEAN OF THE SWEETNESS ATTRIBUTE
mean_of_sweetness # PRINT THE MEAN OF THE SWEETNESS ATTRIBUTE

data <- data.frame( # CREATE A DATAFRAME WITH THE MEANS OF THE ATTRIBUTES
  name = c("Aroma", "Flavor", "Aftertaste", "Acidity", "Body", "Balance", "Uniformity", "Clean Cup", "Sweetness"), # SET THE NAMES OF THE ATTRIBUTES
  value = c(mean_of_aroma, mean_of_flavor, mean_of_aftertaste, mean_of_acidity, mean_of_body,
            mean_of_balance, mean_of_uniformity, mean_of_clean_cup, mean_of_sweetness) # SET THE VALUES OF THE ATTRIBUTES
) # END OF DATAFRAME
ggplot(data, aes(x = name, y = value)) + # MAPPING THE DATA TO THE PLOT
  geom_bar(stat = "identity", fill = "#634832") + # PLOT THE BARS
  geom_text(aes(label = signif(value, digits = 3)), nudge_y = 0.5) + # PLOT THE TEXT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  ggtitle("Arabic Coffee") # SET THE TITLE OF THE PLOT

df <- robusta_aroma # CREATE A NEW DATAFRAME WITH THE AROMA ATTRIBUTE
Rmean_of_aroma <- mean(df$Aroma) # CALCULATE THE MEAN OF THE AROMA ATTRIBUTE
Rmean_of_aroma # PRINT THE MEAN OF THE AROMA ATTRIBUTE

df <- robusta_flavor # CREATE A NEW DATAFRAME WITH THE FLAVOR ATTRIBUTE
Rmean_of_flavor <- mean(df$Flavor) # CALCULATE THE MEAN OF THE FLAVOR ATTRIBUTE
Rmean_of_flavor # PRINT THE MEAN OF THE FLAVOR ATTRIBUTE

df <- robusta_aftertaste # CREATE A NEW DATAFRAME WITH THE AFTERTASTE ATTRIBUTE
Rmean_of_aftertaste <- mean(df$Aftertaste) # CALCULATE THE MEAN OF THE AFTERTASTE ATTRIBUTE
Rmean_of_aftertaste # PRINT THE MEAN OF THE AFTERTASTE ATTRIBUTE

df <- robusta_acidity # CREATE A NEW DATAFRAME WITH THE ACIDITY ATTRIBUTE
Rmean_of_acidity <- mean(df$Acidity) # CALCULATE THE MEAN OF THE ACIDITY ATTRIBUTE
Rmean_of_acidity # PRINT THE MEAN OF THE ACIDITY ATTRIBUTE

df <- robusta_body # CREATE A NEW DATAFRAME WITH THE BODY ATTRIBUTE
Rmean_of_body <- mean(df$Body) # CALCULATE THE MEAN OF THE BODY ATTRIBUTE
Rmean_of_body # PRINT THE MEAN OF THE BODY ATTRIBUTE

df <- robusta_balance # CREATE A NEW DATAFRAME WITH THE BALANCE ATTRIBUTE
Rmean_of_balance <- mean(df$Balance) # CALCULATE THE MEAN OF THE BALANCE ATTRIBUTE
Rmean_of_balance # PRINT THE MEAN OF THE BALANCE ATTRIBUTE

df <- robusta_uniformity # CREATE A NEW DATAFRAME WITH THE UNIFORMITY ATTRIBUTE
Rmean_of_uniformity <- mean(df$Uniformity) # CALCULATE THE MEAN OF THE UNIFORMITY ATTRIBUTE
Rmean_of_uniformity # PRINT THE MEAN OF THE UNIFORMITY ATTRIBUTE

df <- robusta_clean_cup # CREATE A NEW DATAFRAME WITH THE CLEAN CUP ATTRIBUTE
Rmean_of_clean_cup <- mean(df$Clean_cup) # CALCULATE THE MEAN OF THE CLEAN CUP ATTRIBUTE
Rmean_of_clean_cup # PRINT THE MEAN OF THE CLEAN CUP ATTRIBUTE

df <- robusta_sweetness # CREATE A NEW DATAFRAME WITH THE SWEETNESS ATTRIBUTE
Rmean_of_sweetness <- mean(df$Sweetness) # CALCULATE THE MEAN OF THE SWEETNESS ATTRIBUTE
Rmean_of_sweetness # PRINT THE MEAN OF THE SWEETNESS ATTRIBUTE

data <- data.frame( # CREATE A DATAFRAME WITH THE MEANS OF THE ATTRIBUTES
  name = c("Aroma", "Flavor", "Aftertaste", "Acidity", "Body", "Balance", "Uniformity", "Clean Cup", "Sweetness"), # SET THE NAMES OF THE ATTRIBUTES
  value = c(Rmean_of_aroma, Rmean_of_flavor, Rmean_of_aftertaste, Rmean_of_acidity, Rmean_of_body,
            Rmean_of_balance, Rmean_of_uniformity, Rmean_of_clean_cup, Rmean_of_sweetness) # SET THE VALUES OF THE ATTRIBUTES
) # END OF DATAFRAME

ggplot(data, aes(x = name, y = value)) + # MAPPING THE DATA TO THE PLOT
  geom_bar(stat = "identity", fill = "#3b2f2f") + # PLOT THE BARS
  geom_text(aes(label = signif(value, digits = 3)), nudge_y = 0.5) + # PLOT THE TEXT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  ggtitle("Robusta Coffee") # SET THE TITLE OF THE PLOT

data_new3 <- dataset[order(dataset$total_cup_points, decreasing = TRUE),] # ORDER THE DATASET BY THE TOTAL CUP POINTS
data_new3 <- data.table(data_new3, key = "owner") # SET THE KEY OF THE DATASET TO THE OWNER ATTRIBUTE
data_new3 <- data_new3[, head(.SD, 3), by = owner] # GET THE TOP 3 OWNERS BY THE TOTAL CUP POINTS
data_new3 # PRINT THE TOP 3 OWNERS BY THE TOTAL CUP POINTS

processing_method_table <- dataset %>% # CREATE A NEW DATAFRAME WITH THE PROCESSING METHOD ATTRIBUTE
  count(processing = factor(processing_method)) %>% # COUNT THE PROCESSING METHOD ATTRIBUTE
  mutate(pct = prop.table(n)) %>% # CALCULATE THE PERCENTAGE OF THE PROCESSING METHOD ATTRIBUTE
  tibble() # CREATE A TIBBLE
ggplot(processing_method_table, mapping = aes(x = processing, y = pct, group = 1, label = scales::percent(pct))) + # MAPPING THE DATA TO THE PLOT
  theme_fivethirtyeight() + # SET THE THEME TO FIVETHIRTYEIGHT
  geom_bar(stat = "identity", # PLOT THE BARS
           fill = c("#634832", "#3b2f2f", "#634832", "#3b2f2f", "#634832", "#3b2f2f")) + # SET THE COLORS OF THE BARS
  geom_text(position = position_dodge(width = 0.9), # PLOT THE TEXT
            vjust = -0.5, # SET THE VERTICAL JUSTIFICATION
            size = 4) + # SET THE SIZE OF THE TEXT
  scale_y_continuous(labels = scales::percent) + # SET THE Y AXIS TO PERCENTAGE
  ggtitle("Processing Method Utilizados ") # SET THE TITLE OF THE PLOT

dataset %>% # CREATE A NEW DATAFRAME WITH THE PROCESSING METHOD ATTRIBUTE
  filter(!is.na(processing_method)) %>% # REMOVE THE NA VALUES
  group_by(processing_method) %>% # GROUP BY THE PROCESSING METHOD ATTRIBUTE
  summarize(points = mean(total_cup_points)) %>% # CALCULATE THE MEAN OF THE TOTAL CUP POINTS
  arrange(desc(points))  # ORDER THE DATASET BY THE TOTAL CUP POINTS

  coffee_lumped <- dataset %>% # CREATE A NEW DATAFRAME WITH THE VARIETY ATTRIBUTE
  filter(!is.na(variety), # REMOVE THE NA VALUES
         total_cup_points > 10) %>% # REMOVE THE OUTLIERS
  mutate(variety = fct_lump(variety, 10), sort = TRUE) # LUMP THE VARIETY ATTRIBUTE

coffee_lumped %>% # CREATE A NEW DATAFRAME WITH THE VARIETY ATTRIBUTE
  ggplot(aes(total_cup_points, fill = variety)) + # MAPPING THE DATA TO THE PLOT
  geom_histogram(binwidth = 2) + # PLOT THE HISTOGRAM
  facet_wrap(~variety, scales = "free_y") + # SET THE FACET WRAP
  theme(legend.position = "none") + # REMOVE THE LEGEND+
  ggtitle("Scores of the different varieties of coffee ")

dataset %>% # CREATE A NEW DATAFRAME WITH THE VARIETY ATTRIBUTE
  filter(!is.na(altitude_mean_meters)) %>% # REMOVE THE NA VALUES
  filter(!is.na(cupper_points)) %>% # REMOVE THE NA VALUES
  filter(altitude_mean_meters < 2600, altitude != 1, total_cup_points > 70) %>% # REMOVE THE OUTLIERS
  filter(altitude_mean_meters > 600) %>% # REMOVE THE OUTLIERS
  mutate(altitude_mean_meters = pmin(altitude_mean_meters, 2600)) %>% # SET THE MAXIMUM VALUE OF THE ALTITUDE MEAN METERS ATTRIBUTE
  ggplot(aes(altitude_mean_meters, total_cup_points)) + # MAPPING THE DATA TO THE PLOT
  geom_point(color = "#da8620") + # PLOT THE POINTS
  geom_smooth(method = lm, se = TRUE, color = "dark blue") + # PLOT THE LINEAR REGRESSION
  ggtitle("Dependency of coffee quality according to altitude ")
################### MACHINE LEARNING ALGORITHM EVALUATION ###################
### PREPARE AND SPLIT DATA INTO TRAIN/TEST SETS ###
dataset <- na.omit(dataset) # REMOVE ALL ROWS WITH A NA VALUE
data_split <- createDataPartition(dataset$cupper_points, p = 0.8, list = FALSE) # CREATE A 80/20 SPLIT OF THE DATA FOR TRAINING/TESTING PURPOSES
test <- dataset[-data_split,] # SET 20% OF DATA AS TEST SET
train <- dataset[data_split,] # SET THE REMAINING 80% OF DATA FOR TRAINING

# ALGORITHMS ASSESSED USING 10-FOLD CROSS VALIDATION. METRIC FOR ASSESSMENT IN THIS EXAMPLE IS ACCURACY.
control <- trainControl(method = "cv", number = 10) # SET THE CONTROL FOR THE TRAINING (10-FOLD CROSS VALIDATION)
metric <- "Rsquared" # SET THE METRIC FOR THE TRAINING (ACCURACY)

####################### TRAIN ##########################
### K-NEAREST NEIGHBORS ###
set.seed(7) # SET THE SEED FOR REPRODUCIBILITY OF THE RESULTS
fit.knn <- train(cupper_points ~ ., data = train, method = "knn", metric = metric, trControl = control) # TRAIN THE MODEL USING THE KNN METHOD (K-NEAREST NEIGHBORS)

### RANDOM FOREST ###
set.seed(7) # SET THE SEED FOR REPRODUCIBILITY OF THE RESULTS
fit.rf <- train(cupper_points ~ ., data = train, method = "rf", metric = metric, trControl = control) # TRAIN THE MODEL USING THE RF METHOD (RANDOM FOREST)

### SUMMARIZE THE RESULTS ###
results <- resamples(list(knn = fit.knn, rf = fit.rf)) # CREATE A LIST OF THE RESULTS OF THE MODELS
summary(results) # SUMMARIZE THE RESULTS
