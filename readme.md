# 360 Monitoring CLI command plugin

This plugin will collect data that is returned from a command line command. The tool must return a valid json string that is a simple key value list.

## Configuration

```
[cli_command]

enabled = yes
command = /path/to/command
```


### Example for a PHP script

```
[cli_command]

enabled = yes
command = /usr/bin/php /var/tools/redis/stats.php
```

## Output

The command line command has to output a valid JSON string. It is a key value list where the key is a string and the value is the current value as number. 

````json
{"size": 200, "amount": 34}
````
