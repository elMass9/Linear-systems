"""
    2022EMR201 Assignment 2
    -----------------------
    Assessment ID:          2022EMR201A02
    Date:                   2022-07-12
    Surname and initials:   Nyama, K
    Student number:         18232826
"""

from emr201 import load_record

# -- QUESTION 1 --------------------------------------------------------

# Q1.1: Get stats of each hero (1 mark)
def student_hero(option: int) -> list:
    """Return the stats of each student hero.

    Args:
        option (int): Switching Variable

    Returns:
        list: List with record selected student.
    """
    s1 = load_record("s1.txt")
    s2 = load_record("s2.txt")
    s3 = load_record("s3.txt")
    s4 = load_record("s4.txt")
    # s1 = (["FAST", "SPEED", "STRENGTH", "ENDURANCE", "COURAGE", "POWER", "FRIKKIE"],
    #       ["BASE (UP)",   85, 70, 70, 10, 10, 0],
    #       ["LC (SPORT)",  90, 75, 72, 5,  20, 0],
    #       ["STRIP (JOL)", 75, 65, 30, 80, 10, 0],
    #       ["FAUZI (EAT)", 63, 80, 60, 10, 20, 0])
    # s2 = (["WEAPONSMITH", "SPEED", "STRENGTH", "ENDURANCE", "COURAGE", "POWER", "WANDILE"],
    #       ["BASE (UP)",   10, 30, 10, 80, 90, 0],
    #       ["LC (SPORT)",  12, 45, 12, 75, 90, 0],
    #       ["STRIP (JOL)", 30, 25, 8,  95, 45, 0],
    #       ["FAUZI (EAT)", 90, 32, 20, 80, 80, 0])
    # s3 = (["MAGICAL", "SPEED", "STRENGTH", "ENDURANCE", "COURAGE", "POWER", "MISHKA"],
    #       ["BASE (UP)",   60, 40, 30, 30, 75, 0],
    #       ["LC (SPORT)",  80, 50, 20, 50, 70, 0],
    #       ["STRIP (JOL)", 70, 60, 10, 50, 90, 0],
    #       ["FAUZI (EAT)", 55, 80, 60, 10, 20, 0])
    # s4 = (["NONE", "SPEED", "STRENGTH", "ENDURANCE", "COURAGE", "POWER", "NONE"],
    #       ["NONE (UP)",               0,  0,  0,  0,  0,  0],
    #       ["TEKKER TIRENT (SPORT)",   80, 50, 50, 20, 12, 0],
    #       ["DODGY DAN (JOL)",         4,  20, 69, 66, 4,  0],
    #       ["FAT FRANK (EAT)",         10, 80, 15, 60, 55, 0])
    
    # Write code beneath this line, DO NOT EDIT ABOVE THIS LINE --------
    selected_option={
        1:s1,
        2:s2,
        3:s3
    }
    selected_option=selected_option.get(option,s4)
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return selected_option

# Q1.2: Determine hero name (1 mark)
def get_heroname(hero_details: list) -> str:
    """Determine hero name

    Args:
        hero_details (list): Hero stats

    Returns:
        str: Hero name
    """
    # Write code beneath this line, DO NOT EDIT ABOVE THIS LINE --------
    heroname = hero_details[0][0]+" "+hero_details[0][6]
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return heroname

# Q1.3: Average hero stats at each location (2 marks)
def calculate_average(hero_details: list) -> list:
    """Calculate the average stats of the hero at each location.

    Args:
        hero_details (list): Hero stats

    Returns:
        list(float): average = [UP, SPORT, JOL, EAT]
    """
    # average = [UP, SPORT, JOL, EAT]
    average = [0, 0, 0, 0]
    # Write code beneath this line, DO NOT EDIT ABOVE THIS LINE --------
    up=sport=jol=eat=0
    for i in range(1,5):
        for j in range(1,6):
            if i==1:
                up+=int(hero_details[i][j])
            if i==2:
                sport+=int(hero_details[i][j])
            if i==3:
                jol+=int(hero_details[i][j])
            if i==4:
                eat+=int(hero_details[i][j])
    
    for x in range(0,len(average)):
        if x==0:
            average[x]=up/5
        if x==1:
            average[x]=sport/5
        if x==2:
            average[x]=jol/5
        if x==3:
            average[x]=eat/5

    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return average

# Q1.4: Calculate hero rating (1 mark)
def calculate_hero_rating(averages: list) -> list:
    """Calculate the hero rating from the averages.

    Args:
        averages (list): Averages of [UP, SPORT, JOL, EAT]

    Returns:
        list(int): hero_rating = [UP, SPORT, JOL, EAT]
    """
    # hero_rating = [UP, SPORT, JOL, EAT]
    hero_rating = ["", "", "", ""]
    # Write code beneath this line, DO NOT EDIT ABOVE THIS LINE --------
    for i in range(0,len(averages)):
        if averages[i] >= 0 and averages[i] < 33:
            hero_rating[i] = "bad"
        elif averages[i] >= 33 and averages[i] < 66:
            hero_rating[i] = "average"
        elif averages[i] >= 66 and averages[i] <= 100:
            hero_rating[i] = "good"
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return hero_rating

# Q1.5: Determine if student-hero is likely to win against the baddie dudes (1 mark)
def determine_likeliness(hero_rating: list) -> list:
    """Determine whether a student-hero is likely to win against the baddies.

    Args:
        hero_rating (list): Averages of [UP, SPORT, JOL, EAT]

    Returns:
        list: likely_to_win = [SPORT, JOL, EAT]
    """
    baddie_rating = ["average", "bad", "average"]
    likely_to_win = ["", "", ""]
    
    # Write code beneath this line, DO NOT EDIT ABOVE THIS LINE --------
    j=1
    for j in range(1,len(hero_rating)):
        if hero_rating[j]== "bad":
            hero_rating[j] = "0"
        if hero_rating[j]== "average":
            hero_rating[j] = "1"
        if hero_rating[j]== "good":
            hero_rating[j] = "2"
    
    for i in range(0,len(baddie_rating)):
        if baddie_rating[i]== "bad":
            baddie_rating[i] = "0"
        if baddie_rating[i]== "average":
            baddie_rating[i] = "1"
        if baddie_rating[i]== "good":
            baddie_rating[i] = "2"
    x=1
    for y in range(0,len(baddie_rating)):
        if int(hero_rating[x]) > int(baddie_rating[y]) and x < len(hero_rating):
            likely_to_win[y] = "very likely"
            x+=1
        elif int(hero_rating[x]) < int(baddie_rating[y]) and x < len(hero_rating):
            likely_to_win[y] = "not likey"
            x+=1
        elif int(hero_rating[x]) == int(baddie_rating[y]) and x < len(hero_rating):
            likely_to_win[y] = "cannot say"
            x+=1
    # Write code above this line, DO NOT EDIT BELOW THIS LINE ----------
    return likely_to_win

# -- QUESTION 2 --------------------------------------------------------

# Q2: Attempt the fight (2 marks)
def attempt_fighting(hero_health: int, enemy_health: int, potion_inventory: bool) -> bool:
    """
    Args:
        hero_health: int (the health of the hero from 0 to 100)
        enemy_health: int (the health of the enemy from 0 to 100)
        potion_inventory: bool (Does the student-hero have a health potion)

    Returns:
        attempt_fight: bool (If the student-hero should attempt the fight)
    """
    attempt_fight = None
    # write code below this line, DO NOT EDIT ABOVE THIS LINE --------
    if hero_health < 50:
        if potion_inventory:
            attempt_fight = True
        else:
            if hero_health > enemy_health:
                attempt_fight = True
            else:
                attempt_fight = False
    else:
        attempt_fight = True
    # Write code above this line, DO NOT EDIT BELOW THIS LINE --------
    return attempt_fight

# -- QUESTION 3 --------------------------------------------------------

# Q3: Hero fighting simulation (2 mark)
def heroes_fight(hero1_input: str, hero2_input: str, hero1_base_strength: float, hero2_base_strength: float, hero1_init_health: float, hero2_init_health: float) -> list:
    """
    Args:
        hero1_input: (The requested movement direction from hero1)
        hero1_base_strength: (The base hero1 strength)
        hero1_init_health: (The base hero1 initial health)
        hero2_input: (The requested movement direction from hero2)
        hero2_base_strength: (The base hero2 strength)
        hero2_init_health: (The base hero2 initial health)

    Returns:
        hero_movement: list (Contains the calculated information based on users input)
    """
    # hero_movement = [move, strength, health]
    hero_movement = []
    # Write code below this line, DO NOT EDIT ABOVE THIS LINE ------
    hero1 = None
    hero2 = None
    b_1 = None
    b_2 = None
    i_1 = None
    i_2 = None

    
    if hero1_input=="a":
        hero1='Apple'
        i_1=hero1_init_health*(105/100)
        b_1=hero1_base_strength*(110/100)
    elif hero1_input=="p":
        hero1='Pie'
        i_1=hero1_init_health*(115/100)
        b_1=hero1_base_strength*(115/100)
    elif hero1_input=="h":
        hero1='Potion'
        i_1=hero1_init_health*(125/100)
        b_1=hero1_base_strength*(102/100)
    else:
        hero1='Nothing'
        b_1 = hero1_base_strength
        i_1 = hero1_init_health
    
    if hero2_input=="a":
        hero2='Apple'
        i_2=hero2_init_health*(105/100)
        b_2=hero2_base_strength*(110/100)
    elif hero2_input=="p":
        hero2='Pie'
        i_2=hero2_init_health*(115/100)
        b_2=hero2_base_strength*(115/100)
    elif hero2_input=="h":
        hero2='Potion'
        i_2=hero2_init_health*(125/100)
        b_2=hero2_base_strength*(102/100)
    else:
        hero2='Nothing'
        b_2 = hero2_base_strength
        i_2 = hero2_init_health
    
    cont_1 = i_1 - b_2
    cont_2 = i_2 - b_1
    
    if(cont_1 > cont_2):
        hero_movement = [hero1, b_1, i_1]
    else:
        hero_movement = [hero2, b_2, i_2]
    
    # Write code above this line, DO NOT EDIT BELOW THIS LINE -------
    return hero_movement
