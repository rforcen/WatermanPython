import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from rendererGL import RendererGL
from array import array
from cpp.Waterman import waterman
import numpy as np


class Waterman_widget(RendererGL):
    coords = None
    color_set = ((195, 192, 173), (174, 152, 32), (200, 212, 162), (80, 102, 99), (89, 107, 57))  # laurrel set
    # color_set = ((198, 172, 255), (186, 140, 211), (147, 64, 165), (146, 29, 68), (109, 32, 32))  # Violets variations
    # color_set = ((155, 78, 78), (119, 25, 25), (30, 59, 36), (28, 84, 39), (86, 149, 98)) # night field
    scale = 0.8
    win = None
    needs_compile = True
    gl_compiled_list = 1

    def __init__(self, mesh, win):
        super(Waterman_widget, self).__init__()

        self.win = win
        self.coords, self.faces = mesh  # n coords x 3

        self.setFocusPolicy(Qt.StrongFocus)  # accepts key events

    def init(self, gl):

        gl.glCullFace(gl.GL_FRONT)

    def draw(self, gl):

        def draw_points(gl):
            gl.glBegin(gl.GL_POINTS)
            for c in self.coords:
                gl.glVertex3fv(list(c))
            gl.glEnd()

        def draw_lines(gl):
            gl.glLineWidth(2)
            gl.glColor4f(1, 1, 1, 0.1)

            for face in self.faces:
                gl.glBegin(gl.GL_LINE_STRIP)
                for ic in face:
                    gl.glVertex3fv(list(self.coords[ic]))
                gl.glEnd()

        def get_color(l):
            return self.color_set[(l - 3) % len(self.color_set)]

        def draw_faces(gl):
            for face in self.faces:  # traverse faces
                gl.glBegin(gl.GL_POLYGON)
                gl.glColor3ubv(get_color(len(face)))

                for ix_coord in face:
                    gl.glVertex3fv(list(self.coords[ix_coord]))

                gl.glEnd()

        def draw_mesh(gl):
            draw_faces(gl)
            draw_lines(gl)

        def compile(gl):
            if self.needs_compile:
                gl.glNewList(self.gl_compiled_list, gl.GL_COMPILE)
                draw_mesh(gl)
                gl.glEndList()
                self.needs_compile = False

        def draw_list(gl):
            compile(gl)
            gl.glCallList(self.gl_compiled_list)

        gl.glScalef(self.scale, self.scale, self.scale)

        draw_list(gl)


class Main(QMainWindow):
    def __init__(self, mesh, *args):
        super(Main, self).__init__(*args)

        self.setWindowTitle('Waterman polyhedra')
        self.setCentralWidget(Waterman_widget(mesh, self))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    Main(waterman(212))

    app.exec_()
