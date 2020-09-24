from app import db

class Pizza(db.Model):
  __tablename__ = 'pizzas'
  
  id = db.Column(db.Integer,primary_key=True)
  flavour = db.column(db.String(255))
  size =db.Column(db.String(255))
  price = db.Column(db.String(255))
  crust = db.Column(db.String(255))
  toppings = db.Column(db.String(255))
  
  
  def __init__(self,flavour,size, price, crust, toppings):
    '''
    initialize with flavour
    '''
    
    self.flavour = flavour,
    self.size = size,
    self.price = price,
    self.crust = crust,
    self.toppings = toppings
    
  def save_pizza(self):  
    db.session.add(self)
    db.session.commit()
    
    
  @staticmethod
  def get_all():
    return Pizza.query.all()
  
  def delete(self):
    db.session.delete(self)
    db.session.commit()
    
    
  def __repr__(self):
    return "<Pizza: {}, of size{},will cost{}, with crust{}, and toppings{}>".format(self.flavour, self.size,self.price,self.crust,self.toppings)
    