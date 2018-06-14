#Dont look at entire history, only the last one
#Assumptions
# - Markov model only prev step
# - Current model doesnt consider age
# - Death can be other things than cancer (age/accident)
# - Cant get better, only worse over time
#Is it realistic?
# - 2 Forskellige mediciner som er skadelige sammen, over 2 dage. Markov model cant detect.
# - Age is a big factor in health, and is therefore not realistic to not consider.
# - Deaths other than cancer happens all the time, and is therefore very important to consider in the statistics
# - The fact of the matter is, that in reality, people get better from cancer too, and this should be recorded.
#How may we relax these assumptions?