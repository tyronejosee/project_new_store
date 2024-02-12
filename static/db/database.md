// Users App

Table CustomUser {
  id int [pk, increment]
  username varchar(100)
  email varchar(254)
  first_name varchar(200)
  last_name varchar(200)
  address text
  phone_number varchar(15)
  is_active bool(T)
  is_staff bool(F)
  date_joined datetime
}


// Products App
Ref: Product.brand < Brand.id
Ref: Product.deal < Deal.id
Ref: Product.category < Category.id

Table Product {
  id int [pk, increment]
  title varchar(255)
  slug varchar(100)
  brand FK
  normal_price decimal(10)
  sale_price FK
  deal FK
  category FK
  image image
  stock int(100)
  warranty int(1)
  featured bool(F)
  show_hide bool(T)
  description text
  specifications text
  created_at datetime
  updated_at datetime
}

Table Category {
  id int [pk, increment]
  title varchar(50) [unique]
  slug varchar [unique]
  show_hide bool(T)
}

Table Brand {
  id int [pk, increment]
  title varchar(50) [unique]
  slug varchar [unique]
  show_hide bool(T)
}

Table Deal {
  id int [pk, increment]
  name varchar(50) [unique]
  slug varchar [unique]
  image image
  description text
  discount decimal(5)
  start_date datetime
  end_date datetime
  status bool(T)
}

// Cart App
Ref: Cart.user < CustomUser.id
Ref: CartItem.cart < Cart.id
Ref: CartItem.product < Product.id
Ref: Wishlist.user < CustomUser.id
Ref: Wishlist.products < Product.id

Table Cart {
  id int [pk, increment]
  user FK
  adress varchar(255)
}

Table CartItem {
  id int [pk, increment]
  cart FK
  product FK
  quantity int(0)
}

Table Wishlist {
  id int [pk, increment]
  user FK
  products FK
}


// Home App

Table Company {
  id int [pk, increment]
  name varchar(50)
  logo image
  copy varchar(150)
  description text
  email varchar
  github varchar
  linkedin varchar
}

Table Page {
  id int [pk, increment]
  key varchar(50)
  content text
  image image
  created_at datetime
  updated_at datetime
}
