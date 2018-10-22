from ..models import yunwei_user


def getUserInfoWithId(userId):
    """
    根据userId获取用户详情
    :param userId:  int
    :return: dic {...}
    """
    tmp_dic = {}
    if not userId:
        raise("ValueException: no UserId")
    else:
        UserInfo = yunwei_user.objects.get(id=userId)
        tmp_dic['username'], tmp_dic['name'] = UserInfo.username, UserInfo.name
        return tmp_dic
