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
| `language`| `int`    |                                   |


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

| Parameter           | Type     | Description                       |
| :--------           | :------- | :-------------------------------- |
|`event_title`        |`str`     |                                   |
| `general_notes`     | `str`    |                                   |
| `event_type`        | `int`    |                                   |
| `event_organization`| `int`    |                                   |


### List All Events

```https://safe-connected.onrender.com/
  GET /event/all/
```
### List All Clients Available Events
Lanuage Codes
Spanish = `es`
French = `fr`
Swahili = `sw`

```https://safe-connected.onrender.com/
  GET <language_code>/event/all/
```
#### Event Details
Lanuage Codes
Spanish = `es`
French = `fr`
Swahili = `sw`

```https://safe-connected.onrender.com/
  GET <language_code>/event/<int:pk>/details/
```


### List All of an Organizations Events

```https://safe-connected.onrender.com/
  GET org/<int:event_organization_id>/events/
```

### List All Events Created by the Manager

```https://safe-connected.onrender.com/
  GET event/organizer/list/
```

### Search Title of Event or Notes
`add (/?event_title=<searchtext> or /?general_notes=<searchtext>) to url`

```https://safe-connected.onrender.com/
  GET /event/search/
```

### Client Signup for Event
`(pk is event_id)`

```https://safe-connected.onrender.com/
  PATCH /event/roster/<int:pk>/signup/
```

### List of Clients Attending Event
`(pk is event_id)`
```https://safe-connected.onrender.com/
  GET /event/roster/<int:pk>/
```

### Create Organization profile

```https://safe-connected.onrender.com/
  POST /organization/create/
```

| Parameter           | Type     | Description                       |
| :--------           | :------- | :-------------------------------- |
|`org_name`           |`str`     |                                   |
| `street_number`     | `int`    |                                   |
| `street_name`       | `str`    |                                   |
| `city`              | `str`    |                                   |
| `state`             | `str`    |                                   |
| `zipcode`           | `int`    |                                   |
| `phone`             | `int`    |                                   |
| `org_notes`         | `str`    |                                   |

### Create Organization profile

```https://safe-connected.onrender.com/
  PATCH "organization/edit/<int:pk>/"
```

| Parameter           | Type     | Description                       |
| :--------           | :------- | :-------------------------------- |
|`org_name`           |`str`     |                                   |
| `street_number`     | `int`    |                                   |
| `street_name`       | `str`    |                                   |
| `city`              | `str`    |                                   |
| `state`             | `str`    |                                   |
| `zipcode`           | `int`    |                                   |
| `phone`             | `int`    |                                   |
| `org_notes`         | `str`    |                                   |
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

### View organizations Client is a member of

```https://safe-connected.onrender.com/
  GET /org/mem/
```

### List all members of an organization

```https://safe-connected.onrender.com/
  GET /org/<int:organization_id>/clients/
```