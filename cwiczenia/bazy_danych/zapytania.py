# wiele do wielu

# obiekt kategorii nr 1
category = Category.objects.get(pk=1)

# wszystkie artykuły z kategorii 1
category.article.all()

# wszystkie artykuły, które należą do kategorii 1 oraz kategorii 2 jednocześnie
Article.objects.filter(category__in=[category1]).filter(category__in=[category2])
