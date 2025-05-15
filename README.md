# 3D Printing Class Availability Daily Check

An alert for newly available 3d printing classes to schedule at the library.

MLK Labs in DC offers apparently highly desirable 3d printing classes. These are posted 30 days out, but quickly run out of the limited spots each class has. I haven't been able to get one for a few weeks now.

This script checks the page once a day to see if there is any availability and if so, makes a push request to this repository, which then triggers an email to me as a reminder to make an appointment right when I wake up.

In Github, under Settings, I enabled Email Notifications for push events for the repository. The Actions workflow pushes a small text file if availability is found.
