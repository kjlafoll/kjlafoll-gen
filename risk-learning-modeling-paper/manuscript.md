#Latent factors of risk behavior predict the propensity for model-based control

*Kyle J. LaFollette*<sup>1,2</sup>, *Brieann C. Satterfield*<sup>1</sup>, *Michael P. Lazar*<sup>1</sup>, *William D. S. Killgore*<sup>1</sup>

<sup>1</sup> *Department of Psychiatry, College of Medicine, University of Arizona*
<sup>2</sup> *Department of Psychiatry, School of Medicine, Stanford University*

#Abstract

Model-based control, and consequentially model-based learning, is liable to individual differences in risk perception and optimization, yet there is little known about the computational substrates of risk behavior and their association with learning. Here, we propose a number of relationships between distinct latent factors of risk behavior and the propensity for model-based control, and further argue that objective, environmental factors moderate these relationships. We formalize our hypotheses using observable performance indices, and two computational models of risk behavior and reinforcement-learning. These models formulate how individual differences in various latent factors, such as learning-rate and stochasticity of choice, explain variance in risky decision-making, learning strategies, and their intersection. We show that a number of latent factors of risk behavior are associated with the propensity for model-based control, and that these associations are dependent on high versus low-risk contextual factors. These findings suggest that model-based learners perceive more accurate representations of situational risk, and that the rate at which they update their expectations of risk is situationally dependent. Further, we find that model-based learners are more risk-tolerant and choose more stochastically under high-risk conditions than low-risk conditions. Together, our robust analyses support a profile of model-based learning that is influenced by individual differences in latent factors of risk behavior. The profile lends itself to the future investigation of model-based learning in clinical groups such as addiction disorders, which have previously neglected the concurrent assessment of both the computational substrates of model-based learning and risky decision-making.

 
#1 | Introduction

##1.1 | Background

Most choices in life are best guided by learning from the context of past experience. Nonetheless, the extent to which decision-makers rely on context varies. We can make choices habitually, blind to the contingencies that interleave our actions, or we can learn these contingencies and plan our actions deliberately. Classic theoretical accounts of decision-making conceptualize these approaches as two systems, fast and slow, respectively (Sloman, 1996; Stanovich & West, 2000; Kahneman, 2003). Importantly, humans exploit both systems when learning. For example, when playing a game of chess, players rely on intuitive judgments to quickly compile a list of probable and effective moves. Players can then critically examine each of their compiled options. Repetition of intuitive pooling and critical analysis then improves the player’s heuristics for compiling options. Taken together, it is apparent that chess players, and humans in general, learn how to make effective choices by thinking both fast and slow. Recent efforts in computer science and artificial intelligence have aimed to model human learning using reinforcement-learning, a computational framework for representing value-guided decision-making. Reinforcement-learning formalizes these two systems in the form of model-free and model-based strategies (Daw, Niv and Dayan, 2005; Daw et al., 2011). Model-free strategy is both cognitively and computationally inexpensive, albeit to the detriment of accuracy, whereas model-based strategy is more demanding and precise. Accuracy, precision, and recall are all evaluator methods in comparing reinforcement-learning models, and all have analogues for human learning and performance.

Accuracy, however, is dependent on learners’ limited capacities to expend cognitive resources (Smittenaar et al., 2013; Schad et al., 2014). Extraneous factors in a learning environment oftentimes exacerbate these limitations. For example, increased cognitive load, from manipulatives such as acute stress or greater cognitive demands, has been shown to pivot cognitive control from model-based to model-free (De Neys, 2006; Otto et al., 2013). Along these lines, one would expect model-based control to flourish in a relaxed environment. That said, even in an environment where load is not significantly elevated, individual trait-like differences in anxiety and perception can impose differential demands. Factors such as impulsivity (Hogarth, Chase, and Baess, 2012; Deserno et al., 2015) and addiction vulnerability (Sebold et al., 2014; Reiter et al., 2016; Groman et al., 2019) have been found to introduce individual variability in the employment of model-based and model-free strategies. These findings suggest that individual differences in risk perception and risk behavior can modulate our propensity for model-based over model-free control. Indeed, a plethora of studies have linked risk-related phenomena to these dual processes (Slovic et al., 2004; Wang, 2006; Guo, Trueblood & Diederich, 2017), and some have gone further to develop mathematical models that account for their employment under risk (Mukherjee, 2010; Loewenstein et al., 2015; Diederich and Trueblood, 2018). However, learning is iterative, and to our knowledge, efforts to explore these links have been largely restricted to incidental decisions. Few studies have attempted to separate the computational substrates of risk behavior and explore their relationships with sequential decision-making. 

In the present study, we explored the relationships between the computational substrates of model-based and model-free learning and those of risky sequential decision-making. We focused on four aspects of sequential risk behavior: prior beliefs of risk, updating-rate, risk tolerance, and stochasticity. To our knowledge, none of these factors have been studied in the context of model-based learning. Participants completed two separate tasks, the Two-Step task (Daw et al., 2011) designed to quantify their propensity for model-based over model-free strategy, and the Balloon Analogue Risk Task (Lejuez et al., 2002) to quantify these four factors of risk behavior. To further elucidate the potential effect of individual differences in risk behavior, we assessed these factors in both objectively high-risk and low-risk choice environments.

We hypothesized that individuals who perceive lesser risk at the outset of task performance, and who have lesser tolerance for risk under low-risk conditions, would have a greater propensity for model-based learning. Conversely, we hypothesized that the perception of greater risk at the outset of performance and greater risk tolerance under high-risk conditions would be associated with model-based learning. We reason that these hypothesized relationships would reflect an understanding of the risk associated with decision-making in model-based learners. In support of this, Wyckmans et al. recently determined that problem gamblers have impaired model-based learning in comparison to healthy counterparts (2019 PREPRINT). This dissociation could not be explained by differences in mood, impulsivity, or stress. On the other hand, Lorains and colleagues assessed problem gamblers with an Iowa Gambling Task and Loss Aversion Task and found performance detriments solely in non-strategic gamblers (e.g. lottery, slot machines) (2014). While these findings are specific to problem gamblers, decreased baseline risk perception and increased tolerance could explain a delineation in these dual processes and generalize to the larger population. On the other hand, it is possible that the need for greater certainty of choice outcomes is more strongly predictive of the propensity for model-based learning. Should model-based strategies be employed as a means to avoid uncertainty, it follows that high risk-aversion might transcend contextual factors and be associated with model-based strategy.

Secondly, we hypothesized that individuals with slower updating-rates and greater deterministic choice behavior under low-risk conditions would have a greater propensity for model-based learning. Conversely, we hypothesized that faster updating-rates and greater stochastic choice behavior would befit model-based learners in high-risk conditions. Increased learning-rates have been associated with model-based strategy use in low volatility, high-noise situations (Simon and Daw, 2011). A greater tendency for exploratory decisions has been associated with greater model-free influences on choice behavior (da Silva and Hare, 2019 PREPRINT). While these findings concern learning and exploration in the context of the very same task used to infer model-based propensity, we expect these relationships to persist when the risk parameters are measured in a separate risky decision-making task, specifically under conditions of low-risk. Furthermore, we reason that these hypothesized relationships will invert when measured under conditions of high-risk, where volatility is increased and exploration is more penalized.

To test these hypotheses, we fit hierarchical Bayesian models to participant choice data and used Markov Chain Monte Carlo and the No-U-Turn sampler in PyStan (Stan Development Team, 2018) to infer posterior distributions for each model’s parameters. The posteriors of these parameters were then subjected to mixed-effects logistic regression models to test our hypotheses. Additional analyses included simple linear regression models to test associations between parameter pairs.

##1.2 | Objectives

In the present study, we investigated the association between multiple aspects of risk-taking behavior and the tendency to utilize model-based over model-free learning strategies. To elucidate this relationship, we compared performance on the Balloon Analogue Risk Task, or BART, a well-validated measure of risk-taking behavior (Lejuez et al., 2002), and a two-stage reinforcement learning decision task used to dissociate model-based from model-free strategies (Daw et al., 2011). 

#2 | Method

##2.1 | Sample

120 healthy adults (62 F, 21.6 ± 3 years of age) volunteered to participate in this study. All individuals were phone screened and excluded from experimentation on the basis of the following criteria: any history of psychiatric or neurological disorder, history of concussions or traumatic brain injury resulting in loss of consciousness for more than 30 minutes, self-report of cognitive impairment, self-report of any major or chronic medical condition, and treatment with any prescription or over-the-counter medications. Written, informed consent was obtained prior to participation, and compensation was awarded at a fixed amount upon completion and debrief. All participants were compensated $100 irrespective to performance. This study was approved by the University of Arizona’s Institutional Review Board and the USAMRMC Human Research Protection Office.

27 participants were excluded from analyses on the basis of misunderstanding task goals or low reward motivation, leaving a sample size of 93 participants for analysis. Specific exclusionary criteria are described in section 2.3.1.

##2.2 | Procedure

###2.2.1 | General Procedure

After providing informed consent, subjects participated in the study over the course of two separate visits. In the first visit, subjects completed an intake questionnaire to collect basic demographic information. On the second visit, subjects participated in the Two Step task and the BART. The BART task was administered through the Psychology Experiment Building Language (PEBL) test battery (Mueller, 2012). Data reported hereto are a subset of a larger experiment including other aspects of performance under risk and stress.

###2.2.2 | The Two-Step Sequential Reinforcement Learning Task

The Two-Step task, as designed by Daw and colleagues (2011), dissociates model-free from model-based learning strategies. On each trial, subjects choose between two spaceships (Fig. 1A). Each of these first-stage options are linked to two second-stage states with an unknown, but stable transition probability. More specifically, each first-stage option is commonly (70% transition probability) associated with a specific second-stage state (the ‘common’ state) and is rarely (30% transition probability) associated with the other second-stage state (the ‘rare’ state). Subjects are explicitly instructed that this unknown transition structure would remain stable across all trials. Each second-stage state, a red and a purple planet, contains two second-stage choice options, two red or two purple aliens. The subject chooses one of these two presented aliens with the goal of being awarded ‘moon rocks’. The probability of each aliens awarding ‘moon rocks’ adjusts on a trail-by-trial basis by independently drifting Gaussian random walks (SD = 0.025), shifting between 0.2 and 0.8. These dynamic reward probabilities at the second-stage serve to necessitate exploration and encourage continued learning throughout the task. Subjects were instructed to maximize their earnings and that they would receive a cash bonus commensurate to their performance at the conclusion of the experiment.

Each subject completed 200 experimental trials across four blocks. Stage options were presented for a maximum 3000ms, followed by 1000ms animations (i.e., the selected spaceship moving to forward, the selected alien yielding a reward), and 1000ms of feedback. Trials were separated by 1000ms intertrial intervals.

Identifying model-based and model-free learning strategies is accomplished by interpreting first-stage stay behavior as a function of both previous trial reward and transition rarity. For example, a subject who employs more model-based strategies will use a cognitive model of both outcomes and transitions to inform actions, and as such would likely repeat a first-stage choice that led to an expected (via a common path) reward, but not a first-stage choice to led to an unexpected (via a rare path) reward. Conversely, a subject who employs more model-free strategies simply repeats previously rewarded first-stage choices, regardless of transition probability. Thus, extent that model-based learning affects choice behavior is measured by the interactive effect of reward and transition type on stay probability and the extent that model-free learning affects choice is measured by the main effect of reward on stay probability (Fig. 1B).

###2.2.3 | The Balloon Analogue Risk Task (BART)

The Balloon Analogue Risk Task (BART) is a measure of risk taking behavior. On each trial, subjects are presented with the image of a balloon that holds some monetary value (Fig. 2). The value of each balloon is small upon presentation, but should the subject be willing to take a risk, they can ‘pump’ the balloon and inflate its value. However, should the balloon pop, its value becomes null and the subject forfeits their earnings. Alternatively, the subject can choose to ‘cash out’ at any time and secure the balloons current value. A new trial begins when the balloon bursts or the subject cashes out. The probability that a balloon will burst, P_burst, is defined as:

P_(burst,i)=  1/(x-i)  ,such that x>0

where i is the current number of pumps and x is the maximum number of pumps allowed before explosion. Following Lejuez and colleagues original task design (2002), we ascribed three distinct values of x to three different balloon types: orange balloons where x=8; yellow balloons where x=32, and blue balloons where x=128. Subjects were not made aware of any burst probabilities, nor were they informed that probabilities varied across the different colored balloons. To minimize learning effects, we first presented subjects with 30 trials of mixed balloon types. Thereafter, we presented three blocks of 20 trials each, with one color exclusively allocated to each block. Blue, low-risk balloons were presented first, followed by yellow, moderate-risk balloons, and finally orange, high-risk balloons. Recorded performance metrics included the total number of attempted pumps, balloon type, and explosion status.

##2.3 | Data Analysis – Two Step Task

###2.3.1 | Two Step Stage 1 Repetition Probabilities

Two Step task learning strategies were ascertained by analyzing first-stage choice behavior (stay vs. switch) as a function of previous reward (rewarded vs. unrewarded) and previous transition rarity (common vs. rare). An influence of model-free strategy is indicated by a main effect or previous reward, whereas an influence of model-based strategy is indicated by an interaction effect between previous reward and previous transition rarity. Prior studies have consistently found a mixture of both effects in healthy adult performance, suggesting that both model-based and model-free strategies influence first-stage choice in concert. We modeled first-stage choice using a generalized linear mixed-effect logistic regression analysis. Predictors included dummy variables (coded as -1/1) identifying whether the previous trial was rewarded and whether the previous transition was common or rare, and their interaction term. Additional covariates and their interactions with all aforementioned terms were included in models integrating Two Step and BART data. Random effects were taken for all within-subject predictors (Barr et al., 2013).

Firth’s penalized likelihood approach was implemented using the logistf package in R, to account for separation and ensure that all regression parameter estimates were finite (Heinze et al., 2018). These bias-adjusted estimates were necessary to estimate regression coefficients from subjects who exhibited rigid choice behavior under specific event conditions (i.e. stayed on all or nearly all trials in which they were previously rewarded and the previous transition was common). Task comparison analyses replicated these models with the addition of independent covariates. All analyses of behavioral data were conducted using R 3.4 (R Core Team, 2017).

The first 9 trials of each subject’s data were excluded from analyses, as well as any trials in which subjects failed to make a selection at either the first or second stage. 27 subjects who did not have at least 5% more stay decisions on previously rewarded trials with common trials than previously unrewarded trials with common transitions were excluded altogether from analyses, on the basis that such behavior is suggestive of misunderstood task goals or low reward motivation.

###2.3.2 | Two Step Computational Modeling – Model Fitting

To better characterize trial-by-trial choice as a function of a subjects’ entire preceding histories of rewards and transition states, we fit a hybrid reinforcement learning model to subject data, as described by Otto and colleagues (2013). This model is a hybrid of the temporal-difference SARSA(λ) model-free algorithm (Rummery & Niranjan, 1994), which retrospectively updates expected values from prediction errors solely based on reward, and a model-based algorithm, which prospectively informs future first-stage values using the product of second-stage reward and experienced transition probability. Non-pooled, hierarchical models were used to generate individual posterior parameter estimates. Estimates were made using Hamiltonian Markov Chain Monte Carlo simulation in Stan 2.17, interfaced through the PyStan Python package. For each subject, we obtained 50,000 iterative samples across 5 chains (5,000 warmup samples per chain). Chain convergence was indicated by R ̂  ≈1.0.

We used a posteriori estimation to fit 7 free parameters from the hybrid model to subject data. Three of these free parameters originate from the softmax decision rule for calculating the probability of choosing action a at stage i on trial t over all other actions a’:

P(a_(i,t)=a│s_(i,t) )=  (exp⁡(β_i (Q_net (s_(i,t),a)+ ρ ∙rep(a))))/(∑_a'▒〖exp⁡(β_i (Q_net (s_(i,t),〗 a')+ ρ ∙rep(a'))))

where the inverse temperature parameter βi determines the stochasticity of choice at each stage. As there are two stages in the two-step task, β1 denotes stochasticity at the first stage, and β2 at the second. For any inverse temperature βi, as βi → ∞, the probability of choosing a with the greatest expected Q value approaches 1. As βi → 0, choice becomes purely stochastic. The parameter ρ, a measure of first-stage perseverance, scales the indicator variable rep(a), a function of first-stage choice defined as:

rep(a)={ ■(1 if a | s_(i,t-1)@0 if a^' | s_(i,t-1) )

The tendency to perseverate on the prior first-stage action, inconsiderate to action yields, increases where ρ > 0, whereas switching increases where ρ < 0.

###2.3.3 | Two Step Computational Modeling – Model-Free Algorithm

The SARSA(λ) algorithm introduced three additional parameters to the hybrid model. This algorithm updates expected Q values for each state-action pair according to the following delta rule: 

Q_MF (s_(i,t),a_(i,t) )= Q_MF (s_(i,t),a_(i,t) )+ α_i δ_(i,t) e_(i,t) (s_(i,t),a_(i,t))

where

δ_(i,t)=r_(i,t)+ Q_MF (s_(i+1,t),a_(i+1,t) )- Q_MF (s_(i,t),a_(i,t))

is the reward prediction error (RPE), αi are the learning-rate parameters for stage i (which describe how drastically expected values change in response to first-stage, α1, and second-stage, α2, prediction errors), and e_(i,t) (s_(i,t),a_(i,t)) is the eligibility trace that is equal to 0 at the start of each trial and updated such that

e_(i,t) (s_(i,t),a_(i,t) )= e_(i-1,t) (s_(i,t),a_(i,t) )+1

Whereas first-stage RPEs are driven solely by second-stage value (as r_(1,t)=0), second-stage RPEs are modulated by both an eligibility trace decay-rate and reward r_(2,t). This eligibility trace decays exponentially over time, where at the first-stage, e_(1,t)=1, and at the second-stage, e_(2,t)= λe_(1,t). The free parameter λ down-weights second-stage RPEs from trial t-1 to update first-stage expected values on trial t (Sutton & Barto, 1998). Thus, if λ = 0 (standard temporal difference learning), only the current state is eligible for updating. If λ = 1 (Full Monte Carlo Learning), values at all historically visited states are updated. 

###2.3.4 | Two Step Computational Modeling – Model-Based Algorithm

The model-based algorithm introduces no additional parameters but is an essential component for estimating Q-values in the hybrid model. This algorithm updates second-stage state-action pairs similarly to SARSA(λ), with the exception that expected values at the first-stage are instead learned via a single backup operation, defined in terms of Bellman’s equation (Sutton & Barto, 1998):

Q_MB (s_A,a_t )=P(s_B│s_A,a_t )    max┬(a^'∈{a_A,a_B})⁡〖Q_MF (s_B,a^' )+P(s_C│s_A,a_t )   max┬(a^'∈{a_A,a_B})⁡〖Q_MF (s_C,a^' )〗 〗

where s_A is the first-stage state, s_B is one possible second stage state, s_C is another possible second stage state, and P(s_Y│s_X,a_t ) is the probability that state Y will follow state X after choosing a_t. At the second-stage, the process for determining immediate expected values is no different than that of the SARSA(λ) algorithm, since Q_MB (s_(Y,t),a_t )= r_(2,t). As such, both algorithms converge at the second-stage and Q_MB= Q_MF. 

###2.3.5 | Two Step Computational Modeling – Hybrid Algorithm

To assess the influence of both model-based and model-free strategy on choice behavior, we combine the Q-values estimated from both algorithms into net action values, Q_net. These are defined as a weighted sum such that

Q_net (s_A,a_t )= ω∙Q_MB (s_A,a_t )+(1-ω)∙Q_MF (s_A,a_t)

where ω is a weighting parameter that determines the contribution of both model-based and model-free strategies. When ω = 1, the model is informed solely from the model-based algorithm, whereas when ω = 0, the SARSA(λ) algorithm is the sole contributor. As with the model-based algorithm, at the second-stage, Q_net= Q_MB= Q_MF. Given that this hybrid model is a composition of both previously described algorithms, it relies on a total of 7 free parameters: β1 and β2 to determine how stochastic choices are at the first and second stage; α1 and α2 to describe learning-rates at the first and second stage; ρ to account for perseverance of first-stage choices; λ to describe the influence of second-stage RPEs on first-stage expected values; and ω to weight the influence of the model-based and model-free systems on choice behavior.  

##2.4 | Data Analysis – Balloon Analogue Risk Task

###2.4.1 | BART Performance Indices

Two indices of risk tolerance were analyzed: (1) the total number of successfully cashed out balloons, and (2) the total money won. We assessed these measures across all three blocks of low-to-high-risk balloon types. The initial block of 30 mixed trials was excluded from analysis. BART indices were included as covariates in mixed-effects logistic regression models to assess their influence on Two Step model-based/ model-free learning strategies.

###2.4.2 | BART Computational Modeling – Model Fitting

Similar to our modeling of the Two Step task, we fit a re-parameterized formulation of Wallsten et. al’s constant-probability BART model (see Wallsten et. al., 2005) to subject data. We re-parameterized the terms of this model to avoid inter-term correlations in the posterior and to improve sampling efficiency (Papaspiliopoulos, Roberts & Sköld, 2007). This re-parameterized constant-probability model uses a simple Bayesian update rule to iteratively modify the subjective probability that a balloon h will not explode. Non-pooled, hierarchical models were used to generate individual posterior parameter estimates. Estimates were made using Hamiltonian Markov Chain Monte Carlo simulation in Stan 2.17, interfaced through the PyStan Python package. For each subject, we obtained 50,000 iterative samples across 5 chains (5,000 warmup samples per chain). Chain convergence was indicated by R ̂  ≈1.0.

###2.4.3 | BART Computational Modeling – Constant-Probability BART Model 

We used a posteriori estimation to fit 4 free parameters from the constant-probability model to subject data. Two of these free parameters originate from the Bayesian update rule for calculating the subjective probability that balloon h will not explode, q_h , considerate to the number of pumps attempted on the prior balloon, m_(h^' ):

q_h=  (a_0+ ∑_(h^'=1)^(h-1)▒〖(m_(h^' )-d_(h^' ))〗)/(m_0+∑_(h^'=1)^(h-1)▒m_h' )  ,such that d_h'={█(1 if h^' exploded@0 if h^' cashed)┤

where q_h is a beta distribution with parameters a_0, the prior expected value of balloon h, and m_0, the decision-maker’s confidence in the prior expected value of balloon h. A critical assumption of this model is that decision-makers believe that the subjective probability q_h is constant – they are myopically tied to a constant probability of explosion from the first to the last pump. Trial-to-trial variation amounts to pump observations and the prior belief that balloon h will not burst, a_0/m_0 . It is worth noting that some have argued that the learning parameters, a and m, are systematically overestimated in the posterior and therefore redundant, and suggest instead a simpler, 2-parameter model (van Ravenzwaaij, Dutilh & Wagenmakers, 2011). We acknowledge this potential caveat of our chosen model but continued with the inclusion of these parameters to best represent the learning component of BART performance.

For interpretability, we adapted our model’s update rule to the following:

q_h=  (α_h+ μ∑_(h^'=1)^(h-1)▒〖(m_(h^' )-d_(h^' ))〗)/(1+μ∑_(h^'=1)^(h-1)▒m_h' )  ,such that d_h'={█(1 if h^' exploded@0 if h^' cashed)┤

where α_h is the prior belief that balloon h will not explode, and μ is the updating-rate, or the rate at which pumping increases the belief that a balloon will explode. 

###2.4.4 | BART Computational Modeling – Response Rule

Another critical assumption of the constant-probability model is that the decision-maker determines the optimal number of pumps at the beginning of each trial and is tied to that optimization for the trial’s entirety. This optimal number of pumps, g_h, introduces our third free parameter, and can be expressed as:

g_h=  〖-γ〗^+/(ln⁡(q_h))  ,such that γ^+≥0

where γ^+ is the decision-maker’s propensity for risk-taking. From this estimate of optimality, we define the model’s response rule, a logistic equation that calculates the probability that the decision-maker will take any pump i on any balloon h, r_(h,i):

r_(h,i)=  1/(1+e^(β(i-g_h)) )  ,such that β≥0

Where β, our fourth and final free parameter, is the inverse-temperature determining how stochastic pumps are. As β → ∞, the decision-maker’s actions are solely determined by the distance between pump i and the optimal number of pumps g_h. As β → 0, actions become purely stochastic.

#3 | Results

##3.1 | Sensitivity Analyses

For each linear analysis reported hereafter, we computed Cook’s distances to identify bivariate points of influence. Observations with a Cook’s distance greater than the conventional 4/N (or 0.043, where N=93) were excluded from each analysis separately on a model-by-model basis. Analyses were then rerun on remaining subset. All reported linear regressions were subject to this procedure. For transparency, we report ‘cooks’ to indicate the number of subjects excluded from each model due to high leverage.

##3.2 | BART Performance Indices and Two Step Stay Behavior

Subjects completed 200 trials of the two-step task. Mixed effects logistic regression revealed both model-based and model-free signatures in choice behavior at the group level (Fig. 3). The effect of previous reward was determined to significantly predict stay behavior, indicating the use of model-free strategy (B = 0.419, Z = 18.792, p < 0.001). Furthermore, the interaction effect of previous reward and transition type also predicted stay behavior, indicating model-based strategy (B = 0.361, Z = 16.103, p < 0.001). See Table 1.

To examine the relationship between model-based / model-free decision strategy and BART performance, we ran mixed-effects logistic regression models including BART performance variables as covariates. We ran two models in total, one including terms for the total money earned and the adjusted number of balloons across low-risk trials, and one for the total money earned and the adjusted number of balloons across high-risk trials. Firstly, we discovered that money earned across low-risk balloons had a significant and negative effect on Two Step stay probabilities (Z = 2.12, p = 0.034). Neither money earned nor the adjusted number of balloons across low-risk trials predicted the model-based or model-free signatures. These findings suggest that decision-making on low-risk BART trials is not associated with tendencies toward either model-based or model-free learning strategies. See Table 2.

Contrary to these findings, we did determine that total money earned across high-risk balloons was positively associated with the Two Step model-based signature (Z = 3.43, p = 0.001). Further, we found that the number of adjusted (cashed) high-risk balloons moderated this effect (Z = 3.97, p < 0.001). These findings suggest that model-based learners perform better when making high-risk decisions. See Table 3.

##3.3 | BART Modeling Parameters and Two Step Stay Behavior

We next fit subjects’ performance data for low-risk balloons to the constant-probability model described in Method to estimate posterior distributions for each parameter (see Table 4). To support the aforementioned findings, we next ran similar mixed-effects logistic regression models of stay behavior, but with the constant-probability BART modeling parameters as covariates. All modeling parameters with significant positive skew (μ, γ, β) were log transformed to improve linearity, whereas negatively skewed parameters (α) were square transformed. For high-risk and low-risk balloons, we found a significant interaction effect of α, the prior belief that a balloon will not explode, on model-based strategy (Z = 3.19, p < 0.001), such that individuals who believe that balloons are more likely to explode on the high-risk BART trials than the low-risk also tend to utilize more model-based learning strategies on the Two Step. We did not find a similar relationship with the model-free signature. See Table 5 and Fig. 4).

Interestingly, while we did not find a main effect of μ, the updating-rate on the BART, on Two Step model-based strategy, we did find that greater updating-rates under low-risk conditions were associated with a greater model-free effect (Z = 2.12, p = 0.034). This suggests that subjects who engage in model-free strategies also attribute greater risk to individual ‘pumps’ under low-risk conditions. However, under conditions of high-risk, those same subjects’ expectations were not affected. We did not determine any effect of updating-rate on Two-Step stay behavior. See Table 6 and Fig. 5.

As with μ, we found that γ+, a subject’s propensity for risk-taking, was related to Two Step stay probability, specifically under conditions of low-risk. Individuals who were more risk-tolerant on low-risk BART trials were also less inclined to stay on the Two Step (Z = -2.24, p = 0.025) (see Table 7 and Fig. 6). We also found that risk-taking was bidirectionally related to model-based control, dependent on risk condition. Individuals who had greater risk-tolerance on high-risk BART trials than on low-risk trials also tended to have a greater propensity for model-based control (Z = 2.41, p = 0.016). We did not find a similar relationship with the model-free signature. See Fig. 7.

Lastly, we considered the effect of β, the degree to which subjects pumped BART balloons deterministically versus stochastically, on Two Step stay behavior. For low-risk balloons, we found a significant positive effect of β on stay probabilities (Z = 2.26, p = 0.023), such that individuals who pumped more deterministically also tended to repeat more first-stage Two Step choices (see Table 8 and Fig. 8). We also found a four-way interaction between β and the model-based signature (Z = -2.08, p = 0.38) suggesting that greater exploitation during low-risk BART trials than high-risk trials is related to an increased implementation of model-based strategy on the Two Step. Additionally, we found a similar interaction effect with stochasticity in both risk-conditions and the model-free signature (Z = 3.06, p = 0.002) such that increased model-free strategy is associated with greater stochastic choices across both objectively high and low-risk conditions. See Fig.9.

##3.4 | BART and Two Step Modeling Parameters

We next fit subjects’ choice data to the hybrid reinforcement learning model described in Method to estimate posterior distributions for each parameter (see Table 2). To verify and further investigate our findings relating BART modeling parameters to Two Step stay behavior, we conducted simple linear regression models of the estimated Two Step parameter posterior means using the BART posterior means as predictors. As with the BART parameter estimates, Two Step parameters with significant positive skew were log transformed (β1, β2, ρ). 

First, while we could not determine any significant relationships between the BART α estimate and the estimated free parameters of the Two-Step model, we did find that the BART μ, or updating-rate, was positively predictive of the Two Step ω (B = 0.811, t(1,87) = 2.73, p = 0.007; 3 observations excluded due to high leverage). More specifically, we found that the tendency to ascribe greater risk to individual high-risk BART trials than low-risk trials was associated with model-based control. This reflects the reality of performance under objective risk and suggests that model-based learners are capable of adapting quickly in high-risk conditions and slowly in low-risk conditions. See Fig. 10.

Second, we found that the BART γ+, or risk-tolerance, was significantly predictive of the Two Step ρ (B = 0.282, t(1,87) = 2.37, p = 0.019; 3 observations excluded due to high leverage). More specifically, we found that individuals who tend to perseverate on the Two-Step task also tend to have greater risk-tolerance in high-risk conditions than low-risk. This suggests that being more tolerant of risk when more risk is present is associated with a greater tendency to perseverate on previous actions, regardless of outcome. See Fig. 11.

Lastly, we found that BART β, or decision stochasticity, was predictive of the Two Step ω, (B = 0.13, t = 2.12, p = 0.037) such that individuals who choose more stochastically on high-risk BART trials than low-risk trials tend to be more influenced by model-based learning strategies. This suggests that the degree to which individuals explore action-consequence pairs is also associated with their learning strategies, and that objective risk context too modulates this relationship. See Fig. 12.

#4 | Discussion

##4.1 | Summary

In this study, we tested the relationship between individual differences in risk behavior across two conditions of risk, high and low, and the propensity to employ model-free and model-based learning strategies. Model-based strategies are prospective and computationally demanding, whereas model-free strategies are retrospective and inexpensive. We found that individuals made use of both strategies in their choice behavior. We also discovered that the employment of model-based strategy on the Two Step task was moderated by a number of differences in risk behavior on the BART, conditional on the level of risk experienced. In contrast, we found very little evidence for a similar moderating relationship between risk behavior and model-free strategy.

##4.2 | Associations with Risk Behavior

First, we assessed the observable performance indices from the BART, the total number of cashed balloons, and the total amount of money earned. We found that as individuals made more money on low-risk balloons, they tended to make less stay choices on the Two Step. If individuals are inclined to employ similar strategies across these two tasks, this suggests that strong performance under low-risk is associated with non-perseverative behavior. It is difficult to infer from this surface-level analysis what aspect of decision-making could be driving this relationship. One suggestion is that reduced perseveration relates to increased cognitive flexibility (Dreisbach & Goschke, 2004) and that individuals with greater flexibility are more capable of switching from activation to inhibition over the course of ‘pumping’ a low-cost balloon. Turning to high-risk trials, we found that more money earned was associated with a greater propensity for model-based control. Furthermore, we found that the total number of adjusted (cashed) balloons positively interacted with this relationship. If we consider the total number of cashed balloons to be proximal index for risk tolerance, this suggests that the propensity for model-based learning may reflect variability in optimization. Taken together, these findings support the notion that metrics of performance under risk are predictive of individual differences in the deployment of model-based control.

##4.3 | Associations with the Computational Substrates of Risk

We next compared data from the Two Step task with data from the BART, in conjunction with a model that quantified four latent factors of risk behavior. Importantly, we dissociated these factors between two conditions of risk, high and low, to evaluate deviations in subjective risk perception from objective risk. 

In line with our hypotheses, we found that model-based learners tended to more accurately perceive the risk associated with actions on the BART; that is, model-based learners tended to perceive greater risk at the onset of performance under high-risk conditions, and lesser risk under low-risk conditions. Interestingly, we did not discover a relationship between prior risk perception and the model-based/model-free weight, ω. Nonetheless, the former result supports the notion that model-based learners are keener to recognize contextual factors of decision-making, such as objective risk. Considering that ω is estimated from an individual’s entire proceeding history of choices, it is possible that the relationship between model-based strategy and prior risk perception is rooted in a static individual difference that varies little across trials, such as sensation seeking (Demaree et al., 2008) and extroversion (Oehler & Wedlich, 2018). Another interpretation of this finding is that the ability to more accurately recognize contextual factors such as objective risk is what enables the employment of model-based control. Future work should aim to establish a causative relationship between model-based control and risk perception. 

Unfortunately for individuals who suffer from poor risk perception, it might also be true that they struggle to learn about risk and update their expectations accordingly. This is often the case for problem-gamblers who find themselves unable to adjust to more conservative evaluations, even when a conservative frame of mind is optimal. In line with this notion, we found that having comparatively greater updating-rates on high-risk BART trials than low-risk trials was associated with more model-based influence in terms of the ω parameter, supporting our hypotheses. This suggests that model-based learners tend to incrementally update their perceptions of risk with weight that is appropriate for their experienced risk. Model-free learners did not share this pattern of expectation updating.

Beyond risk perception, we explored individual differences in risk optimization. As hypothesized, we found that having comparatively greater risk tolerance on high-risk BART trials than low-risk trials was associated with increased model-based control on the Two-Step. While no study has directly investigated the effect of risk tolerance on the propensity for model-based learning, some have considered the role of loss aversion, a related factor of risk perception that describes the perceived weight of losses to gains. Prior work suggests that individuals who think more about a task’s contextual aspects tend to be less loss averse, such that they weigh losses less than gains (Sokol-Hessner et al., 2009; Sokol-Hessner et al., 2015). A plausible explanation for this is that framing each trial as one opportunity of many decreases worry. On the other hand, a recent report by Solway and colleagues (2019) contradicts these findings, such that the authors concede that some yet unexplored factor might mediate the relationship between loss aversion and model-based control. Of course, it is possible that, as Solway et al. discuss, a fear of negative outcomes prompts the mental simulation of action-reward scenarios (Vasey and Borkovec, 1992). Should this translate to risk tolerance, it is within reason that risk-averse individuals would have a greater propensity for model-based control.
Notably, loss aversion is typically negatively associated with risk tolerance, and so our finding that risk context moderates the direction of the relationship between tolerance and model-based control could seemingly bridge the findings of Sokol-Hessner et al. and Solway et al.. Furthermore, the distinction between high-risk and low-risk contextual factors could explain the present inconsistency in the loss aversion literature – it is possible that differences in task design precipitated individual differences in perceived risk, which differentially affected aversion (Walasek and Stewart, 2015). 

Contrary to our hypotheses, we found that comparatively greater stochasticity of choice on high-risk BART trials than low-risk trials was associated with increased model-based control on the Two-Step. There are several plausible explanations for this finding. Firstly, exploration, when it can be afforded, reduces uncertainty (Speekenbrink and Konstantinidis, 2015). It seems reasonable that individuals who act to reduce uncertainty would be more likely to engage in model-based strategy on the Two Step and exploration on the BART. Why our findings suggest that these individuals are more deterministic under low-risk however, is less clear. It is possible that the utility of exploration diminishes as balloons become more valuable. Under high-risk, the potential cost for reducing uncertainty can be small, whereas under low-risk, the cost when acting on a well ‘pumped’, highly valuable balloon can ironically be quite high. It follows that model-based learners might choose more deterministically on low-risk trials. It is worth noting that these explanations assume that exploration is directed, however, another possibility is that exploration is incidental and that purely random choice leads to a better understanding of the choice space through trial-and-error (Ebitz, Albarran & Moore, 2018). This is distinct from the directed exploration hypothesis in that incidental exploration uncovers context due to reduced cognitive control. This would imply that model-based learners employ less control under high-risk than low-risk. Future studies should expand on this reported moderating relationship by investigating the effect of introducing and releasing cognitive control on the propensity for deterministic choice.

Interestingly, when we expanded on these findings by evaluating the predictive accuracy of BART risk tolerance and stochasticity parameters on Two Step parameter estimates, we found that stochasticity was associated with ω, whereas tolerance was not. Instead, risk tolerance was related to the value-independent perseveration parameter, ρ. This was unexpected, as perseveration is typically associated with value-free habit formation (Tricomi, Balleine & O’Doherty, 2009; Dickinson & Weiskrantz, 1985), and has been found to be lessened by model-based learning (Gillan et al., 2015). That said, our findings do not completely contradict the extant literature, as we found no association between perseveration and model-based control. This suggests that some other latent factor, that is not associated with the propensity for model-based learning, might drive perseveration. A recent report by Miller, Botvinick and Brody hints at these factors being separable, suggesting that perseveration is a slow-learning process that has a timescale independent from reward-seeking processes (2018 PREPRINT). Indeed, we observed that greater risk tolerance on low-risk BART trials was associated with decreased stay behavior across all four previous reward and transition state conditions on the Two-Step. Future studies should aim to disjoin the processes underlying perseveration and reward-seeking, particularly in learning contexts where they are both strengthened.

Previous studies have thoroughly assessed the model-based and model-free learning profiles in clinical addiction disorders (Hogarth, Chase, and Baess, 2012; Lorains et al., 2014; Sebold et al., 2014; Deserno et al., 2015; Reiter et al., 2016; Groman et al., 2019; Wyckmans et al., 2019 PREPRINT). However, to our knowledge, no study has considered the computational substrates of risk perception and optimization that may precipitate these conditions. We have identified four such substrates and have charted a profile for their moderating effects on model-based control with respect to distinct contextual factors. These results support the use of computational methods such as reinforcement-learning models for investigating the underlying bases of decision-making in addiction disorder and other clinical populations with deficits in decision-making. There are multiple paths in which we envision future studies expanding on these findings. First, we suggest that the pursuit of latent factors such as those discussed in this report be paired with neuroimaging methods to identify their neural substrates and relate those to the propensity for model-based control. Such future work could provide insights into the effects of developmental and neurodegenerative disorder and disease on both risk behavior and learning. Second, we suggest that future studies aim to find means to manipulate these factors with the goal of treating deficits in model-based control. For example, a future study could aim to treat patients’ ability to adjust their evaluations of risk to be appropriate for the risk-level of a situation at hand. Kurdi, Gershman & Banaji, recently reported that the updating of implicit evaluations is impervious to model-based learning (2019), so if we interpret the BART’s μ as representative of the updating of an implicit evaluation of risk, future work might aim to treat updating deficits through habitual association. Treatments such as this could have the potential to train latent factors of behavior that contribute to the propensity for model-based control.

#5 | Conclusion

The present findings suggest that the propensity for model-based learning can be identified through the evaluation of individual differences in risk behavior. Further, they suggest that the relationships between this propensity and subjective differences in risk perception and optimization can be dependent on the severity of objective risk. Together, the findings from our robust analyses elucidate for the first time an underlying relationship between latent factors of learning and risk behavior. Through the utilization of two reinforcement learning frameworks, these data provide computational specificity that may guide future studies toward the identification of the neural infrastructure at the intersection of model-based learning and risk behavior. Not only could this provide a better understanding the underlying brain function but elucidating this intersection could have profound implications for the development of learning interventions and behavioral treatment in both typical developing and clinical groups. 

#6 | Footnotes

This work was supported by the U.S. Army Medical Research and Development Command grant W81XWH-17-008.

To whom correspondence may be addressed. Email: kjlafoll@stanford.edu

Author contributions: K.J.L., B.C.S., M.P.L., and W.D.S.K. designed research; K.J.L., B.C.S., and M.P.L. performed research; K.J.L. analyzed data; K.J.L. wrote the paper.

The authors declare no conflict of interest.


 
#7 | References

Barr, DJ., Levy, R., Scheepers, C., Tily, HJ. (2013). Random effects structure for confirmatory hypothesis testing: Keep it maximal. Journal of Memory and Language, 68(3), 255-278

Daw, ND., Niv, Y., Dayan, P. (2005). Uncertainty-based competition between prefrontal and dorsolateral striatal systems for behavioral control. Nature Neuroscience, 8, 1704-1711.

Daw, ND., Gershman, SJ., Seymour, B., Dayan, P., Dolan, RJ. (2011). Model-based influences on humans’ choices and striatal prediction errors. Neuron, 69(6), 1204-1215.

Decker, JH., Otto, AR., Daw, ND., Hartley, CA. (2016). From creatures of habit to goal-directed learners: Tracking the developmental emergence of model-based reinforcement learning. Psychological Science, 27(6), 848-858.

Demaree, HA., DeDonno, MA., Burns, KJ., Everhart, DE. (2008). You bet: How personality differences affect risk-taking preferences. Personality and Individual Differences, 44(7), 1484-1494.

De Neys, W. (2006). Dual processing in reasoning: two systems but one reasoner. Psychological Science, 17(5), 428-433.

Deserno, L., Wilbertz, T., Reiter, A., Horstmann, A., Neumann, J., Villringer, A., Heinze, HJ., Schlagenhauf, F. (2015). Lateral prefrontal model-based signatures are reduced in healthy individuals with high trait impulsivity. Translational Psychiatry, 5:e659.

Dickinson, A., Weiskrantz, L. (1985). Actions and habits: The development of behavioural autonomy. Philosophical Transactions of the Royal Society B, 308(1135).

Diederich, A., Trueblood, JS. (2018). A dynamic dual process model of risky decision making. Psychological Review, 125(2), 270-292.

Dreisbach, G., Goschke, T. (2004). How positive affect modulates cognitive control: Reduced perseveration at the cost of increased distractibility. Journal of Experimental Psychology: Learning, Memory, and Cognition, 30(2), 343-353.

Ebitz, RB., Albarran, E., Moore, T. (2018). Exploration disrupts choice-predictive signals and alters dynamics in prefrontal cortex. Neuron, 97, 450-461.

Feher da Silva, C., Hare, TA. (2019). Humans are primarily model-based and not model-free learners in the two-stage task. BioRxiv 682922 [Preprint]. Available from: https://doi.org/10.1101/682922.

Gillan, CM., Otto, RA., Phelps, EA., Daw, ND. (2015). Model-based learning protects against forming habits. Cognitive, Affective & Behavioral Neuroscience, 15(3), 523-536.

Groman, SM., Massi, B., Mathias, SR., Lee, D., Taylor, JR. (2019). Model-based and model-free influences in addiction-related behaviors. Biological Psychiatry, 85(11), 936-945.

Guo, L., Trueblood, JS., Diederich, A. (2017). Thinking fast increases framing effects in risk decision-making. Psychological Science, 28(4), 530-543.

Heinze, G., Ploner, M., Dunkler, D., Southworth, H. (2018). Firth’s bias-reduced logistic regression. Available from: https://cran.r-project.org/web/packages/logistf/index.html.

Hogarth, L., Chase, HW., Baess, K., (2012). Impaired goal-directed behavioural control in human impulsivity. Quarterly Journal of Experimental Psychology, 65(2), 305-316.

Kahneman, D. (2003). A perspective on judgment and choice: Mapping bounded rationality. American Psychologist, 58, 697-720.

Kurdi, B., Gershman, SJ., Banaji, MR. (2019). Model-free and model-based learning processes in the updating of explicit and implicit evaluations. Proceedings of the National Academy of Sciences, 116(13), 6035-6044.

Lejuez, CW., Read, JP., Kahler, CW., Richards, JB., Ramsey, SE., Stuart, GL., Strong, DR., Brown, RA. (2002). Evaluation of a behavioral measure or risk taking: The Balloon Analogue Risk Task. Journal of Experimental Psychology Applied, 8(2), 75-84.

Loewenstein, G., O’Donoghue, T., Bhatia, S. (2015). Modeling the interplay between affect and deliberation. Decision, 2, Article 55.

Lorains, FK., Dowling, NA., Enticott, PG., Bradshaw, JL., Trueblood, JS., Stout, JC. (2014). Strategic and non-strategic problem gamblers differ on decision making under risk and ambiguity. Addiction, 109(7), 1128-1137.

Miller, KJ., Botvinick, MM., Brody, CD. (2018). From predictive models to cognitive models: An analysis of rat behavior in the two-armed bandit task. BioRxiv 461129 [Preprint]. Available from: https://doi.org/10.1101/461129.

Mueller, ST., Piper, BJ. (2014). The Psychology Experiment Building Language (PEBL) and PEBL test battery. Journal of Neuroscience Methods, 222, 250-259.

Mukherjee, K. (2010). A dual system model of preferences under risk. Psychological Review, 177, 243-245.

Oehler, A., Wedlich, F. (2018). The relationship of extraversion and neuroticism with risk attitude, risk perception, and return expectations. Journal of Neuroscience, Psychology, and Economics, 11(2), 63-92.

Otto, AR., Gershman, SJ., Markman, AB., Daw, ND. (2013). The curse of planning: Dissecting multiple reinforcement-learning systems by taxing the central executive. Psychological Science, 24(5), 751-761.

Otto, AR., Raio, CM., Chiang, A., Phelps, EA., Daw, ND. (2013). Working memory capacity protects model-based learning from stress. Proceedings of the National Academy of Sciences, 110(52), 20941-20946.

Papaspiliopoulos, O., Roberts, GO., Sköld, M. (2007). A general framework for the parameterization of hierarchical models. Statistical Science, 22(1), 59-73.

R Core Team. (2017). R: A language and environment for statistical computing. R Foundation for Statistical Computing. Version 3.4.3. Available from: https://www.R-project.org/.
 
Reiter, AMF., Deserno, L., Wilbertz, T., Heinze, H., Schlagenhauf, F. (2016). Risk factors in addition and their association with model-based behavioral control. Frontiers in Behavioral Neuroscience, 10:26.

Rummery, GA., Niranjan, M. (1994). On-line Q-learning using connectionist systems. Cambridge University.

Schad, DJ., Jünger, E., Sebold, M., Garbusow, M., Bernhardt, N., Javadi, A., Zimmermann, US., Smolka, MN., Heinz, A., Rapp, MA., Huys, QJM. (2014). Processing speed enhances model-based over model-free reinforcements learning in the presence of high working memory functioning. Frontiers in Psychology, 5:1450.

Sebold, M., Deserno, L., Nebe, S., Schad, DJ., Garbusow, M., Hägele, C., Keller, J., Jünger, E., Kathmann, N., Smolka, MN., Rapp, MA., Schlagenhauf, F., Heinz, A., Huys, QJ. (2014). Model-based and model-free decisions in alcohol dependence. Neuropsychobiology, 70(2), 122-131.

Simon, DA., Daw, ND. (2011). Environmental statistics and the trade-off between model-based and TD learning in humans. Advances in Neural Information Processing Systems, Vol. 24., 127-135

Sloman, SA. (1996). The empirical case for two systems of reasoning. Psychological Bulletin, 199, 3-22.

Slovic, P., Finucane, ML., Peters, E., MacGregor, DG. (2004). Risk as analysis and risk as feelings: Some thoughts about affect, reason, risk, and rationality. Risk Analysis, 24(2), 311-322.

Smittenaar, P., FitzGerald, THB., Romei, V., Wright, ND., Dolan, RJ. (2013). Disruption of dorsolateral prefrontal cortex decreases model-based in favor of model-free control in humans. Neuron, 80(4), 914-919.

Sokol-Hessner, P., Hsu, M., Curley, NG., Delgado, MR., Camerer, CF., Phelps, EA. (2009). Thinking like a trader selectively reduces individuals’ loss aversion. Proceedings of the National Academy of Sciences, 106(13), 5035-5040.

Sokol-Hessner, P., Hartley, CA., Hamilton, JR., Phelps, EA. (2015). Interoceptive ability predicts aversion to losses. Cognition and Emotion, 29, 695-701.

Solway, A., Lohrenz, T., Montague, PR. (2019). Loss aversion correlates with the propensity to deploy model-based control. Frontiers in Neuroscience, 13:915.

Speekenbrink, M., Konstantinidis, E. (2015). Uncertainty and exploration in a restless bandit problem. Topics in Cognitive Science, 7(2), 351-367.

Stan Development Team. (2018). PyStan: The Python interface to Stan. Version 2.17.1.0. Available from: http://mc-stan.org.

Stanovich, KE., West, RF. (2000). Individual differences in reasoning: Implications for the rationality debate? Behavioral and Brain Sciences, 23, 645-665.

Sutton, RS., Barto, AG. (1998). Reinforcement learning: An introduction. Cambridge, MA: MIT Press.

Tricomi, E., Balleine, BW., O’Doherty, JP. (2009). A specific role for posterior dorsolateral striatum in human habit learning. The European Journal of Neuroscience, 29(11), 2225-2232.

van Ravenzwaaij, D., Dutilh, G., Wagenmakers, E. (2011). Cognitive model decomposition of the BART: Assessment and application. Journal of Mathematical Psychology, 55, 94-105.

Vasey, MW., Borkovec, TD. (1992). A catastrophizing assessment of worrisome thoughts. Cognitive Therapy and Research, 16(5), 505-520.

Walasek, L., Stewart, N. (2015). How to make loss aversion disappear and reverse: Tests of the decision by sampling origin of loss aversion. Journal of Experimental Psychology: General, 144(1), 7-11.

Wallsten, TS., Pleskac, TJ., Lejuez, CW. (2005). Modeling behavior in a clinically diagnostic sequential risk-taking task. Psychological Review, 112(4), 862-880.

Wang, XT. (2006). Emotions within reason: Resolving conflicts in risk preference. Cognition and Emotion, 20(8), 1132-1152.

Wyckmans, F., Otto, AR., Sebold, M., Daw, ND., Bechara, A., Saeremans, M., Kornreich, C., Chatard, A., Jaafari, N., Noël, X. (2019). Reduced model-based decision-making in gambling disorders. Preprint.

