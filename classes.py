import math

class Hospital:

    def __init__(self,name,location,street,capacity,id):
        """create a hospotal"""
        self.name = name
        self.location = location
        self.street = street
        self.capacity = capacity
        self.id = id


class School:

    def __init__(self,name,location,street,capacity,id):
        """create a school"""
        self.name = name
        self.location = location
        self.street = street
        self.capacity = capacity
        self.id = id


class Residential_building:

    def __init__(self,name,location,street,capacity,id):
        """create a residential building"""
        self.name = name
        self.location = location
        self.street = street
        self.capacity = capacity
        self.id = id


class Mall:

    def __init__(self,name,location,street,id):
        """create a mall"""
        self.name = name
        self.location = location
        self.street = street
        self.id = id


class Clinic:

    def __init__(self,name,location,street,id):
        """create a clinic"""
        self.name = name
        self.location = location
        self.street = street
        self.id = id


class Station:

    def __init__(self,name,location,street,id):
        """create a station"""
        self.name = name
        self.location = location
        self.street = street
        self.id = id


class Park:

    def __init__(self,name,location,street,id):
        """create a park"""
        self.name = name
        self.location = location
        self.street = street
        self.id = id


class Industrial_area:

    def __init__(self,name,location,street,id):
        """create a industrial area"""
        self.name = name
        self.location = location
        self.street = street
        self.id = id

class Police_station:

    def __init__(self,name,location,street,id):
        """create a police station"""
        self.name = name
        self.location = location
        self.street = street
        self.id = id


class Fire_station:

    def __init__(self,name,location,street,id):
        """create a police station"""
        self.name = name
        self.location = location
        self.street = street
        self.id = id


class Subway:

    def __init__(self, name, start, end,id):
        """create a Subway"""
        self.name = name
        self.start = start
        self.end = end
        self.depending_facilities = []
        self.id = id

    def add_facilities(self, facility):
        self.depending_facilities.append((facility.id, cal_distance(self, facility)))

class Street:
    
    def __init__(self,name,start,end,id):
        """create a Street"""
        self.name = name
        self.start = start
        self.end = end
        self.depending_facilities = []
        self.id = id

    def add_facilities(self, facility):
        self.depending_facilities.append((facility.id, cal_distance(self, facility)))

def cal_distance(self, facility):
    start = self.start
    end = self.end
    point = facility.location

    # 计算线段的方向向量
    segment_vector = (end[0] - start[0], end[1] - start[1])
    # 计算起点到目标点的向量
    point_vector = (point[0] - start[0], point[1] - start[1])

    # 计算点到线段起点的向量在线段方向上的投影长度
    projection_length = (segment_vector[0] * point_vector[0] + segment_vector[1] * point_vector[1]) / \
                        (segment_vector[0] ** 2 + segment_vector[1] ** 2)

    # 将投影长度限制在线段范围内
    projection_length = max(0, min(1, projection_length))

    # 计算垂线相交点坐标
    intersection_point = (start[0] + projection_length * segment_vector[0],
                          start[1] + projection_length * segment_vector[1])

    return intersection_point
