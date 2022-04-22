class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        """
        Initialize default channel, volume, and ON/OFF position
        """
        self.tv_channel = 0
        self.tv_volume = 0
        self.tv_status = False
        

    def power(self):
        """
        Method to access and power TV on/off
        :return: TVs new status
        """
        if self.tv_status == False:
            self.tv_status = True
            
        else:
            self.tv_status = False
        
        

    def channel_up(self):
        """
        Method to check and increase channel
        :return: channel position
        """
        if self.tv_status == True:
            if self.tv_channel == Television.MAX_CHANNEL:
                self.tv_channel = Television.MIN_CHANNEL

            else:
                self.tv_channel += 1

    def channel_down(self):
        """
        Method to check and decrease channel
        :return: channel position
        """
        if self.tv_status == True:
            
            if self.tv_channel == Television.MIN_CHANNEL:
                self.tv_channel = Television.MAX_CHANNEL

            else:
                self.tv_channel -= 1

    def volume_up(self):
        """
        Method to access and increase volume
        :return: volume position
        """
        if self.tv_status == True:
            if self.tv_volume == Television.MAX_VOLUME:
                pass
            
            else:
                self.tv_volume += 1
                
    def volume_down(self):
        """
        Method to access and decrease volume
        :return: volume position
        """
        if self.tv_status == True:
            if self.tv_volume == Television.MIN_VOLUME:
                pass
            
            else:
                self.tv_volume -= 1

    def __str__(self):
        """
        Method that accesses tv status, channel, and volume position
        :return: TV details (Volume, Channel, ON/OFF)
        """
        if self.tv_status == True:
            return(f"Tv status: Is on, Channel = {self.tv_channel}, Volume = {self.tv_volume}")
        
        else:
            return(f"Tv status: Is off, Channel = {self.tv_channel}, Volume = {self.tv_volume}")
