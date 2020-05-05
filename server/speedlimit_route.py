from app import application
from flask import request

description = "This page calculate an exponential fine if you exceding the speed limit"
label = "Speed Limit"

@application.route("/speedlimit", methods=["POST"])

def speedlimit():
        content = request.json
        speed = content['speed']
        overlimit = speed - 120
        speed_calc = speed/60
        fine = ''
        
        if speed_calc <= 2:
            return {
            "result": "You are safe. Your speed is {} km/h" .format(speed)
            }
        
        elif speed_calc > 2 and speed_calc <= 2.5:
            fine = speed * 2
            return {
                "result": "You've got a {}$ fine because of your {} km/h speed, {} over the limit of 120 km/h" .format(fine,speed,overlimit)
            }
        
        elif speed_calc > 2.5 and speed_calc <= 3:
            fine = speed * 3
            return {
                "result": "You've got a {}$ fine because of your {} km/h speed, {} over the limit of 120 km/h" .format(fine,speed,overlimit)
            }
        
        else:
            fine = speed * 5
            return {
                "result" : "You are a criminal. Pay this heavy {}$ fine because of your crazy {} km/h speed, {} over the limit of 120 km/h" .format(fine,speed,overlimit)
            }
    
    
    
    
     
        