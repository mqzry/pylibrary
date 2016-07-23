import couchDB
import auth

db = couchDB.Cloudant(auth.user, auth.password)

db.create_db('test')
print(db.replicate('library', 'test'))


## Test enrichment step
# libgen


# google books


## Test download step


## Test upload step