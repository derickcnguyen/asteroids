import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateables, drawables)
    AsteroidField.containers = (updateables)
    asteroidfield = AsteroidField()

    Player.containers = (updateables, drawables)
    Shot.containers = (shots, updateables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # NOTE: check for player inputs

        # NOTE: update game world

        for updateable in updateables:
            updateable.update(dt)

        for asteroid in asteroids:
            # The player loses if their hitbox intersects any existing asteroid.
            if asteroid.intersects(player):
                print("Game over!")
                sys.exit(0)

            # Asteroids and Shots get destroyed when they intersect.
            for shot in shots:
                if asteroid.intersects(shot):
                    asteroid.split()
                    shot.kill()

        # NOTE: draw game to screen

        screen.fill(("black"))

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()