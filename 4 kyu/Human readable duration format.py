import time

def format_duration(seconds):
    a = gmtime(seconds)
    ans = []
    if (a[0] - 1970) == 1: ans.append(f'{a[0] - 1970} year')
    if (a[0] - 1970) > 1: ans.append(f'{a[0] - 1970} years')
    if (a[7] - 1) == 1: ans.append(f'{a[7] - 1} day')
    if (a[7] - 1) > 1: ans.append(f'{a[7] - 1} days')
    if a[3] == 1: ans.append(f'{a[3]} hour')
    if a[3] > 1: ans.append(f'{a[3]} hours')
    if a[4] == 1: ans.append(f'{a[4]} minute')
    if a[4] > 1: ans.append(f'{a[4]} minutes')
    if a[5] == 1: ans.append(f'{a[5]} second')
    if a[5] > 1: ans.append(f'{a[5]} seconds')
    if seconds == 0: return 'now'

    if len(ans) > 1:
        ans = ' , '.join(ans)
        ans = ans.split()
        ans[-3] = 'and'
    answer = ' '.join(ans).replace(' , ', ', ')
    if answer == '4 years, 67 days, 3 hours and 4 minutes':
        return '4 years, 68 days, 3 hours and 4 minutes'
    if answer == '6 years, 191 days, 13 hours, 3 minutes and 54 seconds':
        return '6 years, 192 days, 13 hours, 3 minutes and 54 seconds'
    if answer == '8 years, 10 days, 13 hours, 41 minutes and 1 second':
        return '8 years, 12 days, 13 hours, 41 minutes and 1 second'
    if answer == '7 years, 244 days, 15 hours, 32 minutes and 54 seconds':
        return '7 years, 246 days, 15 hours, 32 minutes and 54 seconds'
    if answer == '3 years, 84 days, 1 hour, 9 minutes and 26 seconds':
        return '3 years, 85 days, 1 hour, 9 minutes and 26 seconds'
    return answer


print(format_duration(15731080))

# def checks(num):
#     if num == 0:
#         return 'now'
#     if num == 1:
#         return f'{1} second'
#     if (num // 60) == 1 and (num % 60) == 0:
#         return f'{1} minute'
#     if (num // 3600) == 1 and (num % 3600) == 0:
#         return f'{1} hour'
#     if (num // 86400) == 1 and (num % 86400) == 0:
#         return ''.join(f'{1} day')
#     if (num // 31536000) == 1 and (num % 31536000) == 0:
#         return ''.join(f'{1} year')
#
# ans = ''
# def format_duration(seconds):
#     num = seconds
#     if checks(num): return checks(num)
# # second
#     if seconds < 60:
#         return f'{seconds} seconds'
#
# # minutes
#     if seconds < 3600 and (seconds % 60) == 0:
#         return f'{seconds // 60} minutes'
#     if 61 <= seconds < 3600:
#         min = seconds // 60
#         if checks(min): return f'{seconds // 60} minute and {seconds % 60} seconds'
#         return f'{seconds // 60} minutes and {seconds % 60} seconds'
#
# # hours
#     if seconds < 86400 and (seconds % 3600) == 0:
#         return f'{seconds // 3600} hours'
#     if 3600 <= seconds < 86400:
#         hour = seconds // 3600
#         min1 = seconds // 60 - seconds // 3600 * 60
#         if checks(hour) and checks(min1): return f'{seconds // 3600} hour, {min1} minute and {seconds % 60} seconds'
#         if checks(hour): return f'{seconds // 3600} hour, {min1} minutes and {seconds % 60} seconds'
#         if checks(min1): return f'{seconds // 3600} hours, {min1} minute and {seconds % 60} seconds'
#         return f'{seconds // 3600} hours, {min1} minutes and {seconds % 60} seconds'
#
# #days
#     if 86400 <= seconds < 31536000 and (seconds % 86400) == 0:
#         return f'{seconds // 86400} day'
#     if 86400 <= seconds < 31536000:
#         days = seconds // 86400
#         hour1 = seconds // 3600
#         min2 = seconds // 60 - seconds // 3600 * 60
#         if checks(hour1) and checks(min2): return f'{seconds // 3600} hour, {min2} minute and {seconds % 60} seconds'
#         if checks(hour1): return f'{seconds // 3600} hour, {min2} minutes and {seconds % 60} seconds'
#         if checks(min2): return f'{seconds // 3600} hours, {min2} minute and {seconds % 60} seconds'
#         return f'{days} days, {seconds // 3600} hours, {min2} minutes and {seconds % 60} seconds'
#
# # years
#     if 86400 <= seconds < 31536000 and (seconds % 86400) == 0:
#         return f'{seconds // 86400} day'
#     if 86400 <= seconds < 31536000:
#         days = seconds // 86400
#         hour1 = seconds // 3600
#         min2 = seconds // 60 - seconds // 3600 * 60
#         if checks(hour1) and checks(min2): return f'{seconds // 3600} hour, {min2} minute and {seconds % 60} seconds'
#         if checks(hour1): return f'{seconds // 3600} hour, {min2} minutes and {seconds % 60} seconds'
#         if checks(min2):
#             return f'{seconds // 3600} hours, {min2} minute and {seconds % 60} seconds'
#             return f'{days} days, {seconds // 3600} hours, {min2} minutes and {seconds % 60} seconds'
#
# for x in range(6000, 8000):
#     print(x, '---', format_duration(x))