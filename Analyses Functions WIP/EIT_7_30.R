data <- read.csv("Master's Final8_1.csv")
             


data <- subset(data, UnusableMeds==0)

data <- subset(data, UnusableEKG==0) 

data <- subset(data,II_V==1) #Subjects that failed EQI valIDity check
datafull <- data 
datafull$HRV_Chg1=datafull$Mean_Ln_HRV_1 - datafull$Mean_Ln_HRV_2
datafull$HRV_Chg2=datafull$Mean_Ln_HRV_3 - datafull$Mean_Ln_HRV_2


datafull$RMSSD_Chg1=datafull$RMSSD_1-datafull$RMSSD_2
datafull$RMSSD_Chg2=datafull$RMSSD_3-datafull$RMSSD_2




data <- subset(data,Outlier==0)

data$HRV_Chg1=data$Mean_Ln_HRV_1 - data$Mean_Ln_HRV_2
data$HRV_Chg2=data$Mean_Ln_HRV_3 - data$Mean_Ln_HRV_2


data$RMSSD_Chg1=data$RMSSD_1-data$RMSSD_2
data$RMSSD_Chg2=data$RMSSD_3-data$RMSSD_2

d<- data
d <- subset(data, select=c(ID,Demo_Sex,Age,Caffeine1_YN,TimeofVisit,Mean_Ln_HRV_1:Mean_Ln_HRV_3,RMSSD_1:RMSSD_3,HRV_Chg1:RMSSD_Chg2,TOT_T,SS_B1:SS_TOT,PHQ,K6))





shapiro.test(d$Mean_Ln_HRV_1)
shapiro.test(d$Mean_Ln_HRV_2) 
shapiro.test(d$Mean_Ln_HRV_3)
shapiro.test(d$HRV_Chg1) #Nogood
shapiro.test(d$HRV_Chg2) #nogood
shapiro.test(d$RMSSD_1) #nogood
shapiro.test(d$RMSSD_2) #Nogood
shapiro.test(d$RMSSD_3) #Nogood
shapiro.test(d$RMSSD_Chg1) #nogood
shapiro.test(d$RMSSD_Chg2) #nogood
shapiro.test(d$SS_B1) #nogood
shapiro.test(d$SS_B2)
shapiro.test(d$SS_B3) #nogood
shapiro.test(d$SS_B4)
shapiro.test(d$SS_EXP) 
shapiro.test(d$SS_REA) #nogood
shapiro.test(d$SS_TOT)
shapiro.test(d$TOT_T)


Res1HRV=lm(Mean_Ln_HRV_2 ~ Mean_Ln_HRV_1, data=d)
Res2HRV=lm(Mean_Ln_HRV_3 ~ Mean_Ln_HRV_2, data=d)
library(gvlma)
gvlma(Res1HRV) 
gvlma(Res2HRV) #Nogood

#Transform Mean_HRV
require(car)
#1
p <- powerTransform(d$Mean_Ln_HRV_1) # Box and Cox (1964)

#"bcPower is the Box Cox transformation using the p  calculated above
ZHRV1 <- bcPower(d$Mean_Ln_HRV_1, as.numeric(p$lambda))
d$ZHRV1 <- ZHRV1

#2
p <- powerTransform(d$Mean_Ln_HRV_2)# Box and Cox (1964)
#"bcPower is the Box Cox transformation using the p  calculated above
ZHRV2 <- bcPower(d$Mean_Ln_HRV_2,as.numeric(p$lambda))
d$ZHRV2 <- ZHRV2
#3
p <- powerTransform(d$Mean_Ln_HRV_3)# Box and Cox (1964)
#"bcPower is the Box Cox transformation using the p  calculated above
ZHRV3 <- bcPower(d$Mean_Ln_HRV_3,as.numeric(p$lambda))
d$ZHRV3 <- ZHRV3



#1
p <- powerTransform(d$RMSSD_1) # Box and Cox (1964)

#"bcPower is the Box Cox transformation using the p  calculated above
ZRMSSD1 <- bcPower(d$RMSSD_1, as.numeric(p$lambda))
d$ZRMSSD1 <- ZRMSSD1

#2
p <- powerTransform(d$RMSSD_2)# Box and Cox (1964)
#"bcPower is the Box Cox transformation using the p  calculated above
ZRMSSD2 <- bcPower(d$RMSSD_2,as.numeric(p$lambda))
d$ZRMSSD2 <- ZRMSSD2
#3
p <- powerTransform(d$RMSSD_3)# Box and Cox (1964)
#"bcPower is the Box Cox transformation using the p  calculated above
ZRMSSD3 <- bcPower(d$RMSSD_3,as.numeric(p$lambda))
d$ZRMSSD3 <- ZRMSSD3


#B1
p <- powerTransform(d$SS_B1) # Box and Cox (1964)

#"bcPower is the Box Cox transformation using the p  calculated above
ZSS_B1 <- bcPower(d$SS_B1, as.numeric(p$lambda))
d$ZSS_B1 <- ZSS_B1

#B2
p <- powerTransform(d$SS_B2) # Box and Cox (1964)

#"bcPower is the Box Cox transformation using the p  calculated above
ZSS_B2 <- bcPower(d$SS_B2, as.numeric(p$lambda))
d$ZSS_B2 <- ZSS_B2

#B3
p <- powerTransform(d$SS_B3) # Box and Cox (1964)

#"bcPower is the Box Cox transformation using the p  calculated above
ZSS_B3 <- bcPower(d$SS_B3, as.numeric(p$lambda))
d$ZSS_B3 <- ZSS_B3
#B4
p <- powerTransform(d$SS_B4) # Box and Cox (1964)

#"bcPower is the Box Cox transformation using the p  calculated above
ZSS_B4 <- bcPower(d$SS_B4, as.numeric(p$lambda))
d$ZSS_B4 <- ZSS_B4


#REA
p <- powerTransform(d$SS_REA) # Box and Cox (1964)

#"bcPower is the Box Cox transformation using the p  calculated above
ZSS_REA <- bcPower(d$SS_REA, as.numeric(p$lambda))
d$ZSS_REA <- ZSS_REA

#EXP
p <- powerTransform(d$SS_EXP) # Box and Cox (1964)

#"bcPower is the Box Cox transformation using the p  calculated above
ZSS_EXP <- bcPower(d$SS_EXP, as.numeric(p$lambda))
d$ZSS_EXP <- ZSS_EXP

#TOT
p <- powerTransform(d$SS_TOT) # Box and Cox (1964)

#"bcPower is the Box Cox transformation using the p  calculated above
ZSS_TOT <- bcPower(d$SS_TOT, as.numeric(p$lambda))
d$ZSS_TOT <- ZSS_TOT

#TOT
p <- powerTransform(d$PHQ) # Box and Cox (1964)

#"bcPower is the Box Cox transformation using the p  calculated above
ZPHQ <- bcPower(d$PHQ, as.numeric(p$lambda))
d$ZPHQ <- ZPHQ

#TOT
p <- powerTransform(d$K6) # Box and Cox (1964)

#"bcPower is the Box Cox transformation using the p  calculated above
ZK6 <- bcPower(d$K6, as.numeric(p$lambda))
d$ZK6 <- ZK6



shapiro.test(d$ZHRV1) 
shapiro.test(d$ZHRV2) 
shapiro.test(d$ZHRV3) 
shapiro.test(d$ZRMSSD1) 
shapiro.test(d$ZRMSSD2) 
shapiro.test(d$ZRMSSD3) 
shapiro.test(d$ZSS_B1) #nogood
shapiro.test(d$ZSS_B2) 
shapiro.test(d$ZSS_B3) #nogood
shapiro.test(d$ZSS_B4) 
shapiro.test(d$ZSS_EXP) 
shapiro.test(d$ZSS_REA) 
shapiro.test(d$ZSS_TOT)



Res1HRV=lm(ZHRV2 ~ ZHRV1, data=d)
Res2HRV=lm(ZHRV3 ~ ZHRV2, data=d)
d$Res1HRV= residuals(Res1HRV)
d$Res2HRV= residuals(Res2HRV)
gvlma(Res1HRV) #acceptable
gvlma(Res2HRV) #skewed


Res1RMSSD=lm(ZRMSSD2 ~ ZRMSSD1, data=d)
Res2RMSSD=lm(ZRMSSD3 ~ ZRMSSD2, data=d)
d$Res1RMSSD = residuals(Res1RMSSD)
d$Res2RMSSD = residuals(Res2RMSSD)
gvlma(Res1RMSSD) #assumptions not satisfied
gvlma(Res2RMSSD) #assumptions not satisfied 

shapiro.test(d$Res1HRV) 
shapiro.test(d$Res2HRV)  #nogood
shapiro.test(d$Res1RMSSD) #nogood
shapiro.test(d$Res2RMSSD) #nogood

library(car)
Boxplot(d$Mean_Ln_HRV_1) # 38 99
Boxplot(d$Mean_Ln_HRV_2) # 20 52 99 40
Boxplot(d$Mean_Ln_HRV_3) # 99
Boxplot(d$HRV_Chg1) #1  3 40 52 58
Boxplot(d$HRV_Chg2) #1  3 35 40 52 58
Boxplot(d$RMSSD_1) #3 4 20 70 79
Boxplot(d$RMSSD_2) #4 20 29 53 56 80 92
Boxplot(d$RMSSD_3) #3 56 70 71 79 
Boxplot(d$RMSSD_Chg1) #1  3  4 52 58 70 79 80
Boxplot(d$RMSSD_Chg2) #3 27 52 56 58 70 79
Boxplot(d$ZSS_B1)
Boxplot(d$ZSS_B2)
Boxplot(d$ZSS_B3)
Boxplot(d$ZSS_B4)
Boxplot(d$ZSS_EXP)
Boxplot(d$ZSS_REA)
Boxplot(d$ZSS_TOT)


HRVCorr <-subset(d, select=c(Mean_Ln_HRV_1, HRV_Chg2, HRV_Chg1,SS_B1:SS_TOT,PHQ,K6))
RMSSDCorr <-subset(d, select=c(RMSSD_1,RMSSD_Chg2,RMSSD_Chg1,SS_B1:SS_TOT,PHQ,K6))


library(Hmisc)
library(corrplot)
flattenCorrMatrix <- function(cormat, pmat) {
  ut <- upper.tri(cormat)
  data.frame(
    row = rownames(cormat)[row(cormat)[ut]],
    column = rownames(cormat)[col(cormat)[ut]],
    cor  =(cormat)[ut],
    p = pmat[ut]
  )
}



HRVCorr <- rcorr(as.matrix(HRVCorr), type="spearman") 
flattenCorrMatrix(HRVCorr$r, HRVCorr$P)

# Insignificant correlations are leaved blank
corrplot(HRVCorr$r, type="upper", order="hclust", 
         p.mat = HRVCorr$P, sig.level = 0.05, insig = "blank")


RMSSDCorr <- rcorr(as.matrix(RMSSDCorr), type="spearman") 
flattenCorrMatrix(RMSSDCorr$r, RMSSDCorr$P)
# Insignificant correlations are leaved blank
corrplot(RMSSDCorr$r, type="upper", order="hclust", 
         p.mat = RMSSDCorr$P, sig.level = 0.05, insig = "blank")


#Transformed correlations

ZHRVCorr <-subset(d, select=c(ZHRV1,Res1HRV,Res2HRV,ZSS_B1:ZSS_TOT,PHQ,K6))
ZRMSSDCorr <-subset(d, select=c(ZRMSSD1,Res1RMSSD,Res2RMSSD,ZSS_B1:ZSS_TOT,PHQ,K6))



ZHRVCorr <- rcorr(as.matrix(ZHRVCorr), type="spearman") 
flattenCorrMatrix(ZHRVCorr$r, ZHRVCorr$P)

# Insignificant correlations are leaved blank
corrplot(ZHRVCorr$r, method="ellipse",type="upper", order="hclust", 
         p.mat = ZHRVCorr$P, sig.level = 0.05, insig = "blank")


ZRMSSDCorr <- rcorr(as.matrix(ZRMSSDCorr), type="spearman") 
flattenCorrMatrix(ZRMSSDCorr$r, ZRMSSDCorr$P)
# Insignificant correlations are leaved blank
corrplot(ZRMSSDCorr$r, method="ellipse", type ="upper",order="hclust", 
         p.mat = ZRMSSDCorr$P, sig.level = 0.05, insig = "blank")
corrplot.mixed(ZRMSSDCorr$r, upper="ellipse")


#Bayesian correlation via Emily Butler

#bfCorTest <- function(x,y){
 # rhoNot0 <- scale(x)
  #zy <- scale(y)
#  zData <- data.frame(rhoNot0, zy)
 # bfOut <- lmBF(zy ~ rhoNot0, data=zData)
#  mcmcOut <- posterior(bfOut, iterations=10000)
 # print(summary(mcmcOut[ ,"rhoNot0"]))
  #return(bfOut)
#}
#require(BayesFactor)
#bfCorTest(d$RMSSD_1, d$SS_B3)




#Baseline association Models

#Models HRV

Base1 <- lm(Mean_Ln_HRV_1 ~ SS_B1, data=d) # Percieving Predicting Baseline HRV
summary(Base1)
gvlma(Base1)

Base2 <- lm(Mean_Ln_HRV_1 ~ SS_B3, data=d) # Understanding Predicting Baseline HRV
summary(Base2)
gvlma(Base2)  
      
Base3 <- lm(Mean_Ln_HRV_1 ~ SS_EXP, data=d) # Experiencing Predicting Baseline HRV
summary(Base3)
gvlma(Base3) 
      
Base4 <- lm(Mean_Ln_HRV_1 ~ SS_REA, data=d) # Reasoning Predicting Baseline HRV
summary(Base4)
gvlma(Base4)  
      
      
Base5 <- lm(Mean_Ln_HRV_1 ~ SS_TOT, data=d) # Total Predicting Baseline HRV
summary(Base5)
gvlma(Base5) 

#Check outliers exlude if Cook's distance >.1
cooksd <- cooks.distance(Base1)
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4*mean(cooksd, na.rm=T), col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4*mean(cooksd, na.rm=T),names(cooksd),""), col="red")  # add labels

cooksd <- cooks.distance(Base2)
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4*mean(cooksd, na.rm=T), col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4*mean(cooksd, na.rm=T),names(cooksd),""), col="red")  # add labels

cooksd <- cooks.distance(Base3)
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4*mean(cooksd, na.rm=T), col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4*mean(cooksd, na.rm=T),names(cooksd),""), col="red")  # add labels

cooksd <- cooks.distance(Base4)
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4*mean(cooksd, na.rm=T), col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4*mean(cooksd, na.rm=T),names(cooksd),""), col="red")  # add labels

cooksd <- cooks.distance(Base5)
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4*mean(cooksd, na.rm=T), col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4*mean(cooksd, na.rm=T),names(cooksd),""), col="red")  # add labels


#Rerun with transformed HRV

ZBase1 <- lm(ZHRV1 ~ ZSS_B1, data=d) # Percieving Predicting ZBaseline HRV
summary(ZBase1)
gvlma(ZBase1)


ZBase2 <- lm(ZHRV1 ~ ZSS_B3, data=d) # Understanding Predicting ZBaseline HRV
summary(ZBase2)
gvlma(ZBase2)  

ZBase3 <- lm(ZHRV1 ~ ZSS_EXP, data=d) # Experiencing Predicting ZBaseline HRV
summary(ZBase3)
gvlma(ZBase3) 

ZBase4 <- lm(ZHRV1 ~ ZSS_REA, data=d) # Reasoning Predicting ZBaseline HRV
summary(ZBase4)
gvlma(ZBase4)


ZBase5 <- lm(ZHRV1 ~ ZSS_TOT, data=d) # Total Predicting ZBaseline HRV
summary(ZBase5)
gvlma(ZBase5)


#Check Outliers

cooksd <- cooks.distance(ZBase1)
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4*mean(cooksd, na.rm=T), col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4*mean(cooksd, na.rm=T),names(cooksd),""), col="red")  # add labels

cooksd <- cooks.distance(ZBase2)
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4*mean(cooksd, na.rm=T), col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4*mean(cooksd, na.rm=T),names(cooksd),""), col="red")  # add labels

cooksd <- cooks.distance(ZBase3)
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4*mean(cooksd, na.rm=T), col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4*mean(cooksd, na.rm=T),names(cooksd),""), col="red")  # add labels

cooksd <- cooks.distance(ZBase4)
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4*mean(cooksd, na.rm=T), col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4*mean(cooksd, na.rm=T),names(cooksd),""), col="red")  # add labels

cooksd <- cooks.distance(ZBase5)
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4*mean(cooksd, na.rm=T), col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4*mean(cooksd, na.rm=T),names(cooksd),""), col="red")  # add labels



#Models RMSSD

RBase1 <- lm(RMSSD_1 ~ SS_B1, data=d) # Percieving Predicting RBaseline RMSSD
summary(RBase1)
gvlma(RBase1)

RBase2 <- lm(RMSSD_1 ~ SS_B3, data=d) # Understanding Predicting RBaseline RMSSD
summary(RBase2)
gvlma(RBase2)  

RBase3 <- lm(RMSSD_1 ~ SS_EXP, data=d) # Experiencing Predicting RBaseline RMSSD
summary(RBase3)
gvlma(RBase3) 

RBase4 <- lm(RMSSD_1 ~ SS_REA, data=d) # Reasoning Predicting RBaseline RMSSD
summary(RBase4)
gvlma(RBase4)  


RBase5 <- lm(RMSSD_1 ~ SS_TOT, data=d) # Total Predicting RBaseline RMSSD
summary(RBase5)
gvlma(RBase5) 

#Assumptions not satisfied

#Check outliers
cooksd <- cooks.distance(RBase1)
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4*mean(cooksd, na.rm=T), col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4*mean(cooksd, na.rm=T),names(cooksd),""), col="red")  # add labels

cooksd <- cooks.distance(RBase2)
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4*mean(cooksd, na.rm=T), col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4*mean(cooksd, na.rm=T),names(cooksd),""), col="red")  # add labels

cooksd <- cooks.distance(RBase3)
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4*mean(cooksd, na.rm=T), col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4*mean(cooksd, na.rm=T),names(cooksd),""), col="red")  # add labels

cooksd <- cooks.distance(RBase4)
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4*mean(cooksd, na.rm=T), col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4*mean(cooksd, na.rm=T),names(cooksd),""), col="red")  # add labels

cooksd <- cooks.distance(RBase5)
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4*mean(cooksd, na.rm=T), col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4*mean(cooksd, na.rm=T),names(cooksd),""), col="red")  # add labels



#Rerun with transformed RMSSD

ZRBase1 <- lm(ZRMSSD1 ~ ZSS_B1, data=d) # Percieving Predicting ZRBaseline RMSSD
summary(ZRBase1)
gvlma(ZRBase1)


ZRBase2 <- lm(ZRMSSD1 ~ ZSS_B3, data=d) # Understanding Predicting ZRBaseline RMSSD ***SIG
summary(ZRBase2)
gvlma(ZRBase2)  

ZRBase3 <- lm(ZRMSSD1 ~ ZSS_EXP, data=d) # Experiencing Predicting ZRBaseline RMSSD
summary(ZRBase3)
gvlma(ZRBase3) 

ZRBase4 <- lm(ZRMSSD1 ~ ZSS_REA, data=d) # Reasoning Predicting ZRBaseline RMSSD  ****SIG
summary(ZRBase4)
gvlma(ZRBase4)


ZRBase5 <- lm(ZRMSSD1 ~ ZSS_TOT, data=d) # Total Predicting ZRBaseline RMSSD   ****SIG
summary(ZRBase5)
gvlma(ZRBase5)


#Check outliers
cooksd <- cooks.distance(ZRBase1)
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4*mean(cooksd, na.rm=T), col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4*mean(cooksd, na.rm=T),names(cooksd),""), col="red")  # add labels

cooksd <- cooks.distance(ZRBase2)
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4*mean(cooksd, na.rm=T), col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4*mean(cooksd, na.rm=T),names(cooksd),""), col="red")  # add labels

cooksd <- cooks.distance(ZRBase3)
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4*mean(cooksd, na.rm=T), col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4*mean(cooksd, na.rm=T),names(cooksd),""), col="red")  # add labels

cooksd <- cooks.distance(ZRBase4)
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4*mean(cooksd, na.rm=T), col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4*mean(cooksd, na.rm=T),names(cooksd),""), col="red")  # add labels

cooksd <- cooks.distance(ZRBase5)
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4*mean(cooksd, na.rm=T), col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4*mean(cooksd, na.rm=T),names(cooksd),""), col="red")  # add labels





# Modulation association models

#Repeated measures long format for modulation
dlong <- subset(data, select=c(ID,Demo_Sex,Mean_Ln_HRV_1:Mean_Ln_HRV_3,RMSSD_1:RMSSD_3,SS_B1:SS_TOT,TOT_T))
dlong <- reshape(dlong, varying = list(3:5), direction="long")



library(nlme)
library(predictmeans)

# start with a "compound symmetric" model that only has one covariance (shared across all time points) and one variance (also shared across all times). This is the model assumed by traditional repeated measures ANOVA.
cs <- gls(Mean_Ln_HRV_1 ~ time, correlation=corCompSymm(form= ~1 |ID), na.action=na.omit, method="ML", data=dlong)
summary(cs)

# compare to a "heterogenous compound symmetric" model that holds covariances equal but allows variances to be unique 
hcs <- gls(Mean_Ln_HRV_1 ~ time, correlation=corCompSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=dlong)
summary(hcs)
anova(cs, hcs) #  nonagreement

# compare to an "unstructured" model that allows both the variances and covariances to be anything
unstruct <- gls(Mean_Ln_HRV_1 ~ time, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=dlong)
summary(unstruct)
anova(cs, unstruct) # strongly prefers the unstructured
#CookD(unstruct)
# how about an autocorrelation model?
ar <- gls(Mean_Ln_HRV_1 ~ time, correlation=corAR1(form= ~1 |ID), na.action=na.omit, method="ML", data=dlong)
summary(ar)
anova(unstruct, ar) # it still prefers the unstructured




#Add EI
SS2Main <- gls(Mean_Ln_HRV_1 ~ time +SS_B2, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=dlong)
summary(SS2Main)
anova(SS2Main, unstruct) # prefers unst
#CookD(SS2Main)

SS2Inter <- gls(Mean_Ln_HRV_1 ~ time*SS_B2, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=dlong)
summary(SS2Inter)
anova(SS2Inter, unstruct) # prefers unst

SS4Main <- gls(Mean_Ln_HRV_1 ~ time +SS_B4, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=dlong)
summary(SS4Main)
anova(SS4Main, unstruct) # prefers unst
#CookD(SS4Main)

SS4Inter <- gls(Mean_Ln_HRV_1 ~ time*SS_B4, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=dlong)
summary(SS4Inter)
anova(SS4Inter, unstruct) # prefers unst

SSEXPMain <- gls(Mean_Ln_HRV_1 ~ time +SS_EXP, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=dlong)
summary(SSEXPMain)
anova(SSEXPMain, unstruct) # prefers unst
#CookD(SSEXPMain)

SSEXPInter <- gls(Mean_Ln_HRV_1 ~ time*SS_EXP, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=dlong)
summary(SSEXPInter)
anova(SSEXPInter, unstruct) # prefers

SSREAMain <- gls(Mean_Ln_HRV_1 ~ time +SS_REA, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=dlong)
summary(SSREAMain)
anova(SSREAMain, unstruct) # prefers
#CookD(SSREAMain)

SSREAInter <- gls(Mean_Ln_HRV_1 ~ time*SS_REA, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=dlong)
summary(SSREAInter)
anova(SSREAInter, unstruct) # prefers

SSTOTMain <- gls(Mean_Ln_HRV_1 ~ time +SS_TOT, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=dlong)
summary(SSTOTMain)
anova(SSTOTMain, unstruct) # prefers
#CookD(SSTOTMain)

SSTOTInter <- gls(Mean_Ln_HRV_1 ~ time*SS_TOT, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=dlong)
summary(SSTOTInter)
anova(SSTOTInter, unstruct) # prefers





#Repeated measures long format for modulation RMSSD
rlong <- subset(data, select=c(ID,Demo_Sex,Mean_Ln_HRV_1:Mean_Ln_HRV_3,RMSSD_1:RMSSD_3,SS_B1:SS_TOT,TOT_T))
rlong <- reshape(rlong, varying = list(6:8), direction="long")



# start with a "compound symmetric" model that only has one covariance (shared across all time points) and one variance (also shared across all times). This is the model assumed by traditional repeated measures ANOVA.
cs <- gls(RMSSD_1 ~ time, correlation=corCompSymm(form= ~1 |ID), na.action=na.omit, method="ML", data=rlong)
summary(cs)

# compare to a "heterogenous compound symmetric" model that holds covariances equal but allows variances to be unique 
hcs <- gls(RMSSD_1 ~ time, correlation=corCompSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=rlong)
summary(hcs)
anova(cs, hcs) #  prefers hcs

# compare to an "unstructured" model that allows both the variances and covariances to be anything
unstruct <- gls(RMSSD_1 ~ time, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=rlong)
summary(unstruct)
anova(hcs, unstruct) #  prefers the unstructured
#CookD(unstruct)
# how about an autocorrelation model?
ar <- gls(RMSSD_1 ~ time, correlation=corAR1(form= ~1 |ID), na.action=na.omit, method="ML", data=rlong)
summary(ar)
anova(unstruct, ar) # it still prefers the unstructured


#Add EI
RSS2Main <- gls(RMSSD_1 ~ time +SS_B2, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=rlong)
summary(RSS2Main)
anova(RSS2Main, unstruct) # prefers unst
#CookD(RSS2Main)

RSS2Inter <- gls(RMSSD_1 ~ time*SS_B2, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=rlong)
summary(RSS2Inter)
anova(RSS2Inter, unstruct) # prefers unst

RSS4Main <- gls(RMSSD_1 ~ time +SS_B4, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=rlong)
summary(RSS4Main)
anova(RSS4Main, unstruct) # prefers unst
#CookD(RSS4Main)

RSS4Inter <- gls(RMSSD_1 ~ time*SS_B4, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=rlong)
summary(RSS4Inter)
anova(RSS4Inter, unstruct) # prefers Inter ***nonSIG

RSSEXPMain <- gls(RMSSD_1 ~ time +SS_EXP, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=rlong)
summary(RSSEXPMain)
anova(RSSEXPMain, unstruct) # prefers
#CookD(RSSEXPMain)

RSSEXPInter <- gls(RMSSD_1 ~ time*SS_EXP, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=rlong)
summary(RSSEXPInter)
anova(RSSEXPInter, unstruct) # prefers


RSSREAMain <- gls(RMSSD_1 ~ time +SS_REA, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=rlong)
summary(RSSREAMain)
anova(RSSREAMain, unstruct) # prefers
#CookD(RSSREAMain)

RSSREAInter <- gls(RMSSD_1 ~ time*SS_REA, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=rlong)
summary(RSSREAInter)
anova(RSSREAInter, unstruct) # prefers Inter ***nonSIG

RSSTOTMain <- gls(RMSSD_1 ~ time +SS_TOT, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=rlong)
summary(RSSTOTMain)
anova(RSSTOTMain, unstruct) # prefers
#CookD(RSSTOTMain)

RSSTOTInter <- gls(RMSSD_1 ~ time*SS_TOT, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=rlong)
summary(RSSTOTInter)
anova(RSSTOTInter, unstruct) # prefers Inter ***SIG







#IDentify potential EKG covariates using LASSO
library(glmnet)
library(sjstats)

# Add number of predictors
set.seed(1)
x1 <- d$Demo_Sex
x2 <- d$Age
x3 <- d$Caffeine1_YN
x4 <- d$TimeofVisit  


#Input Matrix
X <- matrix( c(x1, x2, x3, x4), byrow = F, ncol = 4)

#outcome variable HRV
y <- d$Mean_Ln_HRV_1


# different values of alpha return different estimators, alpha = 1 is the lasso.
fit <-glmnet(x = X, y = y, alpha = 1) 
# different values of alpha return different estimators, alpha = 1 is the lasso.
plot(fit, xvar = "lambda", label = TRUE)


#outcome variable RMSSD
y <- d$RMSSD_1


# different values of alpha return different estimators, alpha = 1 is the lasso.
fit <-glmnet(x = X, y = y, alpha = 1) 
# different values of alpha return different estimators, alpha = 1 is the lasso.
plot(fit, xvar = "lambda", label = TRUE)

#Gender overwhelmingly... >8

 # Models with Gender as covariate
GBase1 <- lm(ZHRV1 ~ Demo_Sex+ZSS_B1, data=d) # Percieving Predicting GBaseline HRV
summary(GBase1)
check_assumptions(GBase1,model.column = NULL, as.logical = TRUE)
#histogram of residuals, as well as summary:
resID.st <- rstandard(GBase1) # create an object with the standardized residuals
hist(resID.st, main="Distribution of residuals for Primary Adjusted Analysis",xlab="outcome:change residuals")
summary(resID.st)


GBase2 <- lm(ZHRV1 ~ Demo_Sex+ZSS_B3, data=d) # Understanding Predicting GBaseline HRV
summary(GBase2)
check_assumptions(GBase2,model.column = NULL, as.logical = TRUE)

GBase3 <- lm(ZHRV1 ~ Demo_Sex+ZSS_EXP, data=d) # Experiencing Predicting GBaseline HRV
summary(GBase3)
check_assumptions(GBase3,model.column = NULL, as.logical = TRUE)

GBase4 <- lm(ZHRV1 ~ Demo_Sex+ZSS_REA, data=d) # Reasoning Predicting GBaseline HRV
summary(GBase4)
check_assumptions(GBase4,model.column = NULL, as.logical = TRUE)

GBase5 <- lm(ZHRV1 ~ Demo_Sex+ZSS_TOT, data=d) # Total Predicting GBaseline HRV
summary(GBase5)
check_assumptions(GBase5,model.column = NULL, as.logical = TRUE)

GSS2Inter <- gls(Mean_Ln_HRV_1 ~ Demo_Sex+time*SS_B2, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=dlong)
summary(GSS2Inter)
anova(SS2Inter,GSS2Inter)

GSS4Inter <- gls(Mean_Ln_HRV_1 ~ Demo_Sex+time*SS_B4, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=dlong)
summary(GSS4Inter)
anova(SS4Inter,GSS4Inter)

GSSREAInter <- gls(Mean_Ln_HRV_1 ~ Demo_Sex+time*SS_REA, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=dlong)
summary(GSSREAInter)
anova(SSREAInter,GSSREAInter)

GSSEXPInter <- gls(Mean_Ln_HRV_1 ~ Demo_Sex+time*SS_EXP, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=dlong)
summary(GSSEXPInter)
anova(SSEXPInter,GSSEXPInter)

GSSTOTInter <- gls(Mean_Ln_HRV_1 ~ Demo_Sex+time*SS_TOT, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=dlong)
summary(GSSTOTInter)
anova(SSTOTInter,GSSTOTInter)



#RMSSD with Gender

GRBase1 <- lm(ZRMSSD1 ~ Demo_Sex+ZSS_B1, data=d) # Percieving Predicting GRBaseline HRV
summary(GRBase1)
check_assumptions(GRBase1,model.column = NULL, as.logical = TRUE)
#histogram of residuals, as well as summary:
resID.st <- rstandard(GRBase1) # create an object with the standardized residuals
hist(resID.st, main="Distribution of residuals for Primary Adjusted Analysis",xlab="outcome:change residuals")
summary(resID.st)
anova(ZRBase1, GRBase1)


GRBase2 <- lm(ZRMSSD1 ~ Demo_Sex+ZSS_B3, data=d) # Understanding Predicting GRBaseline HRV
summary(GRBase2)
check_assumptions(GRBase2,model.column = NULL, as.logical = TRUE)
anova(ZRBase2, GRBase2)

GRBase3 <- lm(ZRMSSD1 ~ Demo_Sex+ZSS_EXP, data=d) # Experiencing Predicting GRBaseline HRV
summary(GRBase3)
check_assumptions(GRBase3,model.column = NULL, as.logical = TRUE)
anova(ZRBase3, GRBase3)

GRBase4 <- lm(ZRMSSD1 ~ Demo_Sex+ZSS_REA, data=d) # Reasoning Predicting GRBaseline HRV
summary(GRBase4)
check_assumptions(GRBase4,model.column = NULL, as.logical = TRUE)
anova(ZRBase4, GRBase4)

GRBase5 <- lm(ZRMSSD1 ~ Demo_Sex+ZSS_TOT, data=d) # Total Predicting GRBaseline HRV
summary(GRBase5)
check_assumptions(GRBase5,model.column = NULL, as.logical = TRUE)
anova(ZRBase5, GRBase5)

#Modulation

# start with a "compound symmetric" model that only has one covariance (shared acroZRSS all time points) and one variance (also shared acroZRSS all times). This is the model aZRSSumed by traditional repeated measures ANOVA.
cs <- gls(RMSSD_1 ~ Demo_Sex+time, correlation=corCompSymm(form= ~1 |ID), na.action=na.omit, method="ML", data=rlong)
summary(cs)

# compare to a "heterogenous compound symmetric" model that holds covariances equal but allows variances to be unique 
hcs <- gls(RMSSD_1 ~ Demo_Sex+time, correlation=corCompSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=rlong)
summary(hcs)
anova(cs, hcs) #  prefers hcs

# compare to an "unstructured" model that allows both the variances and covariances to be anything
unstruct <- gls(RMSSD_1 ~ Demo_Sex+time, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=rlong)
summary(unstruct)
anova(hcs, unstruct) # strongly prefers the unstructured

# how about an autocorrelation model?
ar <- gls(RMSSD_1 ~ Demo_Sex+time, correlation=corAR1(form= ~1 |ID), na.action=na.omit, method="ML", data=rlong)
summary(ar)
anova(unstruct, ar) # strongly prefers the unstructured






GRSS2Inter <- gls(RMSSD_1~ Demo_Sex+time*SS_B2, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=rlong)
summary(GRSS2Inter)
anova(RSS2Inter,GRSS2Inter)

GRSS4Inter <- gls(RMSSD_1~ Demo_Sex+time*SS_B4, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=rlong)
summary(GRSS4Inter)
anova(RSS4Inter,GRSS4Inter)

GRSSREAInter <- gls(RMSSD_1~ Demo_Sex+time*SS_REA, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=rlong)
summary(GRSSREAInter)
anova(RSSREAInter,GRSSREAInter)

GRSSEXPInter <- gls(RMSSD_1~ Demo_Sex+time*SS_EXP, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=rlong)
summary(GRSSEXPInter)
anova(RSSEXPInter,GRSSEXPInter)

GRSSTOTInter <- gls(RMSSD_1~ Demo_Sex+time*SS_TOT, correlation=corSymm(form= ~1 |ID), weights=varIdent(form = ~ 1|time), na.action=na.omit, method="ML", data=rlong)
summary(GRSSTOTInter)
anova(RSSTOTInter,GRSSTOTInter)







#BAYESIAN


library(brms)

#Predicting autonomic



e1 <- brm(Mean_Ln_HRV_1 ~ SS_B1+ SS_B2+ SS_B3+ SS_B4+ SS_EXP+ SS_REA+ SS_TOT, data=d,prior <- c(set_prior("normal(14.46, 6.08)", class="Intercept", coef="")), family=gaussian, warmup=500, iter=1000, chains=3)
saveRDS(e1, "e1.rds")# this saves the object that was produced so you don't have to recreate it everytime. The next line reads it back in. 
e1  <- readRDS("e1.rds")
summary(e1, R2=T)
plot(e1)
marginal_effects(e1) 
hist(residuals(e1)) 
qqnorm(residuals(e1)) 


e2 <- brm(HRV_Chg1 ~ SS_B1+ SS_B2+ SS_B3+ SS_B4+ SS_EXP+ SS_REA+ SS_TOT, data=d, family=gaussian, warmup=500, iter=1000, chains=3)
saveRDS(e2, "e2.rds")# this saves the object that was produced so you don't have to recreate it everytime. The next line reads it back in. 
e2  <- readRDS("e2.rds")
summary(e2, R2=T)
plot(e2)
marginal_effects(e2) 
hist(residuals(e2)) 
qqnorm(residuals(e2))

e3 <- brm(HRV_Chg2 ~ SS_B1+ SS_B2+ SS_B3+ SS_B4+ SS_EXP+ SS_REA+ SS_TOT, data=d, family=gaussian, warmup=500, iter=1000, chains=3)
saveRDS(e3, "e3.rds")# this saves the object that was produced so you don't have to recreate it everytime. The next line reads it back in. 
e3  <- readRDS("e3.rds")
summary(e3, R2=T)
plot(e3)
marginal_effects(e3) 
hist(residuals(e3)) 
qqnorm(residuals(e3))

e4 <- brm(RMSSD_1 ~ SS_B1+ SS_B2+ SS_B3+ SS_B4+ SS_EXP+ SS_REA+ SS_TOT ,data=d, family=gaussian, warmup=500, iter=1000, chains=3)
saveRDS(e4, "e4.rds")# this saves the object that was produced so you don't have to recreate it everytime. The next line reads it back in. 
e4  <- readRDS("e4.rds")
summary(e4, R2=T)
plot(e4)
marginal_effects(e4) 
hist(residuals(e4)) 
qqnorm(residuals(e4))


e5 <- brm(RMSSD_Chg1 ~ SS_B1+ SS_B2+ SS_B3+ SS_B4+ SS_EXP+ SS_REA+ SS_TOT, data=d, family=gaussian, warmup=500, iter=1000, chains=3)
saveRDS(e5, "e5.rds")# this saves the object that was produced so you don't have to recreate it everytime. The next line reads it back in. 
e5  <- readRDS("e5.rds")
summary(e5, R2=T)
plot(e5)
marginal_effects(e5) 
hist(residuals(e5)) 
qqnorm(residuals(e5))

e6 <- brm(RMSSD_Chg2 ~ SS_B1+ SS_B2+ SS_B3+ SS_B4+ SS_EXP+ SS_REA+ SS_TOT, data=d, family=gaussian, warmup=500, iter=1000, chains=3)
saveRDS(e6, "e6.rds")# this saves the object that was produced so you don't have to recreate it everytime. The next line reads it back in. 
e6  <- readRDS("e6.rds")
summary(e6, R2=T)
plot(e6)
marginal_effects(e6) 
hist(residuals(e6)) 
qqnorm(residuals(e6))




m1 <- brm(SS_B1 ~ Mean_Ln_HRV_1 +MeanHR_1+PNN50_1+MSD_1+RMSSD_1+Slope_1, data=data, family=gaussian, warmup=500, iter=1000, chains=3)
saveRDS(m1, "m1.rds")# this saves the object that was produced so you don't have to recreate it everytime. The next line reads it back in. 
m1  <- readRDS("m1.rds")
summary(m1, R2=T)
plot(m1)
marginal_effects(m1) 
hist(residuals(m1)) 
qqnorm(residuals(m1))


m2 <- brm(SS_B2 ~ Mean_Ln_HRV_1 +MeanHR_1+PNN50_1+MSD_1+RMSSD_1+Slope_1, data=data, family=gaussian, warmup=500, iter=1000, chains=3)
saveRDS(m2, "m2.rds")# this saves the object that was produced so you don't have to recreate it everytime. The next line reads it back in. 
m2  <- readRDS("m2.rds")
summary(m2, R2=T)
plot(m2)
marginal_effects(m2) 
hist(residuals(m2)) 
qqnorm(residuals(m2))

m3 <- brm(SS_B3 ~ Mean_Ln_HRV_1 +MeanHR_1+PNN50_1+MSD_1+RMSSD_1+Slope_1, data=data, family=gaussian, warmup=500, iter=1000, chains=3)
saveRDS(m3, "m3.rds")# this saves the object that was produced so you don't have to recreate it everytime. The next line reads it back in. 
m3  <- readRDS("m3.rds")
summary(m3, R2=T)
plot(m3)
marginal_effects(m3) 
hist(residuals(m3)) 
qqnorm(residuals(m3))

m4 <- brm(SS_B4 ~ Mean_Ln_HRV_1 +MeanHR_1+PNN50_1+MSD_1+RMSSD_1+Slope_1, data=data, family=gaussian, warmup=500, iter=1000, chains=3)
saveRDS(m4, "m4.rds")# this saves the object that was produced so you don't have to recreate it everytime. The next line reads it back in. 
m4  <- readRDS("m4.rds")
summary(m4, R2=T)
plot(m4)
marginal_effects(m4) 
hist(residuals(m4)) 
qqnorm(residuals(m4))

m5 <- brm(SS_EXP ~ Mean_Ln_HRV_1 +MeanHR_1+PNN50_1+MSD_1+RMSSD_1+Slope_1, data=data, family=gaussian, warmup=500, iter=1000, chains=3)
saveRDS(m5, "m5.rds")# this saves the object that was produced so you don't have to recreate it everytime. The next line reads it back in. 
m5  <- readRDS("m5.rds")
summary(m5, R2=T)
plot(m5)
marginal_effects(m5) 
hist(residuals(m5)) 
qqnorm(residuals(m5))

m6 <- brm(SS_REA ~ Mean_Ln_HRV_1 +MeanHR_1+PNN50_1+MSD_1+RMSSD_1+Slope_1, data=data, family=gaussian, warmup=500, iter=1000, chains=3)
saveRDS(m6, "m6.rds")# this saves the object that was produced so you don't have to recreate it everytime. The next line reads it back in. 
m6  <- readRDS("m6.rds")
summary(m6, R2=T)
plot(m6)
marginal_effects(m6) 
hist(residuals(m6)) 
qqnorm(residuals(m6))

m7 <- brm(SS_TOT ~ Mean_Ln_HRV_1 +MeanHR_1+PNN50_1+MSD_1+RMSSD_1+Slope_1, data=data, family=gaussian, warmup=500, iter=1000, chains=3)
saveRDS(m7, "m7.rds")# this saves the object that was produced so you don't have to recreate it everytime. The next line reads it back in. 
m7  <- readRDS("m7.rds")
summary(m7, R2=T)


plot(m1) # again no evIDence of convergence problems. Looking at the intercept I am reminded that we do have grounds to set a prior for it, since BMI has known limits.
marginal_effects(m1) # best evIDence is for carb and fat (and sexf and ambiv)
hist(residuals(m1)) # check residuals - see that we are tending to underpredict BMI - can see this from the tail of positive residuals 
qqnorm(residuals(m1))


c1 <- brm(SS_B1 ~ HRV_Chg1+HRV_Chg2+RMSSD_Chg1+RMSSD_Chg2, data=d, family=gaussian, warmup=500, iter=1000, chains=3)
saveRDS(c1, "c1.rds")# this saves the object that was produced so you don't have to recreate it everytime. The next line reads it back in. 
c1  <- readRDS("c1.rds")
summary(c1, R2=T)


c2 <- brm(SS_B2 ~ HRV_Chg1+HRV_Chg2+RMSSD_Chg1+RMSSD_Chg2, data=d, family=gaussian, warmup=500, iter=1000, chains=3)
saveRDS(mc, "c2.rds")# this saves the object that was produced so you don't have to recreate it everytime. The next line reads it back in. 
c2  <- readRDS("m2.rds")
summary(c2, R2=T)

c3 <- brm(SS_B3 ~ HRV_Chg1+HRV_Chg2+RMSSD_Chg1+RMSSD_Chg2, data=d, family=gaussian, warmup=500, iter=1000, chains=3)
saveRDS(m3, "c3.rds")# this saves the object that was produced so you don't have to recreate it everytime. The next line reads it back in. 
c3  <- readRDS("c3.rds")
summary(c3, R2=T)

c4 <- brm(SS_B4 ~ HRV_Chg1+HRV_Chg2+RMSSD_Chg1+RMSSD_Chg2, data=d, family=gaussian, warmup=500, iter=1000, chains=3)
saveRDS(c4, "c4.rds")# this saves the object that was produced so you don't have to recreate it everytime. The next line reads it back in. 
c4  <- readRDS("c4.rds")
summary(c4, R2=T) #****RMSSD_Ch2 non overlap

c5 <- brm(SS_EXP ~ HRV_Chg1+HRV_Chg2+RMSSD_Chg1+RMSSD_Chg2, data=d, family=gaussian, warmup=500, iter=1000, chains=3)
saveRDS(c5, "c5.rds")# this saves the object that was produced so you don't have to recreate it everytime. The next line reads it back in. 
c5  <- readRDS("c5.rds")
summary(c5, R2=T)

c6 <- brm(SS_REA ~ HRV_Chg1+HRV_Chg2+RMSSD_Chg1+RMSSD_Chg2, data=d, family=gaussian, warmup=500, iter=1000, chains=3)
saveRDS(c6, "c6.rds")# this saves the object that was produced so you don't have to recreate it everytime. The next line reads it back in. 
c6  <- readRDS("c6.rds")
summary(c6, R2=T) #*****RMSSD_Ch2 non overlap

c7 <- brm(SS_TOT ~ HRV_Chg1+HRV_Chg2+RMSSD_Chg1+RMSSD_Chg2, data=d, family=gaussian, warmup=500, iter=1000, chains=3)
saveRDS(c7, "c7.rds")# this saves the object that was produced so you don't have to recreate it everytime. The next line reads it back in. 
c7  <- readRDS("c7.rds")
summary(c7, R2=T) #*****RMSSD_Chg2 non overlap


#IDentify clusters for group GLMs
library(FactoMineR)

EKG <- subset(datafull, select=c(Mean_Ln_HRV_1, HRV_Chg2, HRV_Chg1,RMSSD_1,RMSSD_Chg1,RMSSD_Chg2))

# PCA on EKG components 
res <- PCA(EKG, ncp=Inf)
res$eig
res <- PCA(EKG, ncp=3) #3components account for >95% of variance

# Hierarchical ascendant clustering
res.hcpc <- HCPC(res, kk=Inf, consol=TRUE)
names(res.hcpc)
res.hcpc$call$t
datafull$EKGClust=res.hcpc$data.clust$clust

library(sjstats)

#Create group representing degree of autonomic tone 
datafull$EKGClust <- factor(datafull$EKGClust, levels=c(1,2,3), labels=c("Low", "Middle","High"))
datafull$EKGClust <- relevel(datafull$EKGClust, ref="Middle")

B1 <- lm(SS_B1~EKGClust, data=datafull)
anova(B1)
summary(B1)
gvlma(B1)

B2 <- lm(SS_B2~EKGClust,data=datafull)
anova(B2)
summary(B2)
gvlma(B2)


B3 <- lm(SS_B3~EKGClust,data=datafull)
anova(B3)
summary(B3)
gvlma(B3)

B4 <- lm(SS_B4~EKGClust,data=datafull)
anova(B4)
summary(B4)
gvlma(B4)

B5 <- lm(SS_EXP~EKGClust,data=datafull)
summary(B5)
gvlma(B5)

B6 <- lm(SS_REA~EKGClust,data=datafull)
anova(B6)
summary(B6)
gvlma(B6)
      
B7 <- lm(SS_EXP~EKGClust,data=datafull)
anova(B7)
summary(B7)
gvlma(B7)


library(glmnet)
# Add number of predictors
set.seed(1)
x1 <- datafull$Demo_Sex
x2 <- datafull$Age
x3 <- datafull$Caffeine1_YN
x4 <- datafull$TimeofVisit  


#Input Matrix
X <- matrix( c(x1, x2, x3, x4), byrow = F, ncol = 4)

#outcome variable HRV
y <- datafull$EKGClust


# different values of alpha return different estimators, alpha = 1 is the lasso.
fit <-glmnet(x = X, y = as.factor(y), intercept=FALSE, alpha = 1) 
# different values of alpha return different estimators, alpha = 1 is the lasso.
plot(fit, xvar = "lambda", label = TRUE)


data <- subset(data, STRAINunsuable==0) 
#Investigate lifetime stress and adversity
set.seed(1)
x1 <- data$PHQ
x2 <- data$K6
x3 <- data$StressCT
x4 <- data$StressTH
x5 <- data$EvntCT
x6 <- data$DiffCT
x7 <- data$EvntTH
x8 <- data$DiffTH



X <- matrix( c(x1, x2, x3, x4,x5,x6,x7,x8), byrow = F, ncol = 8)

#outcome variable HRV
y <- data$Mean_Ln_HRV_1
# different values of alpha return different estimators, alpha = 1 is the lasso.
fit <-glmnet(x = X, y = y,alpha = 1) 
# different values of alpha return different estimators, alpha = 1 is the lasso.
plot(fit, xvar = "lambda", label = TRUE)

#outcome variable HRV
y <- data$HRV_Chg1
# different values of alpha return different estimators, alpha = 1 is the lasso.
fit <-glmnet(x = X, y = y, alpha = 1) 
# different values of alpha return different estimators, alpha = 1 is the lasso.
plot(fit, xvar = "lambda", label = TRUE)

#outcome variable HRV
y <- data$HRV_Chg2
# different values of alpha return different estimators, alpha = 1 is the lasso.
fit <-glmnet(x = X, y = y, alpha = 1) 
# different values of alpha return different estimators, alpha = 1 is the lasso.
plot(fit, xvar = "lambda", label = TRUE)

#outcome variable RMSSD
y <- data$RMSSD_1
# different values of alpha return different estimators, alpha = 1 is the lasso.
fit <-glmnet(x = X, y = y, alpha = 1) 
# different values of alpha return different estimators, alpha = 1 is the lasso.
plot(fit, xvar = "lambda", label = TRUE)

#outcome variable RMSSD
y <- data$RMSSD_Chg1
# different values of alpha return different estimators, alpha = 1 is the lasso.
fit <-glmnet(x = X, y = y, alpha = 1) 
# different values of alpha return different estimators, alpha = 1 is the lasso.
plot(fit, xvar = "lambda", label = TRUE)

#outcome variable RMSSD
y <- data$RMSSD_Chg2
# different values of alpha return different estimators, alpha = 1 is the lasso.
fit <-glmnet(x = X, y = y, alpha = 1) 
# different values of alpha return different estimators, alpha = 1 is the lasso.
plot(fit, xvar = "lambda", label = TRUE)

