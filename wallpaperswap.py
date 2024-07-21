import datetime
from subprocess import call

def set_wallpaper(path):
    '''
    call is a subprocess that allows python to interact with the OS
    The function constructs a command that tells gsettings to go to the 'org.gnome.desktop.background' schema, use the 'set' command to update the 'picture-uri' setting to the path of the new image.
    --------------------------------------------------------------------------------------------------------------------------------------------
    gsettings:executeable command used to interact with GNOME's settings, allows for the modifcation of various configuration settings.
    
    set: this arguement specifiecs that we want to set a configuration value
    
    org.gnome.desktop.background: the first parameter of the set command, indicates the schema of the gsettings database we want to modify
    
    picture-uri: specifying what in the schema we want to change
    
    you can find documentation here: https://docs.python.org/3/library/subprocess.html#subprocess.call
    '''
    call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", f"file://{path}"])
    
def main():
    now = datetime.datetime.now()
    night_wallpaper = "/usr/share/backgrounds/f40/default/f40-01-night.png"
    day_wallpaper = "/usr/share/backgrounds/f40/default/f40-01-day.png"
    
    if now.hour >= 20 or now.hour <= 6:
        set_wallpaper(night_wallpaper)
    else:
        set_wallpaper(day_wallpaper)
        
        
if __name__ =="__main__":
    main()
