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

# Below is all the variables! They aren't needed now but will come in handy later.

$ mpoint = 0
$ rpoint = 0
$ fpoint = 0
$ ipoint = 0
$ ghpoint = 0
$ pepoint = 0
$ prpoint = 0
$ spoint = 0
$ gpoint = 0
$ cpoint = 0
$ dipoint = 0
$ sepoint = 0

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

    show doppio_neutral

    "More talking just kept going back and fourth and back and fourth. You felt like you almost couldn't breath with the whole squad acting up."

    # Risotto Insult Below! Right when things stop

    "Then, everyone immediately shut up as a large figured jingled over menacingly. He looked to be 6'8. You knew who this man was immediately."

    r "Doppio, right?"

    "Risotto Nero, the leader of La Squadra."

    # Goofy refernce Below

    show doppio_smile

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

        "You decided to go with the man, the myth, the legend himself. Who else was there to choose? Well, there were a bunch of way too crazy assassins and he had nice tiddies."

        d "Risotto."

        "All of the people who considered him higher in rank seemed to understand. Somewhere a little jealous, most notably the creeps, but it seemed to be overwhelmingly okay-ed."

        r "Hm."

        scene la_squadra_hideout

        "He motioned for you to followed as he got you two clear from the door. Upfront was a concrete-walled room with some green couches. Pretty simple but well used and loved."

        r "This is the meeting room. Normally everyone huddles here when its time for their paychecks."

        "He quieted back down rather fast. The little bits of his baritone was nice but it's nice that he just lead you from one place to the other rather than giving you too much information. Up next was the kitchen, of which he just let out a noise of acknowledgment."

        "He was polite but good lord it was like talking to a brick wall with fat tits."

        menu:

            "Start a conversation.":
                jump choicer1_yes

            "Let him stay silent.":
                jump choicer1_no

                label choicer1_yes:

                    d "So. . . How's the weather up there?"

                    show doppio_crack

                    "Shit. Wrong thing."

                    d "I mean weather in gen-"

                    "You hear a groan. Yeah he this isn't his first time hearing this."

                    r "It's raining."

                    "And with that, you were a little bit soggier with some spit. Now was that hot or was that just gross?"

                    show doppio_gasp

                    "That was probably just karma."

                    jump choicer1_done

                label choicer1_no:

                    "Might as well not invote his rage."

                    jump choicer1_done

        label choicer1_done:

        show doppio_smile

        jump choice2_done

    label choice2_pe:

        "You look across the group of hit men and notice a nervous yet excited man with a odd looking head. you remember from his file he has quite the effective stand that paired with his brothers, is almost unstoppable."

        d "Pesci."

        "The man look very excited, happy that he was picked, grinning like a little kid. the others looked suprised and some looked disappointed."

        p "Come on this will be fun!"

        "He grabs you by the hand, pulling you like a hyper four year old."

        d "Hey! Whoa-"

        "You're dragged out of the room."

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

        "Your attention is quickly caught by the scantily clad man in enough purple to make a little girl weep of pure joy. You notice his mask and your mind quickly scratches off anything to do with him being around kids as you remember his stand and his name. You couldn't resist asking him for the tour though."

        d "Melone."

        "The other assassins looked at you like you had just asked for a clown to lead you around. Some had looks of pity, while others were trying to hold back laughter. Oh, you just got yourself into something."

        show doppio_happy at left

        show melone_smile at right

        m "Di molto! Come with me."

        "He dragged you along to the next room by the wrist, pulling out a piece of paper and a pen that you don't want to think much about where he pulled them out of."

        scene la_squadra_hideout

        show doppio_neutral at left

        show melone_smile at right

        m "So this is the common room. We mostly have our meeting, payment, and such here when Rizzy calls us all together. What's your birthday?"

        "The question threw you off guard but it won't hurt to answer."

        d "June 24."

        m "Oh, so you're a Cancer like Pesci. Probably could've expected that. And your birthday... Di molto! Now, come this way."

        "You didn't have time to react as you were next dragged into the kitchen, which was quite obviously so as Melone just scribbled something down on the paper."

        m "So here is the kitchen, if you can't tell. What year were you born?"

        "That's a bit odd. You have to wonder, but it's just when you were born. You did look rather young after all."

        menu:

            "1967":
                jump choicem1_67

            "1981":
                jump choicem1_81

                label choicem1_67:

                    d "I was born in 1967"

                    m "Interesting... What kind of moisturizer do you use?"

                    d "I don't use one."

                    jump choicem1_done

                label choicem1_81:

                    d "I was born in 1981."

                    m "So you're 18? Guess they got you started young."

                    jump choicem1_done

        label choicem1_done:

        "Next up he drags you to a hallway where each door has something marked as he kept writing. It's quite easy to tell who's is who's as Melone kicks open the bathroom door and walks inside. You notice the distinct lack of a mirror."

        m "This is the bathroom, you can put your toiletries under the sink or in the shower. Anyway, what's your blood type?"

        "You could spot the trend."

        menu:

            "What's with all these questions?":
                jump choicem2_what

            "Blood":
                jump choicem2_whatevertypeheendsuphavingidfk

            "Red.":
                jump choicem2_red

                label choicem2_what:

                    show doppio_neutral at left

                    show melone_smile at right

                    "You were getting a bit angry at all this."

                    d "What's with all these questions?"

                    m "I'm just trying to get to know you better. Rizzy didn't let me read your file. Something about privacy. I guess it might be"

                    jump choicem2_done

                label choicem2_whatevertypeheendsuphavingidfk:

                    d "Blood."

                    m "Di molto! Just as I expected. This is perfect."

                    jump choicem2_done

                label choicem2_red:

                    d "Oh, it's red!"

                    show doppio_happy at left

                    show melone_ugh at right

                    "He gives this look that implied he was about to call you a slur but held back. Too bad you were right! He did write something else down though."

                    jump choicem2_done

        label choicem2_done:

        scene la_squadra_rooms

        show doppio_neutral at right

        show melone_smile at left

        "He skips out the door and goes to open more down the line. First the one with one of those singing bass signs on the outside. Locked. Then once that had this very elegant look to it but the distinct smell of shit. Locked. The one with the do not disturb sign written in doctor's handwriting was skipped. Must have been Melone's. "

        "This trend kept on going with him getting progressively poutier. He did open one with what looked to be some snowflake details, but promptly got. . ."

        gh "FUCK OFF MELONE!"

        "Ah. Everyone knew he was coming. At least almost everyone. He managed to open a door with loud hissing coming from behind. Ah, poor bastard."

        m "Di molto! Formaggio left his room unlocked."

        "A grey cat came running out, hissing at the two of you."

        m "Hello to you too, Anal."

        "Melone walked in like he owned the place. strutting over and looking into some things."

        m "Oh well, this is Formaggio's room. By the way, do you happen to know what time you were born?"

        menu:

            "No.":
                jump choicem3_no

            "Cut it out.":
                jump choicem3_cut

                label choicem3_no:

                    d "No, I'm sorry."

                    m "I guess that's just how it goes sometimes."

                    jump choicem3_done

                label choicem3_cut:

                    show doppio_angy at right

                    show melone_upset at left

                    d "Cut it out with the questions!"

                    m "Oh, don't be such a prune, Doppio. This is going to help you."

                    "Bastard."

                    jump choicem3_done

        label choicem3_done:

        "He continued to look around for a bit until he seemed to have a look of frustration on his face. He popped on up."

        m "Come now, let me show you to your room."

        "Melone never gave you time to respond, which seemed to be a growing trend. He led you to a barren room with some furniture practically at the end of the hall if it weren't for the room at the end with another do not enter sign."

        m "This is where you'll be staying from now on, Doppio. If you wouldn't mind, could I look at your palm?"

        menu:

            "I would mind.":
                jump choicem4_no

            "Uh sure.":
                jump choicem4_yes

                label choicem4_no:

                    d "I would mind."

                    show doppio_angy at left

                    show melone_tongue at right

                    "He looked defeatedly at your shoes. Why it was your's he was looking at. You couldn't figure out until he licked his lips. Foot fucker."

                    $persistent.unlock_m1bad = true

                    show screen txt ("Achievent unlocked! Hahahahaha. Shut up!")

                jump choicem4_done

                label choicem4_yes:

                    show doppio_happy at left

                    show melone_smile at right

                    d "Uh, sure."

                    "You sat down on one of the covered pieces of furniture as he began to inspect it. You were beginning to expect the vocal tic. Low and behold. . ."

                    m "Di molto!"

                    "And you too just sat like that for a bit. Him holding your hand and inspecting it. He seemed to have such a close fascination."

                    "Every once and a while he would turn to take a note or two and then go back to inspecting it."

                    "Honestly, his hands were much softer then you'd ever guess that they'd be. They smelt vaguely of lavender too. He had to be using some sort of lotion on them."

                    "But it was still much nicer to watch him as seemed to discover things in your hand. Even though there was a small part of you who wanted to strangle him for poking his nose into things."

                    "But you ignored it."

                    "Eventually he got up though, he did look at you with a small smile though."

                    $persistent.unlock_m1good = true

                    show screen txt ("Achievent unlocked! 50 First Dates.")

                    jump choicem4_done

        label choicem4_done:

        m "I guess it would be time for me to get heading out so you can start organizing."

        "And with that, he pranced out and shut the door."

        jump choice2_done

        label choice2_gh:

            "Looking over the group, they all seem to be somewhat scowling at you. Their lips pursed with what you'd call 'professional distaste'. Asking for a tour of the establishment was going to be a challenge from every one of them, but its a challenge you must overcome for now."

            "Through the serious, stoic and stone cold faces of the group, one stood out to you in particular, the familiar blue haired hothead of the group, clad in all white and his signature red glasses, Ghiaccio."

            d "Ghiaccio."

            "As soon as you vocalised your choice, you notice a quick yet obvious change in the air around you. Snickers were heard and small cracking smiles could be seen from the group as the aforementioned ice powered hot head began twitching and shaking like a dodgy Nokia cell phone. Gripping his temples he gritted his teeth and let out an angered cry of annoyance, obviously he wasn't happy about being tasked with this, but hey, he didn't have a choice now did he?"

            "This was going to be fun."

            "The group looked over at the seething blue hairball with legs throwing a temper tantrum with both a look of pity and amusement."

            "With a final frosty huff, he straightened himself out. Not calm, but just relaxed enough on the outside to present himself as normal. "

            gh "Fine. Don’t fuckin’ mock me with stupid questions while you’re here"

            "You nod as he drags his feet on the ground as he walked, hands stuffed in his pockets, not bothering with any nonchalant chatter as he lead you through the building."

            gh "This is the meeting room, where people keep leaving cards, pins and random crap everywhere!?"

        menu:
            "I would mind.":
                jump choicegh1_is

            "Say nothing":
                jump choicegh1_not

            "It’s…nice?":
                jump choicegh1_nice

                "Ghiacchio turns to you, his eyes blazing. You’d be surprised if he hadn’t melted those glasses to his face. Pinching his temples, he stomps, looking like he would rip his own and possibly your hair out."

                gh "YES. IT IS, BUT IT WOULDN’T BE IF EVERYONE PICKED UP AFTER THEIR SHIT. WE’RE ASSASINS FOR FUCKS-SAKE, AND THEY CAN’T PICK UP AFTER THEMSELVES. IT PISSES ME OFF DAMN IT!"

                "He doesn't pick anything up, instead he does the opposite and starts curb stomping it into the floor, crushing the box of cards under his thickly soled sneaker."

                "This serves as just enough of an indicator for you to quietly shuffle back."

                "After his little tantrum, he returns to you and grumpily continues the tour of the hideout."

                label choicgh1_is:

                jump choicegh1_done

                label choicegh1_not:

                gh "Good. Glad you aren't annoying."

                jump choicegh1_done

                label choicgh1_nice:

                "Ghiacchio glared at you, only seething and muttering something incoherent, before continuing to take you around the house."

                gh "Don't sugar coat shit with me. I’m already going out of my way to do this, I don’t want to deal with some kiss-ass shit while I’m doing it."

                jump choicegh1_done

        label choicegh1_done:

            jump choice2_done

        label choice2_i:

            d "Illuso."

            i "Heh, okay."

            jump choice2_done

        label choice2_sg:

            "You gaze upon the group and notice the inseparable couple. Sorbet and Gelato you remember from their files, quite the names for quite the assassins. They have this ever prevailing look on their faces. Its like they are plotting something. You just can't help but chose them as your guides."

            d "Sorbet and Gelato."

            "The two looked to be a bit surprised by this action, but have appear to be happy to be chosen alongside one another. The men were practically doing it in every photo you saw and they keep up the reputation now. You just had to choose both."
            "You look to the other teammates for their reactions. Some were suprised, others had a look of pity, and some even had a facial expression to match the couple."

            s "Well, come on then, we don't have all day."

            g "I guess not, isn't that right, new guy?"

            "Gelato seemed to have some mockery in his tone, but the fact he was holding onto Sorbet like a baby koala didn't help the intimidation much."

            d "Mhm."

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
