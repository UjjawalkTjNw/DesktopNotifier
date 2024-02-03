#This is just a readme file to note usage of tkinter
1. Tkinter is foundation for creating windows, creating text field, creating menus, toolbars
2. It can be used to display information , give popups on window
3. Can be used to handle events like popup button, clicks




V1: Basic code that just shows notification on desktop
    =>create a new instance of window(root)
    =>close it (withdraw)
V2: Shows notification for a certain duration then gets closed automatically
    =>include a new parameter "duration"
    =>new function to close notification after specified "duration" (if duration is 5 sec, it waits 5 sec to terminate the window/program after Ok is clicked)
    => create a child window of root, and removed messagebox.showinfo(title, message); helpful in closing notitication after given duration