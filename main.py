__author__ = 'tiirz'
from reportlab.pdfgen import canvas
from sys import stdin

curCanvas = canvas.Canvas("plates.pdf")
for i in range(32):
    team = stdin.readline()[:-1]
    if len(team) < 14:
        curCanvas.setFont("Helvetica", 60)
    else:
        curCanvas.setFont("Helvetica", 45)
    curCanvas.line(0, 421, 595, 421)
    curCanvas.line(0, 100, 595, 100)
    curCanvas.line(0, 742, 595, 742)

    curCanvas.rotate(180)
    curCanvas.drawCentredString(-594 / 2, -596, team)
    curCanvas.rotate(180)
    curCanvas.drawCentredString(594 / 2, 245, team)
    curCanvas.showPage()

curCanvas.save()