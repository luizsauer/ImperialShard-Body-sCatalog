import os
import webbrowser

BODY_NAMES = {
    1: "Ogre",
    2: "Ettin",
    3: "Zombie",
    4: "Gargoyle",
    5: "Eagle",
    6: "Bird",
    7: "Orc Captain",
    8: "Whipping Vine",
    9: "Demon",
    10: "Demon smaller",
    11:	"Dread Spider",
    12:	"Dragon Orange",
    13:	"Air Elemental",
    14:	"Earth Elemental",
    15:	"Fire Elemental",
    16:	"Water Elemental",
    17:	"Orc",
    18:	"Ettin w/Club",
    19:	"Dread Spider",
    20:	"Frost Spider",
    21:	"Giant Snake",
    22:	"Gazer",
    23:	"Wolf Grey",
    24:	"Lich",
    25:	"Wolf Light Grey",
    26:	"Wraith",
    27:	"Wolf Dark Grey",
    28:	"Giant Spider",
    29:	"Gorilla",
    30:	"Harpy",
    31:	"Headless",
    33:	"Lizardman",
    34:	"Wolf Grey",
    35:	"Lizardman W/Spear",
    36:	"Lizardman w/mace",
    37:	"Wolf Arctic",
    38:	"Blackgate Demon",
    39:	"Mongbat",
    40:	"Balron",
    41:	"orc w/club",
    42:	"Ratman",
    43:	"Ice Fiend",
    44:	"Ratman w/mace",
    45:	"Ratman w/sword",
    46:	"Ancient Wyrm",
    47:	"Reaper",
    48:	"Scorpion",
    49:	"White Wyrm",
    50:	"Skeleton",
    51:	"Slime",
    52:	"Snake",
    53:	"Troll W/axe",
    54:	"Troll",
    55:	"Troll arctic w/axe",
    56:	"Skeleton w/axe",
    57:	"Skeletal Knight",
    58:	"Wisp",
    59:	"Dragon Red",
    60:	"Drake Brown",
    61:	"Drake Red",
    62:	"Wyvern",
    63:	"Panther Light",
    64:	"Panther Dark",
    65:	"Panther Dark",
    66:	"Whipping Vine Hued Lime",
    67:	"Stone Gargoyle",
    68:	"Gazer",
    69:	"Gazer",
    70:	"Terathan Warrior",
    71:	"Terathan Drone",
    72:	"Terathan Matriarch",
    73:	"Harpy Stone Hued",
    74:	"Imp",
    75:	"Cyclops",
    76:	"Titan",
    77:	"Kraken & Leviathan",
    78:	"Lich Hued Grey",
    79:	"Lich",
    80:	"Giant Toad",
    81:	"Giant Frog",
    82:	"Lich",
    83:	"Ogre",
    84:	"Ogre",
    85:	"Ophidian Justicar",
    86:	"Ophidian avenger",
    87:	"Ophidian Matriarch",
    88:	"Goat",
    89:	"Ice Serpent",
    90:	"Lava Serpent",
    91:	"Giant Serpent Grey",
    92:	"Giant Serpent Grey",
    93:	"Giant Serpent Light Grey",
    94:	"Frost ooze",
    95:	"Turkey",
    96:	"Frost ooze",
    97:	"Hell Hound",
    98:	"Hell Hound Light",
    99:	"Wolf Grey Dark",
    100:	"Wolf Arctic",
    101:	"Centaur",
    102:	"Demon smaller custom colored",
    102:	"6 Uber Turkey",
    103:	"Serpentine Dragon",
    104:	"Skeletal Dragon",
    105:	"Dragon Dark Bluish Grey",
    106:	"Earth Elemental Hued",
    106:	"8 Osiredan The Scalis Enforcer",
    106:	"9 Ancient Hellhound or Worg",
    107:	"Earth Elemental Hued",
    107:	"0 Werewolf small head",
    108:	"Earth Elemental Hued",
    109:	"Earth Elemental Hued",
    110:	"Earth Elemental Hued",
    111:	"Earth Elemental Hued",
    112:	"Earth Elemental Hued",
    113:	"Earth Elemental Hued",
    114:	"Nightmare 1 old style",
    115:	"Inviso Steed",
    116:	"Nightmare 2 new style",
    117:	"HolySteed",
    118:	"Faction Horse Purple",
    119:	"Faction Horse Light Blue",
    120:	"Faction Horse Red",
    121:	"Faction Horse Light Green",
    122:	"Unicorn",
    123:	"Lattice Seeker or angel",
    124:	"Soulbinder 1 or warlock Blue",
    125:	"Soulbinder 2 purple",
    126:	"Soulbinder 3",
    127:	"Hellcat",
    128:	"Pixie",
    129:	"Whipping Vine Hued Red",
    130:	"Blazing Gargoyle",
    131:	"Efreet",
    132:	"kirin",
    133:	"Alligator",
    134:	"Lava Lizard",
    135:	"Arctic Ogre",
    136:	"Ophidian Zealot",
    137:	"Ophidian Avenger",
    138:	"Orc Captain",
    139:	"Orc Captain",
    140:	"Orc",
    141:	"Human male Flesh",
    142:	"Ratman Blue Vest w/sword",
    143:	"Ratman Red Vest w/sword",
    144:	"Seahorse",
    145:	"Sea Serpent Dark Waterline",
    146:	"Harrower & Shadowlords",
    147:	"Skeletal Knight",
    148:	"Skeletal Mage",
    149:	"Succubus",
    150:	"Sea Serpent Bright Waterline",
    151:	"Dolphin",
    152:	"Terathan Avenger",
    153:	"Wraith",
    154:	"Mummy",
    155:	"Rotting Zombie",
    156:	"Turkey",
    157:	"Giant Black Widow",
    158:	"Acid Elemental",
    159:	"Blood Elemental Dark",
    160:	"Blood Elemental Light",
    161:	"Ice Elemental",
    162:	"Poison Elemental",
    163:	"Snow Elemental",
    164:	"Energy Vortex",
    165:	"Shadow Wisp",
    166:	"Earth Elemental Hued",
    167:	"Brown Bear",
    169:	"Blue Beetle",
    172:	"Riktor",
    173:	"Mephitis",
    174:	"Semidar",
    175:	"Lord Oaks",
    176:	"Silvani",
    177:	"Nightmare 3",
    178:	"Nightmare 4 Longhair",
    179:	"Nightmare 5 Longhair",
    180:	"White Wyrm",
    181:	"Orc Scout",
    182:	"Orc Bomber",
    183:	"Human Male",
    184:	"Human Female",
    185:	"Human Male",
    186:	"Human Female",
    187:	"Ridgeback",
    188:	"Tribal Ridgeback",
    189:	"Orc Brute",
    190:	"Fire Steed",
    191:	"Kirin",
    192:	"Unicorn",
    193:	"Ridgeback",
    194:	"Swamp Dragon",
    195:	"Blue Beetle",
    196:	"Kaze Komono",
    197:	"Chaos Variant Dragon",
    198:	"Order Variant Dragon",
    199:	"Rai-Ju",
    200:	"Horse Tan",
    201:	"Cat",
    202:	"Alligator",
    203:	"Pig",
    204:	"Horse Brown",
    205:	"Rabbit",
    206:	"lava Lizard",
    207:	"Sheep",
    208:	"Chicken",
    209:	"Goat",
    210:	"Desert Ostard",
    211:	"Brown Bear",
    212:	"Grizzly Bear",
    213:	"Polar Bear",
    214:	"Panther Light",
    215:	"Giant Rat",
    216:	"Cow Black & White",
    217:	"Dog",
    218:	"Frenzied Ostard Armored",
    219:	"Frenzied Ostard No Armor",
    220:	"Llama",
    221:	"Walrus",
    223:	"Sheep",
    225:	"Wolf Brown",
    226:	"Horse White",
    228:	"Horse Tan",
    231:	"Cow Brown & White",
    232:	"Bull Light Brown",
    233:	"Bull Dark Brown & White",
    234:	"Stag",
    237:	"Deer",
    238:	"rat",
    240:	"Kappa",
    241:	"Oni",
    242:	"Deathwatch Beetle",
    243:	"Hiryu",
    244:	"Rune Beetle",
    245:	"Yomotsu Warrior",
    246:	"Bake Kitsune",
    247:	"Fan Dancer",
    248:	"Gaman",
    249:	"Serado the Awakened",
    250:	"Tsuki Wolf",
    251:	"Revenant Lion",
    252:	"Lady of the Snow",
    253:	"Yomotsu Priest",
    254:	"Crane",
    255:	"Yomotsu Elder",
    256:	"Chief Paroxysmus",
    257:	"Dread Horn",
    258:	"Lady Melisande",
    259:	"Monstrous Interred Grizzle",
    260:	"Shimmering Effusion",
    261:	"Shimmering Effusion 2",
    262:	"Minotaur Female",
    263:	"Minotaur Male",
    264:	"Changeling",
    265:	"Hydra",
    266:	"Dryad",
    267:	"Troglodyte",
    270:	"Mini dino",
    271:	"Satyr",
    272:	"Fetid Essence",
    273:	"Fetid Essence",
    275:	"Reptalon (no graphic)",
    276:	"Cu Sidhe",
    277:	"Squirrel",
    279:	"Ferret",
    280:	"Minotaur Armored",
    281:	"Minotaur W/Hammer",
    282:	"Parrot Perched",
    283:	"Black Bird/crow",
    284:	"Charger of the Fallen",
    285:	"Reaper Form Spellweaving",
    287:	"Bloodworm",
    290:	"Pig",
    291:	"Pack Horse",
    292:	"pack Llama",
    293:	"Vollum",
    300:	"Crystal Elemental",
    301:	"Tree Fellow",
    302:	"Skittering Hopper",
    303:	"Devourer of Souls",
    304:	"Flesh Golem",
    305:	"Gore Fiend",
    306:	"Impaler",
    307:	"Gibberling",
    308:	"Bone Demon",
    309:	"Patchwork Skeleton",
    310:	"Wailing Banshee",
    311:	"Shadow Knight",
    312:	"Abyssmal Horror",
    313:	"Darknight Creeper",
    314:	"Ravager",
    315:	"Flesh Renderer",
    316:	"Wanderer of the Void",
    317:	"Vampire Bat",
    318:	"Dark Father",
    319:	"mound of Maggots",
    334:	"Gray Goblin",
    400:	"Human Male",
    401:	"Human Female",
    402:	"GM",
    403:	"GM",
    432:	"Ridable Boura",
    573:	"Death Vortex",
    574:	"Blade Spirits",
    605:	"Elf Male",
    606:	"Elf Female",
    607:	"GM",
    608:	"GM",
    666:	"Gargoyle Male",
    667:	"Gargoyle Female",
    668:	"GM",
    669:	"GM",
    689:	"Timelord",
    694:	"Gargoyle Male Death",
    695:	"Gargoyle Female Death",
    704:	"Shadowlords New",
    705:	"Stone Form Mysticism",
    713:	"Abyssal Infernal",
    714:	"Iron Beetle",
    715:	"Lowland Boura",
    716:	"Chicken Lizard",
    717:	"Clockwork Scorpion",
    718:	"Fairy Dragon",
    719:	"Werewolf",
    720:	"Lava Elemental",
    721:	"Maddening Horror",
    722:	"Putrid Undead Gargoyle",
    723:	"Green Goblin",
    724:	"Gremlin",
    725:	"Blob",
    726:	"Kepetch",
    727:	"Kepetch Ambusher",
    728:	"Medusa",
    729:	"Crab paralithode",
    730:	"Raptor",
    732:	"Rotworm",
    733:	"Skree",
    734:	"Toxic Slith",
    735:	"Navrey Night-Eyes",
    736:	"Wolf Spider",
    737:	"Trapdoor Spider",
    738:	"Fire Ant",
    739:	"Leather Wolf",
    740:	"Dream Wraith",
    741:	"Slasher of Veils",
    742:	"Charybdis",
    743:	"Tentacles of Osiredon the Scalis Enforcer",
    744:	"Bright White Human Male",
    745:	"Bright White Human Female",
    746:	"Horrific Beast Necromancy Form 1",
    747:	"Wailing Banshee Necro Female Form",
    748:	"Wraith Necro Male Form",
    749:	"Lichform Necro",
    750:	"Human Male",
    751:	"Human Female",
    752:	"Golem",
    753:	"Enslaved Gargoyle",
    754:	"Gargoyle Enforcer",
    755:	"gargoyle Destroyer",
    756:	"Exodus Overseer",
    757:	"Exodus Minion",
    758:	"Gargoyle Color Glitched In Directions",
    763:	"Exodus Minion Huge",
    764:	"Juka Warrior",
    765:	"Juka Mage",
    766:	"Juka Lord",
    767:	"Betrayer",
    768:	"Blackthorn Juggernaut",
    770:	"Meer Mage",
    771:	"Meer Warrior",
    772:	"Meer Eternal",
    773:	"Meer Captain",
    774:	"Dawn",
    775:	"Plague Beast",
    776:	"Horde Minion Small",
    777:	"Doppleganger",
    778:	"Gazer Larva",
    779:	"Bogling",
    780:	"Bog Thing",
    781:	"Red Solen Worker",
    782:	"Red Solen Warrior",
    783:	"Red Solen Queen",
    784:	"Arcane Demon",
    785:	"Horrific Beast Moloch",
    787:	"Ant Lion",
    788:	"Sphinx",
    789:	"Quagmire",
    790:	"kaze komono",
    791:	"Blue Beetle",
    792:	"Chaos Demon",
    793:	"Skeletal Steed",
    794:	"Swamp Dragon Barded",
    796:	"Horde Minion Large",
    797:	"Riktor",
    798:	"Ancient Wyrm",
    799:	"Swamp Dragon Barded",
    804:	"Red Solen Queen",
    805:	"Red Solen Worker",
    806:	"Red Solen Warrior",
    807:	"Red Solen Queen",
    808:	"red Solen Queen",
    829:	"Rising Colossus",
    830:	"Prime-Evil Lich",
    831:	"Parrot (Tropical)",
    832:	"Phoenix",
    970:	"Deathshroud",
    987:	"GM Robe Body",
    990:	"Lord British",
    991:	"Lord Blackthorn",
    993:	"Floating Shield",
    994:	"Dupre",
    999:	"Multicolored Horde Demon",
    1026:	"Uber Turkey",
    1068:	"Osiredan The Scalis Enforcer",
    1069:	"Ancient Hellhound or Worg",
    1070:	"Werewolf small head",
    1308:	"Gorilla Giant",
    1309:	"Baby Tiger",
    1400:	"Dino Trex",
    1401:	"Turanchula Mount",
    1402:	"Myrmidex Drone",
    1403:	"Myrmidex Warrior",
    1404:	"Myrmidex Queen",
    1405:	"DrSpector",
    1406:	"Golem Aztec",
    1407:	"Horse Unicorn RB",
    1408:	"Horse Palomino",
    1409:	"Dragon Hildebrandt",
    1410:	"Canine Windrunner",
    1415:	"Dino Triceratops",
    1416:	"Tiger Sabertooth",
    1417:	"Dragon Small Platinum",
    1418:	"Dragon Ele Platinum",
    1419:	"Dragon Small Crimson",
    1420:	"Dragon Ele Crimson",
    1421:	"Dragon Small Stygian",
    1422:	"Dragon Ele Stygian",
    1423:	"Fox Small",
    1424:	"Beetle Rhino",
    1425:	"Goat Necromancer",
    1427:	"Titan Water Tentacle",
    1431:	"Titan Earth Head",
    1432:	"Titan Air Whirlwind",
    1433:	"Titan Fire Demon",
    1434:	"Dragon Asian Mount",
    1440:	"Peacock Mount",
    1441:	"Skeletal Tiger Mount",
    1479:	"Giant Undead",
    1484:	"Krampus",
    1485:	"Krumpus Imp",
    1510:	"Giant Crab",
    1511:	"Crab",
    1512:	"Giant Crab (larger)",
    1526:	"War Boar Mount",
    1527:	"Capybara Mount",
    1528:	"Capybara, smaller",
    1541:	"Doom Rabbit",
    1542:	"Rabbit (or mini Doom Rabbit)",
    1546:	"Giant Dog",
    1547:	"Giant Dog, Husky",
    1548:	"Dog, Great Dane",
    1549:	"Giant Dog, Saint Bernard",
    1551:	"Giant Dog, Schnauzer",
    1552: "Giant Dog, Rottweiler"
}

def generate_html_report(screenshot_dir):
    html_report = os.path.join(screenshot_dir, "index.html")
    png_files = sorted([f for f in os.listdir(screenshot_dir) if f.lower().endswith('.png')])
    
    valid_files = []
    for filename in png_files:
        try:
            body_value = int(filename.split('.')[0])
            full_path = os.path.join(screenshot_dir, filename)
            if os.path.exists(full_path) and os.path.getsize(full_path) >= 1024:
                valid_files.append(filename)
        except ValueError:
            continue

    items_added = len(valid_files)
    
    with open(html_report, 'w', encoding='utf-8') as f:
        f.write(f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Imperial Shard - Catálogo de BodyValues</title>
    <style>
        :root {{
            --primary: #2c3e50;
            --secondary: #34495e;
            --accent: #3498db;
            --light: #ecf0f1;
            --dark: #2c3e50;
            --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            --transition: all 0.3s ease;
        }}
        
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f5f7fa;
            color: var(--dark);
            line-height: 1.6;
        }}
        
        .header {{
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            padding: 1.5rem;
            text-align: center;
            box-shadow: var(--shadow);
            margin-bottom: 1rem;
        }}
        
        .controls {{
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            padding: 1rem;
            background: white;
            box-shadow: var(--shadow);
            position: sticky;
            top: 0;
            z-index: 100;
            align-items: center;
        }}
        
        .search-container {{
            flex: 1;
            min-width: 300px;
            display: flex;
            gap: 1rem;
            align-items: center;
        }}
        
        #searchInput {{
            flex: 1;
            padding: 0.75rem 1rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
            min-width: 200px;
        }}
        
        .range-filter {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        
        .range-input {{
            width: 80px;
            padding: 0.5rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            text-align: center;
        }}
        
        .view-toggle {{
            display: flex;
            gap: 0.5rem;
        }}
        
        .view-btn {{
            padding: 0.5rem 1rem;
            background: #eee;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: var(--transition);
        }}
        
        .view-btn.active {{
            background: var(--accent);
            color: white;
        }}
        
        .container {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 1.5rem;
            padding: 1.5rem;
        }}
        
        .container.list-view {{
            grid-template-columns: 1fr;
        }}
        
        .item {{
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: var(--shadow);
            transition: var(--transition);
            display: flex;
            flex-direction: column;
        }}
        
        .item:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }}
        
        .item-img-container {{
            height: 250px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #f8f9fa;
            padding: 1rem;
            cursor: pointer;
        }}
        
        .item-img {{
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
        }}
        
        .item-info {{
            padding: 1rem;
            text-align: center;
            border-top: 1px solid #eee;
        }}
        
        .item-info h3 {{
            margin: 0;
            color: var(--primary);
            font-size: 1.1rem;
        }}
        
        /* Modal Styles */
        .modal {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.9);
            z-index: 1000;
            overflow: hidden;
        }}
        
        .modal.show {{
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .modal-content {{
            position: relative;
            max-width: 90%;
            max-height: 90%;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .modal-img {{
            max-width: 100%;
            max-height: 90vh;
            object-fit: contain;
            transform-origin: center center;
            transition: transform 0.3s ease;
        }}
        
        .modal-info {{
            position: absolute;
            bottom: 20px;
            left: 0;
            width: 100%;
            text-align: center;
            color: white;
            padding: 10px;
            background: rgba(0, 0, 0, 0.7);
        }}
        
        .modal-close {{
            position: absolute;
            top: 20px;
            right: 20px;
            color: white;
            font-size: 2rem;
            cursor: pointer;
            background: rgba(0, 0, 0, 0.5);
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .modal-nav {{
            position: absolute;
            top: 50%;
            width: 100%;
            display: flex;
            justify-content: space-between;
            padding: 0 20px;
            transform: translateY(-50%);
        }}
        
        .nav-btn {{
            background: rgba(0, 0, 0, 0.5);
            color: white;
            border: none;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            font-size: 1.5rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .zoom-controls {{
            position: absolute;
            top: 20px;
            left: 20px;
            display: flex;
            gap: 10px;
        }}
        
        .zoom-btn {{
            background: rgba(0, 0, 0, 0.5);
            color: white;
            border: none;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            font-size: 1.2rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .footer {{
            position: fixed;
            bottom: 0;
            width: 100%;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            text-align: center;
            padding: .5rem;
            margin-top: 1rem;
            box-shadow: var(--shadow);
            font-size: 0.9rem;
        }}
        
        @media (max-width: 768px) {{
            .container {{
                grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
                gap: 1rem;
                padding: 1rem;
            }}
            
            .item-img-container {{
                height: 200px;
            }}
            
            .controls {{
                flex-direction: column;
                align-items: stretch;
            }}
            
            .search-container {{
                min-width: auto;
            }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Imperial Shard - Catálogo de BodyValues</h1>
    </div>

    <div class="controls">
        <div class="search-container">
            <span id="itemCount" style="white-space: nowrap; margin-left: 10px;">{items_added} Bodys</span>
            <input type="text" id="searchInput" placeholder="Pesquisar body value ou nome..." oninput="searchBody()">
            <div class="range-filter">
                <input type="number" id="minValue" class="range-input" placeholder="Mínimo" oninput="filterByRange()">
                <span>até</span>
                <input type="number" id="maxValue" class="range-input" placeholder="Máximo" oninput="filterByRange()">
            </div>
        </div>
    </div>

    <div class="container" id="imageContainer">''')

        # Gerar os itens dinamicamente
        png_files = sorted([f for f in os.listdir(screenshot_dir) if f.lower().endswith('.png')])
        
        items_added = 0
        
        for filename in png_files:
            try:
                body_value = int(filename.split('.')[0])
            except ValueError:
                continue
            full_path = os.path.join(screenshot_dir, filename)
            
            # Verificar se o arquivo existe e não está vazio (tamanho > 1KB)
            if not os.path.exists(full_path) or os.path.getsize(full_path) < 1024:
                continue
            
            body_name = BODY_NAMES.get(body_value, "Desconhecido")
        
        # ATENÇÃO: Modifique esta parte para os caminhos das imagens:
            f.write(f'''
        <div class="item">
            <div class="item-img-container" onclick="openModal('{filename}')">
                <img class="item-img" src="{filename}" alt="Body {body_value}" loading="lazy">
            </div>
            <div class="item-info">
                <h3>Body {body_value}</h3>
                <p>{body_name}</p>
            </div>
        </div>\n''')
            items_added += 1

        # Se nenhum item foi adicionado, mostrar mensagem
        if items_added == 0:
            f.write('''
        <div style="grid-column: 1 / -1; text-align: center; padding: 2rem;">
            <h3>Nenhuma imagem válida encontrada no diretório</h3>
            <p>Verifique se as screenshots foram capturadas corretamente.</p>
        </div>''')

        f.write('''
    </div>

    <div class="modal" id="myModal">
        <span class="modal-close" onclick="closeModal()">&times;</span>
        <div class="zoom-controls">
            <button class="zoom-btn" onclick="zoomIn()">+</button>
            <button class="zoom-btn" onclick="zoomOut()">-</button>
            <button class="zoom-btn" onclick="resetZoom()">↻</button>
        </div>
        <div class="modal-nav">
            <button class="nav-btn" onclick="navigateImage(-1)">❮</button>
            <button class="nav-btn" onclick="navigateImage(1)">❯</button>
        </div>
        <div class="modal-content" id="modalContent">
            <img class="modal-img" id="modalImage" src="" alt="">
            <div class="modal-info" id="modalInfo"></div>
        </div>
    </div>
    <div class="footer">
        Desenvolvido por Luiz Sauer - <span id="currentYear"></span>
        <script>
            document.getElementById('currentYear').textContent = new Date().getFullYear();
        </script>
    </div>



    <script>
        // Estado da aplicação
        const state = {
            currentImageIndex: 0,
            images: [],
            scale: 1,
            isDragging: false,
            startX: 0,
            startY: 0,
            translateX: 0,
            translateY: 0
        };
        
        // Elementos DOM
        const dom = {
            modal: document.getElementById('myModal'),
            modalContent: document.querySelector('.modal-content'),
            modalImg: document.getElementById('modalImage'),
            modalInfo: document.getElementById('modalInfo'),
            imageContainer: document.getElementById('imageContainer'),
            items: []
        };
        
        // Inicialização
        function init() {
            // Carregar todas as imagens
            dom.items = Array.from(document.querySelectorAll('.item'));
            
            state.images = dom.items.map((item, index) => ({
                src: item.querySelector('img').src,
                bodyValue: item.querySelector('h3').textContent,
                element: item,
                index
            }));
            
            // Aplicar filtros e inicializar
            applyFilters();
            
            // Configurar eventos
            setupEventListeners();
        }
        
        function updateItemCount() {
            const items = document.querySelectorAll('.item');
            const visibleItems = Array.from(items).filter(item => item.style.display !== 'none');
            document.getElementById('itemCount').innerText = `${visibleItems.length} itens`;
        }

        function searchBody() {
            const input = document.getElementById('searchInput').value.toLowerCase();
            const items = document.querySelectorAll('.item');
            
            items.forEach(item => {
                const title = item.querySelector('.item-info h3').innerText.toLowerCase();
                const name = item.querySelector('.item-info p').innerText.toLowerCase();
                if (title.includes(input) || name.includes(input)) {
                    item.style.display = '';
                } else {
                    item.style.display = 'none';
                }
            });
            updateItemCount();
        }

        function filterByRange() {
            const min = parseInt(document.getElementById('minValue').value) || 0;
            const max = parseInt(document.getElementById('maxValue').value) || Infinity;
            const items = document.querySelectorAll('.item');
            
            items.forEach(item => {
                // Só filtra itens que já estão visíveis (não foram ocultados pela pesquisa)
                if (item.style.display === 'none' && item.style.display !== '') {
                    return;
                }
                
                const bodyValue = parseInt(item.querySelector('.item-info h3').innerText);
                if (!isNaN(bodyValue) && bodyValue >= min && bodyValue <= max) {
                    item.style.display = '';
                } else {
                    item.style.display = 'none';
                }
            });
            updateItemCount();
        }
        
        // Configurar listeners de eventos
        function setupEventListeners() {
            // Eventos de arrastar imagem
            dom.modalImg.addEventListener('mousedown', startDrag);
            document.addEventListener('mousemove', drag);
            document.addEventListener('mouseup', endDrag);
            
            // Eventos de zoom com roda do mouse
            dom.modalContent.addEventListener('wheel', handleWheel, { passive: false });
            
            // Navegação por teclado
            document.addEventListener('keydown', handleKeyDown);
        }
        
        // Abrir modal com imagem
        function openModal(srcOrIndex) {
            if (typeof srcOrIndex === 'number') {
                state.currentImageIndex = srcOrIndex;
            } else {
                // Encontrar índice pelo src da imagem
                const clickedSrc = srcOrIndex;
                state.currentImageIndex = state.images.findIndex(img => img.src.includes(clickedSrc));
                
                if (state.currentImageIndex === -1) {
                    state.currentImageIndex = 0;
                }
            }
            
            // Atualizar imagem no modal
            const currentImage = state.images[state.currentImageIndex];
            dom.modalImg.src = currentImage.src;
            
            // Mostrar body value e nome no modal
            const itemInfo = currentImage.element.querySelector('.item-info');
            const bodyValue = itemInfo.querySelector('h3').textContent;
            const bodyName = itemInfo.querySelector('p').textContent;
            dom.modalInfo.innerHTML = `${bodyValue}<br>${bodyName}`;
            
            // Mostrar modal e resetar zoom
            dom.modal.classList.add('show');
            document.body.style.overflow = 'hidden';
            resetZoom();
        }
        
        // Fechar modal
        function closeModal() {
            dom.modal.classList.remove('show');
            document.body.style.overflow = 'auto';
        }
        
        // Navegar entre imagens
        function navigateImage(direction) {
            state.currentImageIndex += direction;
            
            // Circular através das imagens
            if (state.currentImageIndex >= state.images.length) {
                state.currentImageIndex = 0;
            } else if (state.currentImageIndex < 0) {
                state.currentImageIndex = state.images.length - 1;
            }
            
            // Atualizar imagem no modal
            const currentImage = state.images[state.currentImageIndex];
            dom.modalImg.src = currentImage.src;
            dom.modalInfo.textContent = currentImage.bodyValue;
            
            // Resetar zoom para nova imagem
            resetZoom();
        }
        
       // Função de zoom com roda do mouse
        function handleWheel(event) {
            event.preventDefault(); // Impede o comportamento padrão (rolagem da página)
            
            const delta = event.deltaY || event.detail || -event.wheelDelta;
            if (delta < 0) {
                zoomIn(); // Zoom in
            } else {
                zoomOut(); // Zoom out
            }
        }

        // Função para dar zoom in
        function zoomIn() {
            state.scale += 0.1;
            updateZoom();
        }

        // Função para dar zoom out
        function zoomOut() {
            state.scale = Math.max(0.1, state.scale - 0.1); // Impede que o zoom vá abaixo de 0.1
            updateZoom();
        }

        // Função para resetar o zoom
        function resetZoom() {
            state.scale = 1;
            updateZoom();
        }

        // Atualiza o zoom na imagem
        function updateZoom() {
            dom.modalImg.style.transform = `translate(${state.translateX}px, ${state.translateY}px) scale(${state.scale})`;
        }

        
        
        // Funções de arrastar imagem
        function startDrag(e) {
            e.preventDefault();
            state.isDragging = true;
            state.startX = e.clientX - state.translateX;
            state.startY = e.clientY - state.translateY;
            dom.modalImg.style.cursor = 'grabbing';
        }
        
        function drag(e) {
            if (!state.isDragging) return;
            e.preventDefault();
            
            state.translateX = e.clientX - state.startX;
            state.translateY = e.clientY - state.startY;
            
            applyZoom();
        }
        
        function endDrag() {
            state.isDragging = false;
            dom.modalImg.style.cursor = 'grab';
        }
        
        
        // Navegação por teclado
        function handleKeyDown(e) {
            if (!dom.modal.classList.contains('show')) return;
            
            switch (e.key) {
                case 'Escape':
                    closeModal();
                    break;
                case 'ArrowLeft':
                    navigateImage(-1);
                    break;
                case 'ArrowRight':
                    navigateImage(1);
                    break;
                case '+':
                case '=':
                    zoomIn();
                    break;
                case '-':
                    zoomOut();
                    break;
                case '0':
                    resetZoom();
                    break;
            }
        }
        
        // Alternar entre modos de visualização
        function setViewMode(mode) {
            const container = document.getElementById('imageContainer');
            const buttons = document.querySelectorAll('.view-btn');
            
            buttons.forEach(btn => {
                btn.classList.toggle('active', btn.textContent.toLowerCase().includes(mode));
            });
            
            container.classList.toggle('list-view', mode === 'list');
        }
        
        // Inicializar quando o DOM estiver pronto
        document.addEventListener('DOMContentLoaded', init);
    </script>
</body>
</html>''')
    return html_report


def main():
    # Configurações
    SCREENSHOT_DIR = "public/UO_BodyValues"
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

    print("=== UO BodyValue HTML Generator ===")
    print(f"Gerando relatório a partir das imagens em: {os.path.abspath(SCREENSHOT_DIR)}")

    try:
        # Gera o relatório
        html_report = generate_html_report(SCREENSHOT_DIR)
        print(f"\nRelatório gerado com sucesso: {os.path.abspath(html_report)}")
        
        # Abre no navegador
        webbrowser.open(f'file://{os.path.abspath(html_report)}')

    except Exception as e:
        print(f"\nErro durante execução: {str(e)}")

    finally:
        print("Operação finalizada.")

if __name__ == "__main__":
    main()