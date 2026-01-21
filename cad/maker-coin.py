from build123d import *
from ocp_vscode import show

#MM = 1  # millimeter unit
# Coin Parameters
diameter, thickness = 50 * MM, 10 * MM

with BuildPart() as maker_coin:
    # On XZ plane draw the profile of half the coin
    with BuildSketch(Plane.XZ) as profile:
        with BuildLine() as outline:
            l1 = Polyline((0, thickness * 0.6), (0, 0), ((diameter - thickness) / 2, 0))
            l2 = JernArc(
                start=l1 @ 1, tangent=l1 % 1, radius=thickness / 2, arc_size=300
            )  # extend the arc beyond the intersection but not closed
            l3 = DoubleTangentArc(l1 @ 0, tangent=(1, 0), other=l2)
        make_face()  # make it a 2D shape
    revolve()  # revolve 360°

    # Pattern the detents around the coin
    with BuildSketch() as detents:
        with PolarLocations(radius=(diameter + 5) / 2, count=8):
            Circle(thickness * 1.4 / 2)
    extrude(amount=thickness, mode=Mode.SUBTRACT)  # cut away the detents

    fillet(maker_coin.edges(Select.NEW), 2)  # fillet the cut edges

    # Add an embossed label
    with BuildSketch(Plane.XY.offset(thickness)) as label:  # above coin
        Text("NeoDarwin", font_size=7)
    project()  # label on top of coin
    extrude(amount=-thickness / 5, mode=Mode.SUBTRACT)  # emboss label

show(maker_coin)