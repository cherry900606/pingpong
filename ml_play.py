"""
The template of the script for the machine learning process in game pingpong
"""

class MLPlay:
    def __init__(self, side):
        """
        Constructor

        @param side A string "1P" or "2P" indicates that the `MLPlay` is used by
               which side.
        """
        self.ball_served = False
        self.side = side

    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] != "GAME_ALIVE":
            return "RESET"
        
        ball_x = scene_info["ball"][0]
        ball_y = scene_info["ball"][1]
        platform_1p_x = scene_info["platform_1P"][0]
        platform_2p_x = scene_info["platform_2P"][0]

        if not self.ball_served:
            self.ball_served = True
            return "SERVE_TO_RIGHT"
        else:
            if self.side == "1P":
                if scene_info["ball_speed"][1] > 0:
                    if ball_x > platform_1p_x:
                        return "MOVE_RIGHT"
                    else:
                        return "MOVE_LEFT"
            elif self.side == "2P":
                if scene_info["ball_speed"][1] < 0:
                    if ball_x > platform_2p_x:
                        return "MOVE_RIGHT"
                    else:
                        return "MOVE_LEFT"
            else:
                return "NONE"

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
