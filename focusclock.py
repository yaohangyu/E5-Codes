import time

def run_focus_timer(duration_minutes):
    duration_seconds = duration_minutes * 60

    print(f"Focus timer started for {duration_minutes} minutes. Stay focused!")

    time.sleep(duration_seconds)

    print(f"\nFocus session completed! Take a break.")

if __name__ == "__main__":
    focus_duration = 25  # Adjust the focus duration as needed
    break_duration = 5   # Adjust the break duration as needed

    while True:
        run_focus_timer(focus_duration)

        # Optional: You can add a loop to repeat the focus and break cycles
        print(f"\nBreak time! Take a {break_duration}-minute break.")
        time.sleep(break_duration * 60)
