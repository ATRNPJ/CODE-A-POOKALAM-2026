import turtle
import math

# =======3==================================================
# CODE-A-POOKALAM
# Kerala Cultural Theme
# =========================================================

screen = turtle.Screen()
screen.setup(900, 900)
screen.bgcolor("#202020")
screen.title("Code-A-Pookalam")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()


# =========================================================
# BASIC FUNCTIONS
# =========================================================

def circle(radius, color, x=0, y=0):

    pen.goto(x, y - radius)
    pen.setheading(0)
    pen.color(color)

    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


def dot(x, y, size, color):

    pen.goto(x, y)
    pen.dot(size, color)


def half_circle(
    radius,
    color,
    top=True,
    x=0,
    y=0,
    steps=80
):

    pen.color(color)

    if top:

        angles = [
            180 - i * (180 / steps)
            for i in range(steps + 1)
        ]

    else:

        angles = [
            180 + i * (180 / steps)
            for i in range(steps + 1)
        ]

    start = math.radians(angles[0])

    pen.goto(
        x + radius * math.cos(start),
        y + radius * math.sin(start)
    )

    pen.begin_fill()

    for a in angles:

        rad = math.radians(a)

        pen.goto(
            x + radius * math.cos(rad),
            y + radius * math.sin(rad)
        )

    pen.goto(
        x - radius,
        y
    )

    pen.end_fill()


# =========================================================
# ROSE PETALS
# =========================================================

def rose_petal(size, color):

    pen.color(color)

    pen.begin_fill()

    for _ in range(2):

        pen.circle(
            size,
            45
        )

        pen.left(135)

    pen.end_fill()


def outer_rose_ring(
    count,
    distance,
    size,
    color
):

    for i in range(count):

        angle = 360 / count

        pen.goto(0, 0)

        pen.setheading(
            i * angle
        )

        pen.forward(distance)

        pen.left(90)

        rose_petal(
            size,
            color
        )


# =========================================================
# BIG LOTUS / DIAMOND PETALS
# =========================================================

def big_petal(
    cx,
    cy,
    angle_deg,
    length,
    width,
    fill_color,
    outline_color
):

    rad = math.radians(
        angle_deg
    )

    dx = math.cos(rad)
    dy = math.sin(rad)

    px = -dy
    py = dx

    base = (
        cx,
        cy
    )

    tip = (
        cx + dx * length,
        cy + dy * length
    )

    left_mid = (
        cx + dx * length * 0.4
        + px * width / 2,

        cy + dy * length * 0.4
        + py * width / 2
    )

    right_mid = (
        cx + dx * length * 0.4
        - px * width / 2,

        cy + dy * length * 0.4
        - py * width / 2
    )

    pen.fillcolor(
        fill_color
    )

    pen.pencolor(
        outline_color
    )

    pen.pensize(2)

    pen.goto(base)

    pen.begin_fill()

    pen.goto(left_mid)
    pen.goto(tip)
    pen.goto(right_mid)
    pen.goto(base)

    pen.end_fill()

    pen.pensize(1)


def lotus_petal_ring(
    count,
    distance,
    size,
    colors,
    outline
):

    base_radius = distance

    tip_radius = (
        distance + size
    )

    width = size * 0.6

    for i in range(count):

        angle = (
            i * (360 / count)
        )

        rad = math.radians(
            angle
        )

        cx = (
            base_radius
            * math.cos(rad)
        )

        cy = (
            base_radius
            * math.sin(rad)
        )

        big_petal(
            cx,
            cy,
            angle,
            tip_radius - base_radius,
            width,
            colors[
                i % len(colors)
            ],
            outline
        )


# =========================================================
# WHITE FLOWER ACCENTS
# =========================================================

def white_flower(
    x,
    y,
    size
):

    for dx, dy in [
        (0, 0),
        (size, 0),
        (-size, 0),
        (0, size),
        (0, -size)
    ]:

        dot(
            x + dx,
            y + dy,
            size,
            "#FFFFFF"
        )


# =========================================================
# GREEN VINES
# =========================================================

def leaf(
    x,
    y,
    angle,
    size
):

    rad = math.radians(
        angle
    )

    dx = math.cos(rad)
    dy = math.sin(rad)

    px = -dy
    py = dx

    tx = (
        x + dx * size
    )

    ty = (
        y + dy * size
    )

    lx = (
        x
        + dx * size * 0.45
        + px * size * 0.35
    )

    ly = (
        y
        + dy * size * 0.45
        + py * size * 0.35
    )

    rx = (
        x
        + dx * size * 0.45
        - px * size * 0.35
    )

    ry = (
        y
        + dy * size * 0.45
        - py * size * 0.35
    )

    pen.color(
        "#2E7D32"
    )

    pen.goto(
        x,
        y
    )

    pen.begin_fill()

    pen.goto(
        lx,
        ly
    )

    pen.goto(
        tx,
        ty
    )

    pen.goto(
        rx,
        ry
    )

    pen.goto(
        x,
        y
    )

    pen.end_fill()


def curved_vine(
    angle_deg
):

    start_radius = 265

    pen.color(
        "#388E3C"
    )

    pen.pensize(3)

    rad = math.radians(
        angle_deg
    )

    sx = (
        start_radius
        * math.cos(rad)
    )

    sy = (
        start_radius
        * math.sin(rad)
    )

    pen.goto(
        sx,
        sy
    )

    pen.pendown()

    for i in range(30):

        t = i / 29

        radius = (
            265 - t * 45
        )

        angle = (
            angle_deg
            + t * 18
        )

        r = math.radians(
            angle
        )

        x = (
            radius
            * math.cos(r)
        )

        y = (
            radius
            * math.sin(r)
        )

        pen.goto(
            x,
            y
        )

    pen.penup()

    pen.pensize(1)

    for j in range(3):

        t = (
            0.25
            + j * 0.25
        )

        radius = (
            265 - t * 45
        )

        angle = (
            angle_deg
            + t * 18
        )

        r = math.radians(
            angle
        )

        x = (
            radius
            * math.cos(r)
        )

        y = (
            radius
            * math.sin(r)
        )

        leaf(
            x,
            y,
            angle + 55,
            12
        )

        leaf(
            x,
            y,
            angle - 55,
            12
        )


# =========================================================
# DOTTED RING
# =========================================================

def dotted_ring(
    radius,
    count,
    size,
    color
):

    for i in range(count):

        angle = math.radians(
            i * 360 / count
        )

        x = (
            radius
            * math.cos(angle)
        )

        y = (
            radius
            * math.sin(angle)
        )

        dot(
            x,
            y,
            size,
            color
        )


# =========================================================
# INNER GAP DECORATION
# LARGE GREEN LEAVES + GOLD DOTS
# =========================================================

def gap_leaf(
    x,
    y,
    angle_deg,
    size=17
):

    rad = math.radians(
        angle_deg
    )

    dx = math.cos(rad)
    dy = math.sin(rad)

    px = -dy
    py = dx

    # Tip of leaf

    tip = (
        x + dx * size,
        y + dy * size
    )

    # Wider shoulders

    left = (
        x
        + dx * size * 0.42
        + px * size * 0.48,

        y
        + dy * size * 0.42
        + py * size * 0.48
    )

    right = (
        x
        + dx * size * 0.42
        - px * size * 0.48,

        y
        + dy * size * 0.42
        - py * size * 0.48
    )

    # Green outline

    pen.color(
        "#1B5E20"
    )

    # Green fill

    pen.fillcolor(
        "#43A047"
    )

    pen.pensize(2)

    pen.goto(
        x,
        y
    )

    pen.begin_fill()

    pen.goto(
        left
    )

    pen.goto(
        tip
    )

    pen.goto(
        right
    )

    pen.goto(
        x,
        y
    )

    pen.end_fill()

    pen.pensize(1)


def inner_gap_decoration():

    # =====================================================
    # GOLD DOT RING
    # =====================================================

    dotted_ring(
        radius=166,
        count=32,
        size=6,
        color="#FFD54F"
    )

    # =====================================================
    # 16 LARGE GREEN LEAVES
    # =====================================================

    count = 16

    for i in range(count):

        angle = (
            i * 360 / count
            + 11.25
        )

        rad = math.radians(
            angle
        )

        x = (
            166
            * math.cos(rad)
        )

        y = (
            166
            * math.sin(rad)
        )

        gap_leaf(
            x,
            y,
            angle,
            size=17
        )


# =========================================================
# MAIN INNER 16 PETALS
# =========================================================

def inner_petal(
    angle_deg,
    inner_radius,
    outer_radius,
    width,
    color
):

    rad = math.radians(
        angle_deg
    )

    dx = math.cos(rad)
    dy = math.sin(rad)

    px = -dy
    py = dx

    base_left = (
        dx * inner_radius
        + px * width / 2,

        dy * inner_radius
        + py * width / 2
    )

    base_right = (
        dx * inner_radius
        - px * width / 2,

        dy * inner_radius
        - py * width / 2
    )

    shoulder_left = (
        dx * (outer_radius - 20)
        + px * width / 2,

        dy * (outer_radius - 20)
        + py * width / 2
    )

    shoulder_right = (
        dx * (outer_radius - 20)
        - px * width / 2,

        dy * (outer_radius - 20)
        - py * width / 2
    )

    tip = (
        dx * outer_radius,
        dy * outer_radius
    )

    pen.color(
        "#AD1457"
    )

    pen.fillcolor(
        color
    )

    pen.pensize(2)

    pen.goto(
        base_left
    )

    pen.begin_fill()

    pen.goto(
        shoulder_left
    )

    pen.goto(
        tip
    )

    pen.goto(
        shoulder_right
    )

    pen.goto(
        base_right
    )

    pen.goto(
        base_left
    )

    pen.end_fill()

    pen.pensize(1)


def inner_petal_ring():

    count = 16

    inner_radius = 82
    outer_radius = 150
    width = 45

    for i in range(count):

        angle = (
            i * 360 / count
        )

        # Top half

        if i < 8:

            color = "#00A6A6"

        # Bottom half

        else:

            color = "#4527A0"

        inner_petal(
            angle,
            inner_radius,
            outer_radius,
            width,
            color
        )


# =========================================================
# BRIGHT CORAL GAP PETALS
# =========================================================

def small_accent_petal(
    angle_deg
):

    angle = math.radians(
        angle_deg
    )

    dx = math.cos(angle)
    dy = math.sin(angle)

    px = -dy
    py = dx

    inner_radius = 83
    outer_radius = 145

    width = 20

    base_left = (
        dx * inner_radius
        + px * width / 2,

        dy * inner_radius
        + py * width / 2
    )

    base_right = (
        dx * inner_radius
        - px * width / 2,

        dy * inner_radius
        - py * width / 2
    )

    shoulder_left = (
        dx * (outer_radius - 18)
        + px * width / 2,

        dy * (outer_radius - 18)
        + py * width / 2
    )

    shoulder_right = (
        dx * (outer_radius - 18)
        - px * width / 2,

        dy * (outer_radius - 18)
        - py * width / 2
    )

    tip = (
        dx * outer_radius,
        dy * outer_radius
    )

    # GOLD OUTLINE

    pen.color(
        "#FFD54F"
    )

    # BRIGHT CORAL FILL

    pen.fillcolor(
        "#FF5252"
    )

    pen.pensize(2)

    pen.goto(
        base_left
    )

    pen.begin_fill()

    pen.goto(
        shoulder_left
    )

    pen.goto(
        tip
    )

    pen.goto(
        shoulder_right
    )

    pen.goto(
        base_right
    )

    pen.goto(
        base_left
    )

    pen.end_fill()

    pen.pensize(1)


def accent_gap_petal_ring():

    count = 16

    # Half of 22.5° = 11.25°
    # So these land exactly in the gaps.

    for i in range(count):

        angle = (
            i * 360 / count
            + 11.25
        )

        small_accent_petal(
            angle
        )


# =========================================================
# KERALA VALLAM
# =========================================================

def draw_vallam(
    x,
    y,
    scale=1
):

    # HULL

    pen.goto(
        x - 110 * scale,
        y
    )

    pen.setheading(0)

    pen.color(
        "#3E2311"
    )

    pen.begin_fill()

    pen.goto(
        x - 135 * scale,
        y + 25 * scale
    )

    pen.goto(
        x - 115 * scale,
        y + 45 * scale
    )

    pen.goto(
        x - 80 * scale,
        y + 25 * scale
    )

    pen.goto(
        x + 90 * scale,
        y + 25 * scale
    )

    pen.goto(
        x + 125 * scale,
        y + 15 * scale
    )

    pen.goto(
        x + 110 * scale,
        y - 15 * scale
    )

    pen.goto(
        x - 80 * scale,
        y - 15 * scale
    )

    pen.goto(
        x - 110 * scale,
        y
    )

    pen.end_fill()


    # RED BOW

    pen.color(
        "#B71C1C"
    )

    pen.goto(
        x - 135 * scale,
        y + 25 * scale
    )

    pen.begin_fill()

    pen.goto(
        x - 145 * scale,
        y + 40 * scale
    )

    pen.goto(
        x - 125 * scale,
        y + 48 * scale
    )

    pen.goto(
        x - 115 * scale,
        y + 45 * scale
    )

    pen.goto(
        x - 135 * scale,
        y + 25 * scale
    )

    pen.end_fill()


    # GOLD EDGE

    pen.color(
        "#FFD54F"
    )

    pen.pensize(2)

    pen.goto(
        x - 100 * scale,
        y + 15 * scale
    )

    pen.pendown()

    pen.goto(
        x + 80 * scale,
        y + 15 * scale
    )

    pen.penup()

    pen.pensize(1)


    # ROWERS

    for i in range(10):

        px = (
            x - 75 * scale
            + i * 16 * scale
        )

        pen.color(
            "#2B1706"
        )

        pen.pensize(2)

        pen.goto(
            px,
            y + 15 * scale
        )

        pen.pendown()

        pen.goto(
            px,
            y + 30 * scale
        )

        pen.penup()

        dot(
            px,
            y + 35 * scale,
            max(
                3,
                int(6 * scale)
            ),
            "#D69B62"
        )

    pen.pensize(1)


    # OARS

    for i in range(10):

        px = (
            x - 75 * scale
            + i * 16 * scale
        )

        pen.color(
            "#8D5524"
        )

        pen.pensize(2)

        pen.goto(
            px,
            y + 18 * scale
        )

        pen.pendown()

        pen.goto(
            px - 20 * scale,
            y - 15 * scale
        )

        pen.penup()

    pen.pensize(1)


# =========================================================
# DRAW POOKALAM
# =========================================================


# 1. OUTER ROSE PETALS

outer_rose_ring(
    count=40,
    distance=310,
    size=48,
    color="#D32F2F"
)


# 2. THICK PINK CIRCLE

circle(
    295,
    "#AD1457"
)


# 3. WHITE AREA

circle(
    275,
    "#FFFDF5"
)


# 4. YELLOW + DARK PINK PETALS

lotus_petal_ring(
    count=16,
    distance=195,
    size=100,
    colors=[
        "#FFD600",
        "#D81B60"
    ],
    outline="#AD1457"
)


# 5. WHITE ACCENTS

for i in range(8):

    angle = math.radians(
        i * 45 + 22.5
    )

    x = (
        280
        * math.cos(angle)
    )

    y = (
        280
        * math.sin(angle)
    )

    white_flower(
        x,
        y,
        6
    )


# 6. GREEN VINES

for i in range(16):

    curved_vine(
        i * 22.5
    )


# 7. GOLD DOT RING

dotted_ring(
    radius=265,
    count=32,
    size=5,
    color="#FFD54F"
)


# 8. PINK DOT RING

dotted_ring(
    radius=200,
    count=32,
    size=4,
    color="#EC407A"
)


# 9. PINK INNER BORDER

circle(
    190,
    "#AD1457"
)


# 10. WHITE INNER RING

circle(
    180,
    "#FFFDF5"
)


# 10.5 INNER GAP DECORATION
# Larger green leaves + gold dots

inner_gap_decoration()


# 11. TURQUOISE + VIOLET MAIN PETALS

inner_petal_ring()


# 12. CORAL ACCENT PETALS IN THE GAPS

accent_gap_petal_ring()


# 13. BLUE WATER

circle(
    80,
    "#1565C0"
)


# 14. ORANGE SKY

half_circle(
    80,
    "#F57C00",
    top=True
)


# 15. SUN

circle(
    10,
    "#FFF176",
    x=5,
    y=42
)


# 16. KERALA VALLAM

draw_vallam(
    x=-8,
    y=-15,
    scale=0.36
)


# =========================================================
# FINISH
# =========================================================

turtle.done()