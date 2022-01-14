# GREEN FEEDER is a program that willhelp you to grow your indoor plants and flowers in a more efficient way
# by reminding the user to water the plants.
# class GREEN_FEEDER():
import sys
from plyer import notification
import time
import winsound
# def __init__(self):


def opptions():
    print("\t\t\tWELCOME TO GREEN FEEDER")
    while(True):
        print("\t\tWHAT WOULD YOU LIKE TO TAKE A LOOK AT :")
        print("\t1.PLANTS")
        print("\t2.FLOWERS")
        print("\t3.Shedule Reminders")
        print("\t0.EXIT")
        while(True):
            try:
                plant_or_flower = int(input("ENTER YOUR CHOICE: "))
            except:
                print("ENTER A VALID INPUT")
            else:
                break
        if(plant_or_flower == 1):
            # INDOOR_PLANTS FUNCTION
            INDOOR_plant()

        elif(plant_or_flower == 2):
            # INDOOR_FLOWERS FUNCTION
            INDOOR_flowers()

        elif(plant_or_flower == 3):
            # SHEDULE REMINDER FUNCTION
            HELPER_REMINDER()

        elif(plant_or_flower == 0):
            print("\n\t\t\tHAVE A GOOD DAY :)")
            break
            sys.exit("HAVE A GOOD DAY :)")


def INDOOR_flowers():

    flower = {
        "Begonia": {"About them": "The Begonias are native to moist subtropical and tropical climates. Some species are commonly grown indoors as ornamental houseplants in cooler climates.", "Natural Habitat": "Begonias have been around for ages, and with good reason: This easy-to-grow annual does well in a variety of conditions and needs little to thrive. ", "Preference": "Light shade, rich well-drained soil, ample water, and plenty of fertilizer", "Tips for better growth": "Provide it with light shade, rich well-drained soil, ample water, and plenty of fertilizer—and you’ll be rewarded with stunning flowers and foliage. With so many different shapes, sizes, and colors, begonias have no problem taking the spotlight in any garden setting."},
        "Bromeliads": {"About them": "Most bromeliads are easy to grow either indoors or in the greenhouse. They have attractive forms and leaf colors, and many with flowers that can last for months.", "Natural Habitat": "Bromeliads are either terrestrial or epiphytic in their natural habitat.Epiphytic bromeliads do not live in soil but survive by clinging to a tree or other supports such as rocks.", "Preference": "Bromeliads need in-direct sunlight to grow well and produce flowers, with a few exceptions. Bromeliads prefer temperatures from 60F to 85F to survive and grow well.",    "Tips for better growth": "Proper drainage is essential. The soil mix must be porous enough to allow water to drain off quickly and allow air to reach the roots. It should never be soggy."},
        "African Violet": {"About them": "African violets (Saintpaulia species) are excellent indoor flowering plants. Available in many flower colors, they produce flowers year-round under the proper growing conditions.",    "Natural Habitat": "African violets require a soil mix that is well-drained. Commercially prepared packaged soil mixtures are available for African violets. Excellent plants can be grown in mixtures containing equal parts (by volume) of soil, peat and horticultural-grade perlite.",    "Preference": "Clay or plastic containers are both satisfactory, but the type of container has an important effect on the frequency of watering. Clay pots require more frequent watering than plastic since the amount of evaporation is greater.",    "Tips for better growth": "Decorative glazed pots without drainage holes should not be used due to the lack of drainage. Sterilized soil and containers are important."},
        "Scented Geranium": {"About them": "Annual geraniums are popular for their wide range of brilliant flower color and attractive leaves. They can be grown as bedding plants and in containers on decks and patios, in hanging baskets, or in window boxes. They will grow in every part of South Carolina.", "Natural Habitat": "Plant geraniums outdoors after all danger of frost is past and the soil has warmed.",    "Preference": "Geraniums need at least four hours a day of direct sunlight in order to flourish and flower well. In very hot areas it may be best to give the plants a few hours of shade midday.",    "Tips for better growth": "Water abundantly after planting, and continue to water regularly, allowing the soil to dry out between watering. Never allow the plants to wilt or the leaves will turn yellow and drop off."},
        "Poinsettia": {"About them": "Poinsettias are a classic holiday plant used to decorate homes from November to December. When South Carolinian Joel Poinsett, the first U.S. Ambassador to Mexico, introduced the poinsettia to the United States in 1825, it is doubtful he had any idea how popular this plant would become.", "Natural Habitat": "When kept in an ideal environment, poinsettias will hold their brightly colored bracts for months.",    "Preference": "Once at home, place the poinsettia in a bright location so that it receives at least 6 hours of indirect sunlight each day. Avoid placing poinsettias in areas with excessive heat. The ideal temperature range is between 50 – 70 °F. Keep the soil moderately moist.",    "Tips for better growth": "Never let the soil completely dry out and never leave the plant in standing water. Poinsettias do not need to be fertilized when blooming."},
        "Peace Lily": {"About them": "Peace lilies are attractive indoor foliage plants that also produce showy white flowers. They are one of the few foliage plants that will flower in low light.", "Natural Habitat": "Most peace lilies grow between 1 to 4 feet tall and wide. The cultivar ‘Sensation’ can reach a height of 6 feet with an equal width.Peace lilies are sturdy plants with glossy, dark green oval leaves that narrow to a point. The leaves rise directly from the soil.",    "Preference": "Peace lily will flourish in almost any well-drained potting mix. Soil should be kept moist but not soggy. The soil should dry out between waterings. Excessive drying out can cause the plant to wilt and the leaves and edges to yellow. When watering, use water that is at room temperature.",    "Tips for better growth": "These plants need very little fertilizer. If you fertilize, use a balanced, liquid houseplant fertilizer such as 20-20-20 every two to three months.Peace lilies enjoy warm conditions between 68 and 85 °F during the day and nighttime temperatures about 10 °F cooler.Peace lilies have wide leaves that accumulate dust. Wipe leaves regularly with a damp cloth to remove dustPeace lily will survive low interior light but would prefer bright filtered light. Peace lily should not be placed in direct sun or it will sunburn."},
        "Lipstick Plant": {"About them": "Nothing brightens up a room like a flowering plant. The Aeschynanthus lipstick vine has pointy, waxy leaves and blooms with bright clusters of flowers. Vivid red blossoms emerge from a dark maroon bud reminiscent of a tube of lipstick. Growing lipstick plants is not difficult, and with proper care you get rewarded with continuous flowers.", "Natural Habitat": "You do not have to know a lot about how to care for a lipstick plant (Aeschynanthus radicans) before you take on the task. Soil and nutrients, water, light and temperature all affect your growing success. If you stick to these guidelines, you can be growing lipstick plants before you know it.",    "Preference": "Lipstick plant care begins with airy soil and proper fertilizer,Too much water is disastrous for growing lipstick plants. You should water the plants moderately and be sure not to soak the soil or you risk root rot and fungal problems. Light The Aeschynanthus lipstick vine will not bloom without adequate light. Avoid placing this plant in full shade or full sun. The plant needs bright light for a portion of the day, but not all day long. Temperature Air and soil temperatures must be a minimum of 70 to 80 F. (21-27 C.) for proper blooming. You will get some blooming at 65 F. (18 C.), but it will be limited. At 50 F. (10 C.), you risk chilling, which is an injury that results in dark red leaves.", "Tips for better growth": "If you start growing lipstick plants from cuttings, the optimal temperature is 70 F. (21 C.) for best blossoming. In the spring, the plant can handle a higher level of light. Because it originates in the tropics, the plant likes high humidity."},
        "Jasmine": {"About them": "Jasmine is one of the first plants that comes to mind when one thinks of sweet fragrance. A single jasmine vine can perfume an entire room or garden.", "Natural Habitat": "Plant jasmine near the house or near a walk so its intense fragrance can be enjoyed and so you can watch hummingbirds and butterflies come to the flowers.", "Preference": "All jasmines prefer full sun to partial shade and a warm site. They grow well in regular garden soil with moderate levels of soil fertility and moisture, and they need frequent pinching and shaping to control growth. Low-growing, shrubby kinds make good hedges. Jasmines bush out and should not be jammed together. Set them at least 8 feet apart in shrub borders. Containerized plants are best planted in the fall.", "Tips for better growth": "If plants become infested with spider mites, cut them to the ground after blooming and discard the infested plant material. Feed the crowns to stimulate new growth."},
        "Impatiens": {"About them": "Impatiens have traditionally been one of the most popular bedding plants in the United States because of their beauty and ease to grow. Few annuals that grow in shade provide the range or intensity of color as impatiens. Unfortunately, particular species of impatiens are susceptible to the disease impatiens downy mildew caused by a water mold.", "Natural Habitat": "Impatiens are tender annuals throughout South Carolina. They work well for edging shady beds, mass plantings under trees, window boxes, and hanging baskets.", "Preference": "All types of impatiens do best in a rich, moist soil mulched to maintain adequate moisture. Fertilize monthly with a water-soluble fertilizer.", "Tips for better growth": "Impatiens grow well in containers. Use a soil-less growing mix with good drainage. Impatiens grown in containers need more frequent watering and possibly more fertilizing than those grown in the garden."},
        "Flowering Kalanchoe": {"About them": "Kalanchoe (Kalanchoe blossfeldiana) is a popular houseplant typically available for sale during late winter and spring months. It is a durable flowering potted plant requiring very little maintenance in the home or office. It has dark green, thick waxy leaves with scalloped-edges and small, four-petaled flowers in clusters held above the foliage.", "Natural Habitat": "Kalanchoe grows best in full sun and a well-drained potting media. Kalanchoe will tolerate bright indoor light levels well. However, plants tend to get spindly in low light conditions. Kalanchoe can be damaged by over watering. Allow the soil to dry slightly between waterings. Fertilize actively growing plants with any houseplant fertilizer once a month. Ideal temperatures are 45-65 °F at night and 50-70 °F during the day. Cool night temperatures prolong flower life.",    "Preference": "Recycled pots should be washed thoroughly using a household cleaner and disinfectant. A good rooting medium consists of 50% peat moss and 50% perlite. Normally, peat moss and perlite don’t need sterilization when new.",    "Tips for better growth": "In the home, plant diseases are rarely a problem. Too much or too little water and insects are the main problems. Root rot usually results from a soil mix that does not drain quickly or from overly frequent watering. Do not let plants sit in water. For more information."}}
    while(True):
        print("1. Begonia\n2. Bromeliads\n3. African Violet\n4. Scented Geranium\n5. Poinsettia\n6. Peace Lily\n7. Lipstick Plant\n8. Jasmine\n9. Impatiens\n10. Flowering Kalanchoe\n0.EXIT\n")
        flower_choice = int(input("enter your choice: "))
        if(flower_choice == 1):
            a = "Begonia"
        elif(flower_choice == 2):
            a = "Bromeliads"
        elif(flower_choice == 3):
            a = "African Violet"
        elif(flower_choice == 4):
            a = "Scented Geranium"
        elif(flower_choice == 5):
            a = "Poinsettia"
        elif(flower_choice == 6):
            a = "Peace Lily"
        elif(flower_choice == 7):
            a = "Lipstick Plant"
        elif(flower_choice == 8):
            a = "Jasmine"
        elif(flower_choice == 9):
            a = "Impatiens"
        elif(flower_choice == 10):
            a = "Flowering Kalanchoe"
        elif(flower_choice == 0):
            break
        while(True):
            print(
                "\n1.About them\n2.Natural Habitat\n3.Preference\n4.Tips for better growth\n0.EIXT\n")
            flower_info_choice = int(input("enter you choice: "))
            if(flower_info_choice == 0):
                break

            if(flower_info_choice == 1):
                b = "About them"
            elif(flower_info_choice == 2):
                b = "Natural Habitat"
            elif(flower_info_choice == 3):
                b = "Preference"
            elif(flower_info_choice == 4):
                b = "Tips for better growth"
            else:
                print("NO INFORMATION FOUND REGARDING YOUR INPUT")
            print(f"FLOWER:{a}\n{b}\n{flower[a][b]}\n\n")


def INDOOR_plant():

    plant = {
        "Monstera deliciosa or “Swiss cheese plant": {"About them": "They're one of the most popular indoor plants going around right now. Their lush green leaves with distinctive holes make a stunning statement in any room and they can grow to fit any space", "Natural Habitat": "In its natural habitat, Monsteras like climbing so provide it with some kind of stake or trellis for support.", "Preference": "Monstera plants prefer a warm climate away from direct sunlight and they benefit from regular cleaning with a soft, damp cloth.", "Tips for better growth": "Let the top 4cm of soil dry out between watering as over watering may lead to root rot, signs of this are yellowing or wilting leaves, “For best results Monsteras should enjoy conditions that are fairly moist so avoid artificial heating and cooling, they will require monthly feeding in spring and summer when planted in containers."},
        "Epipremnum aureum or Devil's Ivy": {"About them": "Devil’s ivy, also known as golden pothos or pothos, is a fast-growing and forgiving vine.The leaves are waxy and heart shaped with colouring dependant on cultivar –Wilcoxii are a mottled white and green, Marble Queen have more of a cream and grayish-green colouring, Neon is a shade of bright, light greeny-yellow and Tricolor have green leaves with yellow, light green and cream dappling.", "Natural Habitat": "Suited to any position in the house, these plants are super low-maintenance and absolutely stunning.", "Preference": "They can be potted in hanging baskets or cuttings placed in glass vases.They're highly drought tolerant and don't require regular fertilisation. Water Devil's Ivy deeply once a week and cut back to every other week in winter.",    "Tips for better growth": "Spring and summer is the best time to prune and propagate your plant, placing the cuttings in glass jars of water to encourage rooting."},
        "Dracaena Massangeana or Mass Cane": {"About them": "This plant is popular amongst beginner green thumbs and it’s often an office staple thanks to its hardy nature.This plant is popular amongst beginner green thumbs and it’s often an office staple thanks to its hardy nature.", "Natural Habitat": "Mass Cane often grows between 1.2 to 1.8 metres tall with stalky stems and long, green leaves featuring light yellow and green stripes running through them.", "Preference": " This plant is best placed in indirect bright light but it can tolerate low light. You’ll only need to water it once a week. ", "Tips for better growth": "However it’s important to note that Dracaena 'Massangeana' is toxic to dogs and cats so it’s not the best option if you have furry friends around the house."},
        "Spathiphyllum or Peace lily": {"About them": "Spathiphyllum, commonly known as the Peace Lily, has long been a popular house plant, especially since NASA featured it in its list of best air-purifying options. It has glossy, dark green foliage and stunning white flowers, usually growing between 45 to 65 centimetres tall.", "Natural Habitat": "These tropical plants thrive in bright, indirect light, it can handle low light but that may cause it to bloom poorly.", "Preference": " A peace lily will usually only need to be watered and misted once a week in warmer months, less often in winter. They hate soggy or wet soil and they’re prone to root rot so let the plants dry out a bit between waterings.", "Tips for better growth": "Be sure to wipe down the foliage to prevent dust from building up. Make sure it is kept away from pets or children who may be tempted to chew it, as the plant is poisonous and may cause severe discomfort if ingested. "},
        "Bromeliad": {"About them": "Don’t be intimidated by the Bromeliad. Although once regarded as a plant for the advanced gardener, these beautifully coloured rosette-forming perennials make for easy, low-maintenance houseplants.", "Natural Habitat": "As they are not heavy feeders, you can drop a slow-release fertiliser into the cup of the plant or mix it into the soil, once a season.", "Preference": "When indoors, they need medium to bright light (but not direct sunlight) and do well in shallow pots with fast drainage. You can water the plant by filling the central cup (otherwise known as the tank) of the plant once a week during the warmer months and less during winter.", "Tips for better growth": "Make sure you flush it on a regular basis to prevent water stagnation"},
        "Sansevieria or Mother-in-law’s Tongue": {"About them": "Originating from Southern Africa and Asia, another low-maintenance houseplant is the Snake Plant, otherwise known as Mother-in-law’s tongue. The name refers to the pointed tips of the leaves, symbolising the sharp tongue of the Mother-in-law.", "Natural Habitat": " This upright, succulent plant can grow up to two metres and is extremely hardy. It takes a lot to kill it, so this is another great option for those who tend to neglect their plants", "Preference": "It should be placed in bright light with some direct sun for several hours a day. It will tolerate shade, however the plant will take longer to grow. ", "Tips for better growth": "Moderate water is required, with the root ball remaining slightly damp in summer, but dryer in winter to avoid rotting. Don’t overwater, as the plant would prefer to be too dry than too damp."},
        "Zanzibar Gem": {"About them": "This stunning plant not only looks great, it has been hailed as being ‘almost indestructible’ and is perfect for those who tend to neglect their plants, as it's drought resistant. Native to Africa, it has deep, green glossy leaves and is able to survive a long period without water. The reason the Zanzibar Gem is so hardy is due to its ability to store water in its potato-like tuber.", "Natural Habitat": "don’t over-water it or sit it in water. In fact it thrives on neglect and prefers you don’t water it too often. Once a month is enough.", "Preference": "It’s best placed in a bright to light shaded area, however it will tolerate a shady spot, but will just take longer to grow.", "Tips for better growth": "Keep it out of direct sunlight as the plant can burn. You can add a slow-release fertiliser in spring and re-pot if you notice the root starting to bulge."},
        "Anthurium Andraeanum": {"About them": "These popular indoor plants are originally from Columbia and feature long, dark-green leathery leaves and produce beautiful, red, pink and white heart-shaped ‘flowers’ that can last for weeks. The ‘flowers’ are actually spathes, which are a leaf-like bract that surrounds a cylindrical spike.", "Natural Habitat": "It can grow up to 45cm high and soil needs to be kept evenly moist from spring to autumn and slightly drier in winter. ", "Preference": "In order for the plant to bloom, it requires bright light (but not direct sun).",    "Tips for better growth": "The Anthurium benefits from being fertilised every two weeks in spring and summer with a high-phosphorus liquid fertiliser."},
        "Maidenhair Fern": {"About them": "If you’re prepared to give a Maidenhair Fern the TLC it needs then it can make a beautiful addition to your home. They have feathery, light green leaves with soft shiny stems and they make a great hanging plant. Not only do they look fragile, Maidenhair Ferns truly are the goldilocks of the plant world when it comes to care instructions.", "Natural Habitat": "They require not too much light, but not too little, growing well in a warm spot with a bit of humidity.", "Preference": "DIY a rainforest environment by placing a saucer filled with pebbles beneath the potted plant.", "Tips for better growth": "Fill the saucer with water to just below the top of the pebbles and as the water evaporates, it creates a humid microclimate around the plant. "},
        "Ficus Elastica or Rubber Plant": {"About them": "With shiny leaves in shades of dark green and burgundy, the Rubber Plant or Rubber Fig is très on trend when it comes to house plants.", "Natural Habitat": "It can either stay small in a little pot or be encouraged to grow into a large indoor tree.", "Preference": "It's a hardy, temperature-resilient option that likes bright, indirect light with weekly watering in warmer seasons.", "Tips for better growth": "In colder seasons it can survive on monthly or fortnightly watering."}}
    while(True):
        print("\n1. Monstera deliciosa or “Swiss cheese plant”\n2. Epipremnum aureum or Devil's Ivy\n3. Dracaena Massangeana or Mass Cane\n4. Spathiphyllum or Peace lily\n5. Bromeliad\n6. Sansevieria or Mother-in-law’s Tongue\n7. Zanzibar Gem\n8. Anthurium Andraeanum\n9. Maidenhair Fern\n10. Ficus Elastica or Rubber Plant\n0.EXIT")
        plant_choice = int(input("enter your choice: "))
        if(plant_choice == 1):
            a = "Monstera deliciosa or “Swiss cheese plant"
        elif(plant_choice == 2):
            a = "Epipremnum aureum or Devil's Ivy"
        elif(plant_choice == 3):
            a = "Dracaena Massangeana or Mass Cane"
        elif(plant_choice == 4):
            a = "Spathiphyllum or Peace lily"
        elif(plant_choice == 5):
            a = "Bromeliad"
        elif(plant_choice == 6):
            a = "Sansevieria or Mother-in-law’s Tongue"
        elif(plant_choice == 7):
            a = "Zanzibar Gem"
        elif(plant_choice == 8):
            a = "JAnthurium Andraeanum"
        elif(plant_choice == 9):
            a = "Maidenhair Fern"
        elif(plant_choice == 10):
            a = "Ficus Elastica or Rubber Plant"
        elif(plant_choice == 0):
            break
        while(True):
            print(
                "\n1.About them\n2.Natural Habitat\n3.Preference\n4.Tips for better growth\n0.EIXT\n")
            plant_info_choice = int(input("enter you choice: "))
            if(plant_info_choice == 0):
                break

            if(plant_info_choice == 1):
                b = "About them"
            elif(plant_info_choice == 2):
                b = "Natural Habitat"
            elif(plant_info_choice == 3):
                b = "Preference"
            elif(plant_info_choice == 4):
                b = "Tips for better growth"
            else:
                print("NO INFORMATION FOUND REGARDING YOUR INPUT")
            print(f"\nPLANT:{a}\n{b}\n{plant[a][b]}\n\n")


def HELPER_REMINDER():
    while(True):
        user_choice = int(
            input("1.CUSTOM REMINDER\n2.DEFULT REMINDER\n0.EXIT\n"))
        if(user_choice == 1):
            custom_title = input("ENTER THE TITLE OF YOUR REMINDER\n")
            custom_msg = input("ENTER THE MESSAGE YOU WANT TO DISPLAY\n")
            type_time = int(
                input("1.Month\n2.Week\n3.Day\n4.Hour\n5.Minute\n6.Seconds\n"))
            custom_time = float(
                input("ENTER THE FREQUENCY YOU WANT TO BE NOTIFIED \n"))
            if(type_time == 1):
                custom_time = custom_time*2629743.83
            elif(type_time == 2):
                custom_time = custom_time*604800
            elif(type_time == 3):
                custom_time = custom_time*86400
            elif(type_time == 4):
                custom_time = custom_time*3600
            elif(type_time == 5):
                custom_time = custom_time*60
            elif(type_time == 6):
                custom_time = custom_time
        elif (user_choice == 2):
            print("COMMING SOON....... :)")
        elif(user_choice == 0):
            break
    while(True):
        notification.notify(
            title=custom_title, message=custom_msg, timeout=10, app_icon="icon2.ico")
        duration = 1000  # milliseconds
        freq = 440  # Hz
        winsound.Beep(freq, duration)
        time.sleep(custom_time)


opptions()
