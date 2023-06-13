clc;
clear all;
close all;

Fs = 500;  % Sampling frequency (Hz)
T = 10;    % Signal duration (seconds)
N = 10;    % Number of heartbeats
HR = 60;   % Heart rate (bpm)

HBD = 60 / HR;
t = linspace(0, T, T * Fs);
ecg = zeros(1, length(t));

for n = 1:N
    start_time = (n - 1) * HBD;
    R_duration = 0.25 * HBD;
    R_samples = round(R_duration * Fs);
    R_wave = sin(linspace(0, 2 * pi, R_samples));
    ecg(start_time * Fs + 1 : start_time * Fs + R_samples) = R_wave;
end

% Add noise (optional)
noise_amplitude = 0.1;
ecg = ecg + noise_amplitude * randn(size(ecg));

% Plot the ECG signal
plot(t, ecg);
xlabel('Time (s)');
ylabel('Amplitude');
title('Synthetic ECG Signal');

%Save the ECG signal to a text file
filename = 'ecg_signal.txt';
dlmwrite(filename, ecg', 'delimiter', '\t');

%Display a confirmation message
disp(['ECG signal saved to ' filename]);

