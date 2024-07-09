import random

def generate_story(user_input):
    # Parse user input (e.g., genre, theme, characters)
    genre = user_input['genre']
    theme = user_input['theme']
    characters = user_input['characters']

    # Create a story template
    story_template = """
    Once upon a time, in a {genre} world,
    there lived a {character1} named {name1}.
    {character1} lived in a {location} with {character2}.
    One day, {character1} discovered a {object} that led them on a journey to {destination}.
    Along the way, they encountered {obstacle} and had to use their {skill} to overcome it.
    In the end, {character1} learned a valuable lesson about {theme}.
    """

    # Generate random values for the story template
    name1 = random.choice(["Alice", "Bob", "Charlie"])
    character1 = random.choice(["princess", "wizard", "adventurer"])
    character2 = random.choice(["dragon", "unicorn", "robot"])
    location = random.choice(["castle", "forest", "city"])
    object = random.choice(["magic wand", "ancient scroll", "mysterious artifact"])
    destination = random.choice(["hidden treasure", "secret garden", "lost city"])
    obstacle = random.choice(["dark forest", "fierce monster", "treacherous path"])
    skill = random.choice(["bravery", "intelligence", "agility"])

    # Fill in the story template with the generated values
    story = story_template.format(
        genre=genre,
        character1=character1,
        name1=name1,
        character2=character2,
        location=location,
        object=object,
        destination=destination,
        obstacle=obstacle,
        skill=skill,
        theme=theme
    )

    return story

def generate_choice(story):
    # Parse the user's current story state
    current_state = story.split(".")[-1]

    # Generate a choice based on the current state
    choices = [
        "Go to the castle",
        "Explore the forest",
        "Visit the city"
    ]
    choice = random.choice(choices)

    return choice

def update_story(story, user_input):
    # Parse the user's choice
    choice = user_input['choice']

    # Update the story based on the choice
    if choice == "Go to the castle":
        story += " They arrived at the castle and met the king."
    elif choice == "Explore the forest":
        story += " They ventured into the forest and encountered a wild animal."
    elif choice == "Visit the city":
        story += " They traveled to the city and discovered a hidden market."

    return story