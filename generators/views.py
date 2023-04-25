from django.shortcuts import render

from .npc_names import gen_npc_name, gen_npc_name_by_syllables

# Create your views here.


def npc_name(request):
    gen_name = gen_npc_name_by_syllables()

    ancestries = ["Dwarf", "Elf", "Goblin", "Halfling", "Half-Orc", "Human"]
    name_per_ancestry = {anc: gen_npc_name(anc) for anc in ancestries}

    return render(
        request,
        template_name="generators/npc_names.html",
        context={"gen_name": gen_name, "names_dict": name_per_ancestry},
    )
