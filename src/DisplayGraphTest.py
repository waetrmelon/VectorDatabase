from VecDB import *

Value = "Hello" # What value you'd like to convert to vector.
Vector = GenerateVector(Value) # Create Vector from value.

node = CalculateNodePosition(Vector) # Generate Node from Vector
print(node.representation) # Represent Node data in List.
# Index 0: Node Value
# Index 1: Vector Array
VectorArray = [node.value]
displayGraph(VectorArray) # Show Graph Data