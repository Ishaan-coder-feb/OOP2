class music:
    def __init__(self,name,genre):
        self.name=name
        self.genre=genre
        self.song=[]
    def add_song(self,song):
        self.song.append(song)
        print("The song has been added")
    def remove_song(self,song):
        self.song.remove(song)
        print("The song has been removed")
    def display_song(self):
        for song in self.song:
            print(song)
    def __del__(self):
        print("The playlist has been deleted")
name=input("Enter playlist name:")
genre=input("Enter playlist genre:")
playlist=music(name,genre)
while True:
    print("You have 4 opitons:1.To add a song.2.To removve a song.3.to display the playlist.4.To delete the playlist")
    choice=input("What is you choice,answer with number 1,2,3,4")
    if choice=="1":
        song=input("Enter the name of the song you want to add")
        playlist.add_song(song)
    elif choice=="2":
        song=input("Enter the name of the song you want to remove")
        playlist.remove_song(song)
    elif choice=="3":
        playlist.display_song()
    elif choice=="4":
      del playlist
      print("Thank you for using playlist manager!")
      break
    else:
        print("Invalid choice!")
        
        
