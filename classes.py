class hospital:

    def __init__(self,name,location,street,capacity):
        """create a hospotal"""
        self.name = name
        self.location = location
        self.street = street
        self.capacity = capacity


class school:

    def __init__(self,name,location,street,capacity):
        """create a school"""
        self.name = name
        self.location = location
        self.street = street
        self.capacity = capacity


class residential_building:

    def __init__(self,name,location,street,capacity):
        """create a residential building"""
        self.name = name
        self.location = location
        self.street = street
        self.capacity = capacity


class mall:

    def __init__(self,name,location,street):
        """create a mall"""
        self.name = name
        self.location = location
        self.street = street


class clinic:

    def __init__(self,name,location,street):
        """create a clinic"""
        self.name = name
        self.location = location
        self.street = street


class park:

    def __init__(self,name,location,street):
        """create a park"""
        self.name = name
        self.location = location
        self.street = street


class industrial_area:

    def __init__(self,name,location,street):
        """create a industrial area"""
        self.name = name
        self.location = location
        self.street = street

class police_station:

    def __init__(self,name,location,street):
        """create a police station"""
        self.name = name
        self.location = location
        self.street = street


class fire_station:

    def __init__(self,name,location,street):
        """create a police station"""
        self.name = name
        self.location = location
        self.street = street


class road:
    
    def __init__(self,name,start,end):
        """create a road"""
        self.name = name
        self.start = start
        self.end = end