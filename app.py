#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, render_template, request

app = Flask(__name__)

#MONGO DB IMPORT LIBRARY
from pymongo import MongoClient
import json
from bson import json_util


# Connect to Mongo db
cluster = MongoClient('mongodb+srv://CookBook_user:nVra6BD7yF9ki5fr@cluster0.gqfwd.mongodb.net/Recipy_db?retryWrites=true&w=majority')
#get database Recipy_db
db = cluster["Recipy_db"]
# get table Recipy_records
collection = db['Recipy_records']

@app.route("/add_data",methods=["POST"])
def add_data():
    """
    this function will retrieve recipy post by user and add it to db
    case 1 : CREATE if new user
    case 2 : UPDATE if user exists and added new recipe
    case 3:  Do NOTHING if same user uploads same recipy
    """
    data = request.json

    filter_result = list(collection.find({ '$and': [{"name": data["name"]},
            {"email": data["email"]},
        ]}))

    if len(filter_result) == 0:
        # case : new user
        collection.insert_one(data)
    else:
        # case : user already exists
        if(data['recipies'][0] not in filter_result[0]['recipies']):
            #updating new recipies..."
            prev_recipies = filter_result[0]['recipies']
            all_recipies = prev_recipies+data['recipies']
            collection.update_one({"_id": filter_result[0]["_id"]}, {"$set": {"recipies": all_recipies}})
        else:
            # same recipy already exists
            return "Recipe already exist"

    return "Added Successfully"

@app.route("/update_data",methods=["POST"])
def update_data():
    """
    this function will update recipy post by user in db
    return success/failure response
    """
    data = request.json
    filter_result = list(collection.find({ '$and': [{"name": data["name"]},
            {"email": data["email"]},
        ]}))
    updated_recipies = data['recipies']
    prev_recipy_name = data["prev_recipe_name"]

    try:
        #updating prev recipies..."
        prev_recipies = filter_result[0]['recipies']
        final_recipies = []
        for recipe in prev_recipies:
                if recipe['recipe_name'] == prev_recipy_name:
                    final_recipies = final_recipies + updated_recipies
                else:
                    final_recipies = final_recipies + recipe

        collection.update_one({"_id": filter_result[0]["_id"]}, {"$set": {"recipies": final_recipies}})
    except:
        return "Something Went Wrong"

    return "Updated Successfully"

@app.route("/delete_my_recipy",methods=["GET"])
def delete_my_recipy():
    """
    To delete given recipy from db
    GET : takes recipy name,user name and user email
    returns delete status
    """
    try:
        name = request.args.get('name')
        email = request.args.get('email')
        recipy_name = request.args.get('recipy_name')

        filter_result = list(collection.find({'$and': [{"name": name},
                                                       {"email": email},
                                                       ]}))

        if len(filter_result) == 0:
            # case : new user
            return "Something Went Wrong"
        else:
            prev_recipies = filter_result[0]['recipies']
            new_recipies = []
            for recipy in prev_recipies:
                # print(recipy['recipy_name'])
                if recipy['recipe_name'] != recipy_name:
                    new_recipies.append(recipy)
            collection.update_one({"_id": filter_result[0]["_id"]}, {"$set": {"recipies": new_recipies}})
    except:
        return "Something went wrong"

    return "Deleted Succesfully"

@app.route("/get_recipes",methods=["GET"])
def get_recipes():
    """
    To get all data from db
    """
    all_recipes = list(collection.find({}))
    return json.dumps(all_recipes,default=json_util.default)

@app.route('/')
def home():
    """
    To view a home page
    """
    all_data = list(collection.find({}))
    return render_template("index.html", all_data=all_data)

@app.route('/recipeView')
def view_recipe():
    """
    To View a specific clicked recipy detail
    GET : takes recipy name, user name and email
    returns that specific recipy containing template
    """
    name = request.args.get('name')
    email = request.args.get('email')
    recipy_name = request.args.get('recipy_name')
    filter_result = list(collection.find({'$and': [{"name": name},
                                                   {"email": email},
                                                   {"recipies.recipe_name":recipy_name},

                                                   ]}))

    return render_template("receipe-post.html",
                           my_recipy=filter_result[0]['recipies'],
                           recipy_name=recipy_name,name=name)

@app.route('/getMyRecipies',methods=["GET"])
def get_my_recipies():
    """
    To get all data of a specific user from db
    pass it to all recipies template
    GET : user_id
    return all recipy template containing recipies of that specific user
    """
    name = request.args.get('name')
    email = request.args.get('email')

    try:
        all_recipes = list(collection.find({ '$and': [{"name": name},
            {"email": email},
        ]}))

        if len(all_recipes[0]['recipies'] ) == 0:
            return "<h2>No Recipies found</h2>"

        return render_template("includes/all_recipies.html",
                               all_recipes=all_recipes[0]['recipies'],
                               user=name,email=email)
    except:
        return "<h2>No data found</h2>"


@app.route('/my_recipies')
def dashboard():
    """
    Template for user to add,update,delete and view there own recipies
    """
    # all_recipes = list(collection.find({"recipies":"recipe_name1"}))
    return render_template("dashboard.html")


if __name__ == '__main__':
    app.run()

