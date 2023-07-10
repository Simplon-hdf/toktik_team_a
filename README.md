# tiktok_team_a

Basic Tiktok clone
- Visitors can only view Post
- User can login or signup
- User can create Posts and Comments
- Post has Comments





<br><hr>

## Documentation

- `docs/conception` : data models





<br><hr>

## API



### Dependencies

- Python
- [PostgreSQL](https://www.postgresql.org/download/) : Database



<br>

### Install

```bash
conda create --name toktik
conda activate toktik
conda install python=3.10 pip
pip install uvicorn fastapi SQLAlchemy
```



<br>

### Run [http://localhost:8000/](http://localhost:8000/)

```bash
conda activate toktik
uvicorn api.main:app --reload
```



<br>

### Endpoints

<br>

> **User**

<details>
 <summary>
  <code>POST</code>
  <code><b>/login</b></code>
  <code>(login with username & password, and get back an auth token)</code>
 </summary>

##### Parameters

> | name      |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | name      |  required | string                  | username                                                              |
> | password  |  required | string                  | password                                                              |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`                | ` `                                                                 |
> | `404`        | `application/json`                | ` `

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
