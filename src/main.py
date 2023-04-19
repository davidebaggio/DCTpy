from image_compression import *

filepath = str(input("Image filepath: "))

block_size = int(input("Block size: "))

R = float(input("Parameter of quantization: "))
while R <= 0 or R >= 100:
    R = float(input("This value must be in range (0, 100): "))

img_comp(filepath, block_size, R, info=True)

jumps = [10, 20, 30, 40, 50, 60, 70, 80, 92, 94, 96, 98, 99]
mse = []
psnr = []

for i in jumps:
    print("Compression parameter R:%s ..." % i)
    m, p = img_comp(filepath, block_size, i)
    mse.append(m)
    psnr.append(p)

for i in range(len(jumps)):
    mse[i] = round(mse[i], 3)
    psnr[i] = round(psnr[i], 3)

fig, (ax1, ax2) = plt.subplots(2)
ax1.set_title("MSE")
for i, txt in enumerate(mse):
    ax1.annotate(txt, (jumps[i], mse[i]))
ax2.set_title("PSNR")
for i, txt in enumerate(psnr):
    ax2.annotate(txt, (jumps[i], psnr[i]))
ax1.plot(jumps, mse, '-o')
ax2.plot(jumps, psnr, '-o')
plt.show()

""" plt.plot(jumps, mse)
plt.ylabel("MSE")
plt.xlabel("R%")
plt.title("MSE")
plt.show() """
