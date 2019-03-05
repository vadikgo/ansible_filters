from ansible import errors


def unionattr(list1, list2, attr):
    try:
        return [el1 for el1 in list1 if (attr in el1) and (el1[attr] not in [el2[attr] for el2 in list2 if attr in el2])] + list2
    except Exception as e:
        raise errors.AnsibleFilterError('unionattr plugin error: %s' % str(e))


class FilterModule(object):
    ''' A filter to union two lists of dicts by attribute. '''
    def filters(self):
        return {
            'unionattr': unionattr
        }
