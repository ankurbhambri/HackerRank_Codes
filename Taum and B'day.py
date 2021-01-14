b=10, w=10
bc=1, wc=1, z=1


if (wc+z) < bc:
    print(b*(wc+z) + w*wc)

elif (bc+z) < wc:
    print(b*bc + w*(bc+z))

else:
    print(b*bc + w*wc)
