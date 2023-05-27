PI = 3.14

def circle_area(r):
    return PI * (r**2)

def rectangle_area(w, h):
    return w * h

if __name__ == '__main__':
    assert circle_area(5) == 78.5
    assert rectangle_area(5,4) == 20


