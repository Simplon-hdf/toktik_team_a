# tiktok_team_a

Basic Tiktok clone
- Visitors can only view Post
- User can login or signup
- User can create Posts and Comments
- Post has Comments





<br><br><br>

# Documentation

- `docs/conception` : data models
- [http://localhost:8000/docs](http://localhost:8000/docs) : auto-generated documentation (*Swagger UI*)
- [http://localhost:8000/redoc](http://localhost:8000/redoc) : auto-generated documentation (*Redoc*)





<br><br><br>

# API
### Dependencies

- Python
- [PostgreSQL](https://www.postgresql.org/download/) : Database
- [uvicorn](https://www.uvicorn.org/) : WebServer
- [fastapi](https://fastapi.tiangolo.com/) : API Framework
- [SQLAlchemy](https://www.sqlalchemy.org/) : ORM
- [psycopg2](https://pypi.org/project/psycopg2/) : PostgreSQL adapter
- [PyJWT](https://pyjwt.readthedocs.io/en/stable/) / [passlib](https://passlib.readthedocs.io/en/stable/) : Password hashing & token generation



### Install

```bash
conda create --name toktik
conda activate toktik
conda install python=3.10 pip
pip install uvicorn fastapi==0.100.0 SQLAlchemy pyjwt passlib psycopg2 hashlib
```



### Run [http://localhost:8000/](http://localhost:8000/)

```bash
conda activate toktik
uvicorn api.src.main:app --reload
```



<br>

### Endpoints

<br>

- **User**

<details>
 <summary>
  <code>GET</code>
  <code><b>/user/:id</b></code>
  <code>(get 1 User)</code>
 </summary>

##### Parameters

> | name      |  type     | data type               | description                                                      |
> |-----------|-----------|-------------------------|------------------------------------------------------------------|
> | id        |  required | int                     | user_id                                                          |

##### Responses

> | http code     | content-type                      | response                                                       |
> |---------------|-----------------------------------|----------------------------------------------------------------|
> | `200`         | `application/json`                | User                                                           |
> | `404`         | `application/json`                | User does not exist                                            |

</details>

<details>
 <summary>
  <code>POST</code>
  <code><b>/user/register</b></code>
  <code>(get an auth token)</code>
 </summary>

 ##### Parameters

> | name        |  type     | data type               | description                                                    |
> |-------------|-----------|-------------------------|----------------------------------------------------------------|
> | username    | required  | str                     | Username                                                       |
> | email       | required  | str                     | Valid email adress                                             |
> | password    | required  | str                     | Password                                                       |

##### Responses

> | http code     | content-type                      | response                                                       |
> |---------------|-----------------------------------|----------------------------------------------------------------|
> | `200`         | `application/json`                | ""\[token\]                                                    |

</details>

<details>
 <summary>
  <code>DELETE</code>
  <code><b>/user/delete/:id</b></code>
  <code>(Delete a User)</code>
 </summary>

##### Responses

> | http code     | content-type                      | response                                                       |
> |---------------|-----------------------------------|----------------------------------------------------------------|
> | `200`         | `application/json`                | `User`                                                         |
> | `404`         | `application/json`                | User does not exist                                            |

</details>

<details>
 <summary>
  <code>GET</code>
  <code><b>/user/token</b></code>
  <code>(get 1 User, by their token)</code>
 </summary>

##### Parameters

> | name      |  type     | data type               | description                                                      |
> |-----------|-----------|-------------------------|------------------------------------------------------------------|
> | token     |  required | str                     | User token                                                       |

##### Responses

> | http code     | content-type                      | response                                                       |
> |---------------|-----------------------------------|----------------------------------------------------------------|
> | `200`         | `application/json`                | User                                                           |
> | `404`         | `application/json`                | User does not exist                                            |

</details>

<details>
 <summary>
  <code>GET</code>
  <code><b>/user/list</b></code>
  <code>(get all Users)</code>
 </summary>

##### Responses

> | http code     | content-type                      | response                                                       |
> |---------------|-----------------------------------|----------------------------------------------------------------|
> | `200`         | `application/json`                | `User`                                                         |

</details>

<details>
 <summary>
  <code>POST</code>
  <code><b>/user/login</b></code>
  <code>(login)</code>
 </summary>

##### Parameters

> | name        |  type     | data type               | description                                                    |
> |-------------|-----------|-------------------------|----------------------------------------------------------------|
> | email       | required  | str                     | Email                                                          |
> | password    | required  | str                     | Password                                                       |

##### Responses

> | http code     | content-type                      | response                                                       |
> |---------------|-----------------------------------|----------------------------------------------------------------|
> | `200`         | `application/json`                | `User`                                                         |

</details>

<details>
 <summary>
  <code>PATCH</code>
  <code><b>/user/:id</b></code>
  <code>(Partially update an existing User)</code>
 </summary>

##### Parameters

> | name        |  type     | data type               | description                                                    |
> |-------------|-----------|-------------------------|----------------------------------------------------------------|
> | username    | optional  | str                     | Username                                                       |
> | email       | optional  | str                     | Email                                                          |
> | password    | optional  | str                     | Password                                                       |
> | token       | optional  | str                     | Token                                                          |

##### Responses

> | http code     | content-type                      | response                                                       |
> |---------------|-----------------------------------|----------------------------------------------------------------|
> | `200`         | `application/json`                | `User`                                                         |
> | `404`         | `application/json`                | User does not exist                                            |

</details>




<br>

- **Post**

<details>
 <summary>
  <code>GET</code>
  <code><b>/post/:id</b></code>
  <code>(get 1 Post)</code>
 </summary>

##### Parameters

> | name      |  type     | data type               | description                                                      |
> |-----------|-----------|-------------------------|------------------------------------------------------------------|
> | id        |  required | int                     | post_id                                                          |

##### Responses

> | http code     | content-type                      | response                                                       |
> |---------------|-----------------------------------|----------------------------------------------------------------|
> | `200`         | `application/json`                | Post                                                           |
> | `404`         | `application/json`                | Post does not exist                                            |

</details>

<details>
 <summary>
  <code>GET</code>
  <code><b>/post/random</b></code>
  <code>(get a random Post)</code>
 </summary>

##### Responses

> | http code     | content-type                      | response                                                       |
> |---------------|-----------------------------------|----------------------------------------------------------------|
> | `200`         | `application/json`                | Post                                                           |

</details>

<details>
 <summary>
  <code>GET</code>
  <code><b>/post/list</b></code>
  <code>(get all Posts)</code>
 </summary>

##### Responses

> | http code     | content-type                      | response                                                       |
> |---------------|-----------------------------------|----------------------------------------------------------------|
> | `200`         | `application/json`                | `Post`                                                         |

</details>

<details>
 <summary>
  <code>POST</code>
  <code><b>/post/create</b></code>
  <code>(create a new Post)</code>
 </summary>

##### Parameters

> | name        |  type     | data type               | description                                                    |
> |-------------|-----------|-------------------------|----------------------------------------------------------------|
> | title       | required  | str                     | Title of Post                                                  |
> | description | optional  | str                     | Description of Post                                            |
> | video_url   | required  | str                     | URL of embedded video                                          |
> | user_id     | required  | int                     | ID of author                                                   |

##### Responses

> | http code     | content-type                      | response                                                       |
> |---------------|-----------------------------------|----------------------------------------------------------------|
> | `200`         | `application/json`                | `Post`                                                         |

</details>

<details>
 <summary>
  <code>DELETE</code>
  <code><b>/post/delete/:id</b></code>
  <code>(Delete a Post)</code>
 </summary>

##### Responses

> | http code     | content-type                      | response                                                       |
> |---------------|-----------------------------------|----------------------------------------------------------------|
> | `200`         | `application/json`                | `Post`                                                         |
> | `404`         | `application/json`                | Post does not exist                                            |

</details>

<details>
 <summary>
  <code>PATCH</code>
  <code><b>/post/update/:id</b></code>
  <code>(Partially update an existing Post)</code>
 </summary>

##### Parameters

> | name        |  type     | data type               | description                                                    |
> |-------------|-----------|-------------------------|----------------------------------------------------------------|
> | title       | optional  | str                     | Title of Post                                                  |
> | description | optional  | str                     | Description of Post                                            |

##### Responses

> | http code     | content-type                      | response                                                       |
> |---------------|-----------------------------------|----------------------------------------------------------------|
> | `200`         | `application/json`                | `Post`                                                         |
> | `404`         | `application/json`                | Post does not exist                                            |

</details>



<br>

- **Comment**

<details>
 <summary>
  <code>GET</code>
  <code><b>/comment/:id</b></code>
  <code>(get 1 Comment)</code>
 </summary>

##### Parameters

> | name      |  type     | data type               | description                                                      |
> |-----------|-----------|-------------------------|------------------------------------------------------------------|
> | id        |  required | int                     | comment_id                                                       |

##### Responses

> | http code     | content-type                      | response                                                       |
> |---------------|-----------------------------------|----------------------------------------------------------------|
> | `200`         | `application/json`                | Comment                                                        |
> | `404`         | `application/json`                | Comment does not exist                                         |

</details>

<details>
 <summary>
  <code>GET</code>
  <code><b>/comment/list</b></code>
  <code>(get all Comments)</code>
 </summary>

##### Responses

> | http code     | content-type                      | response                                                       |
> |---------------|-----------------------------------|----------------------------------------------------------------|
> | `200`         | `application/json`                | `Comment`                                                      |

</details>

<details>
 <summary>
  <code>COMMENT</code>
  <code><b>/comment/create</b></code>
  <code>(create a new Comment)</code>
 </summary>

##### Parameters

> | name        |  type     | data type               | description                                                    |
> |-------------|-----------|-------------------------|----------------------------------------------------------------|
> | content     | required  | str                     | Actual comment                                                 |
> | author_id   | required  | str                     | Author of comment                                              |
> | post_id     | required  | str                     | Post the comment was made on                                   |

##### Responses

> | http code     | content-type                      | response                                                       |
> |---------------|-----------------------------------|----------------------------------------------------------------|
> | `200`         | `application/json`                | `Comment`                                                      |

</details>

<details>
 <summary>
  <code>DELETE</code>
  <code><b>/comment/delete/:id</b></code>
  <code>(Delete a Comment)</code>
 </summary>

##### Responses

> | http code     | content-type                      | response                                                       |
> |---------------|-----------------------------------|----------------------------------------------------------------|
> | `200`         | `application/json`                | `Comment`                                                      |
> | `404`         | `application/json`                | Comment does not exist                                         |

</details>

<details>
 <summary>
  <code>PATCH</code>
  <code><b>/comment/update/:id</b></code>
  <code>(Partially update an existing Comment)</code>
 </summary>

##### Parameters

> | name        |  type     | data type               | description                                                    |
> |-------------|-----------|-------------------------|----------------------------------------------------------------|
> | content     | optional  | str                     | Actual comment                                                 |

##### Responses

> | http code     | content-type                      | response                                                       |
> |---------------|-----------------------------------|----------------------------------------------------------------|
> | `200`         | `application/json`                | `Comment`                                                      |
> | `404`         | `application/json`                | Comment does not exist                                         |

</details>





<br><br><br>

# Client



### Dependencies

- [Bootstrap](https://getbootstrap.com/)

### Run

Just open `index.html` and you're good to go



<br>
