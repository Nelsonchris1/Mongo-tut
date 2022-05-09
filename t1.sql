with t1 as (
    select a.id,a.name, SUM(o.total_amt_usd) total_amt
    from accounts a
    join orders o 
    on a.id = o.account_id
    group by a.name
), t2 as (
    select MAX(total_amt)
    from t1
)
select a.name, w.channel, COUNT(*) as num_web_events
from accounts a
join web_events w
on a.id = w.account_id AND a.id = (SELECT id from t1)
group by 1, 2
having SUM(o.total_amt_usd) = (select * from t2)
