from owlready2 import get_ontology

# Load OWL ontology
ontology_path = "area_shapes_ontology.owl"
onto = get_ontology(ontology_path).load()

def calculate_area(shape, **kwargs):
    if shape == "Square":
        length = kwargs.get("length")
        return length * length
    elif shape == "Rectangle":
        length = kwargs.get("length")
        width = kwargs.get("width")
        return length * width
    elif shape == "Triangle":
        base = kwargs.get("base")
        height = kwargs.get("height")
        return 0.5 * base * height
    elif shape == "Circle":
        radius = kwargs.get("radius")
        return round(3.14 * radius * radius, 2)
    else:
        return None
