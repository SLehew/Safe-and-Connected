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

```https://questionapi.onrender.com
  POST /auth/users/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
|`username` |`str`     |                                   |
| `password`| `str`    |                                   |

#### Logout

```https://safe-connected.onrender.com/
  POST /auth/token/logout/
```