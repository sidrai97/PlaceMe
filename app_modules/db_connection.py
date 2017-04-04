import pymongo

c = pymongo.MongoClient(host=["mongodb://localhost:27017", "mongodb://localhost:27018", "mongodb://localhost:27019"],
                        replicaSet="rs1")  # connection to mongodb via pymongo driver
db = c.placeme  # database name placeme
applicants = db.applicants  # collection applicants
employers = db.employers  # collection employers
jobs = db.jobs  # collection jobs
