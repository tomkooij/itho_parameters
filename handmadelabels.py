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