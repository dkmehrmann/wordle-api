```bash
curl -X GET localhost:5000
curl -X GET localhost:5000/start
curl -X POST localhost:5000/game/<game_id> -d guess=aword
curl -X GET localhost:5000/game/<game_id>

```