# src/main.py
from graph import graph
from state import AgentState


def run_reflection_agent(user_input: str) -> AgentState:
    """
    Runs the reflection agent with user input.
    
    Args:
        user_input: Initial user text
        
    Returns:
        Final state after all iterations
    """
    print("\n" + "="*60)
    print("🚀 STARTING REFLECTION AGENT")
    print("="*60)
    print(f"Input: {user_input}")
    print("="*60)
    
    # Create initial state
    initial_state = AgentState(input=user_input)
    
    # Execute the graph
    final_state = graph.invoke(initial_state)
    
    print("\n" + "="*60)
    print("✅ PROCESS COMPLETED")
    print("="*60)
    print(f"\n📝 FINAL CONTENT:\n{final_state['content']}")
    print(f"\n💬 LAST FEEDBACK:\n{final_state['feedback']}")
    print(f"\n⭐ FINAL SCORE: {final_state['score']}/10")
    print(f"🔄 ITERATIONS: {final_state['iteration']}")
    print("="*60)
    
    return final_state


def main():
    """Main function to run from command line."""
    import sys
    
    # Usage examples
    examples = [
        "Improve this email: Hi, I need pricing info",
        "Write a professional tweet about AI",
        "Draft a formal apology for a delivery delay"
    ]
    
    if len(sys.argv) > 1:
        # If argument is passed, use it
        user_input = " ".join(sys.argv[1:])
    else:
        # Otherwise, use the first example
        print("\n💡 Usage examples:")
        for i, ex in enumerate(examples, 1):
            print(f"   {i}. {ex}")
        print("\n📌 Using example 1...\n")
        user_input = examples[1]
    
    # Run the agent
    run_reflection_agent(user_input)


if __name__ == "__main__":
    main()
