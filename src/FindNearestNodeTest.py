from VecDB import *

vectorsValues = [GenerateGraphValue("Potato"),  GenerateGraphValue("Banana"),  GenerateGraphValue("Apple"),  GenerateGraphValue("Peanut")] # Test Database
# Generates Value from a direct variable, without node.

starting_pos = GenerateGraphValue("Banana") # Value we start from (starting pos).
print(findNearestNode(vectorsValues, starting_pos, 10)) # Put Test Database through the findNodeRange function to find closest node from starting pos (arg-2).
# Arg-1: Test Database
# Arg-2: Starting Node
# Arg-4: The node difference limit.

displayGraph(vectorsValues) # Show Graph Data