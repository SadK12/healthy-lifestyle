from django import template


register = template.Library()


@register.filter
def calc_food_procent(eaten, norm):
    return round(eaten / norm * 100)


@register.filter
def calc_protein_procent(eaten, norm):
    protein_norm = norm * 0.3 / 4
    return round(eaten / protein_norm * 100)


@register.filter
def calc_fat_procent(eaten, norm):
    fat_norm = norm * 0.25 / 9
    return round(eaten / fat_norm * 100)


@register.filter
def calc_hydrate_procent(eaten, norm):
    hydrate_norm = norm * 0.45 / 4
    return round(eaten / hydrate_norm * 100)