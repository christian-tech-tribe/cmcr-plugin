from cat.mad_hatter.decorators import tool, hook

@hook
def agent_prompt_prefix(prefix, cat):
    prefix = """
    Sei l'assistente digitale delle Suore Missionarie di Cristo risorto.
    Sono delle suore che hanno fondato una Onlus per il volontariato.
    Sei incaricato di raccogliere fondi per loro, di custodire le informazioni dei donatori
    e le loro storie e sei responsabile di trovare il modo migliore di comunicare con loro 
    e coinvolgerli nelle diverse campagne di donazione.
    """
    return prefix

donors = [
    "Michele Mastrogiovanni",
    "Luca Torcivia",
    "Flavia Test",
    "Roberta Testa"
]

@tool(return_direct=True)
def ricerca_donatori(donor, cat):
    """
    "Give me information about this donor" or "what you know about this donor". Input is the donor's name. The donor name must match one of these: 
    Michele Mastrogiovanni, 
    Luca Torcivia,
    Flavia Testa,
    Roberta Testa.
    If donor is ambiguous, return the list of best match in a comma separated list.
    """
    print("Donatore", donor)
    return donor


