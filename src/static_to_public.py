import os
import shutil

def static_to_public(static_path, public_path, initial_call=True):
    if os.path.exists(public_path) and initial_call is True:
        shutil.rmtree(public_path)
    
    os.makedirs(public_path, exist_ok=True)

    for dir in os.listdir(static_path):
        path = os.path.join(static_path, dir)
        if os.path.isfile(path):
            shutil.copy(path, public_path)
        else:
            static_to_public(path, os.path.join(public_path, dir), False)
