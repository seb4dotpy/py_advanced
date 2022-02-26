from typing import Dict, List, Tuple

positives: List[int] = [1,2,3,4,5] #Positives is asigned with List data type, imported

users: Dict[str,int] = { #users isasignes with Dict data type, and respective data type
    'Argentina' : 3,
    'Chile' : 3,
}

countries: List[Dict[str,str]] = [ #Countries is asigned with List[Dict] 
    {
        'name' : 'Chile',
        'people' : '19000000'
    },
    {
        'name' : 'Argentina',
        'people' : '38000000'
    }
]

numbers: Tuple[int,float,int] = (1,0.5,3) #How to static typing in tuples

CoordinatesType = List[Dict[str, Tuple[int,int]]]

Coordinates: CoordinatesType = [
    {
        'coord1' : (1,2),
        'coord2' : (3,2)
    }
]