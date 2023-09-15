from plyer import notification
import datetime


def set_task_reminder(task_id, title, deadline):
    # Calculate time until the deadline
    deadline_datetime = datetime.datetime.strptime(deadline, '%Y-%m-%d')
    current_datetime = datetime.datetime.now()
    time_until_deadline = (deadline_datetime - current_datetime).seconds

    # Schedule a reminder notification for the task
    notification.schedule(
        title=title,
        message=f"Task '{title}' is due soon!",
        timeout=time_until_deadline
    )
