from typing import Literal
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage


from utils import parse_json_response
from state import AgentState
from config import settings
from prompts import (
    GENERATOR_SYSTEM_PROMPT,
    REFLECTOR_SYSTEM_PROMPT,
    get_generator_prompt,
    get_reflector_prompt
)


llm = ChatOpenAI(
  model=settings.model_name,
  temperature=settings.temperature,
  api_key=settings.openai_api_key
)

def generator_node(state: AgentState) -> AgentState:
  """
  Node that generates a response using the LLM.

  Args:
    state: Agent current state

  Returns:
    Updated state with new content
  """
  print(f"\n🤖 GENERATOR (Iteration {state.iteration + 1})")
  
  if state.iteration == 0:
    prompt = get_generator_prompt(state.input)
  
  
  if state.iteration > 0:
    feedback = state.feedback
    prompt = get_generator_prompt(state.input, feedback)
  
  messages = [
      SystemMessage(content=GENERATOR_SYSTEM_PROMPT),
      HumanMessage(content=prompt)
  ]
  response = llm.invoke(messages)
  state.content = response.content
  state.iteration += 1
  print(f"   Generated content: {state.content[:100]}...")
  return state

  
def reflector_node(state: AgentState) -> AgentState:
    """
    Node that analyzes and critiques the content.
    
    Args:
        state: Current agent state
        
    Returns:
        Updated state with feedback and score
    """
    print(f"\n🔍 REFLECTOR (Iteration {state.iteration})")
    
    generated_content = state.content
    analisis_prompt = get_reflector_prompt(generated_content)
    messages = [
        SystemMessage(content=REFLECTOR_SYSTEM_PROMPT),
        HumanMessage(content=analisis_prompt)
    ]
    response = llm.invoke(messages)
        # Parse JSON response
    try:
        parsed = parse_json_response(response.content)
        state.feedback = parsed["feedback"]
        state.score = float(parsed["score"])  # Ensure it's a float
        
        print(f"   Feedback: {state.feedback[:100]}...")
        print(f"   Score: {state.score}/10")
    except (ValueError, KeyError) as e:
        print(f"   ⚠️ Error parsing response: {e}")
        print(f"   Raw response: {response.content}")
        # Fallback: assign default values
        state.feedback = "Error parsing feedback"
        state.score = 0.0

    return state


def should_continue(state: AgentState) -> Literal["continue", "end"]:
    """
    Decides whether to continue iterating or finish.
    
    Args:
        state: Current agent state
        
    Returns:
        "continue" to keep iterating, "end" to finish
    """
    print(f"\n⚖️  DECISION: Score={state.score}, Iteration={state.iteration}")
    
    if state.score >= settings.quality_threshold:
        return "end"
    elif state.iteration >= settings.max_iterations:
        return "end"
    else:
        return "continue"