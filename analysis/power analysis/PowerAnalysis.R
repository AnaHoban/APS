library(simr) 
library(lme4)
library(lmerTest)
library(ggplot2)
library(emmeans)

compute_d <- function(mean_diff, VarIntercet_part, VarIntercet_item, Var_residual, VarSlope_item = 0, VarSlope_part = 0){
  return(mean/sqrt( VarIntercet_part + VarSlope_part + VarIntercet_item + VarSlope_item + Var_residual))
}

#compute_d(?,0.07741,0.45042,0.45983 )

#i don't think we can use this one, because i could make only one dep var vary at the time


#online data
french_control = read.csv("C:/Users/anaho/Desktop/research/Language/APS/analysis/Data/CORR_clean_french_online_silentData_formatted.csv", fileEncoding='latin1')
french_aps = read.csv("C:/Users/anaho/Desktop/research/Language/APS/analysis/Data/CORR_clean_french_online_apsData_formatted.csv", fileEncoding='latin1')
columns = c("Session_Name_", "SENTENCE_RT", "group",'Item','syntactic_condition', 'plausibility_condition')
french_all =  rbind(french_control[,columns],french_aps[,columns])


#log and scale data
french_all$log_time = scale(log10(as.numeric(french_all$SENTENCE_RT)))

#GLM for reading time
model = lmer(log_time~ group + syntactic_condition + plausibility_condition + (1|Session_Name_) + (1|Item), data = french_all)


power_sim_x1 = powerSim(model, fixed("syntactic_condition + plausibility_condition + group","t"),nsim=500)

print(power_sim_x1)

power = powerCurve(fit, along = 'Item', nsim=10)


plot(power)


############

set.seed(123)

# Convert variables to factors if necessary
french_all$group <- factor(french_all$group)
french_all$syntactic_condition <- factor(french_all$syntactic_condition)
french_all$plausibility_condition <- factor(french_all$plausibility_condition)
french_all$Session_Name_ <- factor(french_all$Session_Name_)
french_all$Item <- factor(french_all$Item)



model <- lmer(SENTENCE_RT ~ group * syntactic_condition * plausibility_condition + 
                (1 | Session_Name_) + (1 | Item), data = french_all)
summary(model)



# Power analysis for the effect of group
power_sim <- powerSim(model, fixed("groupcontrol", "t"), nsim = 20)
print(power_sim)

#power curve
power_curve <- powerCurve(model, along = "Session_Name_", fixed("syntactic_condition", "t"), nsim = 100)
plot(power_curve)


#plotting
ggplot(french_all, aes(x = group, y = SENTENCE_RT, color = group)) + 
  geom_boxplot() + 
  facet_grid(syntactic_condition ~ plausibility_condition)


#to try: extend the model

# Extend the model to increase sample size
extended_model <- extend(model, along = "Session_Name_", n = 30)  # e.g., 100 participants
power_sim_extended <- powerSim(extended_model, fixed("groupcontrol", "t"), nsim = 100)
print(power_sim_extended)



#in order to 
effect sizes list and odds ratio for response accuracy (log the ratios)

in loop:

change the ef_s in model using modify 

powerSim

keep result
end loop

plot
