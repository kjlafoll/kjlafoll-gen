#Author: Kyle J. LaFollette
#Department of Psychiatry, University of Arizona
#Correspondance: kjlafoll@psychiatry.arizona.edu

#Runs the simulations of two-stage tasks and analyze them.
#See simulation parameters to customize model

import os
import numpy as np
import pandas as pd
import random
from scipy.special import expit
import matplotlib.pyplot as plt
import matplotlib as mpl
import pickle
from sklearn.linear_model import LogisticRegression

# Customizable model components
# ------------------------------------------------------------------------------------------------------
# Simulation parameters
ALPHA1, ALPHA2, LMBD, OMEGA, BETA1, BETA2, PERS = 0.5, 0.5, 0.6, 1.0, 5, 5, 0
# Number of trials
numtrials = 200
# Common probability (the rare probability is 1 - commonprob)
commonprob = 0.7
# Number of simulated agents of each type (model-free, model-based)
numagents = 200
#-------------------------------------------------------------------------------------------------------

paramslist = ((1, ALPHA1, ALPHA2, LMBD, BETA1, BETA2, OMEGA, PERS, None, True),)
commontrans = {
    's1a1': 's2s1',
    's1a2': 's2s2',
	}
resultsf = 'sim_results.pkl'

#Gaussian walk; diffuses probability of state 2 reward
def walk(prob):
    prob += random.gauss(0, 0.025)
    if prob < 0.25:
        prob = 0.50 - prob
    elif prob > 0.75:
        prob = 1.50 - prob
    assert prob >= 0.25 and prob <= 0.75
    return prob

class Exp:
    def __init__(self, rwrd_probs=None):
        if rwrd_probs is None:
            # Determine initial reward probabilities randomly
            self.rwrd_probs = {
                (s, a): random.uniform(0.25, 0.75) \
                for s in ('s2s1', 's2s2') for a in range(2)}
        else:
            self.rwrd_probs = rwrd_probs
        self.trial = 0
        self.trial_info = []
        self.common = None
        self.finalst = None
        self.choice = None
        self.reward = None
    def __iter__(self):
        return self
    def __next__(self):
        if self.trial >= numtrials:
            raise StopIteration
        self.common = random.random() < commonprob  # Probability of common transition
        self.trial += 1
        return self.trial - 1
    def enter_choice1(self, choice):
        """Enter the initial-state choice ('s1a1' or 's1a2')."""
        self.finalst = commontrans[choice]  # Common
        self.choice = choice
        if not self.common:  # Rare
            if self.finalst == 's2s1':
                self.finalst = 's2s2'
            else:
                self.finalst = 's2s1'
    def enter_choice2(self, choice, diffuse_probs=True):
        self.reward = random.random() < self.rwrd_probs[(self.finalst, choice)]
        self.trial_info.append({
            'trial': self.trial + 1,
            'common': int(self.common),
            'choice': self.choice,
            'finalst': self.finalst,
            'reward': int(self.reward),
        })
        if diffuse_probs:
            # Diffuse probability
            for k, v in self.rwrd_probs.items():
                self.rwrd_probs[k] = walk(v)
    def get_results(self):
        """Get dataframe with the results of the experiment."""
        cols = self.trial_info[0].keys()
        results = pd.DataFrame(columns=cols)
        results.trial = results.trial.astype('int')
        results.common = results.common.astype('int')
        results.reward = results.reward.astype('int')

        for trial_num, info in enumerate(self.trial_info):
            results.loc[trial_num] = pd.Series(info)
        return results

def get_sschoice(q2, beta2, finst):
    """Get simulated choice.
    Keyword arguments:
    q2: dict of final-state action values
    beta: exploration parameter
    finst: final state
    """
    probs = np.array([np.exp(beta2 * v) for (s, a), v in q2.items() if s == finst])
    probs /= np.sum(probs)
    r = random.random()
    s = 0
    for action, x in enumerate(probs):
        s += x
        if s >= r:
            return action
    return action

def hybrid_sim(alpha1, alpha2, lmbd, omega, beta1, beta2, p, rwrd_probs, diffuse_probs):
    """Simulates a hybrid agent."""
    q1 = {}
    q1['s1a1'] = 0
    q1['s1a2'] = 0
    q2 = {(s, a): 0 for s in ('s2s1', 's2s2') for a in range(2)}
    exp = Exp(rwrd_probs)
    prev_choice = random.choice(('s1a1', 's1a2'))
    for trial in exp:
        choice1 = max([q2[('s2s1', a)] for a in range(2)])
        choice2 = max([q2[('s2s2', a)] for a in range(2)])
        # Determine the choice
        if commontrans['s1a2'] == 's2s2':
            cv = (2 * commonprob - 1) * (choice1 - choice2)
        else:
            cv = (2 * commonprob - 1) * (choice2 - choice1)
        rep = 1 if prev_choice == 's1a1' else -1
        p_left = expit(beta1 * (omega * (cv) + (1 - omega) * (q1['s1a1'] - q1['s1a2']) + rep * p))
        if random.random() < p_left:
            a1 = 's1a1'
        else:
            a1 = 's1a2'
        exp.enter_choice1(a1)
        prev_choice = a1
        finst = exp.finalst
        a2 = get_sschoice(q2, beta2, finst)
        exp.enter_choice2(a2, diffuse_probs=diffuse_probs)
        r = int(exp.reward)
        q1[a1] = (1 - alpha1) * q1[a1] + alpha1 * q2[(finst, a2)] + \
                 alpha1 * lmbd * (r - q2[(finst, a2)])
        q2[(finst, a2)] = (1 - alpha2) * q2[(finst, a2)] + alpha2 * r
    return exp

def plot_probs(probs, legend=True):
    """Plot probabilities."""
    x = (0, 2)
    plt.bar(left=x, height=[probs[i] for i in x], align='center',
            color='tab:orange', label='common')
    x = (1, 3)
    plt.bar(left=x, height=[probs[i] for i in x], align='center',
            color='tab:green', label='rare')
    plt.xticks((0.5, 2.5), ('rewarded', 'unrewarded'))
    plt.ylabel('stay probability')
    if legend:
        plt.legend(loc='upper right', fontsize='medium')
    plt.ylim(0, 1)
    plt.xlim(-0.5, 3.5)

def get_predictors(results):
    """Get predictors for logistic regression."""
    assert len(results) == 200
    y = []
    x = []
    for (_, trial1), (_, trial2) in zip(results.iloc[:-1].iterrows(), results.iloc[1:].iterrows()):
        transition = 2 * int(trial1.common) - 1
        reward = 2 * trial1.reward - 1
        x.append([1, reward, transition, reward * transition])
        y.append(int(trial1.choice == trial2.choice))
    return x, y

def get_sim_results():
    """Run simulations and get results, or load results from file."""
    if not os.path.exists(resultsf):
        with open(resultsf, 'wb') as outf:
            for params in paramslist:
                sim_results = []
                sim_num, alpha1, alpha2, lmbd, beta1, beta2, omega, pers, rwrd_probs, diffuse_probs = params
                print('Running simulation {}...'.format(sim_num))
                for rep in range(numagents):
                    if rep % 100 == 0:
                        print('Creating hybrid agents {}-{} of {}...'.format(
                            rep + 1, rep + 100, numagents))
                    exp = hybrid_sim(alpha1, alpha2, lmbd, omega, beta1, beta2, pers, rwrd_probs, diffuse_probs)
                    results = exp.get_results()
                    sim_results.append(('Hybrid', results))

                pickle.dump((sim_num, sim_results), outf)
                yield sim_num, sim_results
    else:
        with open(resultsf, 'rb') as outf:
            for params in paramslist:
                sim_num, sim_results = pickle.load(outf)
                yield sim_num, sim_results

def run_simulations():
    """Run simulations, analyze the results, and create figures."""
    mpl.rcParams['xtick.direction'] = 'out'
    mpl.rcParams['ytick.direction'] = 'out'
    analyses = (
        ('standard', get_predictors),
    )
    for sim_num, sim_results in get_sim_results():
        for ana, get_predictors_f in analyses:
            figure = plt.figure()
            figure.set_size_inches(2 * 4, 4)
            for group_num, group in enumerate(('Hybrid', 'Hybrid')):
                group_results = [results for g, results in sim_results if g == group]
                # Perform logistic regression with little regularization
                # although regulatization doesn't make much difference
                logreg = LogisticRegression(fit_intercept=False, C=1e6)
                x, y = [], []
                for i, results in enumerate(group_results):
                    xx, yy = get_predictors_f(results)
                    M = [0] * len(group_results)
                    M[i] = 1
                    for l in xx:
                        x.append(M + l)
                    y += yy
                logreg.fit(x, y)
                del x
                del y

                axes = plt.subplot()
                axes.spines['right'].set_color('none')
                axes.spines['top'].set_color('none')
                axes.xaxis.set_ticks_position('bottom')
                axes.yaxis.set_ticks_position('left')
                plt.title(group)
                coefs = logreg.coef_[0][
                        len(group_results):(len(group_results) + 4)]
                probs = (
                    expit(coefs[0] + coefs[1] + coefs[2] + coefs[3]),
                    expit(coefs[0] + coefs[1] - coefs[2] - coefs[3]),
                    expit(coefs[0] - coefs[1] + coefs[2] - coefs[3]),
                    expit(coefs[0] - coefs[1] - coefs[2] + coefs[3]),
                )
                plot_probs(probs)
                del group_results
                del logreg

            plt.tight_layout()
            plt.savefig(
                'results-sim{}-{}.pdf'.format(sim_num, ana), bbox_inches='tight')
            plt.close()
        del sim_results

if __name__ == '__main__':
    run_simulations()