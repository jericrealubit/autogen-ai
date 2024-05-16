import autogen

config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST.json")
llm_config = {"config_list": config_list}

print(config_list[1])