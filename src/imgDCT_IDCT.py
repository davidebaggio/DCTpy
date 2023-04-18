from importModules import *


def blocks_DCT(image, block_size):
    h, w = np.array(image.shape[:2])
    blocksV = int(h / block_size)
    blocksH = int(w / block_size)
    temp = np.zeros((h, w), np.float32)
    dct_mat = np.zeros((h, w), np.float32)
    temp[:h, :w] = image
    for row in range(blocksV):
        for col in range(blocksH):
            sr = row*block_size
            fr = (row+1)*block_size
            sc = col*block_size
            fc = (col+1)*block_size
            currentblock = cv2.dct(temp[sr:fr, sc:fc])
            dct_mat[sr:fr, sc:fc] = currentblock
    return dct_mat


def blocks_IDCT(DCT_Mat, block_size):
    h, w = np.array(DCT_Mat.shape[:2])
    blocksV = int(h / block_size)
    blocksH = int(w / block_size)
    idct_mat = np.zeros((h, w), np.float32)
    for row in range(blocksV):
        for col in range(blocksH):
            sr = row*block_size
            fr = (row+1)*block_size
            sc = col*block_size
            fc = (col+1)*block_size
            currentblock = cv2.idct(DCT_Mat[sr:fr, sc:fc])
            idct_mat[sr:fr, sc:fc] = currentblock
    return np.uint8(idct_mat)
