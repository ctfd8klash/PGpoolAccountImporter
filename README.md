# PGpoolAccountImporter
Pokemon Map automation importing tool.

If you are a mapper and using pgpool, this is what you can use to import accounts from my database. I don't use maps, but if you guys want to participate in testing, I would like to make it better. Or if you can understand what I write, you can checkout the #api-documentation for more api functions to make this script better. Hope this can help you mappers and save you guys some time

User manual:
1. You need to save account into my database first before using it. Except level 0 new accounts. You can use your shuffle api balace to purchase it everytime you import. 

2. Overwrite these two files in the map directory. 

3. Run the command `python pgpool-import-shuffle -l 30 -cnd good -api {your api} -delay {delay in hours} -n {amount of accounts you want to import everytime} -hour {see nots}`
Notes: 
Put your shuffle api key into {your api}; 
`{delay in hours}` is used to control the import accounts period, the unit is in hour. For example, if you want the script to run every 12 hours, you just put 12 in `{delay in hours}`;
Put how many accounts you want to import into `{amount of accounts you want to import everytime}`. Like 10;
`{hour}` This is actually something useful for non level 0 account users. You can control the age of each account you get from my database. If you only want level 30 accounts that imported to my database within last 12 hours, you put 12 in the field.

4. Once you get your accounts, leave the script running and it will automatically import again with the same amount. 

If the script encountered an error while loading from my database, you will see an Error message shows `Could not load any accounts. Retry in 5 mins...`. This means the script will try again in next 5 mins.
