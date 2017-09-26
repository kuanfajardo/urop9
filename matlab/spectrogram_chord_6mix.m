%wav_files = [{'3000_0_1', '3000_100_1'}];
wav_files = [{'3000_5_1','3000_25_1.wav', '3000_35_1.wav', '3000_65_1.wav', '3000_75_1.wav', '3000_95_1'}];
%wav_files = [{'3000_0_1', '3000_5_1.wav', '3000_25_1.wav', %'3000_35_1.wav', '3000_65_1.wav', '3000_75_1.wav', '3000_95_1.wav', '3000_100_1'}];

for wav_file_counter = 1:length(wav_files)
	[this_wav_file, f] = wavread(wav_files{wav_file_counter}, [1 5000]);
	subplot(1,length(wav_files),wav_file_counter), myspecgram(this_wav_file, 128, f, 12000);
	set(gca,'xtick',[0 .05 .1])
% 	colorbar
	if wav_file_counter > 1
		set(gca,'yticklabel',{' '});
	end
% 	if wav_file_counter < length(wav_files)
% 		COLORBAR('off')
% 	end
	finish_figure_big
%	xlabel('time(s)')
%	ylabel('frequency (1/s)')
end
 [ax,h1]=suplabel('time (s)'); 
 [ax,h2]=suplabel('frequency (1/s)','y'); 
 set(h1,'FontSize', 18, 'FontWeight', 'bold')
 set(h2,'FontSize', 18, 'FontWeight', 'bold')