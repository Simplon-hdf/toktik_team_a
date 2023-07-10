> | Class          |  name                | type           | size      | nullable   | key             | unique   |
> |----------------|----------------------|----------------|-----------|------------|-----------------|----------|
> | users          | id                   | int            | 32        | FALSE      | .               | TRUE     |
> | users          | username             | string         | 20        | FALSE      | .               | TRUE     |
> | users          | email                | string         | 60        | FALSE      | .               | TRUE     |
> | users          | password             | string         | 255       | FALSE      | .               | FALSE    |
> | users          | token                | string         | 255       | FALSE      | .               | TRUE     |
> | posts          | id                   | int            | 32        | FALSE      | .               | TRUE     |
> | posts          | title                | string         | 60        | FALSE      | .               | FALSE    |
> | posts          | description          | text           | .         | TRUE       | .               | FALSE    |
> | posts          | video_url            | string         | 255       | FALSE      | .               | FALSE    |
> | posts          | author_id            | int            | 32        | FALSE      | .               | FALSE    |
> | comments       | id                   | int            | 32        | FALSE      | .               | TRUE     |
> | comments       | content              | text           | .         | FALSE      | .               | FALSE    |
> | comments       | user_id              | int            | 32        | FALSE      | .               | FALSE    |
> | comments       | post_id              | int            | 32        | FALSE      | .               | FALSE    |
