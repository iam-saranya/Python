import time
import winsound

def set_alarm():
    print("Enter the time for the alarm (format: HH:MM AM/PM):")
    alarm_time = input()
    return alarm_time

def play_alarm_sound():
    frequency = 2500  # Set frequency to 2500 Hertz
    duration = 1000  # Set duration to 1000 milliseconds (1 second)
    winsound.Beep(frequency, duration)

def alarm_clock():
    alarm_time = set_alarm()
    
    while True:
        current_time = time.strftime("%I:%M %p")
        
        if current_time == alarm_time:
            print("Time to wake up!")
            play_alarm_sound()
            break
        
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    alarm_clock()
