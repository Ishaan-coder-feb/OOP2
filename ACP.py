class ArtGallery:
    def __init__(self, gallery_name, location):
        self.gallery_name = gallery_name
        self.location = location
        self.artworks = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)
        print(f"'{artwork}' added to {self.gallery_name}.")

    def remove_artwork(self, artwork):
        if artwork in self.artworks:
            self.artworks.remove(artwork)
            print(f"'{artwork}' removed.")
        else:
            print(f"'{artwork}' not found in the gallery.")

    def display(self):
        print(f"\n--- {self.gallery_name} ({self.location}) ---")
        if self.artworks:
            for i, artwork in enumerate(self.artworks, 1):
                print(f"{i}. {artwork}")
        else:
            print("No artworks yet. Add some!")

    def __del__(self):
        print(f"Gallery '{self.gallery_name}' has been deleted. Goodbye!")

my_art = ArtGallery("Art Gallery", "France")

while True:
    print("\n1. Add Artwork")
    print("2. Remove Artwork")
    print("3. View Art Gallery")
    print("4. Delete & Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        artwork = input("Enter artwork name: ")
        my_art.add_artwork(artwork)

    elif choice == "2":
        artwork = input("Enter artwork to remove: ")
        my_art.remove_artwork(artwork)

    elif choice == "3":
        my_art.display()

    elif choice == "4":
        del my_art
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

    
        
