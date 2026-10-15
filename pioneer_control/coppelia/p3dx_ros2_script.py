function sysCall_init()
    sim = require('sim')
    simROS2 = require('simROS2')

    -- Change this if your model is named differently (e.g. "/PioneerP3DX[0]")
    local base = "/PioneerP3DX"

    motorLeft  = sim.getObject(base .. "/leftMotor")
    motorRight = sim.getObject(base .. "/rightMotor")

    usensors = {}
    for i = 1, 16 do
        usensors[i] = sim.getObject(base .. "/ultrasonicSensor[" .. (i - 1) .. "]")
    end

    -- Pioneer 3-DX constants (meters)
    wheelRadius = 0.0975
    wheelBase = 0.331
    maxDetectionDist = 0
    

    cmdVelSub = simROS2.createSubscription('/cmd_vel', 'geometry_msgs/msg/Twist', 'cmdVel_callback')
    sensorPub = simROS2.createPublisher('/ultrasonic_sensors', 'std_msgs/msg/String')
end

function cmdVel_callback(msg)
    local v = msg.linear.x
    local omega = msg.angular.z

    local vLeft  = (v - (omega * wheelBase / 2.0)) / wheelRadius
    local vRight = (v + (omega * wheelBase / 2.0)) / wheelRadius

    sim.setJointTargetVelocity(motorLeft, vLeft)
    sim.setJointTargetVelocity(motorRight, vRight)
end

function sysCall_sensing()
    local readings = {}
    for i = 1, 16 do
        local res, dist = sim.readProximitySensor(usensors[i])
        if res > 0 then
            readings[i] = string.format("%.4f", dist)
        else
            readings[i] = string.format("%.4f", maxDetectionDist)
        end
    end

    -- String message: 16 comma-separated distances
    simROS2.publish(sensorPub, { data = table.concat(readings, ",") })
end

function sysCall_cleanup()
    if cmdVelSub then simROS2.shutdownSubscription(cmdVelSub) end
    if sensorPub then simROS2.shutdownPublisher(sensorPub) end
end