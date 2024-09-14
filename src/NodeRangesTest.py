from VecDB import *

vectorsValues = [GenerateGraphValue("Potato"),  GenerateGraphValue("Banana"),  GenerateGraphValue("Apple"),  GenerateGraphValue("Peanut")] # Test Database
# Generates Value from a direct variable, without node.

print(findNodeRange(vectorsValues, GenerateGraphValue("Banana"), 3, 3)) # Put Test Database through the findNodeRange function to find closest nodes on the graph within a range.
# Arg-1: Test Database
# Arg-2: Starting Node
# Arg-3: How many nodes you want to find.
# Arg-4: The node difference limit.

displayGraph(vectorsValues) # Show Graph Data