from model.system import System


def print_list(list_):
    print('\n'.join(str(i) for i in list_))

def print_systems(systems: System):
    for system in systems:
        print(f"{system.name} ({system.symbol})")
        for location in system.locations:
            print(f'  {location.name} ({location.symbol})')
            print(f'    type: {location.type}')
            print(f'    x: {location.x}')
            print(f'    y: {location.y}')