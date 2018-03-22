def build_profile(first, last, **user_info):
    profile = {
        'first_name': first,
        'last_name': last
    }
    # profile['first_name'] = first
    # profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value

    return profile


me = build_profile('ming', 'wang', location='HeFei', age=18, hobbies=[
    'coding', 'playing games', 'reading books'])
print(me)
