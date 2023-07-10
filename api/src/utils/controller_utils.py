def patch_entity(entity, new_values):
    for key, value in new_values.__dict__.items():
        setattr(entity, key, value)
