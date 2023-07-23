#### Create Event

```https://safe-connected.onrender.com/
  POST /event/create/
```

| Parameter      | Type     | Description                       |
| :--------      | :------- | :-------------------------------- |
|`event_title`   |`str`     |                                   |
| `general_notes`| `str`    |                                   |
| `event_type   `| `int`    |                                   |

### List All Events

```https://safe-connected.onrender.com/
  GET /event/all/
```
### Create Event Roster

```https://safe-connected.onrender.com/
  POST /event/roster/create/
```

| Parameter        | Type     | Description                       |
| :--------        | :------- | :-------------------------------- |
|`event_id`           |`str`  |                                   |
