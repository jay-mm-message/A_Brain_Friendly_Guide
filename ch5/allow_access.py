def allow_access(persion):
    if persion == 'Dr Evil':
        return True
    else:
        return False

ans = allow_access('Codie')
print("allow_asscess('Codie'): ", ans)
ans = allow_access('Dr Evil')
print("allow_access('Dr Evil'): ", ans)
