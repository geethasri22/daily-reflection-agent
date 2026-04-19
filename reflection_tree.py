def reflection_tree():
    print("\n🌱 Welcome to Daily Reflection System\n")

    # Q1: Task Completion
    goal = input("Did you complete your main goal today? (yes/no): ").strip().lower()

    if goal not in ["yes", "no"]:
        print("❌ Invalid input. Please enter 'yes' or 'no'.")
        return

    # CASE 1: Goal NOT completed
    if goal == "no":
        print("\n⚠️ Let's understand what blocked you.")

        blocker = input("Main blocker? (time/focus/distraction): ").strip().lower()

        if blocker == "time":
            print("👉 Suggestion: Break tasks into smaller chunks.")
        elif blocker == "focus":
            print("👉 Suggestion: Use Pomodoro (25 min focus cycles).")
        elif blocker == "distraction":
            print("👉 Suggestion: Reduce environmental distractions.")
        else:
            print("👉 Suggestion: Identify a clear root cause.")

    # CASE 2: Goal completed
    elif goal == "yes":
        try:
            rating = int(input("Rate your satisfaction (1-5): "))
        except ValueError:
            print("❌ Invalid input. Enter a number between 1-5.")
            return

        if rating >= 4:
            win = input("What went well today?: ")
            print("✅ Reinforce this behavior tomorrow.")
        else:
            improve = input("What could be improved?: ")
            print("📈 Focus on improving this tomorrow.")

    # Final Step
    plan = input("\nDo you want to plan tomorrow now? (yes/no): ").strip().lower()

    if plan == "yes":
        print("📝 Write top 3 priorities for tomorrow.")
    else:
        print("👍 Reflection complete. Good job today!")
