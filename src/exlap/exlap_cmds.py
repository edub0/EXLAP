#!/opt/homebrew/bin/python3

import inspect
import exlap_v2 as api

# --Global--
# Because VAG starts at 99
session_number = 98


def conn_count():
    """exlap client message counter included in every client created EXLAP cmd
    to let you track responses
    """
    global session_number
    if session_number <= 999999998:
        session_number += 1
    else:
        session_number = 1

def Req_heartbeat():
    """a subscription heartbeat message sent every 2 seconds"""
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    heartbeat = api.Alive()
    message.set_Alive(heartbeat)
    return str(message)

def Req_Dir(dir_filter):
    """
    create a Dir command to display avaliable commands.
    use '*' for default behavior. Can also submit a specific string to search
    on capabilities matching the string, ie.
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    dir = api.Dir()
    dir.set_urlPattern(dir_filter)
    message.set_Dir(dir)
    return str(message)

def Req_Capability():
    """
    Setup a request capabilities message
    ie. <Req id="99"><Protocol version="1" returnCapabilities=""true""/></Req>
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    protocol = api.Protocol()
    protocol.set_version(1)
    protocol.set_returnCapabilities("true")
    message.set_Protocol(protocol)
    return str(message)


def Sub_displayNightDesign():
    """
    unknown purpose
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("displayNightDesign")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_displayNightDesign():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("displayNightDesign")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_shortTermConsumptionPrimary():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("shortTermConsumptionPrimary")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_serviceInspection():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("serviceInspection")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_Nav_GeoPosition():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("Nav_GeoPosition")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_Car_vehicleState():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("Car_vehicleState")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_System_HMISkin():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("System_HMISkin")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_unitTimeFormat():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("unitTimeFormat")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_gearboxOilTemperature():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("gearboxOilTemperature")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_ExAc_Resources():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("ExAc_Resources")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_relChargingAirPressure():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("relChargingAirPressure")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_reverseGear():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("reverseGear")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_Nav_CurrentPosition():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("Nav_CurrentPosition")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_vehicleDate():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("vehicleDate")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_acceleratorKickDown():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("acceleratorKickDown")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_System_RestrictionMode():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("System_RestrictionMode")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_dayMilage_HP():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("dayMilage_HP")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_offroadTiltAngle():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("offroadTiltAngle")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_Nav_GuidanceDestination():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("Nav_GuidanceDestination")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_unitDateFormat():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("unitDateFormat")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_longTermConsumptionPrimary():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("longTermConsumptionPrimary")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_outsideTemperature():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("outsideTemperature")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_clampState():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("clampState")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_shortTermConsumptionSecondary():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("shortTermConsumptionSecondary")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_combustionEngineDisplacement():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("combustionEngineDisplacement")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_oilTemperature():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("oilTemperature")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_oilLevel():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("oilLevel")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_Nav_GuidanceRemaining():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("Nav_GuidanceRemaining")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_hevacConfiguration():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("hevacConfiguration")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_Nav_Altitude():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("Nav_Altitude")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_tyreTemperatures():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("tyreTemperatures")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_driverIsBraking():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("driverIsBraking")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_ambienceLight_sets():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("ambienceLight_sets")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_engineTypes():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("engineTypes")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_chassisUndersteering():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("chassisUndersteering")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_gearTransmissionMode():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("gearTransmissionMode")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_blinkingState():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("blinkingState")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_longTermConsumptionSecondary():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("longTermConsumptionSecondary")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_stopWatch_totalTime():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("stopWatch_totalTime")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_vehicleTime():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("vehicleTime")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_coastingIsActive():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("coastingIsActive")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_seatHeater_zone1():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("seatHeater_zone1")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_seatHeater_zone2():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("seatHeater_zone2")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_Nav_Heading():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("Nav_Heading")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_seatHeater_zone3():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("seatHeater_zone3")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_Car_ambienceLightColour():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("Car_ambienceLightColour")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_seatHeater_zone4():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("seatHeater_zone4")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_hevOperationMode():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("hevOperationMode")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_combustionEngineInjection():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("combustionEngineInjection")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_currentGear():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("currentGear")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_espTyreVelocities():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("espTyreVelocities")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_fuelLevelState():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("fuelLevelState")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_Nav_GuidanceState():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("Nav_GuidanceState")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_totalDistance():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("totalDistance")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_tyreRequiredPressures():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("tyreRequiredPressures")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_cycleConsumptionPrimary():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("cycleConsumptionPrimary")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_startStopState():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("startStopState")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_Context_States():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("Context_States")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_tyreStates():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("tyreStates")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_unitPressure():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("unitPressure")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_espPassiveSensing():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("espPassiveSensing")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_System_DayNight():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("System_DayNight")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_tyreTemperatures_HP():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("tyreTemperatures_HP")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_ambienceLight_installation():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("ambienceLight_installation")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_brakePressure():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("brakePressure")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_hevacFanLevelRear():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("hevacFanLevelRear")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_maxChargingAirPressure():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("maxChargingAirPressure")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_lightState_front():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("lightState_front")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_currentTorque():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("currentTorque")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_clutch():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("clutch")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_consumptionShortTermGeneral():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("consumptionShortTermGeneral")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_engineSpeed():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("engineSpeed")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_seatVentilation_zone3():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("seatVentilation_zone3")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_stopWatch_lapTime():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("stopWatch_lapTime")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_seatVentilation_zone4():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("seatVentilation_zone4")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_Nav_LastDestinations():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("Nav_LastDestinations")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_absChargingAirPressure():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("absChargingAirPressure")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_System_UnitDistance():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("System_UnitDistance")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_parkingBrake():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("parkingBrake")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_vehicleSpeed():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("vehicleSpeed")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_espLamp():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("espLamp")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_longitudinalAcceleration():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("longitudinalAcceleration")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_doorState():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("doorState")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_cycleConsumptionSecondary():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("cycleConsumptionSecondary")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_System_ProximityRecognition():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("System_ProximityRecognition")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_coolantTemperature():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("coolantTemperature")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_torqueDistribution():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("torqueDistribution")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_ambienceLight_brightness():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("ambienceLight_brightness")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_vehicleIdenticationNumber():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("vehicleIdenticationNumber")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_stopWatch_previousLapTime():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("stopWatch_previousLapTime")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_recuperationLevel():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("recuperationLevel")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_chassisOversteering():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("chassisOversteering")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_tankLevelSecondary():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("tankLevelSecondary")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_unitTemperature():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("unitTemperature")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_lateralAcceleration():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("lateralAcceleration")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_temperatureRearRight():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("temperatureRearRight")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_unitVolume():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("unitVolume")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_acceleratorPosition():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("acceleratorPosition")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_Car_vehicleInformation():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("Car_vehicleInformation")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_offroadTiltAngleMaxValues():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("offroadTiltAngleMaxValues")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_recommendedGear():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("recommendedGear")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_temperatureRearLeft():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("temperatureRearLeft")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_consumptionLongTermGeneral():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("consumptionLongTermGeneral")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_allWheelDriveTorque():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("allWheelDriveTorque")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_currentConsumptionSecondary():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("currentConsumptionSecondary")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_powermeter():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("powermeter")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_tankLevelPrimary():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("tankLevelPrimary")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_relAllWheelDriveTorque():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("relAllWheelDriveTorque")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_navPosition_HP():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("navPosition_HP")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_shiftRecommendation():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("shiftRecommendation")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_fuelWarningSecondaryTank():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("fuelWarningSecondaryTank")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_wheelAngle():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("wheelAngle")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_accIsActive():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("accIsActive")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_currentOutputPower():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("currentOutputPower")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_currentConsumptionPrimary():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("currentConsumptionPrimary")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_suspensionProfile():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("suspensionProfile")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_suspensionStates():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("suspensionStates")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_dayMilage():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("dayMilage")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_batteryVoltage():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("batteryVoltage")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_ambienceLight_profiles():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("ambienceLight_profiles")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_tyrePressures():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("tyrePressures")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_fuelWarningPrimaryTank():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("fuelWarningPrimaryTank")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_serviceOil():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("serviceOil")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_yawRate():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("yawRate")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_driveMode():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("driveMode")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_lightState_rear():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("lightState_rear")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_maxOutputPower():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("maxOutputPower")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_System_Language():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("System_Language")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


# Cmd with Functions


def Sub_Nav_GpxImport():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("Nav_GpxImport")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_temperature_control():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("temperature_control")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_Nav_StartGuidance():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("Nav_StartGuidance")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_stopWatch_control():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("stopWatch_control")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_ExAc_GetToken():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("ExAc_GetToken")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_ExAc_TouchToken():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("ExAc_TouchToken")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_ExAc_ReleaseToken():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("ExAc_ReleaseToken")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_Nav_StopGuidance():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("Nav_StopGuidance")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_Nav_ResolveAddress():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("Nav_ResolveAddress")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_ambienceLight_control():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("ambienceLight_control")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


def Sub_Nav_ResolveLastDestination():
    """
    capability to be determined
    """
    message = api.Req()
    conn_count()
    message.set_id(session_number)
    subscribe = api.Subscribe()
    subscribe.set_url("Nav_ResolveLastDestination")
    subscribe.set_ival(100)
    subscribe.set_timeStamp("true")
    message.set_Subscribe(subscribe)
    return str(message)


# Utilities
#
# CMD = [
#     'displayNightDesign',
#     'shortTermConsumptionPrimary',
#     'serviceInspection',
#     'Nav_GpxImport',
#     'temperature_control',
#     'Nav_GeoPosition',
#     'Car_vehicleState',
#     'System_HMISkin',
#     'unitTimeFormat',
#     'gearboxOilTemperature',
#     'ExAc_Resources',
#     'relChargingAirPressure',
#     'reverseGear',
#     'Nav_CurrentPosition',
#     'vehicleDate',
#     'acceleratorKickDown',
#     'System_RestrictionMode',
#     'dayMilage_HP',
#     'offroadTiltAngle',
#     'Nav_GuidanceDestination',
#     'unitDateFormat',
#     'longTermConsumptionPrimary',
#     'outsideTemperature',
#     'clampState',
#     'shortTermConsumptionSecondary',
#     'combustionEngineDisplacement',
#     'Nav_StartGuidance',
#     'oilTemperature',
#     'oilLevel',
#     'stopWatch_control',
#     'Nav_GuidanceRemaining',
#     'hevacConfiguration',
#     'Nav_Altitude',
#     'tyreTemperatures',
#     'driverIsBraking',
#     'ambienceLight_sets',
#     'engineTypes',
#     'chassisUndersteering',
#     'gearTransmissionMode',
#     'blinkingState',
#     'longTermConsumptionSecondary',
#     'stopWatch_totalTime',
#     'vehicleTime',
#     'coastingIsActive',
#     'seatHeater_zone1',
#     'seatHeater_zone2',
#     'Nav_Heading',
#     'seatHeater_zone3',
#     'Car_ambienceLightColour',
#     'seatHeater_zone4',
#     'hevOperationMode',
#     'combustionEngineInjection',
#     'ExAc_GetToken',
#     'currentGear',
#     'espTyreVelocities',
#     'fuelLevelState',
#     'Nav_GuidanceState',
#     'totalDistance',
#     'tyreRequiredPressures',
#     'cycleConsumptionPrimary',
#     'startStopState',
#     'Context_States',
#     'tyreStates',
#     'unitPressure',
#     'espPassiveSensing',
#     'System_DayNight',
#     'tyreTemperatures_HP',
#     'ambienceLight_installation',
#     'brakePressure',
#     'hevacFanLevelRear',
#     'maxChargingAirPressure',
#     'lightState_front',
#     'currentTorque',
#     'clutch',
#     'consumptionShortTermGeneral',
#     'engineSpeed',
#     'seatVentilation_zone3',
#     'stopWatch_lapTime',
#     'seatVentilation_zone4',
#     'Nav_LastDestinations',
#     'absChargingAirPressure',
#     'System_UnitDistance',
#     'parkingBrake',
#     'vehicleSpeed',
#     'espLamp',
#     'longitudinalAcceleration',
#     'doorState',
#     'cycleConsumptionSecondary',
#     'System_ProximityRecognition',
#     'coolantTemperature',
#     'torqueDistribution',
#     'ambienceLight_brightness',
#     'vehicleIdenticationNumber',
#     'stopWatch_previousLapTime',
#     'recuperationLevel',
#     'chassisOversteering',
#     'tankLevelSecondary',
#     'unitTemperature',
#     'lateralAcceleration',
#     'temperatureRearRight',
#     'unitVolume',
#     'acceleratorPosition',
#     'Car_vehicleInformation',
#     'offroadTiltAngleMaxValues',
#     'recommendedGear',
#     'temperatureRearLeft',
#     'ExAc_TouchToken',
#     'consumptionLongTermGeneral',
#     'allWheelDriveTorque',
#     'currentConsumptionSecondary',
#     'powermeter',
#     'tankLevelPrimary',
#     'relAllWheelDriveTorque',
#     'navPosition_HP',
#     'shiftRecommendation',
#     'fuelWarningSecondaryTank',
#     'wheelAngle',
#     'accIsActive',
#     'currentOutputPower',
#     'ExAc_ReleaseToken',
#     'currentConsumptionPrimary',
#     'suspensionProfile',
#     'Nav_StopGuidance',
#     'Nav_ResolveAddress',
#     'suspensionStates',
#     'ambienceLight_control',
#     'dayMilage',
#     'batteryVoltage',
#     'ambienceLight_profiles',
#     'tyrePressures',
#     'fuelWarningPrimaryTank',
#     'serviceOil',
#     'Nav_ResolveLastDestination',
#     'yawRate',
#     'driveMode',
#     'lightState_rear',
#     'maxOutputPower',
#     'System_Language'
#     ]

# for i in CMD:
#     source = inspect.getsource(Sub_foo)
#     source = source.replace("foo", f"{i}",1)
#     source = source.replace("foo", f"'{i}'")
#     print(source)
