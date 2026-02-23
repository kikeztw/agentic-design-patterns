# test_config.py
from config import settings

print("✅ Configuración cargada:")
print(f"   API Key: {settings.openai_api_key[:10]}...")
print(f"   Model: {settings.model_name}")
print(f"   Max Iterations: {settings.max_iterations}")
print(f"   Quality Threshold: {settings.quality_threshold}")
