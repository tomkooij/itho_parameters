#
# This file contains the original "hand translated status labels"
#  they cannot be replaced by new translation, as this will break
#  MQTT keys.
#
# This is a direct copy-paste of /devices/device.h with {} replaced by [] and ()
StatusLabels = {}

# ihtowifi wpu.h 
StatusLabels['WPU'] = [("Outside temp (°C)", "outside-temp_c"),
    ("Boiler temp down (°C)", "boilertemp-down_c"),
    ("Boiler temp up (°C)", "boilertemp-up_c"),
    ("Evaporator temp (°C)", "evaporator-temp_c"),
    ("Suction gas temp (°C)", "suction-gas-temp_c"),
    ("Compressed gas temp (°C)", "compressed-gas-temp_c"),
    ("Liquid temp (°C)", "liquid-temp_c"),
    ("Temp to source (°C)", "temp-to-source_c"),
    ("Temp from source (°C)", "temp-from-source_c"),
    ("CV supply temp (°C)", "cv-supply-temp_c"),
    ("CV return temp (°C)", "cv-return-temp_c"),
    ("CV pressure (Bar)", "cv-pressure_bar"),
    ("Compressor current (A)", "current-compressor_a"),
    ("Current e-element (A)", "current-e-element_a"),
    ("Pressure switch", "pressure-switch"),
    ("Tariff", "tariff"),
    ("Condensation protection", "condensation-protection"),
    ("Pulse counter", "pulse-counter"),
    ("Flow sensor (lt_hr)", "flow-sensor_lthr"),
    ("Phase detection", "phase-detection"),
    ("Cv pump (%)", "cv-pump_perc"),
    ("Well pump (%)", "well-pump_perc"),
    ("Boiler pump (%)", "boiler-pump_perc"),
    ("Free cooling valve (%)", "free-cooling-valve_perc"),
    ("CV_DHW or cooling temp valve (%)", "cv_dhw-or-cooling-temp-valve_perc"),
    ("Compressor", "compressor"),
    ("Element", "element"),
    ("Trickle heating", "trickle-heating"),
    ("Error", "error"),
    ("Free cooling", "free-cooling"),
    ("Expansion valve (pls)", "expansion-valve_pls"),
    ("Room temp (°C)", "room-temp_c"),
    ("Requested room temp (°C)", "requested-roomemp_c"),
    ("Heat demand thermost. (%)", "heat-demand-thermost._perc"),
    ("Status", "status"),
    ("Sub_status", "sub_status"),
    ("Blockage", "blockage"),
    ("Calculated evaporation temp CV (°C)", "calculated-evaporation-temp-cv_c"),
    ("Calculated CV condensation temp (°C)", "calculated-condensation-temp-cv_c"),
    ("Error code byte 5", "error-code-byte-5"),
    ("Error code byte 4", "error-code-byte-4"),
    ("Error code byte 3", "error-code-byte-3"),
    ("Error code byte 2", "error-code-byte-2"),
    ("Error code byte 1", "error-code-byte-1"),
    ("Error code byte 0", "error-code-byte-0"),
    ("Manual operation", "manual-operation"),
    ("Logging (sec)", "logging_sec"),
    ("Compr block (sec)", "compr-block_sec"),
    ("Elek block (sec)", "elek-block_sec"),
    ("Cv for _ naddraai (sec)", "cv-for_-naddraai_sec"),
    ("Source for _ nadraai (sec)", "source-for_-nadraai_sec"),
    ("Boiler for _ nadraai (sec)", "boiler-for_-nadraai_sec"),
    ("Delay electr (sec)", "delay-electr_sec"),
    ("Drain time (sec)", "Drain-time_sec"),
    ("Min running time compr (sec)", "min-running-time-compr_sec"),
    ("EV pressure offset (sec)", "ev-pressure-offset_sec"),
    ("EV adjust (sec)", "ev-adjust_sec"),
    ("Free cooling interval (sec)", "free-cooling-interval_sec"),
    ("Manual control (sec)", "manual_sec"),
    ("Low pressure timer (sec)", "low-pressure-timer_sec"),
    ("Compressor start (sec)", "compressor-start_sec"),
    ("Compr power on delay (sec)", "compr-power-on-delay_sec"),
    ("Cv start delay (sec)", "cv-start-delay_sec"),
    ("Cv stop delay (sec)", "cv-stop-delay_sec"),
    ("Fault highest priority", "fault-highest-priority"),
    ("time for error history (sec)", "time-for-error_sec"),
    ("Max CV return temp (°C)", "max-cv-return-temp_c"),
    ("FlowHardware", "flowhardware"),
    ("Fault highest priority", "fault-highest-priority"),
    ("Delay cv start (sec)", "delay-cv-start_sec"),
    ("Delay cv stop (sec)", "delay-cv-stop_sec"),
    ("Source pump speed free cooling mode", "source-pump-speed-free-cooling-mode"),
    ("Compressor in Cv mode", "compressor-in-cv-mode"),
    ("Compressor in boiler mode", "compressor-in-boiler-mode"),
    ("Element in CV mode", "element-in-CV-mode"),
    ("Element in boiler mode", "element-in-boiler-mode"),
    ("CV mode blocked", "cv-mode-blocked"),
    ("Boiler mode blocked", "boiler-mode-blocked"),
    ("Free cooling mode blocked", "free-cooling-mode-blocked"),
    ("Bleeding mode blocked", "bleeding-mode-blocked"),
    ("Electr element blocked", "electr-element-blocked"),
    ("Compressor blocked", "compressor-blocked"),
    ("Off mode active", "off-mode-active"),
    ("CV mode active", "cv-mode-active"),
    ("Boiler mode active", "boiler-mode-active"),
    ("Free cooling mode active", "free-cooling-mode-active"),
    ("CV pump prime", "cv-pump-prime"),
    ("Well pump prime", "well-pump-prime"),
    ("Element released", "element-released"),
    ("Additional cooling release", "additional-cooling-release"),
    ("CV enabled", "cv-enabled"),
    ("Free cooling enabled", "free-cooling-enabled"),
    ("Tariff low from thermostat", "tariff-low-from-thermostat"),
    ("Venting from thermostat", "venting-from-thermostat"),
    ("ECO selected on thermostat", "eco-selected-on-thermostat"),
    ("Comfort selected on thermostat", "comfort-selected-on-thermostat"),
    ("Boiler blocked from thermostat", "boiler-blocked-from-thermostat"),
    ("Boiler boost from thermostat", "boiler-boost-from-thermostat"),
    ("Error_found", "error_found"),
    ("Error_retry", "error_retry"),
    ("Task active", "task-active"),
    ("UTC time", "utc-time"),
    ("UTC time valid", "utc-time-valid"),
    ("Element blocked during retry", "element-blocked-during-retry"),
    ("Spare input", "spare-input"),
    ("Electr element DHW blocked", "electr-element-dhw-blocked"),
    ("Calculated evaporation temp DHW (°C)", "calculated-evaporation-temp-dhw_c"),
    ("Calculated condensation temp DHW (°C)", "calculated-condensation-temp-dhw_c"),
    ("Adaptive timer (sec)", "adaptive-timer_sec"),
    ("Adaptive overheat (K)", "adaptive-overheat_k"),
    ("adaptive fifo index", "adaptive-fifo-index"),
    ("Heat demand total (%)", "heat-demand-total_perc"),
    ("P source flow error", "p-source-flow-error"),
    ("I error sourceflow", "i-error-sourceflow"),
    ("Pi error sourceflow", "pi-error-sourceflow"),
    ("Current source valve position (%)", "current-source-valve-position_perc"),
    ("Utc Time offset (min)", "utc-time-offset_min"),
    ("Gateway Time Receive", "gateway-time-receive"),
    ("OT time valid", "ot-time-valid"),
    ("Time hours (hrs)", "time-hours_hours"),
    ("Time minutes (min)", "time-minutes_min"),
    ("time seconds (sec)", "time-seconds_sec"),
    ("Free cooling block time (min)", "free-cooling-block-time_min"),
    ("Cooling temp control valve setpoint (%)", "cooling-temp-control-valve-setpoint_perc"),
    ("CO valve position (%)", "co-valve-position_perc"),
    ("HRU blowout temp (°C)", "hru-blowout-temp_c"),
    ("HRU blowout flow (m3_h)", "hru-blowout-flow_m3h"),
    ("Regeneration active", "regeneration-active"),
    ("Latest valid source supply temp. (°C)", "latest-valid-source-supply-temp._c"),
    ("Source pump flow setpoint (l_h)", "source-pump-flow-setpoint_lh"),
    ("Well pump speed at airreg (%)", "well-pump-speed-at-airreg_perc"),
    ("Source pump speed at free cooling (%)", "source-pump-speed-at-free-cooling_perc"),
    ("Free cooling mode", "free-cooling-mode"),
    ("Free cooling on time (sec)", "free-cooling-on-time_sec"),
    ("Time CO valve start position (sec)", "time-co-valve-start-position_sec"),
    ("Reserve", "reserve"),
    ("E-consumption during stand-by (kWh)", "e-consumption-during-stand-by_kwh"),
    ("E-consumption during heating (kWh)", "e-consumption-during-heating_kwh"),
    ("E-consumption during DHW (kWh)", "e-consumption-during-dhw_kwh"),
    ("E-consumption during cooling (kWh)", "e-consumption-during-cooling_kwh"),
    ("Minimum release time external cooling (sec)", "minimum-release-time-external-cooling_sec"),
    ("Block time-release external cooling (sec)", "block-time-release-external-cooling_sec"),
    ("External heating release time (sec)", "external-heating-release-time_sec"),
    ("Preheat tap water", "preheat-tap-water"),
    ("Blocking time trickle low after power-up (sec.)", "blocking-time-trickle-low-after-power-up_sec"),
    ("Blocking time trickle low after CV operation (sec)", "blocking-time-trickle-low-after-cv-operation_sec"),
    ("Block time pre-heating tap water (sec)", "block-time-pre-heating-tap-water_sec"),
    ("Well pump speed at compr (%)", "well-pump-speed-at-compr_perc"),
    ("Slow start well pump (sec)", "slow-start-well-pump_sec"),
    ("Source return temperature too low (sec.)", "source-return-temperature-too-low_sec"),
    ("Source flow control period (sec)", "source-flow-control-period_sec"),
    ("Stabilisation waiting time-free cooling (sec.)", "stabilisation-waiting-time-free-cooling_sec"),
    ("Minimum time for preheating potable water (sec)", "minimum-time-for-preheating-potable-water_sec"),
    ("Maximum time for preheating potable water (sec)", "maximum-time-for-preheating-potable-water_sec"),
    ("Electrical element release (min)", "electrical-element-release_min"),
    ("Correction measurement delta source temperature (K)", "correction-measurement-delta-source-temperature_k")]


StatusLabels['Autotemp'] = [("Mode", "mode"),
    ("Condition", "condition"),
    ("Particulars", "Particulars"),
    ("Error", "error"),
    ("Room 1 temp", "room-1-temp"),
    ("Room 1 setp", "room-1-setp"),
    ("Room 1 power % (%)", "room-1-power-%_perc"),
    ("Room 1 power kW (kW)", "room-1-power-kw_kw"),
    ("Room 2 temp", "room-2-temp"),
    ("Room 2 setp", "room-2-setp"),
    ("Room 2 power % (%)", "room-2-power-%_perc"),
    ("Room 2 power kW (kW)", "room-2-power-kw_kw"),
    ("Room 3 temp", "room-3-temp"),
    ("Room 3 setp", "room-3-setp"),
    ("Room 3 power % (%)", "room-3-power-%_perc"),
    ("Room 3 power kW (kW)", "room-3-power-kw_kw"),
    ("Room 4 temp", "room-4-temp"),
    ("Room 4 setp", "room-4-setp"),
    ("Room 4 power % (%)", "room-4-power-%_perc"),
    ("Room 4 power kW (kW)", "room-4-power-kw_kw"),
    ("Room 5 temp", "room-5-temp"),
    ("Room 5 setp", "room-5-setp"),
    ("Room 5 power % (%)", "room-5-power-%_perc"),
    ("Room 5 power kW (kW)", "room-5-power-kw_kw"),
    ("Room 6 temp", "room-6-temp"),
    ("Room 6 setp", "room-6-setp"),
    ("Room 6 power % (%)", "room-6-power-%_perc"),
    ("Room 6 power kW (kW)", "room-6-power-kw_kw"),
    ("Room 7 temp", "room-7-temp"),
    ("Room 7 setp", "room-7-setp"),
    ("Room 7 power % (%)", "room-7-power-%_perc"),
    ("Room 7 power kW (kW)", "room-7-power-kw_kw"),
    ("Room 8 temp", "room-8-temp"),
    ("Room 8 setp", "room-8-setp"),
    ("Room 8 power % (%)", "room-8-power-%_perc"),
    ("Room 8 power kW (kW)", "room-8-power-kw_kw"),
    ("Room 9 temp", "room-9-temp"),
    ("Room 9 setp", "room-9-setp"),
    ("Room 9 power % (%)", "room-9-power-%_perc"),
    ("Room 9 power kW (kW)", "room-9-power-kw_kw"),
    ("Room 10 temp", "room-10-temp"),
    ("Room 10 setp", "room-10-setp"),
    ("Room 10 power % (%)", "room-10-power-%_perc"),
    ("Room 10 power kW (kW)", "room-10-power-kw_kw"),
    ("Room 11 temp", "room-11-temp"),
    ("Room 11 setp", "room-11-setp"),
    ("Room 11 power % (%)", "room-11-power-%_perc"),
    ("Room 11 power kW (kW)", "room-11-power-kw_kw"),
    ("Room 12 temp", "room-12-temp"),
    ("Room 12 setp", "room-12-setp"),
    ("Room 12 power % (%)", "room-12-power-%_perc"),
    ("Room 12 power kW (kW)", "room-12-power-kw_kw"),
    ("Distributor 1 valve 1", "distributor-1-valve-1"),
    ("Distributor 1 valve 2", "distributor-1-valve-2"),
    ("Distributor 1 valve 3", "distributor-1-valve-3"),
    ("Distributor 1 valve 4", "distributor-1-valve-4"),
    ("Distributor 1 valve 5", "distributor-1-valve-5"),
    ("Distributor 1 valve 6", "distributor-1-valve-6"),
    ("Distributor 1 valve 7", "distributor-1-valve-7"),
    ("Distributor 1 valve 8", "distributor-1-valve-8"),
    ("Distributor 1 valve 9", "distributor-1-valve-9"),
    ("Distributor 1 valve 10", "distributor-1-valve-10"),
    ("Distributor 1 valve 11", "distributor-1-valve-11"),
    ("Distributor 1 valve 12", "distributor-1-valve-12"),
    ("Distributor 2 valve 1", "distributor-2-valve-1"),
    ("Distributor 2 valve 2", "distributor-2-valve-2"),
    ("Distributor 2 valve 3", "distributor-2-valve-3"),
    ("Distributor 2 valve 4", "distributor-2-valve-4"),
    ("Distributor 2 valve 5", "distributor-2-valve-5"),
    ("Distributor 2 valve 6", "distributor-2-valve-6"),
    ("Distributor 2 valve 7", "distributor-2-valve-7"),
    ("Distributor 2 valve 8", "distributor-2-valve-8"),
    ("Distributor 2 valve 9", "distributor-2-valve-9"),
    ("Distributor 2 valve 10", "distributor-2-valve-10"),
    ("Distributor 2 valve 11", "distributor-2-valve-11"),
    ("Distributor 2 valve 12", "distributor-2-valve-12"),
    ("Distributor 3 valve 1", "distributor-3-valve-1"),
    ("Distributor 3 valve 2", "distributor-3-valve-2"),
    ("Distributor 3 valve 3", "distributor-3-valve-3"),
    ("Distributor 3 valve 4", "distributor-3-valve-4"),
    ("Distributor 3 valve 5", "distributor-3-valve-5"),
    ("Distributor 3 valve 6", "distributor-3-valve-6"),
    ("Distributor 3 valve 7", "distributor-3-valve-7"),
    ("Distributor 3 valve 8", "distributor-3-valve-8"),
    ("Distributor 3 valve 9", "distributor-3-valve-9"),
    ("Distributor 3 valve 10", "distributor-3-valve-10"),
    ("Distributor 3 valve 11", "distributor-3-valve-11"),
    ("Distributor 3 valve 12", "distributor-3-valve-12"),
    ("Valve failure distributor 1", "valve-failure-distributor-1"),
    ("Valve failure distributor 2", "valve-failure-distributor-2"),
    ("Valve failure distributor 3", "valve-failure-distributor-3"),
    ("Valve failure detection distributor 1", "failure-valve-detection-distributor-1"),
    ("Malfunction valve detection dist 2", "malfunction-valve-detection-distributor-2"),
    ("Malfunction valve detection dist 3", "malfunction-valve-detection-dist-3"),
    ("Heat source", "heat-source"),
    ("Desired power (%)", "desired power _perc"),
    ("Condition off", "condition-off"),
    ("Condition cool", "condition-cool"),
    ("State heating", "state-heating"),
    ("State hand", "state-hand"),
    ("Malfunction valve detection dist 1", "malfunction valve-detection-dist-1"),
    ("Malfunction valve detection dist 2", "malfunction-valve-detection-dist-2"),
    ("Malfunction valve detection dist 3", "malfunction valve-detection-dist-3"),
    ("LED_On", "led_on"),
    ("LED_Slow", "led_slow"),
    ("LED_Fast", "led_fast"),
    ("Empty battery ( 0=OK )", "empty-battery-(-0=ok-)"),
    ("V1_valve", "v1_valve"),
    ("V2_valve", "v2_valve"),
    ("V3_valve", "v3_valve"),
    ("Outdoor temp (°C)", "outdoor-temp _c"),
    ("Rest cycle time (sec)", "rest-cycle-time_sec"),
    ("Rest vent time (sec)", "rest-vent-time_sec"),
    ("Comm space A (sec)", "comm-space-a_sec"),
    ("Comm space B (sec)", "comm-space-b_sec"),
    ("Comm space C (sec)", "comm-space-c_sec"),
    ("Comm space D (sec)", "comm-space-d_sec"),
    ("Comm space E (sec)", "comm-space-e_sec"),
    ("Comm space F (sec)", "comm-space-f_sec"),
    ("Comm space G (sec)", "comm-space-g_sec"),
    ("Comm space H (sec)", "comm-space-h_sec"),
    ("Comm space I (sec)", "comm-space-i_sec"),
    ("Comm space J (sec)", "comm-space-j_sec"),
    ("Comm space K (sec)", "comm-space-k_sec"),
    ("Comm space L (sec)", "comm-space-l_sec"),
    ("State off", "state-off"),
    ("State cool", "state-cool"),
    ("State heating", "state-heating"),
    ("state hand", "state-hand"),
    ("LED_On", "led_on"),
    ("LED_Slow", "led_slow"),
    ("LED_Fast", "led_fast"),
    ("Empty battery ( 0=OK )", "empty-battery-(-0=ok-)"),
    ("V1_valve", "v1_valve"),
    ("V2_valve", "v2_valve"),
    ("V3_valve", "v3_valve"),
    ("Cycle counter (sec)", "cycle-counter_sec"),
    ("Rest vent time (sec)", "rest-vent-time_sec"),
    ("Time active zone too cold (sec)", "time-active-zone-too-cold_sec")]