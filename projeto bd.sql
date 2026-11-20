create table Cliente(
	id int identity,
	nome varchar(100) not null,
	email varchar(45) not null,
	fone varchar(100) not null,
	primary key(id)
)
create table Servico(
	id int identity,
	descricao varchar(45) not null,
	valor decimal(10, 2) not null,
	primary key(id)
)
create table Horario(
	id int identity,
	data datetime not null,
	confrimado bit not null,
	id_servico int not null,
	id_cliente int not null,
	primary key(id),
	foreign key(id_servico) references Servico(id),
	foreign key(id_cliente) references Cliente(id)
)