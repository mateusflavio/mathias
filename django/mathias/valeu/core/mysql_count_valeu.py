
def query(user_name_from):
    params = {
        'user_name_from': user_name_from
    }

    return """
        select count(1) as points, v.user_name_to
          from valeu v
        where month(v.create_at) = month(now())
        and v.user_name_to = '{user_name_from}'
          group by v.user_name_to
    """.format(**params)
