import pygame, sys, os, math, vCube


def un_lock_mouse(was_locked):
    global locked
    if was_locked:
        print("isUnlocked")
        pygame.event.get()
        pygame.mouse.get_rel()
        pygame.mouse.set_visible(1)
        pygame.event.set_grab(0)
        locked = False
    else:
        print("isLocked")
        pygame.event.get()
        pygame.mouse.get_rel()
        pygame.mouse.set_visible(0)
        pygame.event.set_grab(1)
        locked = True


def rotate2d(pos, rot):
    x, y = pos
    s, c = rot
    return x * c - y * s, y * c + x * s


class Cam:
    def __init__(self, pos=(0, 0, 0), rot=(0, 0)):
        self.pos = list(pos)
        self.rot = list(rot)
        self.update_rot()

    def update_rot(self):
        self.rotX = math.sin(self.rot[0]), math.cos(self.rot[0])
        self.rotY = math.sin(self.rot[1]), math.cos(self.rot[1])

    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            x, y = event.rel
            x /= 200
            y /= 200
            self.rot[0] += y
            self.rot[1] += x
            self.update_rot()

    def update(self, dt, key):
        s = dt * 10

        if key[pygame.K_LSHIFT]:
            self.pos[1] += s
        if key[pygame.K_SPACE]:
            self.pos[1] -= s

        x, y = s * math.sin(self.rot[1]), s * math.cos(self.rot[1])
        if key[pygame.K_w]: self.pos[0] += x; self.pos[2] += y
        if key[pygame.K_s]: self.pos[0] -= x; self.pos[2] -= y
        if key[pygame.K_a]: self.pos[0] -= y; self.pos[2] += x
        if key[pygame.K_d]: self.pos[0] += y; self.pos[2] -= x


# dont need to check if z is 0 (we clip z at min value)
def get2D(v): return cx + int(v[0] / v[2] * projX), cy + int(v[1] / v[2] * projY)


def get3D(v):
    x, y, z = v[0] - cam.pos[0], v[1] - cam.pos[1], v[2] - cam.pos[2]
    x, z = rotate2d((x, z), cam.rotY)
    y, z = rotate2d((y, z), cam.rotX)
    return x, y, z


def getZ(A, B, newZ):
    if B[2] == A[2] or newZ < A[2] or newZ > B[2]: return None
    dx, dy, dz = B[0] - A[0], B[1] - A[1], B[2] - A[2]
    i = (newZ - A[2]) / dz
    return A[0] + dx * i, A[1] + dy * i, newZ


minZ = 1
locked = False

cube_points = [(x * 2, y * -2, z * 2) for x in range(0, 8) for y in range(0, 8) for z in range(0, 8)]
cubes = [vCube.Cube(False, (x, y, z)) for x, y, z in cube_points]


def main():
    global projX, projY, cx, cy, cam, minZ
    pygame.init()
    w, h = 800, 600
    cx, cy = w // 2, h // 2

    fov = 90 / 180 * math.pi
    half_fov = fov / 2
    half_w, half_h = w / 2, h / 2
    projY = half_h / math.tan(half_fov)
    projX = half_w / math.tan(half_fov) / (w / h)

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption('3D Graphics')
    screen = pygame.display.set_mode((w, h))
    fpsclock = pygame.time.Clock()

    cam = Cam((0, 0, -5))

    while True:
        dt = fpsclock.tick() / 1000
        pygame.display.set_caption('3D Graphics - FPS: %.2f' % fpsclock.get_fps())

        key = pygame.key.get_pressed()
        cam.update(dt, key)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and key[pygame.K_LALT]:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_0:
                    minZ = 0.4
                elif event.key == pygame.K_1:
                    minZ = 1
                elif event.key == pygame.K_2:
                    minZ = 2
                elif event.key == pygame.K_9:
                    minZ = 9
                elif event.key == pygame.K_MINUS:
                    minZ = max(0.4, minZ - 1)
                elif event.key == pygame.K_EQUALS:
                    minZ += 1
                elif event.key == pygame.K_LCTRL:
                    un_lock_mouse(locked)
            cam.events(event)

        screen.fill((128, 128, 255))

        face_list = []
        face_color = []
        depth = []  # store faces (polygons / colors / depth for sorting)

        for obj in cubes:  # go through all models

            vert_list = [get3D(v) for v in obj.verts]  # get translated 3d vertices for entire model

            for f in range(len(obj.faces)):  # go through faces (build from indexing)

                verts = [vert_list[i] for i in obj.faces[f]]  # get verts for poly

                # clip verts

                i = 0
                while i < len(verts):
                    if verts[i][2] < minZ:  # behind camera
                        sides = []
                        l = verts[i - 1]
                        r = verts[(i + 1) % len(verts)]
                        if l[2] >= minZ: sides += [getZ(verts[i], l, minZ)]
                        if r[2] >= minZ: sides += [getZ(verts[i], r, minZ)]
                        verts = verts[:i] + sides + verts[i + 1:]
                        i += len(sides) - 1
                    i += 1

                if len(verts) > 2:
                    # add face (gen 2d poly / get color / average face depth)
                    face_list += [[get2D(v) for v in verts]]
                    face_color += [obj.colors[f]]
                    depth += [sum(sum(v[i] / len(verts) for v in verts) ** 2 for i in range(3))]

        # sort and render all polygons
        order = sorted(range(len(face_list)), key=lambda i: depth[i], reverse=1)
        for i in order:
            try:
                pygame.draw.polygon(screen, face_color[i], face_list[i])
            except:
                pass

        pygame.display.flip()


if __name__ == '__main__':
    main()
