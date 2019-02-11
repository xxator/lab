

%read image
I = imread('/home/placements2019/Documents/Parth/iivp/Lenna_(test_image).png');

%display image
figure(1)
imshow(I);

%export imagehttps://scottontechnology.com/flip-image-opencv-python/
imwrite(I,'/home/placements2019/Documents/Parth/iivp/test.png');

%FLIP IMAGE
B = I(:,end:-1:1,:);
figure(2)
imshow(B);

%concatenate image horizontally
C = [I B];
figure(3)
imshow(C)

%concatenate image vertically
d = [I;B];
figure(4)
imshow(d);

%convert into bionary image
BW = im2bw(I,0.4);
cc = bwconncomp(BW);
imshow(BW);


