#!/bin/bash

wav_dir=$1
hmm_dir=$2/en-us/en-us
phone_dir=$2/en-us/en-us-phone.lm.bin

sample_rate=16000
channels=1
info=$(soxi $wav_dir)
echo ${info: 3}
echo $info
# If sample rate is not 16kHz, 
# then alter sample rate using ffmpeg"
#if [$sample_rate = True]; then
#	echo "Changing sample rate of the .wav file specified."
	#ffmpeg -i $wav_dir -y -ar 16000 $wav_dir
#fi

#if [$channels = False]; then
#	echo "Marging channels to mono."
#	ffmpeg -i $wav_dir -y -ac 1 $wav_dir
#fi


export LD_LIBRARY_PATH=/usr/local/lib
export LD_CONFIG_PATH=/usr/local/lib/pkgconfig
#pocketsphinx_continuous -infile $wav_dir -hmm $hmm_dir -allphone $phon_dir -backtrace yes -beam 1e-20 -pbeam 1e-20 -lw 2.0

