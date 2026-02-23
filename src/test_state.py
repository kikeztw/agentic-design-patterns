# test_state.py
from state import AgentState

# Test 1: Crear state válido
state = AgentState(
    input="Mejora este email: Hola, necesito ayuda"
)
print("✅ State creado:", state)
print(f"   Content: '{state.content}'")
print(f"   Score: {state.score}")
print(f"   Iteration: {state.iteration}")

# Test 2: Actualizar state
state.content = "Estimado cliente..."
state.score = 7.5
state.iteration = 1
print("\n✅ State actualizado:", state)

# Test 3: Validación (debería fallar)
try:
    state.score = 15  # Fuera de rango
except ValueError as e:
    print(f"\n✅ Validación funciona: {e}")

# Test 4: Crear con todos los campos
state_full = AgentState(
    input="Test",
    content="Contenido inicial",
    feedback="Mejora la claridad",
    score=6.5,
    iteration=2
)
print(f"\n✅ State completo: {state_full}")
