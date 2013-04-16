
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
Location.objects.delete()
redis_client.flushdb()

```

## Api

### Search(redis_client, namespace)
  return a new search instance using `redis_client` with `namespace`

### Search#push(index, string)
  add search index `string`

### Search#query(query)
  returns search results for `query`

### SwahiliSearch(redis_client, namespace)
  used to search swahili texts

## Test

```
make
```

## License

MIT
