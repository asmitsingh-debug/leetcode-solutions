with delcte as (
    select id,email,row_number() over(partition by email order by id) as dup
     from person 
)
delete from person where id in (select id from delcte where dup>1);
