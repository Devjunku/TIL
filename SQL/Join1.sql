
-- like만 사용
select i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
from ANIMAL_INS i, ANIMAL_OUTS o
where i.ANIMAL_ID = o.ANIMAL_ID and (i.SEX_UPON_INTAKE like "Intact%" and (o.SEX_UPON_OUTCOME like "Spayed%" or o.SEX_UPON_OUTCOME like "Neutered%"))
order by i.ANIMAL_ID

-- !=를 사용(코드 작성 면에서는 이게 제일 좋음)
select i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
from ANIMAL_INS i, ANIMAL_OUTS o
where i.ANIMAL_ID = o.ANIMAL_ID and i.SEX_UPON_INTAKE != o. SEX_UPON_OUTCOME
order by i.ANIMAL_ID