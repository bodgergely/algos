

"""
Overlapping rectangles
"""

def find_range_overlap(point1,len1,point2,len2):
    s = max(point1,point2)
    e = min(point1+w1, point2+w2)
    if s < e:
        return (s, e-s)
    else:
        return (None, None)

