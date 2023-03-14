class Guests:
    def __init__(self, name, wallet, fave_song):
        self.name = name
        self.wallet = wallet
        self.fave_song = fave_song

    def pay_entry(self, entry_fee):
        self.wallet -= entry_fee

        # guest is only one who should access its wallet
    
    # def fave_song_reaction(self, fave_song):
    #     if self.fave_song 
    #         print("Whoo!") 
    # no, conditional loop, if song == fave song return whoop
    # or return nothing
    