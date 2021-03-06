from plugin import plugin


@plugin("calories")
def calories(jarvis, s):
    """
    Tells the recommended daily calorie intake, also recommends
    calories for weight add and loss.(Source 1)
    It is based on gender, age, height and weight.
    Uses the Miffin-St Jeor Equation as it is considered the
    most accurate when we don't know our body fat percentage(Source 2).
    Add gender(man/woman), age(15 - 80 recommended), metric height(cm),
    weight(kg), workout level(1-4). No decimal weight for now.
    Workout Levels:
        [1] Little or no exercise
        [2] Light 1-3 per week
        [3] Moderate 4-5 per week
        [4] Active daily exercise or physical job
    #Example: health calories woman 27 164 60 3
    ^Sources:
            1) https://en.wikipedia.org/wiki/Basal_metabolic_rate
            2) https://jandonline.org/article/S0002-8223(05)00149-5/fulltext
    """

    strings = s.split()
    if len(strings) == 5:
        gender = strings[0]
        age = int(strings[1])
        height = int(strings[2])
        weight = float(strings[3])
        level = int(strings[4])
    else:
        jarvis.say("You wrote less or more arguments than it needed.")
        return None

    gender_no = 0
    if(gender == 'man'):
        gender_no = 5
    elif(gender == 'woman'):
        gender_no = -161

    if gender_no != 0 and age > 14 and height > 0.0 and weight > 0.0 and level > 0 and level < 5:
        brm = float(10 * weight + 6.25 * height - 5
                    * age + gender_no) * exercise_level(level)
        brm_loss = brm - 500.0
        brm_put_on = brm + 500.0
        jarvis.say("Daily caloric intake :    " + str(brm))
        jarvis.say("Loss weight calories :    " + str(brm_loss))
        jarvis.say("Put on  weight calories : " + str(brm_put_on))
    else:
        jarvis.say("Please add correct input!")
        return None


def exercise_level(level):
    multiplier = 1
    if(level == 1):
        multiplier = 1.2
    elif(level == 2):
        multiplier = 1.4
    elif(level == 3):
        multiplier = 1.6
    else:
        multiplier = 1.95
    return multiplier
