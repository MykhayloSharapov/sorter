import configparser,os
config = configparser.ConfigParser()
config.read ('configfile')

if config.get("Settings", "input_mode") == 'manual':
    import manual_input_module as inp_module
elif config.get("Settings", "input_mode") == 'file_input':
    import file_input_module as inp_module
else:
    print ('check settings')

contact_list=inp_module.contact_list

if config.get("Settings", "sort_algorythm_type") == 'DSU':
    import DSU_sort_module as sort_module
elif config.get("Settings", "sort_algorythm_type") == 'panda':
    import panda_sort_module as sort_module
else:
    print ('check settings')




