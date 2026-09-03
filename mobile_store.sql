create database mobile_store;
use mobile_store;
create table admins(
admin_id int auto_increment primary key,
full_name varchar(100) not null,
username varchar(50) unique not null,
email varchar(100) unique not null,
password varchar(255) not null);
create table users(
user_id int auto_increment primary key,
full_name varchar(100) not null,
username varchar(50) not null,
email varchar(100) unique not null,
mobile varchar(50) unique not null,
password varchar(255)  not null);
create table products(
product_id int auto_increment primary key,
brand varchar(50) not null,
model varchar(100) not null,
ram varchar(20) not null,
storage varchar(20) not null,
processor varchar(100) not null,
display varchar(50) not null,
battery varchar(30) not null,
camera varchar(50) not null,
color varchar(30) not null,
price decimal(10,2) not null,
stock int not null);
CREATE TABLE categories(
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) UNIQUE NOT NULL
);
insert into categories(category_name) values
('Android'),
('Iphone'),
('Gaming'),
('Budget'),
('Flagship');
alter table products
add category_id int;
alter table products
add foreign key(category_id) references categories(category_id);
insert into products
(brand, model, ram, storage, processor, display, battery, camera, color, price, stock, category_id)
values
('Samsung','Galaxy S24','8GB','256GB','Snapdragon 8 Gen 3','6.2 Inch','4000mAh','50MP','Black',74999,10,1),

('OnePlus','12R','8GB','256GB','Snapdragon 8 Gen 2','6.78 Inch','5500mAh','50MP','Blue',42999,15,1),

('Apple','iPhone 15','128GB','128GB','A16 Bionic','6.1 Inch','3349mAh','48MP','Pink',69999,8,2),

('ASUS','ROG Phone 8','16GB','512GB','Snapdragon 8 Gen 3','6.78 Inch','5500mAh','50MP','Black',89999,5,3),

('Redmi','Note 14','6GB','128GB','Dimensity 7025','6.67 Inch','5000mAh','108MP','Green',17999,20,4),

('Samsung','Galaxy S24 Ultra','12GB','512GB','Snapdragon 8 Gen 3','6.8 Inch','5000mAh','200MP','Titanium Gray',129999,6,5);
create table cart(
cart_id int auto_increment primary key,
user_id int not null,
product_id int not null,
quantity int not null,
total_price decimal(10,2) not null,
foreign key(user_id) references users(user_id),
foreign key(product_id) references products(product_id));
create table orders(
order_id int auto_increment primary key,
user_id int not null,
total_amount decimal(10,2) not null,
order_date date default(current_date()),
order_status enum('Pending','Confirmed','Shipped','OutOfDelivery','Delivered','Cancelled') default 'Pending',
foreign key(user_id)references users(user_id));
create table payments(
payment_id int auto_increment primary key,
order_id int not null,
user_id int not null,
amount decimal(10,2) not null,
payment_method enum('UPI', 'Card',' Cash',' Net Banking'),
payment_status enum('Pending','Success','Failed','Refunded')default 'Pending',
payment_date date default (current_date()),
foreign key(order_id) references orders(order_id),
foreign key(user_id) references users(user_id));
