# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    "Creditos de arte a: https://puppetbomb.itch.io/
    Image Pack : College Life
    Sitio web: https://puppetbomb.itch.io/college-students-sprite-pack"
    "Licencia CC No comercial y con atribución
    E-mail : puppetbomb@gmail.com"
    "Música: YannZ / Yanni Ziangos 
    Sitio web: https://yannz41.itch.io/contemplative-fantasy-music-pack
    Email: yziango@gmail. 
    Licencia CC No comercial y con atribución"

    pause 2.0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg hallway

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show an body at right

    "Hola mundo!"

    show m body at left

    "No me llamo mundo"

    play music "Déjà Vus (in-game OST loop).ogg"

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
