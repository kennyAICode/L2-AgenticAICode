from persona import Persona, respond


BEGINNER = Persona("Maya", "beginner tutor", "warm and simple", ("Use an analogy",))
EXPERT = Persona("Arun", "software architect", "precise and technical", ("Mention trade-offs",))


if __name__ == "__main__":
    question = input("Question for both personas: ")
    for persona in (BEGINNER, EXPERT):
        print(f"\n{persona.name}:\n{respond(persona, question)}")
