from django.shortcuts import render

from .npc_names import gen_npc_name, gen_npc_name_by_syllables
from .chargen import roll_stats
from .forms import ClassChoiceForm

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


def get_stats(request):
    stats, total = roll_stats()
    context = {"stats": stats, "total": total, "form": ClassChoiceForm}
    return render(request, template_name="generators/get_stats.html", context=context)
