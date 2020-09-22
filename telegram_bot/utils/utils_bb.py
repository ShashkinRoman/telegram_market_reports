from telegram_bot.models import Users, Profiles, ModelHasRoles, Roles, Bids


def sorted_masters_and_salon(users_id):
    """
    :param user_id: [{'user_id': user_id, 'role': 'master'}, ...]
    :return: {master: 12, salon: 13, ....}
    """
    roles_count = {}
    for user in users_id:
        role = user.get('role')
        check = roles_count.get(role)
        if check is None:
            roles_count[role] = 1
        else:
            roles_count[role] += 1
    return roles_count


def add_roles(users_id):
    """ add role by user_id from model_has_roles
       :argument:[{'user_id': user_id, 'profile_id': profile_id}, ...]
       :return: [{'user_id': user_id, 'profile_id': profile_id, 'role': studio or masters, ...]"""
    for user_id in users_id:
        try:
            us_id = user_id['user_id']
            role = ModelHasRoles.objects.get(model_id=us_id).role.ru_name
            user_id['role'] = role
        except:
            user_id['role'] = 'none'


def corrected_users_id(list_users_id):
    """take set list user id and forms dict
    :arg: [userid, ...]
    :return: [{'id_user': user_id}, ...]"""
    list_profile_user_id = []
    for user_id in list_users_id:
        list_id = {'user_id': user_id}
        list_profile_user_id.append(list_id)
    return list_profile_user_id


def find_registered_users(start_date, end_date):
    """
    search users registered between start_date - end_date
    :param start_date: '2020-09-15'
    :param end_date: '2020-09-15'
    :return: [userid, ...]
    """
    users = Users.objects.filter(created_at__range=[start_date + ' 00:00', end_date + ' 23:59'])
    user_id_list = []
    for user in users:
        user_id_list.append(user.userid)
    return user_id_list


def profiles_users_id(users_id):
    """take list user id and find prodiles id in profiles table
    :arg: list user_id = [int(user_id), ...]
    :return: dict [{'id_profile': id_profile, 'user_id': user_id}, ...]"""
    if type(users_id) is int:
        users_id = [users_id]
    list_profile_user_id = []
    for id_user in users_id:
        try:
            iterate_obj = Profiles.get(userid_id=id_user)
            profile_id = iterate_obj.profileid
        except:
            profile_id = 'none'
        list_id = {'id_profile': profile_id,
                   'user_id': id_user}
        list_profile_user_id.append(list_id)
    return list_profile_user_id


def users_who_created_bids(start_date, end_date):
    """
    find users who created bids for a specific date.
    :param: str(end_date=%Y-%m-%d, start_date=%Y-%m-%d)
    :return: [{'userid': 123123, 'name': "Березка", 'bids': 12, 'profile_id': 123123}, ...]
    """
    result_obj = Bids.objects.filter(created_at__range=[start_date + ' 00:00', end_date + ' 23:59'])
    set_profile_id = []
    for user in result_obj:
        if user.profileid.profileid not in set_profile_id:
            set_profile_id.append(user.profileid.profileid)
    results = []
    for profile_id in set_profile_id:
        user_obj = result_obj.filter(profileid=profile_id)
        user_id = user_obj.last().profileid.userid.userid
        info = {}
        info['user_id'] = user_id
        info['name'] = Users.objects.get(userid=user_id).name
        info['bids'] = len(user_obj.filter(profileid=profile_id))
        info['profile_id'] = profile_id
        results.append(info)
    return len(result_obj), results
