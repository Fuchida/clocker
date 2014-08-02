from clocker import Clocker

#setup
timeWatcher = Clocker()

#start the clock
timeWatcher.start()

elapsedHours = timeWatcher.elapsed_hours()
print(elapsedHours)

>> <The time in hours that has passed>

elapsedMinutes = timeWatcher.elapsed_minutes()
print(elapsedMinutes)

>> <The time in minutes that has passed>

elapsedSeconds = timeWatcher.elapsed_seconds()
print(elapsedSeconds)

>> <The time in seconds that has passed>


status = timeWatcher.current_mode()
print(status)

>> < The current running state "init" / "running" / "stopped" >

#stop the clock but do not clear the timer
timeWatcher.stop()

#stop and clear counters
timerWatcher.reset()
