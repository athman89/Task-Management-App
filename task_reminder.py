import datetime
from plyer import notification


def set_task_remainder(task_id, title, deadline, reminder_seconds):
    try:
        # Parse the deadline string into a datetime object
        deadline_datetime = datetime.datetime.strptime(deadline, "%Y-%m-%d %H:%M:%S")

        # Calculate the reminder time based on the provided seconds
        reminder_time = deadline_datetime - datetime.timedelta(seconds=reminder_seconds)

        # Calculate the time until the reminder
        current_datetime = datetime.datetime.now()
        time_until_reminder = reminder_time - current_datetime

        if time_until_reminder.total_seconds() > 0:
            # Schedule a notification for the specified time
            notification.schedule(
                title="Task Reminder",
                message=f"Task '{title}' with ID {task_id} is due!",
                timeout=time_until_reminder.total_seconds(),
            )
        else:
            print("Reminder time is in the past. Skipping reminder.")

    except ValueError as e:
        print(f"Error parsing date: {e}")
    except Exception as e:
        print(f"Error scheduling reminder: {e}")
