import json

def assemble_project(complete_paths_obj, model_list, tags, metadata):
    final_obj = {}

    # aggregate paths obj with project info
    final_obj['paths'] = complete_paths_obj
    
    # add the metadata to the final object
    final_obj['swagger'] = metadata['swagger']
    final_obj['info'] = metadata['info']            
    final_obj['definitions'] = {}
    
    # inject the models into the final object
    for model_file in model_list:
        with open(model_file) as mdl:
            model_obj = json.load(mdl)
        
        for model in model_obj['definitions']:
            final_obj['definitions'][model] = model_obj['definitions'][model]
    
    # inject top-level tags
    final_obj['tags'] = []
    
    for tag in tags:
        final_obj['tags'].append({
            'name': tag[0],
            'description': tag[1]
        })

    with open('swagger.json', 'w') as outfile:
        json.dump(final_obj, outfile, indent=4 * ' ')