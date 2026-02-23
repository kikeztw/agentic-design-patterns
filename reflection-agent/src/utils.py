# src/utils.py
import json
import re
from typing import Dict, Any


def parse_json_response(response: str) -> Dict[str, Any]:
    """
    Parsea la respuesta JSON del LLM.
    
    Args:
        response: Respuesta del LLM (puede contener markdown)
        
    Returns:
        Diccionario con los datos parseados
        
    Raises:
        ValueError: Si no se puede parsear el JSON
    """
    try:
        # Intenta parsear directamente
        return json.loads(response)
    except json.JSONDecodeError:
        # Si falla, intenta extraer JSON de markdown code blocks
        # Busca ```json ... ``` o ``` ... ```
        json_match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', response, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
            return json.loads(json_str)
        
        # Si aún falla, intenta encontrar cualquier objeto JSON
        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(0))
        
        raise ValueError(f"No se pudo parsear JSON de la respuesta: {response}")
