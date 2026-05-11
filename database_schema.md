# Database Schema

### Tables

`meals`

| Name          | Type      | Nullable | Default        | Other                           | Description               |
| ------------- | --------- | -------- | -------------- | ------------------------------- | ------------------------- |
| id            | integer   | false    | auto increment | primary key                     | meal's unique id          |
| name          | text      | true     | null           |                                 | meal's name               |
| description   | text      | true     | null           |                                 | meal's description        |
| price         | integer   | false    | 0              |                                 | meal's price              |
| status        | enum      | false    | AVAILABLE      | AVAILABLE SOLD_OUT DISCONTINUED | meal's status             |
| type_id       | integer   | true     | null           | foreign key                     | meal's type               |
| collection_id | integer   | true     | null           | foreign key                     | meal's collection         |
| created_at    | timestamp | false    | now()          |                                 | time of creating this row |
| updated_at    | timestamp | false    | now()          | update trigger                  | time of updating this row |

`types`
| Name        | Type      | Nullable | Default        | Other          | Description               |
| ----------- | --------- | -------- | -------------- | -------------- | ------------------------- |
| id          | integer   | false    | auto increment | primary key    | type's unique id          |
| name        | text      | true     | null           |                | type's name               |
| description | text      | true     | null           |                | type's description        |
| created_at  | timestamp | false    | now()          |                | time of creating this row |
| updated_at  | timestamp | false    | now()          | update trigger | time of updating this row |

`collections`
| Name        | Type      | Nullable | Default        | Other          | Description               |
| ----------- | --------- | -------- | -------------- | -------------- | ------------------------- |
| id          | integer   | false    | auto increment | primary key    | collection's unique id    |
| name        | text      | true     | null           |                | collection's name         |
| description | text      | true     | null           |                | collection's description  |
| created_at  | timestamp | false    | now()          |                | time of creating this row |
| updated_at  | timestamp | false    | now()          | update trigger | time of updating this row |

`tables`
| Name        | Type      | Nullable | Default        | Other                                                      | Description               |
| ----------- | --------- | -------- | -------------- | ---------------------------------------------------------- | ------------------------- |
| id          | integer   | false    | auto increment | primary key                                                | table's unique id         |
| name        | text      | true     | null           |                                                            | table's name              |
| description | text      | true     | null           |                                                            | table's description       |
| capacity    | integer   | false    | 0              |                                                            | table's capacity          |
| status      | enum      | false    | AVAILABLE      | AVAILABLE OCCUPIED PAYING CLEANING RESERVED OUT_OF_SERVICE | table's status            |
| created_at  | timestamp | false    | now()          |                                                            | time of creating this row |
| updated_at  | timestamp | false    | now()          | update trigger                                             | time of updating this row |

`orders`
| Name           | Type      | Nullable | Default        | Other                                  | Description               |
| -------------- | --------- | -------- | -------------- | -------------------------------------- | ------------------------- |
| id             | integer   | false    | auto increment | primary key                            | order's unique id         |
| order_serial   | text      | true     | null           |                                        | order's serial number     |
| table_id       | integer   | true     | null           | foreign key                            | order's table             |
| session_token  | uuid      | false    | uuid()         |                                        | order's uuid          s   |
| status         | enum      | false    | PENDING        | PENDING PREPARING SERVED PAID CANCELED | order's status            |
| payment_method | enum      | false    | UNPAID         | UNPAID CASH ATM CREDIT_CARD LINE_PAY   | order's payment method    |
| total_amount   | integer   | false    | 0              |                                        | order's total amount      |
| note           | text      | true     | null           |                                        | order's note              |
| created_at     | timestamp | false    | now()          |                                        | time of creating this row |
| updated_at     | timestamp | false    | now()          | update trigger                         | time of updating this row |

`order_item`
| Name       | Type      | Nullable | Default             | Other          | Description               |
| ---------- | --------- | -------- | ------------------- | -------------- | ------------------------- |
| id         | integer   | false    | auto increment      | primary key    | order's unique id         |
| order_id   | integer   | false    | order's primary key | foreign key    | order's id                |
| meal_id    | integer   | false    | meal's primary key  | foreign key    | meal's id                 |
| quantity   | integer   | false    | 0                   |                | order's quantity          |
| unit_price | integer   | false    | 0                   |                | order's unit price        |
| created_at | timestamp | false    | now()               |                | time of creating this row |
| updated_at | timestamp | false    | now()               | update trigger | time of updating this row |

`staffs`
| Name       | Type      | Nullable | Default        | Other                                      | Description               |
| ---------- | --------- | -------- | -------------- | ------------------------------------------ | ------------------------- |
| id         | integer   | false    | auto increment | primary key                                | staff's unique id         |
| username   | text      | false    |                |                                            | staff's username          |
| password   | text      | false    |                |                                            | staff's password          |
| role       | enum      | false    | STAFF          | ADMIN MANAGER CASHIER WAITER KITCHEN STAFF | staff's role              |
| is_active  | enum      | false    | ACTIVE         | ACTIVE INACTIVE                            | staff's status            |
| created_at | timestamp | false    | now()          |                                            | time of creating this row |
| updated_at | timestamp | false    | now()          | update trigger                             | time of updating this row |

`staff_sessions`
| Name       | Type      | Nullable | Default        | Other          | Description               |
| ---------- | --------- | -------- | -------------- | -------------- | ------------------------- |
| id         | integer   | false    | auto increment | primary key    | staff_session's unique id |
| staff_id   | integer   | false    |                | foreign key    | staff's id                |
| session_id | text      | false    |                | index          | session id                |
| expires_at | timestamp | true     | null           |                | session's expiration time |
| created_at | timestamp | false    | now()          |                | time of creating this row |
| updated_at | timestamp | false    | now()          | update trigger | time of updating this row |