from modele.Terrain import Case


class Tiles:

    tiles = {
        ".": Case(
            passable=True,
            bloqueVision=False,
            img="img/dev_floor.png"
        ),

        "X": Case(
            passable=False,
            bloqueVision=True,
            img="img/dev_wall.png"
        ),

        "_": Case(
            passable=False,
            bloqueVision=True,
            img="img_dev_void.png"
        )
    }