try:
    from edubot_sdk import EdubotGCS
    from aruco_api_rpi import omegabot_aruco
    import path as omegapath
except:
    from omegabot_poligon77.edubot_sdk import EdubotGCS
    from omegabot_poligon77.aruco_api_rpi import omegabot_aruco
    import omegabot_poligon77.path as omegapath

def recalc_points_to_cords(point):
    return 5 - point*0.18

def recalc_cords_to_points(point):
    return int(27 - int(point/0.18))




class Robot:
    def __init__(self, ip, port = 5656):
        self.ip = ip
        self.port = port
        self.cv = omegabot_aruco('rtsp://' + ip + ':8554/picam_h264')
        self.bot = EdubotGCS(ip=self.ip, mavlink_port=self.port)
