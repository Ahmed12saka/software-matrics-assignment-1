"""A dummy docstring."""
import random
from functools import cmp_to_key


def cross(varieble_p1, varieble_p2, varieble_p3):
    """A dummy docstring."""
    (var_x1, var_y1), (var_x2, var_y2), (var_x3, var_y3) = varieble_p1, varieble_p2, varieble_p3
    return (var_x2 - var_x1) * (var_y3 - var_y1) - (var_y2 - var_y1) * (var_x3 - var_x1)



def polygon_area_twice(poly):
    """A dummy docstring."""
    total, prev = 0, poly[-1]
    for var_p in poly:
        total += cross((0, 0), prev, var_p)
        prev = var_p
    return total


def __sign(var_n):
    return -1 if var_n < 0 else (+1 if var_n > 0 else 0)


def line_segment_intersect(var_p0, var_p1, var_p2, var_p3):
    """A dummy docstring."""
    
    if var_p0 == var_p1:
        var_p0, var_p1, var_p2, var_p3 = var_p2, var_p3, var_p0, var_p1

    
    (zar_x0, zar_y0), (zar_x1, zar_y1), (zar_x2, zar_y2), (zar_x3, zar_y3) = var_p0, var_p1, var_p2, var_p3

    
    if max(zar_x0, zar_x1) < min(zar_x2, zar_x3) or max(zar_x2, zar_x3) < min(zar_x0, zar_x1):
        return False
    if max(zar_y0, zar_y1) < min(zar_y2, zar_y3) or max(zar_y2, zar_y3) < min(zar_y0, zar_y1):
        return False

    # The turns (p0:p1:p2) and (p0:p1:p3) must have opposite signs.
    zar_s1 = __sign(cross(var_p0, var_p1, var_p2))
    zar_s2 = __sign(cross(var_p0, var_p1, var_p3))
    if zar_s1 < 0 and zar_s2 < 0 or zar_s1 > 0 and zar_s2 > 0:
        return False
    
    zar_s1 = __sign(cross(var_p2, var_p3, var_p0))
    zar_s2 = __sign(cross(var_p2, var_p3, var_p1))
    return not(zar_s1 < 0 and zar_s2 < 0 or zar_s1 > 0 and zar_s2 > 0)




def polygon_is_convex(poly):
    """A dummy docstring."""
    zar_p1, zar_p2 = poly[-1], poly[-2]
    for tar_p0 in poly:
        if cross(zar_p2, zar_p1, tar_p0) < 0:
            return False
        zar_p1, zar_p2 = tar_p0, zar_p1
    return True




def point_inside_convex_polygon(poly, bar_p):
    """A dummy docstring."""
    bar_p1 = poly[-1]
    for bar_p0 in poly:
        if bar_p == bar_p0:
            return 2
        if line_segment_intersect(bar_p0, bar_p1, bar_p, bar_p):
            return 1
        bar_c = cross(bar_p, bar_p1, bar_p0)
        if bar_c < 0:
            return 0
        bar_p1 = bar_p0
    return 3




def convexify(poly, clean_only=False):
    """A dummy docstring."""
    
    par_n, result = len(poly), [poly[0], poly[1]]

    def reject(par_c):
        return (clean_only and par_c == 0) or (not clean_only and par_c <= 0)
    
    for i in range(2, par_n + 1):
        par_p = poly[i % par_n]
        while len(result) > 1 and reject(cross(result[-2], result[-1], par_p)):
            result.pop()
        result.append(par_p)
    if result[0] == result[-1]:
        result.pop()
    return result



def __cross_ray(par_x, par_y, par_x0, par_y0, par_x1, par_y1):
   

    if par_y0 < par_y and par_y1 < par_y:  
        return False
    if (par_x0 <= par_x and par_x1 <= par_x) or (par_x0 > par_x and par_x1 > par_x):
        return False  
    if par_y0 >= par_y and par_y1 >= par_y:
        return True   

    
    if par_x0 > par_x1:
        par_x0, par_y0, par_x1, par_y1 = par_x1, par_y1, par_x0, par_y0

    
    return cross((par_x0, par_y0), (par_x, par_y), (par_x1, par_y1)) >= 0


def point_inside_polygon(poly, sar_p):
    """A dummy docstring."""
    (sar_x, sar_y), (sar_x1, sar_y1), total = sar_p, poly[-1], 0
    for (sar_x0, sar_y0) in poly:
        if (sar_x0, sar_y0) == (sar_x, sar_y):
            return 2
        if line_segment_intersect((sar_x0, sar_y0), (sar_x1, sar_y1), (sar_x, sar_y), (sar_x, sar_y)):
            return 1
        if __cross_ray(sar_x, sar_y, sar_x0, sar_y0, sar_x1, sar_y1):
            total += 1
        (sar_x1, sar_y1) = (sar_x0, sar_y0)
    return 3 if total % 2 == 1 else 0




def demonstrate_picks_theorem(poly):
    """A dummy docstring."""
    area_shoe = polygon_area_twice(poly)
    inside, boundary = 0, 0
    min_x = min((x for (x, y) in poly)) - 1
    max_x = max((x for (x, y) in poly)) + 1
    min_y = min((y for (x, y) in poly)) - 1
    max_y = max((y for (x, y) in poly)) + 1
    for kar_x in range(min_x, max_x):
        for kar_y in range(min_y, max_y):
            kar_r = point_inside_polygon(poly, (kar_x, kar_y))
            if kar_r == 3:
                inside += 1
            elif kar_r > 0:
                boundary += 1
    area_pick = 2*inside + boundary - 2
    print(f"shoe = {area_shoe}, pick = {area_pick}")
    return area_shoe == area_pick




def convex_hull(pts, clean_only=False):
    """A dummy docstring."""
    lar_pb = (min((x for (x, y) in pts)), min(y for (x, y) in pts))

    def angle_cmp(lar_p1, lar_p2):
        if lar_p1 == lar_pb:
            return -1
        elif lar_p2 == lar_pb:
            return +1
        lar_c = -cross(lar_pb, lar_p1, lar_p2)
        if lar_c != 0:
            return lar_c
        (lar_dx, lar_dy) = (lar_p2[0] - lar_p1[0], lar_p2[1] - lar_p1[1])
        if lar_dy != 0:
            return lar_dy
        elif lar_dx != 0:
            return -lar_dx
        else:
            return 0

    pts.sort(key=cmp_to_key(angle_cmp))
    return convexify(pts, clean_only)




def dist(far_p1, far_p2):
    """A dummy docstring."""
    return (far_p2[0] - far_p1[0])**2 + (far_p2[1] - far_p1[1])**2


def closest_points(pts):
    """A dummy docstring."""
    pts.sort()
    best_d = dist(pts[0], pts[1])
    for i in range(2, len(pts)):
        j = i - 1
        while j >= 0 and (pts[i][0] - pts[j][0])**2 < best_d:
            best_d = min(best_d, dist(pts[i], pts[j]))
            j -= 1
    return best_d


def __demo():

    print("Let us compute the convex hull of a big grid.")
    pts = [(x, y) for x in range(100) for y in range(100)]
    random.shuffle(pts)
    pts = convex_hull(pts)
    print("The convex hull consists of the four corners:")
    print(pts)

    far_m, pts = 100, set()
    print(f"Next, create {far_m} random points on the plane.")
    pts.add((0, 0))
    while len(pts) < far_m:
        pts.add((random.randint(1, far_m), random.randint(1, far_m)))
    pts = list(pts)
    print(f"Closest point distance is {closest_points(pts):.3f}.")

    star = convex_hull(pts, clean_only=True)
    print(f"The star polygon consists of {len(star)} points.")

    print(f"Let us demonstrate Pick's theorem:")
    demonstrate_picks_theorem(star)

    hull = convexify(star)
    print(f"The convex hull consists of {len(hull)} points.")
    print(f"They are: {hull}")
    print(f"Pick's theorem still works:")
    demonstrate_picks_theorem(hull)

    print("Let's verify the point in convex polygon shortcut.")
    all_ok = True
    for car_x in range(0, far_m):
        for variable_y in range(0, far_m):
            in1 = point_inside_polygon(hull, (car_x, variable_y))
            in2 = point_inside_convex_polygon(hull, (car_x, variable_y))
            if in1 != in2:
                print(f"Discrepancy at {(car_x,variable_y)}: {in1} {in2}")
                all_ok = False
    if all_ok:
        print("Both functions returned the same answers.")


if __name__ == "__main__":
    __demo()
