from django.db import models
from django.db.models import ExpressionWrapper, F, fields, Max


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255)
    lft = models.PositiveIntegerField()
    rght = models.PositiveIntegerField()
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @classmethod
    def build_tree(cls):
        return cls.objects.select_related("parent").annotate(
            depth=ExpressionWrapper(F('rght') - F('lft') - 1, output_field=fields.IntegerField())
        ).order_by('lft')

    @classmethod
    def get_tree_as_dict(cls):
        def build_tree_recursive(node, all_children):
            if not all_children.get(node.id):
                return {'node': node, 'children': []}

            children = []
            for child in all_children[node.id]:
                children.append(build_tree_recursive(child, all_children))

            return {'node': node, 'children': children}

        tree_data = cls.build_tree()
        all_children = {obj['parent_id']: [] for obj in tree_data.values()}

        # Загрузка дочерних элементов в один запрос
        for child in cls.objects.filter(parent__in=all_children.keys()):
            all_children[child.parent_id].append(child)

        tree_dict = {}
        for node in tree_data:
            tree_dict[node.name] = build_tree_recursive(node, all_children)

        return tree_dict