from ..models import listt, yunwei


def getAllDataBy_sortId():
    """
    获取所有数据
    :return: 模块列表, 项目数据
    """
    data = {}
    templates = []
    title_list = listt.objects.order_by('sortId')
    for title in title_list:
        templates.append(title)
        title_id = listt.objects.values('id').filter(name=title)
        res = yunwei.objects.values('name', 'link').filter(title_id=title_id)
        data[title] = res
    return templates, data
