def form_data_serializer(obj):
    serialized_data = {"primary": {}, "secondary": {}}

    for _index, item in enumerate(obj['image']):
        if len(obj['object-id']) >= _index + 1:
            serialized_data['primary'][_index] = {
                'object-id': obj['object-id'][_index],
                'image': obj['image'][_index],
                'heading': obj['heading'][_index],
                'sub-heading': obj['sub-heading'][_index],
                'banner-description': obj['banner-description'][_index],
                'read-more': obj['read-more'][_index]
            }
        else:
            serialized_data['secondary'][_index] = {
                'image': obj['image'][_index],
                'heading': obj['heading'][_index],
                'sub-heading': obj['sub-heading'][_index],
                'banner-description': obj['banner-description'][_index],
                'read-more': obj['read-more'][_index]
            }

    return serialized_data
