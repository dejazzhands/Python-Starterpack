from os import terminal_size
from model.Tile import Tile

class TileMap:
    def __init__(self, tilemap_dict) -> None:
        self.map_height = tilemap_dict['mapHeight']
        self.map_width = tilemap_dict['mapWidth']
        self.tiles = [] 
        for row_dict in tilemap_dict['tiles']:
            tile_row = []
            for tile in row_dict:
                tile_row.append(Tile(tile))
            self.tiles.append(tile_row)
        
        