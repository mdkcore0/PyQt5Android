import QtQuick 2.12

Item {
    id: root

    anchors.fill: parent

    Rectangle {
        anchors.centerIn: parent

        width: parent.width * 0.8
        height: parent.height * 0.8
        color: "red"

        AnimatedImage {
            id: vitor

            anchors.centerIn: parent

            width: parent.width * 0.75
            height: parent.height * 0.75

            fillMode: Image.PreserveAspectFit

            source: "test.gif"
            paused: true

            MouseArea {
                anchors.fill: parent
                onClicked: vitor.paused = !vitor.paused
            }
        }
    }
}
