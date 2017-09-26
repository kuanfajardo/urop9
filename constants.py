
class Color:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Event:
    PROGRAM_VERSION          = 1
    MAX_TRIAL_NUMBER         = 2
    MAX_REWARD_NUMBER        = 3
    MAX_SESSION_DURATION     = 4
    EXPERIMENT_START         = 5
    EXPERIMENT_STOP          = 6
    TRIAL_START              = 7
    TRIAL_STOP               = 8
    ITI_ON                   = 9
    ITI_OFF                  = 10
    ITI_MIN                  = 11
    ITI_MAX                  = 12
    LICK                     = 13
    SOLENOID_ON              = 14
    SOLENOID_DURATION        = 15
    SOLENOID_OFF             = 16
    LED_ON                   = 17
    LED_PWM                  = 18
    LED_DURATION             = 19
    LED_OFF                  = 20
    TONE1_ON                 = 21
    TONE1_FREQ               = 22
    TONE1_DURATION           = 23
    TONE1_OFF                = 24
    TONE5_ON                 = 21
    TONE5_FREQ               = 22
    TONE5_DURATION           = 23
    TONE5_OFF                = 24
    TONE2_ON                 = 25
    TONE2_FREQ               = 26
    TONE2_DURATION           = 27
    TONE2_OFF                = 28
    STATE                    = 29
    EVENT                    = 30
    CORRECT_REPONSE          = 31
    INCORRECT_RESPONSE       = 32
    OMISSION                 = 33
    ITI_DURATION             = 34
    EOD                      = 35
    STIM_TYPE                = 36
    STIM_ON                  = 37
    STIM_DURATION            = 38
    STIM_OFF                 = 39
    BLOCK_SIZE               = 40
    THRESHOLD                = 41
    LIGHT_INTENSITY_START    = 42
    LIGHT_INTENSITY_STEP     = 43
    NOLIGHT_NTRIALS          = 44
    
    MEGA_STATE               = 45
    SLOW_SEARCH_STEP         = 46
    FAST_SEARCH_STEP         = 47
    BASELINE_THRESHOLD       = 48
    SLOW_SEARCH_THRESHOLD    = 49
    FAST_SEARCH_THRESHOLD    = 50
    BASELINE_SIZE            = 51
    SLOW_SEARCH_SIZE         = 52
    FAST_SEARCH_SIZE         = 53
    SLOW_SEARCH_STARTING_POINT = 54
    NSUCC_TEST = 55
    
    LED_VOLTAGE_MV = 56
    OFFER_ACCEPTED = 57
    OFFER_REJECTED = 58
    AFTERTONEDELAYMSEC = 59
    RESPONSEDURATIONMSEC = 60
    
    DELAYBEFORETONEMSEC = 61
    DELAYAFTEROFFERMSEC = 62
    
    SERVOPOSITION = 63
    
    AFTERDECISIONDELAYMSEC = 64
    CONSUMPTIONPERIODMSEC  = 65
    CONSUMPTIONLICKNUMBER  = 66
    TRIALTYPE              = 67
    MAXWAITFORFIRSTLICKMSEC = 68
    
    QUENCHINGPERIODMSEC  = 69
    QUENCHINGLICKNUMBER  = 70
    REST_ON  = 71
    QUENCHING_ON  = 72
    
    OPTO_ON                  =  83
    OPTO_OFF                 = 84
    OPTO_POWER               =  85
    OPTO_WAVELENGTH          =  86
    
    REWARD_DURATION_1  = 87
    REWARD_DURATION_2  = 88
    
    NLICK_TOT  = 89
    NLICK_CURRENT  = 90
    
    NLICK_DURING_DECISION    = 91
    NDROPS                   = 92
    
    TONE3_ON                 = 93
    TONE3_FREQ               = 94
    TONE3_DURATION           = 95
    TONE3_OFF                = 96
    TONE6_ON                 = 93
    TONE6_FREQ               = 94
    TONE6_DURATION           = 95
    TONE6_OFF                = 96
    
    OFFER1_REW                = 97
    OFFER1_LIGHT              = 98
    OFFER2_REW                = 99
    OFFER2_LIGHT              = 100
    OFFER3_REW                = 101
    OFFER3_LIGHT              = 102

    TONE7_ON                 = 103
    TONE7_FREQ               = 104
    TONE7_DURATION           = 105
    TONE7_OFF                = 106
    TONE8_ON                 = 107
    TONE8_FREQ               = 108
    TONE8_DURATION           = 109
    TONE8_OFF                = 110

    OFFER1_REW                = 111
    OFFER1_LIGHT              = 112
    OFFER2_REW                = 113
    OFFER2_LIGHT              = 114


# BLOCK_NUMBER = 73
    # CURRENT_BLOCK_NUMBER = 74
    # 
    # CUE_LIGHT_INTENSITY_1   = 75
    # CUE_LIGHT_INTENSITY_2   = 76
    # OFFER_LIGHT_INTENSITY_1 = 77
    # OFFER_LIGHT_INTENSITY_2 = 78
    # CUE_LIGHT_DURATION_1    = 79
    # CUE_LIGHT_DURATION_2    = 80
    # OFFER_LIGHT_DURATION_1  = 81
    # OFFER_LIGHT_DURATION_2  = 82
