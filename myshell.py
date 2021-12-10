import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE","learning_log.settings")

import django
django.setup()

from MainApp.models import Topic, Entry


#making sure our data is in the database, first we select * all from our topic to see if all of it is there
topics = Topic.objects.all()

for topic in topics: 
    print(topic.id, topic)

t=Topic.objects.get(id=1)

print(t.text)
print(t.date_added)

entries=t.entry_set.all()

for entry  in entries: 
    print(entry)