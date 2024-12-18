from django.shortcuts import render
from .ontology_utils import calculate_area

def home(request):
    if request.method == "POST":
        shape = request.POST.get("shape")
        
        # Handle empty input fields
        def safe_float(value):
            try:
                return float(value)
            except ValueError:
                return 0.0  # Default to 0.0 if input is empty or invalid
        
        length = safe_float(request.POST.get("length", "0"))
        width = safe_float(request.POST.get("width", "0"))
        base = safe_float(request.POST.get("base", "0"))
        height = safe_float(request.POST.get("height", "0"))
        radius = safe_float(request.POST.get("radius", "0"))

        # Calculate area
        area = calculate_area(shape, length=length, width=width, base=base, height=height, radius=radius)

        return render(request, "home.html", {"area": area, "shape": shape})
    return render(request, "home.html")
