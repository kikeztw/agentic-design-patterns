# test_nodes.py
from state import AgentState
from nodes import generator_node, reflector_node, should_continue

# Test del flujo completo
state = AgentState(input="Mejora este email: Hola, necesito info de precios")

print("=" * 60)
print("PRUEBA DE NODOS")
print("=" * 60)

# Iteración 1
state = generator_node(state)
state = reflector_node(state)
decision = should_continue(state)
print(f"\nDecisión: {decision}")

# Si continúa, hacer otra iteración
if decision == "continue":
    state = generator_node(state)
    state = reflector_node(state)
    decision = should_continue(state)
    print(f"\nDecisión: {decision}")

print("\n" + "=" * 60)
print("ESTADO FINAL:")
print("=" * 60)
print(f"Content: {state.content}")
print(f"Feedback: {state.feedback}")
print(f"Score: {state.score}")
print(f"Iterations: {state.iteration}")
