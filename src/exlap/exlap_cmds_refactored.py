#!/opt/homebrew/bin/python3
"""
Refactored EXLAP commands module with factory pattern to reduce code duplication.
"""
import exlap_v2 as api

# Session counter
_session_number = 98
_MAX_SESSION_ID = 999999998


def _increment_session() -> int:
    """Increment and return session number"""
    global _session_number
    if _session_number <= _MAX_SESSION_ID:
        _session_number += 1
    else:
        _session_number = 1
    return _session_number


def create_subscribe_command(url: str, ival: int = 100, timestamp: str = "true") -> str:
    """
    Factory function to create subscription commands.
    
    Args:
        url: The capability URL to subscribe to
        ival: Interval value (default 100)
        timestamp: Whether to include timestamp (default "true")
    
    Returns:
        XML string representation of the subscribe command
    """
    message = api.Req()
    message.set_id(_increment_session())
    
    subscribe = api.Subscribe()
    subscribe.set_url(url)
    subscribe.set_ival(ival)
    subscribe.set_timeStamp(timestamp)
    message.set_Subscribe(subscribe)
    
    return str(message)


def create_heartbeat() -> str:
    """Create heartbeat command"""
    message = api.Req()
    message.set_id(_increment_session())
    heartbeat = api.Alive()
    message.set_Alive(heartbeat)
    return str(message)


def create_dir_command(pattern: str = "*") -> str:
    """Create directory listing command"""
    message = api.Req()
    message.set_id(_increment_session())
    dir_cmd = api.Dir()
    dir_cmd.set_urlPattern(pattern)
    message.set_Dir(dir_cmd)
    return str(message)


def create_capability_request() -> str:
    """Create protocol capability request"""
    message = api.Req()
    message.set_id(_increment_session())
    protocol = api.Protocol()
    protocol.set_version(1)
    protocol.set_returnCapabilities("true")
    message.set_Protocol(protocol)
    return str(message)


# ============================================================================
# Pre-defined subscription commands using factory function
# ============================================================================

# Vehicle Dynamics
Sub_lateralAcceleration = lambda: create_subscribe_command("lateralAcceleration", ival=0)
Sub_longitudinalAcceleration = lambda: create_subscribe_command("longitudinalAcceleration")
Sub_espTyreVelocities = lambda: create_subscribe_command("espTyreVelocities", ival=0)
Sub_vehicleSpeed = lambda: create_subscribe_command("vehicleSpeed")
Sub_wheelAngle = lambda: create_subscribe_command("wheelAngle")
Sub_acceleratorPosition = lambda: create_subscribe_command("acceleratorPosition")
Sub_brakePressure = lambda: create_subscribe_command("brakePressure")
Sub_currentGear = lambda: create_subscribe_command("currentGear", ival=0)
Sub_engineSpeed = lambda: create_subscribe_command("engineSpeed")
Sub_chassisUndersteering = lambda: create_subscribe_command("chassisUndersteering")
Sub_chassisOversteering = lambda: create_subscribe_command("chassisOversteering")

# Engine & Powertrain
Sub_oilTemperature = lambda: create_subscribe_command("oilTemperature")
Sub_oilLevel = lambda: create_subscribe_command("oilLevel")
Sub_coolantTemperature = lambda: create_subscribe_command("coolantTemperature")
Sub_gearboxOilTemperature = lambda: create_subscribe_command("gearboxOilTemperature")
Sub_combustionEngineDisplacement = lambda: create_subscribe_command("combustionEngineDisplacement")
Sub_combustionEngineInjection = lambda: create_subscribe_command("combustionEngineInjection")
Sub_currentTorque = lambda: create_subscribe_command("currentTorque")
Sub_currentOutputPower = lambda: create_subscribe_command("currentOutputPower")
Sub_maxOutputPower = lambda: create_subscribe_command("maxOutputPower")
Sub_torqueDistribution = lambda: create_subscribe_command("torqueDistribution")
Sub_allWheelDriveTorque = lambda: create_subscribe_command("allWheelDriveTorque")
Sub_relAllWheelDriveTorque = lambda: create_subscribe_command("relAllWheelDriveTorque")
Sub_gearTransmissionMode = lambda: create_subscribe_command("gearTransmissionMode")
Sub_recommendedGear = lambda: create_subscribe_command("recommendedGear")
Sub_shiftRecommendation = lambda: create_subscribe_command("shiftRecommendation")
Sub_clutch = lambda: create_subscribe_command("clutch")

# Fuel & Consumption
Sub_fuelLevelState = lambda: create_subscribe_command("fuelLevelState")
Sub_tankLevelPrimary = lambda: create_subscribe_command("tankLevelPrimary")
Sub_tankLevelSecondary = lambda: create_subscribe_command("tankLevelSecondary")
Sub_fuelWarningPrimaryTank = lambda: create_subscribe_command("fuelWarningPrimaryTank")
Sub_fuelWarningSecondaryTank = lambda: create_subscribe_command("fuelWarningSecondaryTank")
Sub_shortTermConsumptionPrimary = lambda: create_subscribe_command("shortTermConsumptionPrimary")
Sub_shortTermConsumptionSecondary = lambda: create_subscribe_command("shortTermConsumptionSecondary")
Sub_longTermConsumptionPrimary = lambda: create_subscribe_command("longTermConsumptionPrimary")
Sub_longTermConsumptionSecondary = lambda: create_subscribe_command("longTermConsumptionSecondary")
Sub_cycleConsumptionPrimary = lambda: create_subscribe_command("cycleConsumptionPrimary")
Sub_cycleConsumptionSecondary = lambda: create_subscribe_command("cycleConsumptionSecondary")
Sub_currentConsumptionPrimary = lambda: create_subscribe_command("currentConsumptionPrimary")
Sub_currentConsumptionSecondary = lambda: create_subscribe_command("currentConsumptionSecondary")
Sub_consumptionShortTermGeneral = lambda: create_subscribe_command("consumptionShortTermGeneral")
Sub_consumptionLongTermGeneral = lambda: create_subscribe_command("consumptionLongTermGeneral")
Sub_powermeter = lambda: create_subscribe_command("powermeter")

# Navigation
Sub_Nav_GeoPosition = lambda: create_subscribe_command("Nav_GeoPosition")
Sub_Nav_CurrentPosition = lambda: create_subscribe_command("Nav_CurrentPosition")
Sub_Nav_Heading = lambda: create_subscribe_command("Nav_Heading")
Sub_Nav_Altitude = lambda: create_subscribe_command("Nav_Altitude")
Sub_Nav_GuidanceDestination = lambda: create_subscribe_command("Nav_GuidanceDestination")
Sub_Nav_GuidanceRemaining = lambda: create_subscribe_command("Nav_GuidanceRemaining")
Sub_Nav_GuidanceState = lambda: create_subscribe_command("Nav_GuidanceState")
Sub_Nav_StartGuidance = lambda: create_subscribe_command("Nav_StartGuidance")
Sub_Nav_StopGuidance = lambda: create_subscribe_command("Nav_StopGuidance")
Sub_Nav_LastDestinations = lambda: create_subscribe_command("Nav_LastDestinations")
Sub_Nav_ResolveAddress = lambda: create_subscribe_command("Nav_ResolveAddress")
Sub_Nav_ResolveLastDestination = lambda: create_subscribe_command("Nav_ResolveLastDestination")
Sub_Nav_GpxImport = lambda: create_subscribe_command("Nav_GpxImport")
Sub_navPosition_HP = lambda: create_subscribe_command("navPosition_HP")

# Climate & Interior
Sub_outsideTemperature = lambda: create_subscribe_command("outsideTemperature")
Sub_temperatureRearRight = lambda: create_subscribe_command("temperatureRearRight")
Sub_temperatureRearLeft = lambda: create_subscribe_command("temperatureRearLeft")
Sub_hevacConfiguration = lambda: create_subscribe_command("hevacConfiguration")
Sub_hevacFanLevelRear = lambda: create_subscribe_command("hevacFanLevelRear")
Sub_seatHeater_zone1 = lambda: create_subscribe_command("seatHeater_zone1")
Sub_seatHeater_zone2 = lambda: create_subscribe_command("seatHeater_zone2")
Sub_seatHeater_zone3 = lambda: create_subscribe_command("seatHeater_zone3")
Sub_seatHeater_zone4 = lambda: create_subscribe_command("seatHeater_zone4")
Sub_seatVentilation_zone3 = lambda: create_subscribe_command("seatVentilation_zone3")
Sub_seatVentilation_zone4 = lambda: create_subscribe_command("seatVentilation_zone4")

# Lights & Ambience
Sub_ambienceLight_sets = lambda: create_subscribe_command("ambienceLight_sets")
Sub_ambienceLight_installation = lambda: create_subscribe_command("ambienceLight_installation")
Sub_ambienceLight_brightness = lambda: create_subscribe_command("ambienceLight_brightness")
Sub_ambienceLight_control = lambda: create_subscribe_command("ambienceLight_control")
Sub_ambienceLight_profiles = lambda: create_subscribe_command("ambienceLight_profiles")
Sub_Car_ambienceLightColour = lambda: create_subscribe_command("Car_ambienceLightColour")
Sub_lightState_front = lambda: create_subscribe_command("lightState_front")
Sub_lightState_rear = lambda: create_subscribe_command("lightState_rear")

# Suspension & Chassis
Sub_suspensionProfile = lambda: create_subscribe_command("suspensionProfile")
Sub_suspensionStates = lambda: create_subscribe_command("suspensionStates")
Sub_offroadTiltAngle = lambda: create_subscribe_command("offroadTiltAngle")
Sub_offroadTiltAngleMaxValues = lambda: create_subscribe_command("offroadTiltAngleMaxValues")

# Tyres
Sub_tyreTemperatures = lambda: create_subscribe_command("tyreTemperatures")
Sub_tyreTemperatures_HP = lambda: create_subscribe_command("tyreTemperatures_HP")
Sub_tyrePressures = lambda: create_subscribe_command("tyrePressures")
Sub_tyreRequiredPressures = lambda: create_subscribe_command("tyreRequiredPressures")
Sub_tyreStates = lambda: create_subscribe_command("tyreStates")

# Vehicle State
Sub_Car_vehicleState = lambda: create_subscribe_command("Car_vehicleState")
Sub_Car_vehicleInformation = lambda: create_subscribe_command("Car_vehicleInformation")
Sub_vehicleIdenticationNumber = lambda: create_subscribe_command("vehicleIdenticationNumber")
Sub_vehicleTime = lambda: create_subscribe_command("vehicleTime")
Sub_vehicleDate = lambda: create_subscribe_command("vehicleDate")
Sub_doorState = lambda: create_subscribe_command("doorState")
Sub_parkingBrake = lambda: create_subscribe_command("parkingBrake")
Sub_startStopState = lambda: create_subscribe_command("startStopState")
Sub_driveMode = lambda: create_subscribe_command("driveMode")
Sub_hevOperationMode = lambda: create_subscribe_command("hevOperationMode")
Sub_coastingIsActive = lambda: create_subscribe_command("coastingIsActive")
Sub_recuperationLevel = lambda: create_subscribe_command("recuperationLevel")
Sub_accIsActive = lambda: create_subscribe_command("accIsActive")
Sub_blinkingState = lambda: create_subscribe_command("blinkingState")
Sub_driverIsBraking = lambda: create_subscribe_command("driverIsBraking")
Sub_reverseGear = lambda: create_subscribe_command("reverseGear")
Sub_acceleratorKickDown = lambda: create_subscribe_command("acceleratorKickDown")

# ESP & Safety
Sub_espLamp = lambda: create_subscribe_command("espLamp")
Sub_espPassiveSensing = lambda: create_subscribe_command("espPassiveSensing")

# System & Configuration
Sub_System_DayNight = lambda: create_subscribe_command("System_DayNight")
Sub_System_HMISkin = lambda: create_subscribe_command("System_HMISkin")
Sub_System_Language = lambda: create_subscribe_command("System_Language")
Sub_System_ProximityRecognition = lambda: create_subscribe_command("System_ProximityRecognition")
Sub_System_RestrictionMode = lambda: create_subscribe_command("System_RestrictionMode")
Sub_System_UnitDistance = lambda: create_subscribe_command("System_UnitDistance")
Sub_displayNightDesign = lambda: create_subscribe_command("displayNightDesign")

# Units
Sub_unitTimeFormat = lambda: create_subscribe_command("unitTimeFormat")
Sub_unitDateFormat = lambda: create_subscribe_command("unitDateFormat")
Sub_unitPressure = lambda: create_subscribe_command("unitPressure")
Sub_unitTemperature = lambda: create_subscribe_command("unitTemperature")
Sub_unitVolume = lambda: create_subscribe_command("unitVolume")

# StopWatch
Sub_stopWatch_totalTime = lambda: create_subscribe_command("stopWatch_totalTime")
Sub_stopWatch_lapTime = lambda: create_subscribe_command("stopWatch_lapTime")
Sub_stopWatch_previousLapTime = lambda: create_subscribe_command("stopWatch_previousLapTime")
Sub_stopWatch_control = lambda: create_subscribe_command("stopWatch_control")

# Distance & Mileage
Sub_totalDistance = lambda: create_subscribe_command("totalDistance")
Sub_dayMilage = lambda: create_subscribe_command("dayMilage")
Sub_dayMilage_HP = lambda: create_subscribe_command("dayMilage_HP")

# Service & Maintenance
Sub_serviceInspection = lambda: create_subscribe_command("serviceInspection")
Sub_serviceOil = lambda: create_subscribe_command("serviceOil")

# Charging & Air Pressure
Sub_absChargingAirPressure = lambda: create_subscribe_command("absChargingAirPressure")
Sub_relChargingAirPressure = lambda: create_subscribe_command("relChargingAirPressure")
Sub_maxChargingAirPressure = lambda: create_subscribe_command("maxChargingAirPressure")

# Battery & Electrical
Sub_batteryVoltage = lambda: create_subscribe_command("batteryVoltage")

# Engine Types
Sub_engineTypes = lambda: create_subscribe_command("engineTypes")

# Context & States
Sub_Context_States = lambda: create_subscribe_command("Context_States")

# Clamp State
Sub_clampState = lambda: create_subscribe_command("clampState")

# ExAc (External Access)
Sub_ExAc_Resources = lambda: create_subscribe_command("ExAc_Resources")
Sub_ExAc_GetToken = lambda: create_subscribe_command("ExAc_GetToken")
Sub_ExAc_TouchToken = lambda: create_subscribe_command("ExAc_TouchToken")
Sub_ExAc_ReleaseToken = lambda: create_subscribe_command("ExAc_ReleaseToken")

# Yaw Rate
Sub_yawRate = lambda: create_subscribe_command("yawRate")

# Heartbeat
Req_heartbeat = create_heartbeat
Req_Dir = create_dir_command
Req_Capability = create_capability_request
