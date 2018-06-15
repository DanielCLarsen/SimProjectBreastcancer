#Task 11
#WHAT ASSUMPTIONS HAVE BEEN ELIMINATED?
#No longer, we have assumed that one timestep is a month, making it so that women can die at any time, which is way more realistic.
#The timestep for moving around from one point to another was set in stone before, but now there are different transition rates for the states.
#Since erlang distribution is just a more general exponential distribution, and since the exponential distribution is sbasically an erlang distribution wit
#size = 1, then we can simply add the shape parameter, increasing it to flatten out the distribtion.
