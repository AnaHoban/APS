#This code outputs the descriptive statistics for the eyetracking data

library(ggplot2)
library(dplyr)
library(formattable)
library(tidyr)
library(flextable)
library(magrittr)
library(data.table)
library(scales)
library(rlang)
library(gridExtra)
library(glue)

### SETUP ###
ggsave <- function(..., bg = 'white') ggplot2::ggsave(..., bg = bg)


#set path to directory where the report is
path_to_report = "C:/Users/anaho/Desktop/CONTROL_dataviewer/Output/report_control_Sentence_ReadingTime.txt"

#import the data
data = read.delim(path_to_report)

# filtering the eyetracking data
#keeping only correct trials
data <- data[data$PARAPHRASE_ACCURACY == 1, ]

#######################

# rename the IA (Interest Area) IDs and place them in <region> column


# Convert necessary columns to numeric (replace 'ffd_column_name' with actual column names)
numeric_columns <- c("IA_FIRST_FIXATION_DURATION",
                     "IA_FIRST_RUN_DWELL_TIME",
                     "IA_REGRESSION_PATH_DURATION",
                     "IA_DWELL_TIME",
                     "IA_REGRESSION_IN",
                     "IA_REGRESSION_OUT",
                     "IA_SKIP")
# create the summary statistics table

# Replace '.' with NA across the entire data frame
data[data == '.'] <- NA

#convert all the rows to numeric

data[ , numeric_columns] <- lapply(data[ , numeric_columns], as.numeric)


###  DATA CLEANING ###
#remove fixations times not in 80-1200 ms range
data <- data[(data$IA_FIRST_FIXATION_DURATION > 80 & data$IA_FIRST_FIXATION_DURATION < 1200), ]

# trim like they did
# Log-transform and scale the reading times
data$LOG_READING_TIME <- scale(log(data$SENTENCE_RT))

# Function to trim data based on condition
trim_outliers <- function(data, condition_col, value_col) {
  data <- data %>%
    group_by(across(all_of(condition_col))) %>%
    mutate(
      mean_value = mean(get(value_col), na.rm = TRUE),
      sd_value = sd(get(value_col), na.rm = TRUE)
    ) %>%
    filter(
      get(value_col) >= (mean_value - 2 * sd_value),
      get(value_col) <= (mean_value + 2 * sd_value)
    ) %>%
    select(-mean_value, -sd_value) # Remove intermediate columns
  return(data)
}

# Specify the column names for condition and reading time
condition_column <- "condition"  # Replace with the actual column name for condition
reading_time_column <- "LOG_READING_TIME"

# Trim data within each condition
data_trimmed <- trim_outliers(data, condition_column, reading_time_column)

# Check the resulting data
head(data_trimmed)

data <- data_trimmed

#####

# dictionnary to convert between our variable and column's names
measure_columns <- list(
  ffd = "IA_FIRST_FIXATION_DURATION",
  gd = "IA_FIRST_RUN_DWELL_TIME",
  gp = "IA_REGRESSION_PATH_DURATION",
  tt = "IA_DWELL_TIME",
  ri = "IA_REGRESSION_IN",
  ro = "IA_REGRESSION_OUT",
  sk = "IA_SKIP"
)

#now we name the regions that interest us and clean the dataset
# Initialize the new column with NA values
data$Region <- NA

# Assign values based on the combination of sentence_type and IA_ID
#for SRCs
data$Region[data$syntactic_condition == "subject" & data$IA_ID == 2] <- "FN"
data$Region[data$syntactic_condition == "subject" & data$IA_ID == 4] <- "RCV"
data$Region[data$syntactic_condition == "subject" & data$IA_ID == 6] <- "SN"
data$Region[data$syntactic_condition == "subject" & data$IA_ID == 7] <- "MC"

#for ORCs
data$Region[data$syntactic_condition == "object" & data$IA_ID == 2] <- "FN"
data$Region[data$syntactic_condition == "object" & data$IA_ID == 5] <- "RCV"
data$Region[data$syntactic_condition == "object" & data$IA_ID == 4] <- "SN"
data$Region[data$syntactic_condition == "object" & data$IA_ID == 6] <- "MC"

# remove all rows in which there is no fn, rcv, sn, mc
data = data[data$Region %in% c("FN", "RCV", "SN", "MC"), ]


# the table (note that for RI and RO, the data is not continuous, so we compute)
df_summary <- data %>%
  group_by(Region, syntactic_condition, plausibility_condition) %>%
  summarise(
    ffd = paste0(round(mean(get(measure_columns$ffd), na.rm = TRUE), 2), " (", round(sd(get(measure_columns$ffd), na.rm = TRUE), 2), ")"),
    gd = paste0(round(mean(get(measure_columns$gd), na.rm = TRUE), 2), " (", round(sd(get(measure_columns$gd), na.rm = TRUE), 2), ")"),
    gp = paste0(round(mean(get(measure_columns$gp), na.rm = TRUE), 2), " (", round(sd(get(measure_columns$gp), na.rm = TRUE), 2), ")"),
    tt = paste0(round(mean(get(measure_columns$tt), na.rm = TRUE), 2), " (", round(sd(get(measure_columns$tt), na.rm = TRUE), 2), ")"),
    ri_proportion = paste0(round(mean(get(measure_columns$ri) == 1, na.rm = TRUE) * 100, 2), "%"),
    ro_proportion = paste0(round(mean(get(measure_columns$ro) == 1, na.rm = TRUE) * 100, 2), "%"),
    sk_proportion = paste0(round(mean(get(measure_columns$sk) == 1, na.rm = TRUE) * 100, 2), "%"),
  )%>%
  ungroup()%>%
  mutate(
    Combined = paste(Region, syntactic_condition, plausibility_condition, sep = " | ")
  ) %>%
  select(Combined, ffd, gd, gp, tt, ri_proportion, ro_proportion, sk_proportion)

# Use formattable to create the table
formattable(df_summary, list(
  ffd = color_tile("white", "orange"),
  gd = color_tile("white", "orange"),
  gp = color_tile("white", "orange"),
  tt = color_tile("white", "orange"),
  ri_proportion = color_tile("white", "orange"),
  ro_proportion = color_tile("white", "orange"),
  sk_proportion = color_tile("white", "orange")
))



##################################################3
# plot 

# Filter the data for plotting
data_for_plot <- data%>%
  mutate(condition = case_when(
    syntactic_condition == "subject" & plausibility_condition == "plausible" ~ 1,
    syntactic_condition == "subject" & plausibility_condition == "implausible" ~ 2,
    syntactic_condition == "object" & plausibility_condition == "plausible" ~ 3,
    syntactic_condition == "object" & plausibility_condition == "implausible" ~ 4,
    TRUE ~ NA_integer_  # Use NA for any rows that don't match the conditions
  ))


for(col in unique(head(numeric_columns,4))) {
  
  # Create the plot
  plot = ggplot(data_for_plot, aes_string(x = "factor(condition)", y = col)) +
    geom_boxplot() +
    facet_wrap(~Region) + 
    labs(x = "condition",y = col, title = col) +
    theme_minimal()
  print(plot)
  
  #save the plot
  # save the plot
  ggsave(plot, 
         filename = glue("C:/Users/anaho/Desktop/research/Language/APS/analysis/Code/Eyetracking/control_{col}.png"),
         device = "png",
         height = 6, width = 5, units = "in")
}

#regressions and skipping variables

prop_cols<- tail(numeric_columns, 3) 

proportion_data <- data_for_plot %>%
  group_by(condition, speech_condition, Region) %>%
  summarise(across(all_of(prop_cols), ~ mean(.x, na.rm = TRUE), .names = "{col}")) %>%
  ungroup()



for(col in unique(prop_cols)) {
  # Create the plot
  plot <- ggplot(proportion_data, aes_string(x = "factor(condition)", y = col, fill = "speech_condition")) +
    geom_bar(stat = "identity", position = "dodge") +
    facet_wrap(~Region) + 
    labs(x = "Condition", y = "Proportion of 1s", fill = "Speaker", title = col) +
    theme_minimal()
  
  # Print the plot
  print(plot)
  
  # save the plot
  ggsave(plot, 
         filename = glue("C:/Users/anaho/Desktop/research/Language/APS/analysis/Code/Eyetracking/control_{col}.png"),
         device = "png",
         height = 6, width = 5, units = "in")
}


#save the proportion_data table
write.csv(proportion_data,"C:/Users/anaho/Desktop/research/Language/APS/analysis/Code/Eyetracking/control_eyetracking_table.csv", row.names = FALSE)





