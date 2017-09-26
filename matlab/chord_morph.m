function [y, Fs] = chord_morph(base_frequency, morph_fraction_percent, left_or_right)

% [y, Fs] = chord_morph(base_frequency, morph_fraction_percent, left_right)

if (100 < morph_fraction_percent || 0 > morph_fraction_percent)
    error('morph fraction should be integer between 0 and 100');
end
Fs = 44100;
t=0:1/Fs:0.5;
x = zeros(6, size(t,2));
for k=1:6
    x(k,:)=cos(base_frequency*k*pi*t);
end
morph_fraction = morph_fraction_percent/100;
x(1,:) = (1 - morph_fraction) * 0.5 * x(1,:);
x(2,:) = (1 - morph_fraction) * 1.0 * x(2,:);
x(3,:) = (1 - morph_fraction) * 0.5 * x(3,:);
x(4,:) = morph_fraction * 0.5 * x(4,:);
x(5,:) = morph_fraction * 1.0 * x(5,:);
x(6,:) = morph_fraction * 0.5 * x(6,:);
yt = 0.49 * sum(x, 1);
if (0 == left_or_right)
    y = yt;
elseif(1 == left_or_right || 2 == left_or_right)
    y = zeros(length(yt), 2);
    y(:, left_or_right) = yt;
end
sound(y, Fs);
audiowrite([num2str(base_frequency) '_' num2str(round(morph_fraction_percent)) '_' num2str(left_or_right) '.wav'], y, Fs);
