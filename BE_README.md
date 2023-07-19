#Safe-And_ConnectedAPI

Safe and ConnectedAPI is a Django REST Framework that provides endpoints that enables users to register, login, post questions, answers, and files regarding topics of their choosing.


## API Reference

#### URL

https://safe-connected.onrender.com/

#### Create User

```https://safe-connected.onrender.com/
  POST /auth/users/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email`   |`str`     |                                   |
|`username` |`str`     |                                   |
| `password`| `str`    |                                   |
| `role`    | `str`    |Client/Manager                     |


#### Create Token

```https://safe-connected.onrender.com/
  POST /auth/token/login
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
|`username` |`str`     |                                   |
| `password`| `str`    |                                   |

#### Logout

```https://safe-connected.onrender.com/
  POST /auth/token/logout/
```
#### Create Event

```https://safe-connected.onrender.com/
  POST /event/create/
```

| Parameter      | Type     | Description                       |
| :--------      | :------- | :-------------------------------- |
|`event_title`   |`str`     |                                   |
| `general_notes`| `str`    |                                   |

### List Event

```https://safe-connected.onrender.com/
  GET /event/list/
```
### Search Event

```https://safe-connected.onrender.com/
  GET /event/search/
```

### Create Event Roster

```https://safe-connected.onrender.com/
  POST /event/roster/create/
```

| Parameter        | Type     | Description                       |
| :--------        | :------- | :-------------------------------- |
|`event_id`           |`str`  |                                   |
| `client_attendee`   | `str` |                                   |
|`event_manager`      |`str`  |                                   |
| `event_organization`|`str`  |                                   |


### Get event roster details
```https://safe-connected.onrender.com/
  GET /event/roster/<int:pk>/
```

### Update event roster details
```https://safe-connected.onrender.com/
  PATCH /event/roster/<int:pk>/
```

### Delete event roster
```https://safe-connected.onrender.com/
  DELETE /event/roster/<int:pk>/
```

### Create Organization profile

```https://safe-connected.onrender.com/
  POST /organization/create/
```

| Parameter        | Type     | Description                       |
| :--------        | :------- | :-------------------------------- |
|`org_name`           |`str`  |                                   |

### Get Organization list

```https://safe-connected.onrender.com/
  GET /organization/
```

### Get Organization DETAILS

```https://safe-connected.onrender.com/
  GET /organization/<int:pk>/
```

### Update Organization DETAILS

```https://safe-connected.onrender.com/
  PATCH /organization/<int:pk>/
```

### Delete Organization 

```https://safe-connected.onrender.com/
  DELETE /organization/<int:pk>/
```

### Add language 

```https://safe-connected.onrender.com/
  POST language/add/
```

| Parameter        | Type     | Description                       |
| :--------        | :------- | :-------------------------------- |
|`lang`            |`str`     |                                   |