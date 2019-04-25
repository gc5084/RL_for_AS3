# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent


class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        states = mdp.getStates()
        for i in range(iterations):
            pre_values = self.values.copy()
            for state in states:
                if not mdp.isTerminal(state):
                    actions = self.mdp.getPossibleActions(state)
                    max_value = -float('inf')
                    for action in actions:
                        Q_value = 0
                        for next_state,prob in self.mdp.getTransitionStatesAndProbs(state,action):
                            #print "getReward:",self.mdp.getReward(state,action,next_state),"state:",state,"action:",action,"next_state:",next_state,"prob:",prob
                            Q_value += prob*(self.mdp.getReward(state,action,next_state)+self.discount*pre_values[next_state])
                        max_value = max(Q_value,max_value)
                    self.values[state] = max_value
                
         

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        #print "---getValue,state:",state,"ret value:",self.values[state]
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        Q_value = 0
        for next_state,prob in self.mdp.getTransitionStatesAndProbs(state,action):
            Q_value += prob*(self.mdp.getReward(state,action,next_state)+self.discount*self.values[next_state])
        #print "---computeQ,state:",state,"action:",action, "ret Q_value:",Q_value
        return Q_value

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        
        actions = self.mdp.getPossibleActions(state)
        max_value = -float('inf')
        best_action = None;
        
        for action in actions:
            Q_value = self.computeQValueFromValues(state, action)
            if Q_value > max_value:
                max_value = Q_value
                best_action = action
         
        #print "---computeActionFromValues,state:",state,"return action:",best_action        
        return best_action
    
            

    def getPolicy(self, state):
        print "---getPolicy"
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        print "---getAction"
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        print "---getQValue"
        return self.computeQValueFromValues(state, action)
