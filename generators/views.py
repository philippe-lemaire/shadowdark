from django.shortcuts import render, redirect

from .npc_names import gen_npc_name, gen_npc_name_by_syllables
from .chargen import roll_stats
from .forms import ClassChoiceForm
from .chargen import PC_Character
from .game_facts import talents_dict

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
    stats, best = roll_stats()
    context = {"stats": stats, "best": best, "form": ClassChoiceForm()}
    request.session["stats_d"] = stats
    return render(request, template_name="generators/get_stats.html", context=context)


def create_PC(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ClassChoiceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            ancestry = int(form.cleaned_data.get("ancestry"))
            background = int(form.cleaned_data.get("background"))
            class_ = int(form.cleaned_data.get("class_"))
            stats_d = request.session.get("stats_d")
            character = PC_Character(stats_d, ancestry, background, class_)
            stats_zip = character.get_stats()
            talents = talents_dict.get(character.class_)

            return render(
                request,
                template_name="generators/display_character.html",
                context={
                    "character": character,
                    "stats_zip": stats_zip,
                    "talents": talents,
                },
            )
    else:
        return redirect(get_stats)
