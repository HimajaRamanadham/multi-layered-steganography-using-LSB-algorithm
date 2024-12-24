clc:

clear all;

% Read the cover image.

cover = imread('hari.jpeg');

% Read the secret message image secret_message = imread('hello.png');

% Resize the secret message image to match the size of the cover image secret_message = imresize(secret_message, size(cover(:,:, 1)));

% Convert the secret message image to binary

secret_message_binary dec2bin(secret_message(:), 8);

% Reshape the binary secret message to a matrix

secret_message_matrix reshape(secret_message_binary, size(cover, 1), size(cover, 2), []);

% Get the number of bits in the secret message

num_bits_secret = numel(secret_message);

% Divide the cover image into two layers

layer1 = bitand(cover, 248);

% Use the first 5 bits of each pixel in layer 1

layer2 cover - layer1;

% Use the last 3 bits of each pixel in layer 2

% Embed the secret message in the first layer using the LSB algorithm
for i 1:size(layer1, 1)

for j 1:size(layer1, 2)

fork 1:size(layer1, 3)

if bit_counter <= num_bits_secret

layer1(i. j. k) bitor(layer1(i, j, k), str2num(secret_message_matrix(i, j, k)));

bit_counter bit_counter + 1;

else

break:

end

end

if bit_counter > num_bits_secret

break:

end

end

if bit_counter > num_bits_secret

break;

end

end

% Combine the two layers to get the stego image

stego layer1 + layer2:

% Display the cover image and the stego image

subplot(2, 2, 1);

imshow(cover);

title(Cover Image);

subplot(2, 2, 2);

imshow(stego);

title('Stego Image');
% Extract the secret message from the stego image

extracted_secret_message_matrix = zeros(size(cover, 1), size(cover, 2), size(secret_message, 3),

'uint8');

bit counter=1;

for i=1:size(layer1, 1)

for j 1:size(layer1, 2)

for k=1:size(layer1, 3)

if bit_counter <= num_bits_secret

extracted_secret_message_matrix(i, j. k) = bitget(layer1(i, j, k), 1);

bit counter bit counter+1;

else

break:

end

end

if bit_counter > num_bits_secret

break;

end

end

if bit_counter > num_bits_secret

break;

end

end

% Convert the extracted secret message from binary to an image

extracted_secret_message = bin2gray(reshape(extracted_secret_message_matrix, [].

size(secret_message, 3)), 'pam', 256);

35/44

% Reshape the extracted secret message to an image

extracted_secret_message = reshape(extracted_secret_message, size(secret_message, 1), size(secret_message, 2), []);
% Display the extracted secret message

subplot(2, 2, 3);

imshow(secret_message);

title('Secret Message Image');

subplot(2, 2, 4);

imshow(extracted_secret_message);

title('Extracted Secret Message Image');
