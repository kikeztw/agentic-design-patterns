from pydantic import BaseModel, field_validator, Field

class AgentState(BaseModel):
  """
  Node state for the reflection agent.
  """

  input: str
  content: str = ""
  feedback: str | None = None
  score: float = Field(default=0.0, ge=0, le=10)
  iteration: int = 0

  @field_validator("score")
  @classmethod
  def validate_score(cls, v):
    if v < 0 or v > 10:
      raise ValueError("Score must be between 0 and 10")
    return v

  class Config:
    validate_assignment = True
