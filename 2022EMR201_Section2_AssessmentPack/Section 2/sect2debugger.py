import a2022EMR201A02_Submission as s
import emr201

if __name__ == "__main__":
    # ------------------------------------------------------------------
    # Question 1
    # ------------------------------------------------------------------
    # Question 1.1
    print(" student_hero ".center(80, "-"))
    option = 2
    res = s.student_hero(option)
    print(f"Result type:  {type(res)}")
    print(f"Result value: {res}")

    # Question 1.2
    print(" get_heroname ".center(80, "-"))
    hero_details = emr201.test_hero_stats
    res = s.get_heroname(hero_details)
    print(f"Result type:  {type(res)}")
    print(f"Result value: {res}")

    # Question 1.3
    print(" calculate_average ".center(80, "-"))
    hero_details = emr201.test_hero_stats
    res = s.calculate_average(hero_details)
    print(f"Result type:  {type(res)}")
    print(f"Result value: {res}")

    # Question 1.4
    print(" calculate_hero_rating ".center(80, "-"))
    averages = [5, 50, 80, 100]
    res = s.calculate_hero_rating(averages)
    print(f"Result type:  {type(res)}")
    print(f"Result value: {res}")

    # Question 1.5
    print(" determine_likeliness ".center(80, "-"))
    hero_rating = ["average", "bad", "good", "bad"]
    res = s.determine_likeliness(hero_rating)
    print(f"Result type:  {type(res)}")
    print(f"Result value: {res}")

    # ------------------------------------------------------------------
    # Question 2
    # ------------------------------------------------------------------
    print(" attempt_fighting ".center(80, "-"))
    res = s.attempt_fighting(50, 25, True)
    print(f"Result type:  {type(res)}")
    print(f"Result value: {res}")

    # ------------------------------------------------------------------
    # Question 3
    # ------------------------------------------------------------------
    print(" heroes_fight ".center(80, "-"))
    res = s.heroes_fight("p", "h", 8, 4, 40, 75)
    print(f"Result type:  {type(res)}")
    print(f"Result value: {res}")
    print("")