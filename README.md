# tiktok_team_a

Basic Tiktok clone
- Visitors can only view Post
- User can login or signup
- User can create Posts and Comments
- Post has Comments





<br><hr>

## Documentation

- `docs/conception` : data models
- [http://localhost:8000/docs](http://localhost:8000/docs) : auto-generated documentation (*Swagger UI*)
- [http://localhost:8000/redoc](http://localhost:8000/redoc) : auto-generated documentation (*Redoc*)





<br><hr>

## API



### Dependencies

- Python
- [PostgreSQL](https://www.postgresql.org/download/) : Database
- [uvicorn](https://www.uvicorn.org/) : WebServer
- [fastapi](https://fastapi.tiangolo.com/) : API Framework
- [SQLAlchemy](https://www.sqlalchemy.org/) : ORM
- [psycopg2](https://pypi.org/project/psycopg2/) : PostgreSQL adapter
- [PyJWT](https://pyjwt.readthedocs.io/en/stable/) / [passlib](https://passlib.readthedocs.io/en/stable/) : Password hashing & token generation



<br>

### Install

```bash
conda create --name toktik
conda activate toktik
conda install python=3.10 pip
pip install uvicorn fastapi==0.100.0 SQLAlchemy pyjwt passlib psycopg2 hashlib
```



<br>

### Run [http://localhost:8000/](http://localhost:8000/)

```bash
conda activate toktik
uvicorn api.src.main:app --reload
```



<br>

### Endpoints

<br>

**Post**

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



**Comment**

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





<br><hr>

## Client



### Dependencies

- a
- b



<br>

### Install

```bash
[commands]
```



<br>

### Run

```bash
[commands]
```



<br>
