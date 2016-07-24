from apiclient import build

service = build('books', 'v1')
volumes = service.volumes().get