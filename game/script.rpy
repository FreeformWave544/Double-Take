define Kaz = Character("Kaz")
define n = Character("Narrator", color="#8492a6")

label start:
    menu:
        "Detective?":
            jump Kaz
        "Kasper?":
            jump Kasper

label Kaz:
    "???" "Kaz! Wake up!"
    "???" "You've got a new case!"
    n "You groan awake."
    Kaz "What kind of case?"




# ====================
# =======KASPER=======
# ====================

define Kasper = Character("Kasper")

label Kasper:
    $ n = Character("Narrator", color="#ec3750")
    n "You're running through a dark alley way."
    n "Nothing but a bath robe covering you..."
    n "How did you end up like this?"
    Kasper "How did I end up like this?"
    Kasper "How did I... even get here...?"
    "???" "Kasper! Why did you do it?"
    n "You look back to see a boy, who seems your age, blood covering his hands, and tears rinsing it from his face."
