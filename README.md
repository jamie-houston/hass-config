# Home Assistant Configuration

## Naming
https://developers.home-assistant.io/blog/2022/07/10/entity_naming/
https://github.com/CCOSTAN/Home-AssistantConfig/tree/master/config

### Devices

Area [Location][Brand Model][Type]
(single for one device, plural for group)
Upper Case

examples

- Kitchen Google Home
- Art Room Google Mini
- Kitchen Light
- Kitchen Cabinet Light
- Kitchen Lights (group of kitchen lights)

### Entities
domain.area[_device][_purpose][_location in room]

plural for groups

examples

- light.home_theater_wall
- light.home_theater_led_front_wall
- sensor.home_theater_motion
- light.stairs_down
- sensor.server_room_temperature
- media_player.art_room_speaker
- lock.backdoor

### Possible Domains

- automation
- binary_sensor
- button
- cover
- light
- lock
- media_player
- sensor
- switch

### Possible Purposes

- motion
- battery
- power_usage
- speaker (not needed with media_player)?
- temperature

### Find Entities by Convention

To programmatically find entities in an area (room), use the same across areas

`domain`.`area`[_group]

- Temperature
- Window Open
- Lights
- Fan
- Motion
- Media
- Remote
- Lock

Example (Master Bedroom)
- sensor.master_bedroom_temperature
- sensor.master_bedroom_window
- light.master_bedroom
- fan.master_bedroom

Example (Kitchen)
- sensor.kitchen_temperature
- sensor.kitchen_window
- light.kitchen_lights
- media_player.kitchen


## Alerts and Notifications
https://community.home-assistant.io/t/simple-and-effective-alerting/394027

Notifications/alerts to show on dashboard and/or send to devices

Steps
1. Define entity/group for notification
1. Define input_boolean for each notification (show/dismiss) - input_boolean/notifications/
2. Define template with binary_sensor including entity to check and input_boolean to show
  - binary sensor for each entity/group to check
  - trigger (optional) for when to check binary_sensor
- notifications.yaml for notification levels "Notify_<Information, Warning, Critical>_Devices"
3. View

## To contemplate
Groups
light.basement_lights
light.play_room_light
media_player.play_room
media_player.home_theater_chromecast (tv?)
media_player.art_room(_speaker)