from app import db, Recipe, app

def add_recipe(title, ingredients, instructions):
    with app.app_context():
        recipe = Recipe(title=title, ingredients=ingredients, instructions=instructions)
        db.session.add(recipe)
        db.session.commit()

# Example recipes
add_recipe("Adobo", "Chicken, soy sauce, vinegar", "1. Marinate chicken in soy sauce and vinegar. 2. Cook until done.")
add_recipe("Sinigang", "Pork, tamarind, vegetables", "1. Boil pork with tamarind. 2. Add vegetables. 3. Simmer until cooked.")
# Add more recipes as needed
