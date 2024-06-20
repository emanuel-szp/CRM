create database CRM;
use CRM;

create table cliente (
id int auto_increment not null primary key,
nome varchar(50) not null,
telefone varchar(50) not null,
compra_passada date not null
);

insert into cliente (nome,telefone,compra_passada) values ('helia','(99)991467393','1972-02-29');

select*from cliente;
