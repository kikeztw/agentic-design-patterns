# src/graph.py
from langgraph.graph import StateGraph, END
from state import AgentState
from nodes import generator_node, reflector_node, should_continue


def create_reflection_graph() -> StateGraph:
    """
    Creates the reflection graph with LangGraph.
    
    Returns:
        Compiled graph ready to execute
    """
    
    # 1. Create the graph with the state type
    workflow = StateGraph(AgentState)
    
    # 2. Add the nodes
    workflow.add_node("generator", generator_node)
    workflow.add_node("reflector", reflector_node)
    
    # 3. Define the entry point
    workflow.set_entry_point("generator")
    
    # 4. Add the connections (edges)
    # Generator always goes to Reflector
    workflow.add_edge("generator", "reflector")
    
    # 5. Add conditional edge from Reflector
    # According to should_continue, goes to "generator" (continue) or END (end)
    workflow.add_conditional_edges(
        "reflector",  # From this node
        should_continue,  # Function that decides
        {
            "continue": "generator",  # If returns "continue", goes back to generator
            "end": END  # If returns "end", finishes
        }
    )
    
    # 6. Compile the graph
    return workflow.compile()


# Create global graph instance
graph = create_reflection_graph()
