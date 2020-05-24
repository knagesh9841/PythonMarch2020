from jproperties import Properties

configs = Properties()

with open('app-config.properties', 'rb') as config_file:
    configs.load(config_file)

print(configs.get("DB_User").data)
print(configs.get("DB_HOST").data)

