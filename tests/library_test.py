import enrich_db
import couchDB
import auth

db = couchDB.Cloudant(auth.user, auth.password)