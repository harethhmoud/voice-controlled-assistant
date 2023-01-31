import os

d = '/Applications'
dy = "/System/Applications"
native_apple = ["App Store", "Automator", "Books", "Calculator", "Calendar", "Chess", "Clock", "Contacts",
                "Dictionary", "FaceTime", "Find My", "Font Book", "GarageBand", "Home", "Image Capture", "iMovie",
                "Keynote", "Launchpad", "Mail", "MainStage", "Maps", "Messages", "Mission Control", "Motion", "Music",
                "News", "Notes", "Numbers", "Pages", "Photo Booth", "Photos", "Podcasts", "Preview",
                "QuickTime Player", "Reminders", "Safari", "Shortcuts", "Siri", "Stickies", "Stocks",
                "System Settings", "TextEdit", "Time Machine", "TV", "Utilities", "Voice Memos", "Weather"]
apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))


def opens_app(app):
    app = app.title()
    if app in native_apple:
        os.system('open ' + dy + '/%s.app' % app.replace(' ', '\ '))
    else:
        os.system('open ' + d + '/%s.app' % app.replace(' ', '\ '))
