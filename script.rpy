# The script of the game goes in this file.

# Below has all the characters with easier ways to call them. We can add color later and easier!

define m = Character("Melone")
define r = Character("Risotto")
define f = Character("Formaggio")
define i = Character("Illuso")
define gh = Character("Ghiaccio")
define pe = Character("Pesci")
define pr = Character("Proscuitto")
define s = Character("Sorbet")
define g = Character("Gelato")
define c = Character("Cioccolata")
define se = Character("Secco")
define di = Character("Diavolo")
define d = Character("Doppio")

# The game starts here.

label start:

    # Introduction Paragraphs

    scene clouds

    "Today's the day, a very special day in fact."
    "Though it seems mundane, with a shimmering sun, beaming down on the green grass and multicoloured flowers that lines sidewalks and studded garden hedges. With a blue sky so clear and clouds so fluffy, one could think it was a painting."
    "A mundane day at best for any normal person, though you aren't normal, are you?"
    "A phone call had greeted you a few weeks prior, explaining the details of your mission for today. You had eagerly waited to complete it, spending all that time mulling it over in your mind, trying to plan out every move and every possible outcome."
    "Though in the light of the rather small room you stayed in, those thoughts were never left solved or set in stone, until today."
    "Today's the day, you, Vinegar Doppio, have to go check up on La Squadra Ezecusioni, the assassins team of Passione. As the boss's right hand, he thought of no better person than you to tackle this head on."
    "La Squadra's relations with the boss are complicated, far to complicated for you to worry about right now, the one thing you're after here is information on the group as a whole."
    "The boss mentioned traitors, so, like you affirmed, you're going to do your best to sniff any of them out as they come."

    scene street

    "A cool wind buffeted the trees and bushes that lined the streets you crossed to get here. Despite it being sunny, you felt a creeping frost slither its way up your spine, chilling you to the core."
    "Passing house by house, business by business, they all looked the same, those buildings, all peach and brick red in colour, with square windows that cats and birds would lay on and bathe in the warm summer glow."
    "Reaching the place on your map, you feel cold and stiff. This was it, this was what you'd been waiting for, isnt it? This division were as unpredictable as they were efficient, one wrong move and it could all be over for you."
    "Mucking up the courage, you step up the bumpy, uneven path. your shoes clacking against the rocks as they rolled under your weight."

    scene hideout_closed

    "The place was intimidating, a tall building, casting a long shadow on what little surroundings it had, though, you felt a certain calmness that whatever happens, the boss has his faith in you, and with that you cannot fail."
    "Taking a deep breath in and out through the mouth, you bring down your fist onto the door.."
    "Only to have it swing open as you do."

    # This is where Dop gets to meet the group, starting with Formaggio

    scene hideout_open

    show doppio_gasp

    d "Huh?"

    f "Oh! You're the new guy..."

    show doppio_neutral

    # A simple red hearing, maybe it could be used in routes that include missions?

    python:
        name = renpy.input(_("What's your alias?"))

        name = name.strip() or __("Aceto")

    d "[name]."

    f "[name]?"

    "He lets out a casual laugh. What?"

    f "Oh, Vinny, were you not told that we knew your name? I was just trying to fuck with you."

    # The first choise! Like to try to keep them orgnaized with easy to remember names

    menu:

        "No. . .":
            jump choice1_no

        "Yeah, I was just trying to fuck with you.":
            jump choice1_yes

        "Vinny?":
            jump choice1_vinny

    label choice1_no:

        show doppio_sad

        d "No. . ."

        f "Ah man, that sucks, but atleast your real name isn't [name]."

        f ". . ."

        f "Right?"

        d "It's not."

        jump choice1_done

    label choice1_yes:

        show doppio_smile

        d "Yeah, I was just trying to fuck with you."

        f "Oh, I like your style already."

        jump choice1_done

    label choice1_vinny:

        d "Vinny?"

        f "I just though it was a cool name, amirite?"

        d "Um. . ."

        "Before you could object or comply he cuts you off."

        jump choice1_done

    label choice1_done:

    show doppio_smile

    # Here is where the chaos kicks off. The show command will be used and changed very fast.

    f "Oh, I'm Formaggio by the way, everyone will be coming around soon enough."

    gh "MELONE YOU PIECE OF SHIT MOTHER FUCKER, WHAT THE FUCK? YOU DON'T COOK IT THEN PUT THE TOPPINGS ON! YOU DO IT IN ONE GO! YOU DON'T SHIT, FLUSH, AND THEN TAKE A PISS!"

    m "Mhm, oh, you are the new guy! Doppio, right? Oh Di Molto!"

    gh "JESUS, MELONE, ARE YOU EVEN LISTENING TO ME?"

    m "Yeah, yeah, Ghiaccio look over here."

    gh "Oh, you're the new guy, huh?"

    d "Yeah-"

    pr "God, do you guys ever stop fighting?"

    pe "Fra! Illuso is bulling me for drinking milk!"

    i "Damn right I am!"

    pr "Well you did you consider that you deserve it?"

    "You struggled to get another word in, what's going on?"

    f "Be nice to our sexy beast, Pro."

    gh "What the everloving FUCK?"

    m "Ok, not even I can explain that."

    s "What is going on here?"

    "You tried to speak up again but the talking never stopped."

    g "The new guy has arrived it seems."

    s "Well it looks like he might not last that long."

    "More talking just kept going back and fourth and back and fourth. You felt like you almost couldn't breath with the whole squad acting up."

    # Risotto Insult Below! Right when things stop

    "Then, everyone immediately shut up as a large figured jingled over menacingly. He looked to be 6'8. You knew who this man was immediately."

    r "Doppio, right?"

    "Risotto Nero, the leader of La Squadra."

    # Goofy refernce Below

    d "Yes. I am."

    "He looked you up and down as other memebers either echoed it or fidgeted to themselves."

    r "Do you have a preference for who gives you a tour? You should already know who everyone is from our files."

    # Should the tours be kinda like a tutorial section or an impact to the routes?

    # Also note the abbrivations!

    menu:

        "You.":
            jump choice2_r

        "Pesci.":
            jump choice2_pe

        "Proscuitto.":
            jump choice2_pr

        "Formaggio.":
            jump choice2_f

        "Melone.":
            jump choice2_m

        "Ghiaccio.":
            jump choice2_gh

        "Illuso.":
            jump choice2_i

        "Sorebt and Gelato.":
            jump choice2_sg

    label choice2_r:

        d "Ypu."

        r "Hm."

        jump choice2_done

    label choice2_pe:

        d "Pesci."

        pe "Oh! Uh. Me? Really?"

        jump choice2_done

    label choice2_pr:

        d "Proscuitto."

        pr "Ok, come with me."

        jump choice2_done

    label choice2_f:

        d "Formaggio."

        f "Hell yeah! Let's get moving, Vinny."

        jump choice2_done

    label choice2_m:

        d "Melone."

        m "Di molto!"

        jump choice2_done

    label choice2_gh:

        "Looking over the group, they all seem to be somewhat scowling at you. Their lips pursed with what you'd call 'professional distaste'. Asking for a tour of the establishment was going to be a challenge from every one of them, but its a challenge you must overcome for now."
        "Through the serious, stoic and stone cold faces of the group, one stood out to you in particular, the familiar blue haired hothead of the group, clad in all white and his signature red glasses, Ghiaccio."

        d "Ghiaccio."

        "As soon as you vocalised your choice, you notice a quick yet obvious change in the air around you. Snickers were heard and small cracking smiles could be seen from the group as the aforementioned ice powered hot head began twitching and shaking like a dodgy Nokia cell phone. Gripping his temples he gritted his teeth and let out an angered cry of annoyance, obviously he wasn't happy about being tasked with this, but hey, he didn't have a choice now did he?"
        "This was going to be fun."

        jump choice2_done

    label choice2_i:

        d "Illuso."

        i "Heh, okay."

        jump choice2_done

    label choice2_sg:

        d "Sorbet and Gelato."

        g "I wasn't expecting you to choose that."

        s "I guess we might as well start before anything else."

        jump choice2_done

    label choice2_done:

    # This is my testing grounds! Basically just to make sure everything works.

    scene la_squadra_hideout

    show doppio_crack

    "You reach over, give a hard slap to Risotto's fat ass."

    d "Buenos dias, Risotto."

    "He snaps your fucking neck like a twig."

    # This next command ends the game. Fancy.

    return
