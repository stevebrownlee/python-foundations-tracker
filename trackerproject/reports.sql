select * from trackerwebapp_submission;
select * from trackerwebapp_classroom;
select * from trackerwebapp_studentcohort;
select * from trackerwebapp_cohort;
select * from trackerwebapp_student s;

delete from trackerwebapp_studentcohort where id = 56;


select s.first_name,
    s.last_name,
    c.name,
    count(su.id) as exercise_count
from trackerwebapp_student s
    left join trackerwebapp_cohort c on c.id = s.cohort_id
    left join trackerwebapp_submission su on s.id = su.student_id
where c.name is NULL
group by s.first_name,
    s.last_name,
    c.name
order by exercise_count desc;


select
    s.id,
    s.first_name,
    s.last_name,
    c.name,
    c.id as cohort_id,
    sc.initial
from trackerwebapp_student s
left join trackerwebapp_studentcohort sc on sc.student_id = s.id
left join trackerwebapp_cohort c on sc.cohort_id = c.id
where sc.initial is not 0
;