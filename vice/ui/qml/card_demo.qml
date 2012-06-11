import QtQuick 1.0

Rectangle {
    id: page
    width: 500; height: 300
    color: "lightgray"

    Image {
        id: cardImage
        anchors.horizontalCenter: page.horizontalCenter
        anchors.verticalCenter: page.verticalCenter
        source: "dark_adept.jpg"
        asynchronous: true
    }

    MouseArea {
        anchors.fill: cardImage
        onClicked: {
            if (page.state == "")
                page.state = "down"
            else
                page.state = ""
        }
    }

    states: State {
        name: "down"
        PropertyChanges { 
            target: cardImage; 
            rotation: 90;
        }
    }

    transitions: Transition {
        from: ""; to: "down"; reversible: true
        NumberAnimation { 
            properties: "y.rotation"; duration: 500
            easing.type: Easing.InOutQuad
        }
    }
}
