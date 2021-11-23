

Functions = globals()


def perform_not(pairs, option):
    print('TODO: not')
    return pairs


def perform_filter(actions, pairs, option):
    actions = actions.split('.')
    for action in actions:
        f = f'perform_{action}'
        if f in Functions:
            pairs = Functions[f](pairs, option)
    return pairs


if __name__ == '__main__':
    print(Functions)
    perform_filter('not.if', [], {})
