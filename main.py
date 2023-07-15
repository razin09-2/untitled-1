namespace SpriteKind {
    export const projectilte_1 = SpriteKind.create()
    export const projectile_3 = SpriteKind.create()
}
namespace StatusBarKind {
    export const invertory = StatusBarKind.create()
    export const time = StatusBarKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile0`, function (sprite, location) {
    mySprite.setImage()
    if (controller.right.isPressed()) {
        animation.runImageAnimation(
        mySprite,
        [],
        100,
        true
        )
    }
    if (controller.left.isPressed()) {
        animation.runImageAnimation(
        mySprite,
        [],
        100,
        true
        )
    }
    if (controller.up.isPressed()) {
        animation.runImageAnimation(
        mySprite,
        [],
        100,
        true
        )
    }
    if (controller.down.isPressed()) {
        animation.runImageAnimation(
        mySprite,
        [],
        100,
        true
        )
    }
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    [],
    100,
    true
    )
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.stairNorth, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`level7`)
    mySprite3 = sprites.create(, SpriteKind.projectilte_1)
    mySprite3.setPosition(1, 6)
    myCounter = sevenseg.createCounter(SegmentStyle.Thick, SegmentScale.Half, 1)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.stairLadder, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`level11`)
})
scene.onOverlapTile(SpriteKind.Player, sprites.castle.tileDarkGrass1, function (sprite, location) {
    mySprite.setImage()
    if (controller.right.isPressed()) {
        animation.runImageAnimation(
        mySprite,
        [],
        100,
        true
        )
    }
    if (controller.left.isPressed()) {
        animation.runImageAnimation(
        mySprite,
        [],
        100,
        true
        )
    }
    if (controller.up.isPressed()) {
        animation.runImageAnimation(
        mySprite,
        [],
        100,
        true
        )
    }
    if (controller.down.isPressed()) {
        animation.runImageAnimation(
        mySprite,
        [],
        100,
        true
        )
    }
})
controller.down.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    [],
    100,
    true
    )
})
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
})
scene.onOverlapTile(SpriteKind.Player, sprites.castle.tileDarkGrass3, function (sprite, location) {
    mySprite.setImage()
    if (controller.right.isPressed()) {
        animation.runImageAnimation(
        mySprite,
        [],
        100,
        true
        )
    }
    if (controller.left.isPressed()) {
        animation.runImageAnimation(
        mySprite,
        [],
        100,
        true
        )
    }
    if (controller.up.isPressed()) {
        animation.runImageAnimation(
        mySprite,
        [],
        100,
        true
        )
    }
    if (controller.down.isPressed()) {
        animation.runImageAnimation(
        mySprite,
        [],
        100,
        true
        )
    } else {
    	
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestClosed, function (sprite, location) {
    statusbar.setImage()
    scaling.scaleToPixels(statusbar, 26.364, ScaleDirection.Uniformly, ScaleAnchor.TopLeft, false)
    statusbar.setPosition(80, 113)
    tiles.setCurrentTilemap(tilemap`level1`)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    [],
    100,
    true
    )
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite, otherSprite) {
    tiles.setCurrentTilemap(tilemap`level-2`)
    sprites.destroy(mySprite2)
})
controller.up.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    [],
    100,
    true
    )
})
scene.onOverlapTile(SpriteKind.Player, sprites.castle.tileDarkGrass2, function (sprite, location) {
    mySprite.setImage()
    if (controller.right.isPressed()) {
        animation.runImageAnimation(
        mySprite,
        [],
        100,
        true
        )
    }
    if (controller.left.isPressed()) {
        animation.runImageAnimation(
        mySprite,
        [],
        100,
        true
        )
    }
    if (controller.up.isPressed()) {
        animation.runImageAnimation(
        mySprite,
        [],
        100,
        true
        )
    }
    if (controller.down.isPressed()) {
        animation.runImageAnimation(
        mySprite,
        [],
        100,
        true
        )
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.projectilte_1, function (sprite, otherSprite) {
    tiles.setCurrentTilemap(tilemap`level13`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile10`, function (sprite, location) {
    statusbar3.setImage()
    scaling.scaleToPixels(statusbar3, 20, ScaleDirection.Uniformly, ScaleAnchor.TopLeft)
    statusbar3.setPosition(64, 113)
})
controller.combos.attachCombo("L+B", function () {
    animation.runImageAnimation(
    mySprite,
    [],
    100,
    true
    )
})
controller.combos.attachCombo("R+B", function () {
    animation.runImageAnimation(
    mySprite,
    [],
    100,
    true
    )
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.stairLarge, function (sprite, location) {
    tiles.setCurrentTilemap(tilemap`level11`)
})
let myCounter: DigitCounter = null
let mySprite3: Sprite = null
let statusbar3: StatusBarSprite = null
let statusbar: StatusBarSprite = null
let mySprite2: Sprite = null
let mySprite: Sprite = null
game.setDialogFrame()
mySprite = sprites.create(, SpriteKind.Player)
mySprite2 = sprites.create(, SpriteKind.Projectile)
mySprite.setPosition(130, 85)
mySprite2.setPosition(220, 220)
animation.runImageAnimation(
mySprite2,
[],
100,
true
)
controller.moveSprite(mySprite)
tiles.setCurrentTilemap(tilemap`level1`)
scene.cameraFollowSprite(mySprite)
info.setLife(3)
statusbar = statusbars.create(15, 15, StatusBarKind.invertory)
statusbar.setColor(1, 2)
statusbar.setBarBorder(1, 13)
statusbar.positionDirection(CollisionDirection.Bottom)
let statusbar2 = statusbars.create(15, 15, StatusBarKind.invertory)
statusbar2.setColor(1, 2)
statusbar2.setBarBorder(1, 13)
statusbar2.positionDirection(CollisionDirection.Bottom)
statusbar2.setPosition(95, 113)
statusbar3 = statusbars.create(15, 15, StatusBarKind.invertory)
statusbar3.setColor(1, 2)
statusbar3.setBarBorder(1, 13)
statusbar3.positionDirection(CollisionDirection.Bottom)
statusbar3.setPosition(65, 113)
game.onUpdate(function () {
    for (let walltitle of tiles.getTilesByType(sprites.builtin.forestTiles0)) {
        tiles.setWallAt(walltitle, true)
    }
})
game.onUpdateInterval(0.1, function () {
    for (let walltitle2 of tiles.getTilesByType(sprites.dungeon.floorLight0)) {
        tiles.setWallAt(walltitle2, true)
    }
})
