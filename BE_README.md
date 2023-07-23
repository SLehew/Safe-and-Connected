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


#### Create Token Login

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
| `event_type   `| `int`    |                                   |


### List All Events

```https://safe-connected.onrender.com/
  GET /event/all/
```
### List All Organizers Events

```https://safe-connected.onrender.com/
  GET event/organizer/list/
```

### Search Title of Event or Notes
add (/?event_title= or /?general_notes=) to url

```https://safe-connected.onrender.com/
  GET /event/search/
```

### Client Signup for Event

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
  POST /language/add/
```

| Parameter        | Type     | Description                       |
| :--------        | :------- | :-------------------------------- |
|`lang`            |`str`     |                                   |

### create membership

```https://safe-connected.onrender.com/
  POST /org/client/mem/create/
```

| Parameter        | Type     | Description                       |
| :--------        | :------- | :-------------------------------- |
|`member`          |`str`     |                                   |
|`organization`    |`str`     |                                   |

### Add file 

```https://safe-connected.onrender.com/
  POST /uploads/
```

| Parameter        | Type     | Description                       |
| :--------        | :------- | :-------------------------------- |
|`file`            |`file`    |                                   |

### view organiz you are a member of

```https://safe-connected.onrender.com/
  GET /org/mem/
```

### view list of all members of an organization

```https://safe-connected.onrender.com/
  GET /org/<int:organization_id>/clients/
```