SELECT owner.owner_id, owner.owner_name, category.category_title, COUNT(DISTINCT category_title) as frequency
FROM article
INNER JOIN owner on article.owner_id = owner.owner_id
INNER JOIN category_article_mapping on category_article_mapping.article_id = article.article_id
INNER JOIN category on article.category_id = category.category_id
GROUP by owner.owner_id, owner.owner_name
ORDER by COUNT(DISTINCT category_title) DESC
