wav_files = [{'3000_0_1', '3000_100_1'}];
%wav_files = [{'3000_0_1', '3000_5_1.wav', '3000_25_1.wav', '3000_35_1.wav', '3000_65_1.wav', '3000_75_1.wav', '3000_95_1.wav', '3000_100_1'}];
for wav_file_counter = 1:length(wav_files)
	[this_wav_file, f] = wavread(wav_files{wav_file_counter}, [1 5000]);
	subplot(1,length(wav_files),wav_file_counter), myspecgram(this_wav_file,128,f);
	xlabel('% A')
	%set(gca,'xtick',[0 .5])
end
%
set(gca,'ytick',[0 2000 4000 6000 8000 10000 12000])
[ax1,h1]=suplabel('time(s)', 'x'); 
[ax2,h2]=suplabel('frequency','y'); 
%[ax,h3]=suplabel('x','t'); 
set(h1,'FontSize', 12)
set(h2,'FontSize', 12)
%set(h3,'FontSize',18)
finish_figure
%wavplay(funky, f);
% 
% subplot(2,1,1), plot(funky), title('Entire waveform');
% smallRange = 1000:1000+floor(f/100);
% subplot(2,1,2), plot(smallRange, funky(smallRange)), title('100 milliseconds');

%subplot(2,1,1), plot(funkyy), axis('tight');