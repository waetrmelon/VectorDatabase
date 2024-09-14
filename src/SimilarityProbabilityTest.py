from VecDB import *

GraphValue1 = GenerateGraphValue("Potato")
GraphValue2 = GenerateGraphValue("Potat")
# Generates Value from a direct variable, without node.

print(SimilarityProbability(GraphValue1, GraphValue2)) # Displays the probabilistic value of the two GraphValues being similar,
# Returns 86% (Rounded Up).