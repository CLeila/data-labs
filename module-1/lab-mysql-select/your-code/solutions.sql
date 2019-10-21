use publications;

##############################
########## n° 1 ##############
###### pas de group by car sinon ça retire tous les doubles et ca donne 19 lignes au lieu de 25 

select a.au_id as author_id, a.au_lname as last_name, a.au_fname as first_name, t.title as title, p.pub_name as publisher
from authors a
inner join titleauthor ta on ta.au_id=a.au_id
inner join titles t on t.title_id=ta.title_id
inner join publishers p on p.pub_id=t.pub_id;

##############################
########## n° 2 ##############

select a.au_id as author_id, a.au_lname as last_name, a.au_fname as first_name, p.pub_name as publisher, count(t.title) as count_title
from authors a
inner join titleauthor ta on ta.au_id=a.au_id
inner join titles t on t.title_id=ta.title_id
inner join publishers p on p.pub_id=t.pub_id
group by ta.au_id;

##############################
########## n° 3 ##############
select a.au_id as author_id, a.au_lname as last_name, a.au_fname as first_name, t.title as title, count(s.title_id) as total
from authors a
inner join titleauthor ta on ta.au_id=a.au_id
inner join titles t on t.title_id=ta.title_id
inner join sales s on s.title_id=t.title_id
group by a.au_id
order by total desc
limit 3;

##############################
########## n° 4 ##############
select a.au_id as author_id, a.au_lname as last_name, a.au_fname as first_name, t.title as title, count(s.title_id) as total
from authors a
left join titleauthor ta on ta.au_id=a.au_id
left join titles t on t.title_id=ta.title_id
left join sales s on s.title_id=t.title_id
group by a.au_id
order by total desc;

