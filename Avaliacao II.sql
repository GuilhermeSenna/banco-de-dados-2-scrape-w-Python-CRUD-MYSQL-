create database saladeaula;

use saladeaula;

create table estudante(
	ID int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    sexo varchar(1) NOT NULL,
    idade int NOT NULL,
    endereco varchar (1) NOT NULL,
    tamfamilia varchar (3) NOT NULL,
    tempoviagem int NOT NULL,
    tempoestudo int NOT NULL,
    materiasperdidas int NOT NULL,
    reforco varchar (3) NOT NULL,
    pagar varchar (3) NOT NULL,
    extracurriculares varchar (3) NOT NULL,
    superior varchar (3) NOT NULL,
    internet varchar (3) NOT NULL,
    namoro varchar (3) NOT NULL,
    relfamilia int NOT NULL,
    tempolivre  int NOT NULL,
    vidasocial  int NOT NULL,
    saude  int NOT NULL,
    faltas  int NOT NULL
);

select * from estudante order by ID desc;
select *, count(ID) from estudante where sexo='F';
select * from estudante order by materiasperdidas;
select * from estudante order by faltas;
select count(ID) as Quantidade_Tuplas from estudante;


drop table estudante;
