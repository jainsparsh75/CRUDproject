import pymongo


def db_collection():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["employeedb"]
    return db

db = db_collection()
employee_collection = db['employee_register_employee']

def check_document(check_query, collection=employee_collection):
    document = collection.find(check_query)
    document_list = list(document)
    if len(document_list)> 0 :
        return {"status": True, "document": document_list}
    return {"status": False}


def insert_document(dict, collection = employee_collection  ):
    try:
        collection.insert(dict)
    except:
        collection.insert_one(dict)
    return

query = {"id": 40}

response = check_document(query, employee_collection)
if response['status'] == True:
    doc = response['document']
    print("response>>", response)
    print("doc>>>", doc)
