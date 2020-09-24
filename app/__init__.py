from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import  request,jsonify,abort

# local import
from instance.config import app_config



# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
    from app.models import Pizza
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    @app.route('/pizzas/',methods =['POST','GET'])
    def pizzas():
        if request.method =="POST":
            flavour = str(request.data.get('flavour',''))
            size =str(request.data.get('size',''))
            price = str(request.data.get('cost','899'))
            crust =str(request.data.get('crust',''))
            toppings = str(request.data.get('toppings',''))
            if flavour:
                pizza = Pizza(flavour=flavour,size=size,price=price,crust=crust,toppings=toppings)
                pizza.save_pizza()
                response =jsonify({
                    'id': pizza.id,
                    'flavour': pizza.flavour,
                    'size':pizza.size,
                    'price':pizza.price,
                    'crust':pizza.crust,
                    'toppings':pizza.toppings
                }) 
                response.status_code = 201
                return response
            
        else:
            pizzas = Pizza.get_all()
            results = []
            
            for pizza in pizzas:
                obj = {
                'id': pizza.id,
                'flavour': pizza.flavour,
                'size':pizza.size,
                'price':pizza.price,
                'crust':pizza.crust,
                'toppings':pizza.toppings
                }
            results.append(obj)
            response = jsonify(results)
            return response
            
    @app.route('/pizzas/<int:id>',methods=['GET', 'PUT', 'DELETE'])   
    def pizza_manipulation(id, **kwargs):
        pizza = Pizza.query.filter_by(id=id).first()
        if not pizza: 
            abort(404)
            
            
        if request.method == 'DELETE':
            pizza.delete()
            return{
            "message": "pizza {} deleted successfully".format(pizza.id) 
            },200
            
            
        elif request.method == 'PUT': 
            flavour =  str(request.data.ge('name',''))
            pizza.flavour = flavour
            pizza.save()
            response = jsonify({
            'id': pizza.id,
            'flavour':pizza.flavour,
            'size':pizza.size,
            'price':pizza.price,
            'crust':pizza.crust,
            'toppings':pizza.toppings
            })        
            response.status_code = 200
            return response
        else:
            response =jsonify({
            'id': pizza.id,
            'flavour': pizza.flavour,
            'size':pizza.size,
            'price':pizza.price,
            'crust':pizza.crust,
            'toppings':pizza.toppings
        })
            response.status_code= 200
            return response


    return app