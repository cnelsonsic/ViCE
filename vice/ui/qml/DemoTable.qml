import QtQuick 1.0

Item {
    id: demoTable

    Flickable {
        id: boardFlickable
        anchors.fill: parent

        contentWidth: card.width + 50; contentHeight: card.height + 50
        maximumFlickVelocity: 500
        flickDeceleration: 1000

        Image {
            id: card
            anchors.centerIn: parent
            source: "../dark_adept.jpg"
            height: 200; width: 100
        }
    }
}


