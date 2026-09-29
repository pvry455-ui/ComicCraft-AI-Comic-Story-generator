import json


def generate_outline(user_prompt: str) -> list:
    """
    Generate a structured 5-panel comic outline
    based on the user's story idea.
    """

    if not user_prompt or not user_prompt.strip():
        return []

    return [
        {
            "panel": 1,
            "title": "The Beginning",
            "scene_description": f"The story begins with: {user_prompt}",
            "image_prompt": "Comic book style opening scene, cinematic composition"
        },
        {
            "panel": 2,
            "title": "The Problem",
            "scene_description": "The main character discovers a problem or challenge.",
            "image_prompt": "Comic book style scene showing a dramatic challenge"
        },
        {
            "panel": 3,
            "title": "The Conflict",
            "scene_description": "The main character faces the main conflict.",
            "image_prompt": "Dynamic comic book action scene with dramatic lighting"
        },
        {
            "panel": 4,
            "title": "The Solution",
            "scene_description": "The main character finds a way to solve the problem.",
            "image_prompt": "Comic book hero overcoming the challenge"
        },
        {
            "panel": 5,
            "title": "The Ending",
            "scene_description": "The story reaches a satisfying conclusion.",
            "image_prompt": "Happy comic book ending scene, cinematic style"
        }
    ]
