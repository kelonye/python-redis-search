
## Install


```
pip install -e git://github.com/kelonye/python_redis_search.git#egg=reds
```

## Example (django)

```
import reds
import redis
from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=50)

location_names = ['Osaka', 'Tokyo']
for name in location_names:
    location = Location(name=name)
    location.save()

# create client
redis_client = redis.StrictRedis(db='test_db')
reds_client = reds.SwahiliSearch('locations', redis_client)

# add some indicies
for location in Location.objects.all():
    reds_client.push(location.pk, location.name)

# search
results = reds_client.query('dokyo')
for pk in results:
    print Location.objects.get(pk=pk).name

# teardown
for name in location_names:
    location = Location.objects.get(name=name)
    location.delete()

redis_client.flushdb()

```

## Api


### Search(redis_client, namespace)

  - redis_client: new redis client
  - namespace: search group name

  returns a new reds client

### Search#push(string)
  - string: search index
  adds a search index

### Search#query(query_string)
  - query_string: text to query

  returns search results by query_string

### SwahiliSearch(redis_client, namespace)
  - client to search swahili texts
  - extends `Search`

## Test

```
make
```

## License

MIT

```

## Api

### Search(redis_client, namespace)
  - redis_client: new redis client
  - namespace: search group name
  returns a new reds client

### Search#push(string)
  - string: search index
  adds a search index

### Search#query(query_string)
  - query_string: text to query
  returns search results by query_string

### SwahiliSearch(redis_client, namespace)
  - client for swahili texts
  - extends `Search`

## Test

```
make
```

## License

MIT
