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
- power_usage
- speaker (not needed with media_player)?
- temperature


### To contemplate
Groups
light.basement_lights
light.play_room_light
media_player.play_room
media_player.home_theater_chromecast (tv?)
media_player.art_room(_speaker)