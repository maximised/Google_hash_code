from random import shuffle, sample


pics = open('/users/bscdsa2022/mc64/d_pet_pictures.txt')

pictures = {}

count = -1

for line in pics:
    words = line.split(' ')
    words[-1] = words[-1][:-1]

    pictures[count] = words

    count += 1

del pictures[-1]
#print(pictures)

pics.close()

#---------------------------------------------------------

V_list = []
H_list = []

for id, att in pictures.items():
    if att[0] == 'V':
        V_list.append(id)
    else:
        H_list.append(id)





#------------------------------------------------------------------

def countPoints(sl):
    total = 0


    for i in range(0, len(sl)-1):
        if isinstance(sl[i], list):
            tags1 = list(set([tag for tag in pictures[sl[i][0]][2:] + pictures[sl[i][1]][2:]]))
        else:
            tags1 = [tag for tag in pictures[sl[i]][2:]]

        if isinstance(sl[i+1], list):
            tags2 = list(set([tag for tag in pictures[sl[i+1][0]][2:] + pictures[sl[i+1][1]][2:]]))
        else:
            tags2 = [tag for tag in pictures[sl[i+1]][2:]]

        points = []
        c = 0
        for tag in tags1:
            if tag in tags2:
                c += 1

        points.append(c)


        points.append(len(tags1)-c)
        points.append(len(tags2)-c)

        total += min(points)


    return total

print(countPoints([0, 3, [1, 2]]))

#----------------------------------------------------------------------------------------------------



def slideGenerator(dic):
    V_slide_order = sample(V_list,len(V_list))


    V_pairs = []

    for i in range(0, len(V_slide_order)-1, 2):
        V_pairs.append([V_list[i], V_list[i+1]])

    total_slide = sample(V_pairs + H_list, len(V_pairs + H_list))

    return total_slide
points=0
while points < 174000:
    slide = slideGenerator(pictures)
    points = countPoints(slide)

print(points)


f = open('ans.txt', 'w')
f.writelines(str(len(slide))+ '\n')
for line in slide:
    if isinstance(line, list):
        f.writelines(str(line[0])+ ' ' + str(line[1]) + '\n')
    else:
        f.writelines (str(line) + '\n')

f.close()