"""
Stage 2: Ingredient Data Class
==============================
Concepts: Classes, dataclasses, type hints

To test your work:
    uv run python stages/stage2_ingredient.py

Your Task:
----------
Create an Ingredient dataclass that represents a single analyzed ingredient.

Learning Objectives:
- Use the @dataclass decorator
- Define class attributes with type hints
- Understand when to use dataclasses vs regular classes
- Use default values in dataclass fields
"""

from dataclasses import dataclass, field
from typing import Optional, Literal


@dataclass
class Ingredient:
    name: str
    category: Literal["healthy", "moderate", "harmful", "unknown"] = field(default= "unknown")
    health_score: Literal[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10] = field(default= 5)
    description: str = field(default="No information available")
    found_in_database: bool = field(default=False)

    """
    Represents a single ingredient with its health analysis.

    Requirements:
    1. Define the following fields with appropriate types:
       - name: str (the ingredient name, required)
       - category: str (one of "healthy", "moderate", "harmful", or "unknown")
       - health_score: int (0-10 scale, where 10 is healthiest)
       - description: str (explanation of why it's healthy/harmful)
       - found_in_database: bool (whether the ingredient was found in our database)

    2. Set sensible default values:
       - category should default to "unknown"
       - health_score should default to 5
       - description should default to "No information available"
       - found_in_database should default to False

    Example usage:
        >>> ing = Ingredient(name="sugar")
        >>> ing.name
        'sugar'
        >>> ing.category
        'unknown'

        >>> ing2 = Ingredient(
        ...     name="water",
        ...     category="healthy",
        ...     health_score=10,
        ...     description="Essential for hydration",
        ...     found_in_database=True
        ... )
        >>> ing2.health_score
        10
    """

    # ============================================================
    # TODO: YOUR CODE HERE
    # ============================================================
    # Define the dataclass fields below.
    #
    # Hints:
    # 1. Use type hints for each field (e.g., name: str)
    # 2. For default values, simply assign them (e.g., category: str = "unknown")
    # 3. Required fields (no default) must come before fields with defaults
    #
    # Delete the placeholder below and define your fields:

    #name: str = "__NOT_IMPLEMENTED__"

    # Add the remaining fields here:
    # category: str = ...
    # health_score: int = ...
    # description: str = ...
    # found_in_database: bool = ...

    # ============================================================


def create_unknown_ingredient(name: str) -> Ingredient:
    return Ingredient(name=name)
    """
    Factory function to create an Ingredient that wasn't found in the database.

    Args:
        name: The ingredient name

    Returns:
        An Ingredient instance with default "unknown" values

    Example:
        >>> ing = create_unknown_ingredient("mystery powder")
        >>> ing.name
        'mystery powder'
        >>> ing.found_in_database
        False
    """
    # ============================================================
    # TODO: YOUR CODE HERE
    # ============================================================
    # Create and return an Ingredient instance with:
    # - The given name
    # - All other fields at their default values
    #
    # This should be a single line once your Ingredient class is defined!
    #
    # Delete the line below and write your implementation:
    #return Ingredient()
    # ============================================================


def is_implemented() -> bool:
    """Check if this stage is implemented."""
    try:
        ing = Ingredient(name="test")
        return (
            ing.name != "__NOT_IMPLEMENTED__"
            and hasattr(ing, "category")
            and hasattr(ing, "health_score")
            and hasattr(ing, "description")
            and hasattr(ing, "found_in_database")
        )
    except Exception:
        return False


if __name__ == "__main__":
    print("Testing Ingredient dataclass...")

    ing1 = Ingredient(name="sugar")
    print(f"\nIngredient with only name:")
    print(f"  name: {ing1.name}")
    print(f"  category: {getattr(ing1, 'category', 'NOT DEFINED')}")
    print(f"  health_score: {getattr(ing1, 'health_score', 'NOT DEFINED')}")

    print("\nIngredient with all fields:")
    ing2 = Ingredient(
        name="water",
        category="healthy",
        health_score=10,
        description="Essential for hydration",
        found_in_database=True,
    )
    print(f"  {ing2}")

    print("\nUsing create_unknown_ingredient():")
    unknown = create_unknown_ingredient("mystery powder")
    print(f"  {unknown}")
