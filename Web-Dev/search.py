import os
import json
from google import genai
from google.genai import types


client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

RECIPE_SCHEMA = {
    "type": "object",
    "properties": {
        "url": {"type": "string"},
        "name": {"type": "string"},
        "author": {"type": "string"},
        "source": {"type": "string"},
        "rating": {"type": "number"},
        "reviews": {"type": "integer"},
        "prepT": {"type": "string"},
        "cookT": {"type": "string"},
        "totalT": {"type": "string"},
        "servings": {"type": "string"},
        "calories": {"type": "string"},
        "category": {"type": "string"},
        "cuisine": {"type": "string"},
        "description": {"type": "string"},
        "ingredients": {
            "type": "array",
            "items": {"type": "string"}
        },
        "notes": {"type": "string"}
    },
    "required": [
        "url", "name", "author", "source", "rating", "reviews",
        "prepT", "cookT", "totalT", "servings", "calories",
        "category", "cuisine", "description", "ingredients", "notes"
    ]
}


def generate_recipe(query: str) -> dict:
    prompt = f"""
Generate one recipe for this request: {query}.

Return a realistic cooking recipe as JSON only.
Use a stable recipe-style URL slug.
If a field is unknown, still provide a reasonable value.
""" 
    if not query or len(query) > 100:
        return "Invalid input"

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_json_schema=RECIPE_SCHEMA,
        ),
    )

    recipe_data = json.loads(response.text)

    # Convert ingredients list to the JSON string for the current database column
    recipe_data["ingredients"] = json.dumps(recipe_data["ingredients"])

    return recipe_data